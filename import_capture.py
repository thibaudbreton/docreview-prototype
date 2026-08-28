#!/usr/bin/env python3
"""
import_capture.py — Convert RFP capture .xlsx files into data.js for the SRM prototype.

Merges every capture file into ONE continuous tender, preserving each row's source
document and its position, per the domain model.

Usage:
    python3 import_capture.py                          # all files in the default folder
    python3 import_capture.py --only "*_v2.xlsx"       # just the v2 capture
    python3 import_capture.py --src "some/folder" --out data.js
    python3 import_capture.py --seed-demo              # add plausible workflow state (see below)

Reads .xlsx only. Writes one file: data.js. Touches nothing else.
"""

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    sys.exit("pandas is required:  pip3 install pandas openpyxl")

DEFAULT_SRC = "Turnkey RFP Example/Capturé excel"

# The capture's Type values map 1:1 onto the model's three categories.
TYPE_MAP = {
    "requirement": "requirement",
    "information": "information",
    "heading": "heading",
}

HEADING_COLS = ["Heading 1", "Heading 2", "Heading 3", "Heading 4"]


def clean(v):
    """Blank-ish cell -> empty string."""
    if v is None:
        return ""
    s = str(v).strip()
    return "" if s.lower() in ("nan", "none", "") else s


def doc_short_name(filename: str) -> str:
    """capture_M-ESD-...-000002-01_v2.xlsx -> M-ESD-...-000002-01_v2"""
    stem = Path(filename).stem
    return re.sub(r"^capture[_-]", "", stem, flags=re.I)


# USER-TEST-session-3.md §1.4 — one identifier scheme across headings, information
# and requirements, not one counter per category. SRM-00001 (5 digits), continuous
# across the whole tender.
ID_PREFIX = "SRM"


def build_rows(path: Path, doc_index: int, doc_id: str, doc_name: str):
    df = pd.read_excel(path, sheet_name=0)

    missing = [c for c in ("ID", "Type", "Text") if c not in df.columns]
    if missing:
        print(f"  !! skipping {path.name}: missing column(s) {missing}")
        return []

    present_headings = [c for c in HEADING_COLS if c in df.columns]

    rows = []
    for pos, (_, r) in enumerate(df.iterrows()):
        raw_type = clean(r.get("Type")).lower()
        category = TYPE_MAP.get(raw_type)
        if category is None:
            # Unknown category: keep the row, flag it rather than silently guessing.
            category = "information"
            unknown = clean(r.get("Type"))
        else:
            unknown = ""

        # Only keep heading levels that actually carry a value — the capture leaves
        # Heading 3 empty throughout and Heading 4 nearly so, and emitting empty
        # levels would invent a hierarchy depth the document doesn't have.
        path_parts = [clean(r.get(c)) for c in present_headings]
        path_parts = [p for p in path_parts if p]

        rows.append({
            "id": None,  # assigned in main(), continuously across the tender
            "sourceId": clean(r.get("ID")),
            "docId": doc_id,
            "docName": doc_name,
            "docIndex": doc_index,
            "position": pos,
            "category": category,
            "unknownCategory": unknown,
            "text": clean(r.get("Text")),
            "path": path_parts,
            "section": path_parts[0] if path_parts else "",
            "subsection": path_parts[1] if len(path_parts) > 1 else "",
        })
    return rows


def seed_demo_state(rows):
    """
    Optional. Gives requirements a plausible spread of workflow state so the
    prototype's filters and status columns have something to show.

    This is DEMO SCAFFOLDING, not captured data — nothing here came from the RFP.
    Off by default precisely so real and invented data never get confused.
    """
    import hashlib

    statuses = ["Incomplete", "Doubt", "To validate", "Valid"]
    weights = [1, 2, 5, 2]  # most rows sit in "To validate", as on a fresh project
    bucket = []
    for s, w in zip(statuses, weights):
        bucket += [s] * w

    for r in rows:
        if r["category"] != "requirement":
            r["status"] = None
            continue
        # Deterministic from the id, so reruns produce an identical file.
        h = int(hashlib.md5(r["id"].encode()).hexdigest(), 16)
        r["status"] = bucket[h % len(bucket)]
        r["_demoState"] = True
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=DEFAULT_SRC, help="folder containing the .xlsx captures")
    ap.add_argument("--out", default="data.js", help="output file (default: data.js)")
    ap.add_argument("--only", default="*.xlsx", help="glob to select files, e.g. '*_v2.xlsx'")
    ap.add_argument("--seed-demo", action="store_true",
                    help="add invented workflow state for demo purposes (clearly flagged in output)")
    args = ap.parse_args()

    src = Path(args.src).expanduser()
    if not src.is_dir():
        sys.exit(f"Not a folder: {src}")

    files = sorted(p for p in src.glob(args.only)
                   if p.suffix.lower() == ".xlsx" and not p.name.startswith("~$"))
    if not files:
        sys.exit(f"No .xlsx matching {args.only!r} in {src}")

    all_rows, documents = [], []
    for i, path in enumerate(files):
        name = doc_short_name(path.name)
        doc_id = f"DOC-{i + 1}"
        print(f"[{i + 1}/{len(files)}] {path.name}")
        rows = build_rows(path, i, doc_id, name)
        if not rows:
            continue
        counts = {}
        for r in rows:
            counts[r["category"]] = counts.get(r["category"], 0) + 1
        print(f"    {len(rows)} rows  ->  " +
              ", ".join(f"{k}: {v}" for k, v in sorted(counts.items())))
        unknown = {r["unknownCategory"] for r in rows if r["unknownCategory"]}
        if unknown:
            print(f"    !! unmapped Type value(s), imported as 'information': {sorted(unknown)}")
        documents.append({"id": doc_id, "name": name, "order": i, "rowCount": len(rows)})
        all_rows.extend(rows)

    # One continuous tender: rows stay in document order, then row order within each.
    all_rows.sort(key=lambda r: (r["docIndex"], r["position"]))
    for n, r in enumerate(all_rows):
        r["index"] = n
        r["id"] = f'{ID_PREFIX}-{n + 1:05d}'

    if args.seed_demo:
        all_rows = seed_demo_state(all_rows)

    payload = {
        "documents": documents,
        "rows": all_rows,
        "meta": {
            "totalRows": len(all_rows),
            "sourceFiles": [p.name for p in files],
            "demoStateSeeded": bool(args.seed_demo),
        },
    }

    banner = "// Generated by import_capture.py — do not edit by hand. Re-run the script instead.\n"
    if args.seed_demo:
        banner += "// NOTE: workflow status values in this file are INVENTED demo scaffolding, not captured data.\n"

    out = Path(args.out)
    out.write_text(
        banner + "window.SRM_DATA = " + json.dumps(payload, ensure_ascii=False, indent=1) + ";\n",
        encoding="utf-8",
    )

    size_kb = out.stat().st_size / 1024
    print(f"\nWrote {out}  —  {len(all_rows)} rows from {len(documents)} document(s), {size_kb:.0f} KB")
    if len(all_rows) > 3000:
        print("!! Over 3,000 rows: the prototype renders every row into the DOM, so expect "
              "the table to feel slow. Use --only to load fewer documents for a user test.")


if __name__ == "__main__":
    main()
