# SPEC — Document view (standalone prototype)

> Status: draft for a small standalone prototype, 2026-09-30 — input is a **PDF** (revised the same day; the first draft took text and .docx).
> Scope: **the document view only** — the "paper" on which a tender document is shown, cut into blocks, each block read as a requirement, a piece of information or a heading. Not the toolbar, not the navigation, not the side panels, not the review table.
> Reference implementation: `renderDoc()`, `renderTable()`, `natureTag()` and the "Document view" / "Blocks" CSS in `revue-documentaire.html`. Where this file and the maquette differ on how something looks, the maquette wins.

## 1. Purpose

Take a tender PDF, cut it into lines, and show those lines the way the maquette shows a captured tender: the original text, in reading order, on a page, with each block visibly typed and selectable. The prototype exists to try the **segmentation and its reading** on real documents, outside the full application.

The prototype answers one question: *once a document is cut into blocks, can a person read it, see which blocks are requirements, and correct the cut where it is wrong?*

## 2. What the prototype does

1. **Load** a PDF (§3) and rebuild its text as lines and paragraphs (§3.2).
2. **Segment** it into blocks — one block per paragraph, with the option to cut paragraphs into sentences (§4).
3. **Classify** each block as Heading, Information or Requirement, and flag the ones whose cut is doubtful (§5).
4. **Render** the blocks on the paper, with the maquette's visual grammar (§7).
5. Let the reader **select** a block, **reclassify** it, and **correct the cut** (split, merge) (§8).
6. **Export** the result (§9).

## 3. Input — a PDF

### 3.1 Loading

- A **PDF file**, dropped on the page or picked with a file button. One document at a time; loading another replaces it.
- Read **in the browser** with pdf.js (Mozilla, from cdnjs, with its worker). Nothing leaves the browser: no upload, no server.
- Only PDFs with a **text layer** are supported. A page with no extractable text (a scan) produces no block and is counted: "3 pages have no text layer — scanned pages need OCR, not supported here." A PDF with no text at all is refused with that message.
- A `.segmented.json` exported by the prototype (§9) can be reloaded instead of a PDF.
- The document title is the PDF's metadata title when it has one, the file name (without extension) otherwise.
- A progress line while reading ("Reading page 12 / 84…"); the paper appears when every page is read.

### 3.2 From positioned text to lines and paragraphs

pdf.js returns, per page, text items with a position and a size — not lines. The prototype rebuilds the reading text in this order:

1. **Lines.** Items whose baselines are within half a font height of each other form one line, joined left to right; a horizontal gap wider than one space width inserts a space.
2. **Headers, footers, page numbers.** A line found at (about) the same vertical position on **at least half the pages**, with the same text once digits are ignored, is a running header or footer and is dropped. A line that is only a number, or "Page N", "N / M", "- N -", within the top or bottom 8% of the page, is a page number and is dropped.
3. **Paragraphs.** Consecutive lines form one paragraph unless: the vertical gap to the previous line is larger than 1.5× the usual line spacing of the page; or the line starts with a bullet or an enumerator (§4, rule 3); or the line starts with a section number (§5, rule 1); or the previous line looks like a heading. A paragraph can continue across a page break when the last line of the page does not end with `.`, `;` or `:` and the next page's first line starts with a lowercase letter.
4. **Hyphenation.** A line ending with a hyphen followed by a line starting with a lowercase letter is joined without the hyphen ("require-" + "ments" → "requirements").
5. **Reading order.** Top to bottom, left to right, on one column. Two-column pages are not reordered in v1 (§13).

Each paragraph keeps the **page** it starts on.

## 4. Segmentation — lines into blocks

**Rule 1 — one paragraph, one block.** Each paragraph rebuilt in §3.2 becomes one block, in reading order. Empty or whitespace-only paragraphs never become blocks.

**Rule 2 — sentences in paragraphs** (the maquette's capture setting of the same name, `docs/current/CAPTURE.md`). A switch with two values:
- **As in the source** (default): a paragraph stays one block.
- **Split**: a line that is neither a heading nor a list item is cut into one block per sentence. A sentence ends at `.`, `;`, `?` or `!` followed by a space and an uppercase letter or a digit. Abbreviations (`e.g.`, `i.e.`, `etc.`, `No.`, `Fig.`, `Vol.`, `Art.`, `Ref.`) and numbers (`2.3`, `99.7%`) never end a sentence.

Changing the switch re-segments the whole document and discards manual corrections — say so before doing it ("Re-cut the document? Your N manual corrections will be lost").

**Rule 3 — list items.** A line starting with a bullet (`•`, `-`, `*`, `–`, `▪`) or an enumerator (`a)`, `(a)`, `i.`, `1)`) is its own block and is never merged into the line before. The bullet is kept in the text, as in the maquette.

**Rule 4 — tables.** Not recognised in v1: a table in the PDF arrives as lines of text, and each rebuilt paragraph is a block — cells of one row usually end up on one line. (The maquette's table rendering, `.doc-tbl`, is §12.)

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
  "document": { "title": "WPS 1.06 - OCC Technical Specification", "source": "wps106.pdf", "pages": 84, "pagesWithoutText": [], "sentenceSplit": false },
  "blocks": [
    { "id": "SRM-00001", "index": 0, "page": 3, "nature": "heading", "level": 1, "text": "2. PROJECT OVERVIEW", "uncertain": false, "edited": false },
    { "id": "SRM-00002", "index": 1, "page": 3, "nature": "info", "level": null, "text": "The objective of this document is…", "uncertain": false, "edited": false },
    { "id": "SRM-00003", "index": 2, "page": 4, "nature": "requirement", "level": null, "text": "The Contractor shall…", "uncertain": true, "edited": false }
  ]
}
```

- **id**: `SRM-` + 5 digits, sequential over every block in reading order — the maquette's convention (`data.js`). Ids are **not** renumbered after a split or merge: a split adds `-B` to the new block (`SRM-00003-B`, as `doSeg()` does), a merge keeps the first block's id.
- **page**: the PDF page the block starts on (1-based). A split keeps the page; a merge keeps the first block's.
- **nature** is what the prototype detected, or what the reader chose (`edited: true` once the reader changed nature or cut).
- No status, no allocation, no person: those belong to the full application.

## 7. Rendering

Values below are the maquette's, light theme. Use them as written; they are what makes the prototype read like the real thing.

### 7.1 Page

- Background around the paper: `#F4F5FA`. The paper scrolls; nothing else does.
- **Paper**: width `min(760px, 100% − 48px)`, centred, background `#ffffff`, ink `#1d2129`, radius 4px, shadow `0 1px 2px rgba(0,0,0,.5), 0 12px 40px rgba(0,0,0,.45)`, padding `64px 72px 72px`.
- **Document font**: Georgia, "Times New Roman", serif — 13px, line height 1.65. UI labels on the paper (chips, ids, page footer) use Noto Sans; ids use a monospace (`ui-monospace, "SF Mono", Menlo`).
- **Footer**: centred, 26px from the bottom, 11px Noto Sans, `#4a5162`: "N pages — N blocks — M requirements".
- **Page marks**: the paper is one continuous sheet, as in the maquette — PDF pages are not drawn as separate sheets. Where a new PDF page starts, a small mark sits in the right margin, level with the first block of that page: "p. 12", 11px Noto Sans, `#4a5162` at 50% opacity. It is a landmark for going back to the PDF, not a break in the text.

### 7.2 Title

- **Title**: the document title, 21px bold, letter-spacing −0.2px.
- **Subtitle**: the source file name and page count ("wps106.pdf · 84 pages"), 13px italic, `#4a5162`, 34px below.

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

- One self-contained HTML file, no build step. pdf.js (script and worker) from cdnjs is the only external dependency. pdf.js's worker does not load from `file://` in every browser: serve the file over `http://localhost` (any static server) — say so in the page if the worker fails.
- Light theme only.
- Must stay fluid with **2 000 blocks** (the maquette's capture set is ~1 400): render the paper once and patch changed blocks, don't re-render everything on hover.
- Reading a **200-page** PDF must finish in under 20 seconds on a laptop, with the progress line of §3.1 moving throughout.

## 11. Acceptance

- DV-T01: a PDF page with 5 paragraphs separated by blank space gives exactly 5 blocks, whatever the number of printed lines in each.
- DV-T01b: a running header ("M-ESD-700000 … Rev. 13") and page numbers present on every page produce no block.
- DV-T01c: "require-" at the end of a line and "ments" at the start of the next give "requirements"; a sentence continuing on the next page is one block.
- DV-T01d: a scanned page produces no block and is reported by number; a fully scanned PDF is refused with the OCR message.
- DV-T02: "2.4.1 Commercial speed" is a Heading of level 3; "2.4.1 The Contractor shall provide a speed of 80 km/h." is a Requirement, not a heading.
- DV-T03: "The system SHALL log every event." and "Le système doit journaliser chaque événement." are both Requirements; "The objective of this document is to…" is Information.
- DV-T04: a block containing "The Contractor shall… The Supplier must…" is flagged Check boundaries.
- DV-T05: with Sentences in paragraphs = Split, a paragraph of three sentences gives three blocks; "e.g. the OCC" and "99.7%" never cut a sentence.
- DV-T06: requirement ids show in the left gutter; Information and Headings show none.
- DV-T07: the type chip appears only on hover or selection.
- DV-T08: reclassifying a Requirement to Information changes its frame at once (left rule, dimmed) and Undo restores it.
- DV-T09: Split on a two-sentence block gives `SRM-000NN` and `SRM-000NN-B`; Merge ↓ gives back one block with the first id.
- DV-T10: each block's page mark matches the PDF page it starts on.
- DV-T11: the exported JSON reloads to the same view (import of a `.segmented.json` is accepted as a source).
- DV-T12: 2 000 blocks scroll without visible lag; hovering does not re-render the page.

## 12. Out of scope (v1)

- Everything around the paper in the maquette: toolbar, filters, search and dimming, navigation tree, detail panel, review table, compare mode and diff marks, redaction (restricted view), comment markers, "Unassigned" badges, requirement statuses other than the default look.
- Other inputs (`.docx`, pasted text), OCR of scanned pages, images and figures (`.doc-fig`), tables as tables (`.doc-tbl`, row/table granularity), equations, two-column reading order, the maquette's capture settings "Conversion range" (all pages are read) and "Format of equations".
- AI classification: v1 detects with the rules of §5 only. Replacing them with the capture engine is the obvious next step and changes nothing in §6–§8.
- Several documents at once.

## 13. Open

1. **Keywords.** §5's lists are a starting point (EN + FR). Should `will` / `should` / `is to be` count as obligations for the tenders being tested? Recommendation: no in v1 — they would turn much of the descriptive text into requirements — but flag such blocks as Check boundaries if testing shows they matter.
2. **Headings on real PDFs.** The text rules of §5 ignore what the PDF says for free: font size and weight. pdf.js gives both. Recommendation: in v1, also treat a line whose font is at least 1.2× the page's body size, or bold and under 120 characters, as a heading — measure on the reference tenders before keeping it.
3. **Sentence split default.** The maquette defaults to "As in the source". Keep the same default here, or default to Split for testing? Recommendation: same default, so both tools cut the same way.
4. **Layout on the reference tenders.** Two columns, landscape annex pages and tables drawn with rules will degrade the rebuild of §3.2. Recommendation: run v1 on the three documents of the maquette's capture set (Vol.2.2 TSO-Part 1, WPS 1.06, WPS 4.01) and list what breaks before adding any layout handling.
