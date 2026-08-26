#!/usr/bin/env python3
"""
import_capture_doors.py — Convert DOORS "ViewText" .numbers capture exports into data.js.

This is a SEPARATE importer from import_capture.py, which handles a different,
older capture schema (.xlsx, columns ID / Type / Text / Heading 1..4). That
script is untouched and still works for captures in that format — use
whichever importer matches the files you have. Both write the same data.js
shape (window.SRM_DATA), so revue-documentaire.html's buildDataFromCapture()
doesn't need to know which one produced it.

This schema is a Numbers export of a DOORS module's "ViewText" view, one
sheet per file:
  - MetaData  — export metadata (DOORS username, database, timestamps). Never
    read into data.js: it can carry the exporter's own DOORS username, which
    has no business in a public deployment.
  - ViewText  — the actual capture, columns in order:
      Source module        the document this row came from (repeated per row)
      Object Identifier    numeric DOORS ID, NOT sequential / NOT document order
      Num Heading           dotted section number ("1", "1.1", "1.1.1"...),
                            blank on the top-level title row
      Text                  the content
      Type                  Heading / Requirement / Information / (others —
                            see UNMAPPED handling below)
      Responsible Entity    the activity/ies this row belongs to, one per line
                            when a row has more than one

Requires the numbers-parser package (pip3 install numbers-parser) — it reads
the .numbers container format directly, no Numbers.app / AppleScript needed.

Usage:
    python3 import_capture_doors.py FILE1.numbers FILE2.numbers FILE3.numbers
    python3 import_capture_doors.py FILE1.numbers FILE2.numbers FILE3.numbers --out data.js

Row order is document order, not Object Identifier order — this script never
sorts by it. Document order across files is derived from each file's own
"Source module" string (they sort lexicographically into the tender's real
volume/WPS order — "Vol.2.2" < "Vol.2.3 WPS 1.06" < "Vol.2.3 WPS 4.01" — so
no hardcoded file order is needed).
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path

try:
    import numbers_parser
except ImportError:
    sys.exit("numbers-parser is required:  pip3 install numbers-parser")

# The capture's Type values that map cleanly onto the model's three categories.
TYPE_MAP = {
    "heading": "heading",
    "requirement": "requirement",
    "information": "information",
}

# Matches the prototype's own convention: REQ-00001 (5 digits), H-… for
# headings, INF-… for information rows — continuous across the whole tender,
# per category, so it reads as one document rather than three concatenated
# ones. Matches import_capture.py's own convention exactly.
ID_PREFIX = {"requirement": "REQ", "heading": "H", "information": "INF"}


def clean(v):
    """Blank-ish cell -> empty string."""
    if v is None:
        return ""
    s = str(v).strip()
    return "" if s.lower() in ("nan", "none", "") else s


def depth_of(num_heading: str) -> int:
    """'' -> 0 (title row); '1' -> 1; '1.1' -> 2; '1.1.1' -> 3; 'Appendix A' -> 1."""
    nh = clean(num_heading)
    return 0 if not nh else nh.count(".") + 1


def read_view_text(path: Path):
    """Returns (source_module, [row_tuples]) for one .numbers capture file."""
    doc = numbers_parser.Document(str(path))
    sheet = next((s for s in doc.sheets if s.name == "ViewText"), None)
    if sheet is None:
        sys.exit(f"  !! {path.name}: no 'ViewText' sheet — is this the DOORS capture schema?")
    table = sheet.tables[0]
    rows = table.rows(values_only=True)
    header = [clean(c) for c in rows[0]]
    expected = ["Source module", "Object Identifier", "Num Heading", "Text", "Type", "Responsible Entity"]
    if header != expected:
        sys.exit(f"  !! {path.name}: unexpected ViewText columns {header} — expected {expected}")
    data = rows[1:]
    source_module = next((clean(r[0]) for r in data if clean(r[0])), path.stem)
    return source_module, data


def build_rows(path: Path):
    source_module, data = read_view_text(path)
    rows = []
    current_top_heading = ""
    for pos, r in enumerate(data):
        _src, obj_id, num_heading, text, raw_type, entity = r
        raw_type_clean = clean(raw_type)
        category = TYPE_MAP.get(raw_type_clean.lower())
        if category is None:
            # Unknown category (e.g. "Obsolete"): keep the row, flag it rather
            # than silently guessing — same convention as import_capture.py.
            category = "information"
            unknown = raw_type_clean
        else:
            unknown = ""

        depth = depth_of(num_heading)
        if raw_type_clean == "Heading" and depth <= 1:
            # Opens a new top-level section — every row until the next one
            # like it (including this row's own text) belongs under it.
            current_top_heading = clean(text)

        perim = []
        for tok in clean(entity).split("\n"):
            tok = tok.strip().lower()
            if tok and tok not in perim:
                perim.append(tok)

        rows.append({
            "id": None,  # assigned in main(), continuously across the tender
            "sourceId": clean(obj_id),
            "docId": None,  # assigned in main(), after documents are ordered
            "docName": source_module,
            "position": pos,
            "category": category,
            "unknownCategory": unknown,
            "text": clean(text),
            "section": current_top_heading,
            "numHeading": clean(num_heading),
            "level": depth if raw_type_clean == "Heading" else None,
            "perim": perim,
        })
    return source_module, rows


# TICKET-ai-uncertainty-display.md — the real capture carries no confidence
# column (the source .numbers export never had one), so it's generated here,
# deterministically from each row's own id, as demo scaffolding standing in
# for the real AI engine's graded output. See revue-documentaire.html's own
# OBS_THRESHOLD (kept identical, 75) for the JS side of this same bar.
CONFIDENCE_THRESHOLD = 75
# Every row carries a Type confidence (is this really a heading/information/
# requirement?) — the only field information and heading rows ever get, since
# they never enter the characterisation/allocation pipeline. Requirement rows
# additionally carry Class, ABS, PBS and the activity (OBS) derived from them.
CONFIDENCE_FIELDS = {
    "heading": ["type"],
    "information": ["type"],
    "requirement": ["type", "class", "abs", "pbs", "obs"],
}


def _field_hash(row_id: str, field: str) -> int:
    digest = hashlib.md5(f"{row_id}:{field}".encode("utf-8")).hexdigest()
    return int(digest, 16)


def seed_demo_confidence(rows):
    """Deterministically generate a per-field AI confidence (0-99) for every
    row, mutating each in place as row["confidence"].

    Per SPEC/TICKET-ai-uncertainty-display.md: confidence is generated per
    FIELD, not per row (a row can be confident on one field and unsure on
    another), but the target distribution ("~87% of decisions come out
    confident", "roughly one row in eight needs review") is a ROW-level
    statistic — independently rolling each field at 87% would compound to a
    much higher review rate. So the roll is row-level first (~87% of rows are
    fully confident), and only when a row lands in the ~13% is exactly one of
    its applicable fields picked (deterministically) to carry the low score
    that actually drives its "To review" status — every other applicable
    field still gets its own independently-varied high score.
    """
    for row in rows:
        fields = CONFIDENCE_FIELDS.get(row["category"], ["type"])
        row_roll = _field_hash(row["id"], "__row__") % 1000
        row_confident = row_roll >= 130  # ~87.0% confident, ~13.0% to review
        weak_field = None
        if not row_confident:
            weak_idx = (_field_hash(row["id"], "__weak__") // 1000) % len(fields)
            weak_field = fields[weak_idx]
        confidence = {"generated": True}
        for field in fields:
            h = _field_hash(row["id"], field)
            if field == weak_field:
                confidence[field] = 30 + (h % 45)  # 30-74, below the bar
            else:
                confidence[field] = 76 + (h % 24)  # 76-99, confident
        row["confidence"] = confidence


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+", help=".numbers capture files (DOORS ViewText export)")
    ap.add_argument("--out", default="data.js", help="output file (default: data.js)")
    args = ap.parse_args()

    paths = [Path(f).expanduser() for f in args.files]
    missing = [p for p in paths if not p.is_file()]
    if missing:
        sys.exit("Not found: " + ", ".join(str(p) for p in missing))

    # Document order = lexicographic order of each file's own "Source module"
    # string, which already encodes the tender's real volume/WPS numbering
    # ("Vol.2.2" < "Vol.2.3 WPS 1.06" < "Vol.2.3 WPS 4.01") — not the order
    # the files were listed on the command line.
    parsed = []
    for path in paths:
        print(f"Reading {path.name}")
        source_module, rows = build_rows(path)
        parsed.append((source_module, path, rows))
    parsed.sort(key=lambda t: t[0])

    all_rows, documents = [], []
    entity_counts = {}
    unknown_types = {}
    max_depth = 0
    for i, (source_module, path, rows) in enumerate(parsed):
        doc_id = f"DOC-{i + 1}"
        for r in rows:
            r["docId"] = doc_id
            r["docIndex"] = i
        counts = {}
        for r in rows:
            counts[r["category"]] = counts.get(r["category"], 0) + 1
            if r["unknownCategory"]:
                unknown_types[r["unknownCategory"]] = unknown_types.get(r["unknownCategory"], 0) + 1
            for tok in r["perim"]:
                entity_counts[tok] = entity_counts.get(tok, 0) + 1
            max_depth = max(max_depth, depth_of(r["numHeading"]))
        print(f"  [{i + 1}/{len(parsed)}] {source_module}")
        print(f"    {len(rows)} rows  ->  " + ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
        documents.append({"id": doc_id, "name": source_module, "order": i, "rowCount": len(rows)})
        all_rows.extend(rows)

    # One continuous tender: rows stay in document order, then row order
    # within each — never sorted by the source Object Identifier.
    all_rows.sort(key=lambda r: (r["docIndex"], r["position"]))
    counters = {"requirement": 0, "heading": 0, "information": 0}
    for n, r in enumerate(all_rows):
        r["index"] = n
        cat = r["category"]
        counters[cat] += 1
        r["id"] = f'{ID_PREFIX[cat]}-{counters[cat]:05d}'

    if unknown_types:
        print(f"\n!! unmapped Type value(s), imported as 'information': {sorted(unknown_types.items())}")
    print(f"\nActivity codes found in Responsible Entity ({len(entity_counts)} distinct):")
    for tok, cnt in sorted(entity_counts.items()):
        print(f"    {tok.upper():8s} {cnt}")
    print(f"\nMax hierarchy depth (Num Heading segments): {max_depth}")

    seed_demo_confidence(all_rows)

    payload = {
        "documents": documents,
        "rows": all_rows,
        "meta": {
            "totalRows": len(all_rows),
            "sourceFiles": [p.name for _, p, _ in parsed],
            "demoStateSeeded": True,
            "demoStateNote": "Every row's confidence object is generated demo scaffolding, not captured data — see seed_demo_confidence().",
            "importer": "import_capture_doors.py",
        },
    }

    banner = (
        "// Generated by import_capture_doors.py — do not edit by hand. Re-run the script instead.\n"
        "// Every row's \"confidence\" object is DEMO SCAFFOLDING (see seed_demo_confidence() in this\n"
        "// script, and SPEC/TICKET-ai-uncertainty-display.md): deterministic per-field values derived\n"
        "// from the row id, calibrated to ~87% confident, standing in for the real AI engine's own\n"
        "// graded confidence output. Not captured data — never read as if it came from the source files.\n"
    )
    out = Path(args.out)
    out.write_text(
        banner + "window.SRM_DATA = " + json.dumps(payload, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8",
    )

    size_kb = out.stat().st_size / 1024
    print(f"\nWrote {out}  —  {len(all_rows)} rows from {len(documents)} document(s), {size_kb:.0f} KB")


if __name__ == "__main__":
    main()
