# Ticket — Wire real RFP capture data into the prototype

> **COMPLETED.** Kept for historical reference; see `docs/decisions/DECISIONS.md` (D14). Do not treat anything below as open work.

> For Claude Code, run inside the `SRM-PROTO` repo. Prototype-only, no backend. Read `HANDOVER.md` first for conventions.

## Goal

Replace the prototype's synthetic requirement data with the real captured RFP data, so user tests run on genuine content instead of generated placeholder strings.

## What already exists

- **`import_capture.py`** (at the repo root) converts the `.xlsx` captures in `Turnkey RFP Example/Capturé excel` into **`data.js`**, which sets a single global: `window.SRM_DATA`.
- Run it with `python3 import_capture.py`, or `python3 import_capture.py --only "*_v2.xlsx"` for one document. Do not modify `data.js` by hand — it is generated.

**`window.SRM_DATA` shape:**

```js
{
  documents: [ { id:"DOC-1", name:"…", order:0, rowCount:803 } ],
  rows: [
    {
      id:"REQ-00001",          // follows the prototype's own convention (REQ-/H-/INF- + 5 digits)
      sourceId:"CAP-000071",   // original ID from the capture file
      docId:"DOC-1", docName:"…", docIndex:0,
      position: 70,            // row order within its source document
      index: 123,              // row order across the whole tender
      category:"requirement",  // "requirement" | "heading" | "information"
      unknownCategory:"",      // non-empty only if the capture used an unmapped Type value
      text:"For Line 7 Phase 1 the depot shall be composed of…",
      path:["3 OVERHAUL WORKSHOP","3.2 Layout"],  // only levels that actually carry a value
      section:"3 OVERHAUL WORKSHOP",
      subsection:"3.2 Layout"
    }
  ],
  meta: { totalRows:803, sourceFiles:[…], demoStateSeeded:false }
}
```

## What to change

### 1. Inline `data.js` in the build

`build_merge.py` already inlines scripts into `docreview-app.html`. Add `data.js` to that pipeline so it loads **before** the review screen's own script — `window.SRM_DATA` must exist when the table initialises.

The merged output must stay a **single standalone HTML file** that works from `file://`. Do not introduce a `fetch()` of `data.js` — that fails under `file://` and would break the existing workflow.

### 2. Map the captured rows into the prototype's row model

In `revue-documentaire.html`, the review table is currently fed by `buildBigData(n)`, which fabricates rows (`REQ-` + index, text assembled from `BIG_VERBS`/`BIG_OBJ`/`BIG_QUAL`, and cycled values for type/domain/manager/alloc).

Add a new function — e.g. `buildDataFromCapture()` — that returns the same row shape from `window.SRM_DATA.rows`, and use it when `window.SRM_DATA` is present, falling back to `buildBigData(n)` when it isn't. Keep the fallback: it keeps the prototype runnable when nobody has run the import script.

**Field mapping:**

| Prototype field | From capture | Notes |
|---|---|---|
| `id` | `row.id` | already in `REQ-00001` format, use as-is |
| `kind` | `row.category` | `"requirement"` maps to the existing `"requirement"` kind; `heading` and `information` are handled in step 3 |
| `text` | `row.text` | real requirement text |
| `section` | `{num, title}` derived from `row.section` | see below |

The capture's `section` is a single string that usually already carries its number (`"3 OVERHAUL WORKSHOP"`). Split leading digits/dots into `num` and keep the rest as `title`, matching the existing `SECTIONS` shape (`{num:"1", title:"Scope and purpose"}`). If there's no leading number, leave `num` empty rather than inventing one.

**Fields with no captured equivalent** — `type`, `domain`, `perim`, `manager`, `alloc`, `status`, confidence: the capture contains none of these. Do **not** invent per-row values in the mapping code. Two acceptable options, pick one and apply it consistently:
- leave them empty/unset, so every row reads as `Incomplete` (truthful: nothing has been characterised yet), or
- run `import_capture.py --seed-demo`, which assigns a deterministic spread of statuses and marks each seeded row with `_demoState:true` plus a banner in the generated file.

The first is more honest; the second makes filters and status columns demonstrable. If the user hasn't said which, use the first and mention the flag exists.

### 3. Headings and information rows

The capture returns three categories, and the table must show all three (per batch-4 ticket B8):

- `heading` rows → render as the existing **section/heading row** style, not as requirements. They carry no typology, allocation, compliance or status.
- `information` rows → render in the table as their own category. Per B8, **information rows carry no fields at all beyond their category** — no typology, no allocation, no compliance, no status.
- `requirement` rows → the normal requirement row.

Do not filter any category out. Seeing information and heading rows in context is the point.

### 4. Document provenance

`window.SRM_DATA.documents` replaces the hardcoded `DOCS` array. Every row already knows its `docId`, so the existing document filter should work once it reads from the imported list. All documents belong to **one continuous tender** — do not present them as separate projects.

## Constraints

- **Do not hand-edit `data.js`.** If the data is wrong, fix `import_capture.py` and re-run it.
- **Do not delete `buildBigData(n)`** — it stays as the fallback and is still useful for volume testing.
- Everything produced stays in **English** (code, comments, UI copy, commit messages).
- Follow the existing verify loop: edit the source file, run `build_merge.py`, `node --check` on any script block touched, then the jsdom link check — **zero dead hrefs** required.

## Performance note

The current v2 capture is 803 rows, which the DOM handles fine. Across all six capture files the total is far larger, and the prototype renders every row into the DOM with no virtualisation — loading everything will make the table feel slow, and a user test would end up measuring that rather than the design. Use `--only` to load a single document for testing. Virtualisation is a separate ticket, not part of this one.

## Definition of done

1. `python3 import_capture.py --only "*_v2.xlsx"` produces `data.js`.
2. `build_merge.py` inlines it; the merged file opens from `file://` and shows the real RFP content.
3. The review table shows requirement, heading and information rows in original document order.
4. Removing/renaming `data.js` makes the prototype fall back to `buildBigData(n)` without errors.
5. `node --check` passes; jsdom link check reports zero dead hrefs.
