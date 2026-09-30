# SPEC — Document view (standalone prototype)

> Status: draft for a small standalone prototype, 2026-09-30.
> Scope: **the document view only** — the "paper" on which a tender document is shown, cut into blocks, each block read as a requirement, a piece of information or a heading. Not the toolbar, not the navigation, not the side panels, not the review table.
> Reference implementation: `renderDoc()`, `renderTable()`, `natureTag()` and the "Document view" / "Blocks" CSS in `revue-documentaire.html`. Where this file and the maquette differ on how something looks, the maquette wins.

## 1. Purpose

Take a document, cut it into lines, and show those lines the way the maquette shows a captured tender: the original text, in reading order, on a page, with each block visibly typed and selectable. The prototype exists to try the **segmentation and its reading** on real documents, outside the full application.

The prototype answers one question: *once a document is cut into blocks, can a person read it, see which blocks are requirements, and correct the cut where it is wrong?*

## 2. What the prototype does

1. **Load** a document (§3).
2. **Segment** it into blocks — one block per line, with the option to cut paragraphs into sentences (§4).
3. **Classify** each block as Heading, Information or Requirement, and flag the ones whose cut is doubtful (§5).
4. **Render** the blocks on the paper, with the maquette's visual grammar (§7).
5. Let the reader **select** a block, **reclassify** it, and **correct the cut** (split, merge) (§8).
6. **Export** the result (§9).

## 3. Input

| Source | v1 | How |
|---|---|---|
| Pasted text | Yes | A text area; the pasted text is the document |
| `.txt` / `.md` file | Yes | Read in the browser (`FileReader`), UTF-8 |
| `.docx` file | Yes | Converted in the browser with mammoth.js (`extractRawText`), then treated as text |
| `.pdf` file | No | Needs a conversion service — out of scope (§12) |

- One document at a time. Loading another replaces it.
- The file name (without extension) becomes the document title (§7.2). Pasted text is titled "Pasted document".
- Nothing leaves the browser: no upload, no server.

## 4. Segmentation — lines into blocks

**Rule 1 — one line, one block.** The text is split on line breaks. Each non-empty line (after trimming) becomes one block, in order. Empty lines are dropped; they never become blocks.

**Rule 2 — sentences in paragraphs** (the maquette's capture setting of the same name, `docs/current/CAPTURE.md`). A switch with two values:
- **As in the source** (default): a paragraph stays one block.
- **Split**: a line that is neither a heading nor a list item is cut into one block per sentence. A sentence ends at `.`, `;`, `?` or `!` followed by a space and an uppercase letter or a digit. Abbreviations (`e.g.`, `i.e.`, `etc.`, `No.`, `Fig.`, `Vol.`, `Art.`, `Ref.`) and numbers (`2.3`, `99.7%`) never end a sentence.

Changing the switch re-segments the whole document and discards manual corrections — say so before doing it ("Re-cut the document? Your N manual corrections will be lost").

**Rule 3 — list items.** A line starting with a bullet (`•`, `-`, `*`, `–`, `▪`) or an enumerator (`a)`, `(a)`, `i.`, `1)`) is its own block and is never merged into the line before. The bullet is kept in the text, as in the maquette.

**Rule 4 — tables.** Not recognised in v1: a table pasted as text arrives as lines, and each line is a block. (The maquette's table rendering, `.doc-tbl`, is §12.)

## 5. Classification — what each block is

Each block gets one **nature**: `heading`, `info` or `requirement` (the maquette's `NATURE_LABEL`: Heading, Information, Requirement). Rules apply in this order; the first that matches wins.

| # | Nature | Detected when |
|---|---|---|
| 1 | **Heading** | The line starts with a section number (`^\d+(\.\d+)*\.?\s`, e.g. `2.`, `2.4.1 `) **and** is under 120 characters **and** does not end with `.` or `;`. Also a line in all capitals under 80 characters. Level = number of numeric parts (`2` → 1, `2.4` → 2, `2.4.1` → 3); an all-caps line without a number is level 1 |
| 2 | **Requirement** | The text contains an obligation keyword, whole word, case-insensitive: EN `shall`, `must`, `is required to`, `are required to`, `shall not`, `must not`; FR `doit`, `doivent`, `devra`, `devront`, `est tenu de`, `sont tenus de`, `il est exigé` |
| 3 | **Information** | Anything else |

**Doubtful cut** (`uncertain: true`) — the maquette's "Check boundaries" state. A block is flagged when:
- it contains **two or more** obligation keywords in different sentences (probably two requirements in one block), or
- it is a requirement that **does not end** with `.`, `;`, `:` or `)` and the next block starts with a lowercase letter (probably one requirement cut in two).

The flag is informative: it never changes the nature. Splitting or merging the block clears it (§8.4).

## 6. Data model

```json
{
  "document": { "title": "WPS 1.06 - OCC Technical Specification", "source": "wps106.docx", "sentenceSplit": false },
  "blocks": [
    { "id": "SRM-00001", "index": 0, "nature": "heading", "level": 1, "text": "2. PROJECT OVERVIEW", "uncertain": false, "edited": false },
    { "id": "SRM-00002", "index": 1, "nature": "info", "level": null, "text": "The objective of this document is…", "uncertain": false, "edited": false },
    { "id": "SRM-00003", "index": 2, "nature": "requirement", "level": null, "text": "The Contractor shall…", "uncertain": true, "edited": false }
  ]
}
```

- **id**: `SRM-` + 5 digits, sequential over every block in reading order — the maquette's convention (`data.js`). Ids are **not** renumbered after a split or merge: a split adds `-B` to the new block (`SRM-00003-B`, as `doSeg()` does), a merge keeps the first block's id.
- **nature** is what the prototype detected, or what the reader chose (`edited: true` once the reader changed nature or cut).
- No status, no allocation, no person: those belong to the full application.

## 7. Rendering

Values below are the maquette's, light theme. Use them as written; they are what makes the prototype read like the real thing.

### 7.1 Page

- Background around the paper: `#F4F5FA`. The paper scrolls; nothing else does.
- **Paper**: width `min(760px, 100% − 48px)`, centred, background `#ffffff`, ink `#1d2129`, radius 4px, shadow `0 1px 2px rgba(0,0,0,.5), 0 12px 40px rgba(0,0,0,.45)`, padding `64px 72px 72px`.
- **Document font**: Georgia, "Times New Roman", serif — 13px, line height 1.65. UI labels on the paper (chips, ids, page footer) use Noto Sans; ids use a monospace (`ui-monospace, "SF Mono", Menlo`).
- **Footer**: centred, 26px from the bottom, 11px Noto Sans, `#4a5162`: "N blocks — M requirements".

### 7.2 Title

- **Title**: the document title, 21px bold, letter-spacing −0.2px.
- **Subtitle**: the source file name, 13px italic, `#4a5162`, 34px below.

### 7.3 Blocks — shared frame

Every non-heading block is a `.blk`:
- Margin `12px −14px` (it bleeds 14px into the paper's padding so its border does not touch the text), padding `8px 16px`, radius 4px.
- Border `1.5px solid transparent`, cursor pointer, transitions 0.15s on border, background, shadow.
- **Hover**: background = accent at 5% (`color-mix(in srgb, #0B294A 5%, transparent)`).
- **Selected**: border solid `#0B294A`, background accent at 7%, ring `0 0 0 3px` accent at 18%.
- **Type chip** (top right, `top:-9px; right:10px`): 11px Noto Sans bold, uppercase, letter-spacing 0.4px, padding `2px 8px`, radius 12px. Hidden (opacity 0, translated 3px down) until hover or selection.
- **Id** (requirements only): in the left gutter, `top:8px; left:−58px`, 11px monospace, `#4a5162` at 60% opacity.

### 7.4 By nature

| Nature | Look | Chip |
|---|---|---|
| **Requirement** | The document text, full ink. Border dashed `rgba(130,80,220,.5)` — the maquette's "To validate", which is what a freshly captured requirement is | "REQUIREMENT", background `#ead9f9`, text `#6c3fa8` |
| **Requirement, doubtful cut** | Border dashed `rgba(229,84,75,.55)` (overrides the above) | "REQUIREMENT · CHECK BOUNDARIES", background `#f6d5d2`, text `#a5342c` |
| **Information** | No border, no background; a 2px left rule in `#4a5162`, padding `4px 0 4px 16px`, whole block at 72% opacity (92% on hover); text `#4a5162`, 13px, line height 1.6. Cursor default | "INFORMATION", background `rgba(0,0,0,.06)`, text `#4a5162` |
| **Heading** | Not a `.blk`. Bold, ink `#1d2129`, letter-spacing −0.2px, margin `24px 0 8px`. Level 1: 16px. Level 2: 13px. Level 3 and deeper: 13px, 16px left padding, a 2px left rule `#4a5162`, 90% opacity. Hover: background `rgba(0,0,0,.03)`, radius 6px | None — the nature pill (§8.2) is its only label |

The block text is the source text as it is: no reformatting, no highlighting of the keyword that made it a requirement.

## 8. Interactions

### 8.1 Select

- Click a block → it becomes the only selected block. Click it again, or press `Esc` → nothing selected.
- `↓` / `↑` move the selection to the next / previous block (headings included) and scroll it into view (centred, smooth).
- Selection is only visual in this prototype — there is no panel to open.

### 8.2 Reclassify

- On hover (and while selected), each block and heading shows a **nature pill**, "Requirement ▾" / "Information ▾" / "Heading ▾": 11px Noto Sans semibold, `#4a5162`, background `rgba(0,0,0,.05)`, radius 6px, padding `2px 8px`, beside the chip for blocks, after the text for headings. Hidden (opacity 0) otherwise.
- Clicking it opens a small menu with the three natures, the current one marked. Choosing one changes the block's nature, re-renders it, and marks it `edited`.
- A block turned into a heading gets level 2 (the reader can't set levels in v1).

### 8.3 Correct the cut

A **Segmentation** switch (above the paper, the prototype's only control besides loading and export). When on, hovering or selecting a block shows two small buttons centred on its bottom edge (`bottom:−12px`): **Split** and **Merge ↓** — 11px bold, white on violet `#8250dc`, radius 12px, shadow `0 2px 8px rgba(0,0,0,.35)`.

- **Split**: cut the block at its middle sentence boundary into two blocks; the second takes id `<id>-B`. A single sentence can't be split — say so ("Nothing to split — single sentence").
- **Merge ↓**: join the block with the next one (text joined with a space); the merged block keeps the first id and nature. The last block can't merge down.
- Both mark the resulting blocks `edited` and clear `uncertain`.
- One level of **undo** (`Ctrl/⌘+Z`) for the last split, merge or reclassification — the maquette's toast-with-undo pattern.

### 8.4 What the reader sees change

A reclassification or a cut is applied at once and confirmed by a toast at the bottom of the screen ("SRM-00012 → Information", "SRM-00012 split in two", "SRM-00012 merged with SRM-00013"), with **Undo** in it.

## 9. Export

A button **Export JSON** downloads the data model of §6 (`<title>.segmented.json`). Nothing else is exported in v1.

## 10. Build constraints

- One self-contained HTML file, openable from disk, no build step. mammoth.js from cdnjs is the only external script.
- Light theme only.
- Must stay fluid with **2 000 blocks** (the maquette's capture set is ~1 400): render the paper once and patch changed blocks, don't re-render everything on hover.

## 11. Acceptance

- DV-T01: pasting 5 lines separated by blank lines gives exactly 5 blocks; blank lines never produce a block.
- DV-T02: "2.4.1 Commercial speed" is a Heading of level 3; "2.4.1 The Contractor shall provide a speed of 80 km/h." is a Requirement, not a heading.
- DV-T03: "The system SHALL log every event." and "Le système doit journaliser chaque événement." are both Requirements; "The objective of this document is to…" is Information.
- DV-T04: a block containing "The Contractor shall… The Supplier must…" is flagged Check boundaries.
- DV-T05: with Sentences in paragraphs = Split, a paragraph of three sentences gives three blocks; "e.g. the OCC" and "99.7%" never cut a sentence.
- DV-T06: requirement ids show in the left gutter; Information and Headings show none.
- DV-T07: the type chip appears only on hover or selection.
- DV-T08: reclassifying a Requirement to Information changes its frame at once (left rule, dimmed) and Undo restores it.
- DV-T09: Split on a two-sentence block gives `SRM-000NN` and `SRM-000NN-B`; Merge ↓ gives back one block with the first id.
- DV-T10: a `.docx` and the same text pasted give the same blocks.
- DV-T11: the exported JSON reloads to the same view (import of a `.segmented.json` is accepted as a source).
- DV-T12: 2 000 blocks scroll without visible lag; hovering does not re-render the page.

## 12. Out of scope (v1)

- Everything around the paper in the maquette: toolbar, filters, search and dimming, navigation tree, detail panel, review table, compare mode and diff marks, redaction (restricted view), comment markers, "Unassigned" badges, requirement statuses other than the default look.
- PDF input, images and figures (`.doc-fig`), tables as tables (`.doc-tbl`, row/table granularity), equations.
- AI classification: v1 detects with the rules of §5 only. Replacing them with the capture engine is the obvious next step and changes nothing in §6–§8.
- Several documents at once.

## 13. Open

1. **Keywords.** §5's lists are a starting point (EN + FR). Should `will` / `should` / `is to be` count as obligations for the tenders being tested? Recommendation: no in v1 — they would turn much of the descriptive text into requirements — but flag such blocks as Check boundaries if testing shows they matter.
2. **Heading detection on real files.** Numbering in `.docx` often lives in the list style, not the text, and mammoth's raw text drops it. Recommendation: accept that v1 misses such headings, measure how many on the reference documents, then decide whether to read the docx styles (mammoth's HTML output) in v2.
3. **Sentence split default.** The maquette defaults to "As in the source". Keep the same default here, or default to Split for testing? Recommendation: same default, so both tools cut the same way.
