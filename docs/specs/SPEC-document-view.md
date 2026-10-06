# SPEC — Document view on the original PDF (standalone prototype)

> Status: draft for a small standalone prototype, 2026-09-30. Rewritten the same day: the first drafts rebuilt the document as HTML; the goal is the opposite — **show the original PDF, untouched, and put the blocks on top of it**.
> Scope: the document view only — the pages, and the blocks drawn over them. Not the toolbar, not the navigation, not the side panels, not the review table. The prototype has a minimal control strip (§8.6) only because it runs on its own.
> Reference for the block grammar: `renderDoc()`, `natureTag()` and the "Blocks" CSS in `revue-documentaire.html`. Where this file and the maquette differ on how a block reads, the maquette wins.

## 1. Purpose — trust

In the maquette, the document view shows the tender **re-typeset**: our own rendering of text the tool extracted. A reader cannot tell from it whether the capture missed a line, cut a sentence in two, or read a table wrong — the only thing on screen is the tool's own output.

This prototype shows **the original document, exactly as the client issued it**, and draws the capture on top of it: every block is a frame over the real text. What the tool read, how it cut it and what it thinks each piece is become visible *against the source*. That is what brings trust — and it is where a wrong cut is easiest to spot.

## 2. What the prototype does

1. **Load** a PDF and render its pages as they are (§3).
2. **Capture** it: extract the text with its position, rebuild lines and paragraphs, cut them into blocks — each block keeps the **area it covers on the page** (§4).
3. **Classify** each block: Heading, Information or Requirement, and flag doubtful cuts (§5).
4. **Draw** each block as a frame over the page, with the maquette's visual grammar (§7).
5. Let the reader **hover, select, compare with what was read, and reclassify** — on the original (§8). Blocks are not cut, merged or resized by hand: the capture's cut is what is shown and checked.
6. **Export** the blocks with their text and their areas (§9).

## 3. Input and page rendering

- A **PDF file**, dropped on the page or picked with a file button. One document at a time. A `.segmented.json` exported by the prototype (§9) can be reloaded together with its PDF.
- Everything runs **in the browser** with pdf.js (Mozilla, from cdnjs, with its worker): rendering, text extraction, geometry. No upload, no server.
- **Pages are rendered as images of themselves** (pdf.js canvas), one under the other, centred, each with a light shadow, 24px apart — the original layout, fonts, tables, figures, stamps and signatures included. The prototype never re-typesets anything.
- Only PDFs with a **text layer** can be captured. A page without text (a scan) is still shown, with a banner across its top: "No text on this page — it needs OCR, nothing was captured here." A PDF with no text at all is shown with no block and the same message.
- A progress line while capturing ("Capturing page 12 / 84…"). Pages appear as soon as they are rendered; their frames appear when the capture of that page is done.

## 4. Capture — from positioned text to blocks with an area

pdf.js gives, per page, text items with a position, a size and a font. The prototype builds blocks from them in this order. **Every step keeps geometry**: a block is its text *and* the rectangles it covers.

1. **Lines.** Items whose baselines are within half a font height of each other form one line, joined left to right; a horizontal gap wider than one space width inserts a space. A line's rectangle is the union of its items' boxes.
2. **Ignored areas.** A line found at about the same vertical position on **at least half the pages**, with the same text once digits are ignored, is a running header or footer. A line that is only a number, or "Page N", "N / M", "- N -", in the top or bottom 8% of the page, is a page number. These lines produce **no block**, but they are **kept as ignored areas** and drawn as such (§7.5) — the reader sees what was left out and why.
3. **Paragraphs.** Consecutive lines form one paragraph unless: the vertical gap to the previous line is larger than 1.5× the usual line spacing of the page; or the line starts with a bullet (`•`, `-`, `*`, `–`, `▪`) or an enumerator (`a)`, `(a)`, `i.`, `1)`); or it starts with a section number (§5); or the previous line looks like a heading. A paragraph continues across a page break when the page's last line does not end with `.`, `;` or `:` and the next page's first line starts with a lowercase letter.
4. **Hyphenation.** A line ending with a hyphen followed by a line starting with a lowercase letter is joined without the hyphen in the block's text ("require-" + "ments" → "requirements"). The frame still covers both lines.
5. **Sentences in paragraphs** (the maquette's capture setting): **Split** (default, decided 2026-09-30) — one block per sentence; or **As in the source** — one paragraph, one block. The default differs from the maquette's on purpose: the prototype tests the finer cut. A sentence ends at `.`, `;`, `?` or `!` followed by a space and an uppercase letter or a digit; abbreviations (`e.g.`, `i.e.`, `etc.`, `No.`, `Fig.`, `Vol.`, `Art.`, `Ref.`) and numbers (`2.3`, `99.7%`) never end one. A sentence that starts or ends mid-line gets a frame that starts or ends at that character's position (§7.2). Changing the setting re-captures the document and discards reclassifications — say so first ("Re-cut the document? Your N reclassifications will be lost").
6. **Reading order.** Top to bottom, left to right, one column. Two-column pages are not reordered in v1 (§13).

Tables, figures and equations are not recognised in v1: their text, if any, is captured as lines like any other; their drawing is simply visible on the page, since the page is the original.

## 5. Classification

Each block gets one **nature** — `heading`, `info` or `requirement` (the maquette's Heading, Information, Requirement). First rule that matches wins.

| # | Nature | Detected when |
|---|---|---|
| 1 | **Heading** | The text starts with a section number (`^\d+(\.\d+)*\.?\s`) **and** is under 120 characters **and** does not end with `.` or `;` — or its font is at least 1.2× the page's body size, or bold, and under 120 characters. Level = number of numeric parts (`2` → 1, `2.4.1` → 3); 1 when unnumbered |
| 2 | **Requirement** | An obligation keyword, whole word, case-insensitive: EN `shall`, `shall not`, `must`, `must not`, `will`, `will not`, `should`, `should not`, `is to be`, `are to be`, `is required to`, `are required to`; FR `doit`, `doivent`, `devra`, `devront`, `est tenu de`, `sont tenus de`, `il est exigé` |
| 3 | **Information** | Anything else |

**Doubtful cut** (`uncertain`) — the maquette's "Check boundaries": the block has two or more obligation keywords in different sentences (probably two requirements), or it is a requirement that does not end with `.`, `;`, `:` or `)` while the next block starts with a lowercase letter (probably one requirement cut in two). The flag never changes the nature; it is a warning for the reader, who can only reclassify, not re-cut.

## 6. Data model

```json
{
  "document": { "title": "WPS 1.06 - OCC Technical Specification", "source": "wps106.pdf", "pages": 84,
                "pagesWithoutText": [61, 62], "sentenceSplit": true },
  "ignored": [ { "page": 3, "reason": "header", "text": "M-ESD-700000-0000-ESP-000002-13", "rect": [56, 28, 480, 11] } ],
  "blocks": [
    { "id": "SRM-00003", "index": 2, "nature": "requirement", "level": null, "uncertain": true, "edited": false,
      "text": "The Contractor shall provide…",
      "areas": [ { "page": 4, "rect": [72, 512, 451, 38] }, { "page": 5, "rect": [72, 84, 451, 13] } ] }
  ]
}
```

- **id**: `SRM-` + 5 digits, sequential in reading order — the maquette's convention.
- **areas**: one rectangle per page the block covers, `[x, y, width, height]` in PDF points, origin at the page's top-left. A block that crosses a page break has two areas; a mid-line sentence has an area that starts or ends at that character. Rectangles are what the frames are drawn from — never recomputed from the text.
- **text**: what the capture read, de-hyphenated. Shown to the reader on selection (§8.2) — the check that the text matches the page.
- No status, no allocation, no person: those belong to the full application.

## 7. Drawing blocks over the page

### 7.1 Layers

Each page is two layers: the **page image** (pdf.js canvas, never modified), and above it an **overlay** of the same size holding the frames, ignored areas and labels. Overlay coordinates are the areas' PDF points × the current scale, so frames stay exactly on the text at every zoom (§8.5).

**Never obscure the original.** Frames have a light tint at most; nothing opaque ever covers text. Unlike the maquette's re-typeset view, Information blocks are **not dimmed** — dimming the source would defeat the purpose.

### 7.2 Frame

- A block's frame is its area on that page, padded 4px on every side (screen pixels), radius 4px, border 1.5px. A block with two areas has two frames that highlight together.
- A mid-line sentence (Split setting) is drawn as the shape its lines make: first line from the sentence's first character to the right edge, full middle lines, last line to its last character — drawn as one outline, not three boxes.
- **Hover**: tint = accent `#0B294A` at 8%; the block's border becomes visible if it was not.
- **Selected**: border `#0B294A` 2px solid, ring `0 0 0 3px` of `#0B294A` at 18%, tint 7%.

### 7.3 By nature

| Nature | Frame at rest | Type chip (hover / selected) |
|---|---|---|
| **Requirement** | Border dashed `rgba(130,80,220,.6)`, tint `rgba(130,80,220,.05)` — the maquette's "To validate" look, what a freshly captured requirement is | "REQUIREMENT" on `#ead9f9`, text `#6c3fa8` |
| **Requirement, doubtful cut** | Border dashed `rgba(229,84,75,.7)`, tint `rgba(229,84,75,.05)` | "REQUIREMENT · CHECK BOUNDARIES" on `#f6d5d2`, text `#a5342c` |
| **Information** | No border, no tint; a 3px bar in the page's left margin, level with the block, `#4a5162` at 35% | "INFORMATION" on `rgba(0,0,0,.06)`, text `#4a5162` |
| **Heading** | No border, no tint; a 3px bar in the left margin, `#1d2129` at 70%, with the level beside it ("H2", 10px) | "HEADING" on `rgba(0,0,0,.06)`, text `#1d2129` |

- **Type chip**: top-right of the frame (`top:-9px; right:10px`), 11px UI face (Alstom, DEC-115) bold, uppercase, letter-spacing 0.4px, padding `2px 8px`, radius 12px, hidden until hover or selection.
- **Id** (requirements only): in the page's left margin, level with the frame's top, 10px monospace `#4a5162` on a white pill (so it reads over any margin content). When the margin is too narrow (< 60px at the current zoom), the id moves inside the chip instead ("SRM-00012 · REQUIREMENT").

### 7.4 Page marks

- Above each page, left-aligned, 11px UI face `#4a5162`: "Page 12 / 84 — 9 blocks · 4 requirements".
- Pages without text carry the OCR banner of §3.

### 7.5 Ignored areas

Headers, footers and page numbers dropped by §4.2 are shown as a very light diagonal hatch (`rgba(0,0,0,.05)` stripes) with, on hover, "Ignored — running header" / "footer" / "page number". A **Show ignored areas** switch hides them (on by default).

## 8. Interactions

### 8.1 Select

- Click a frame → its block becomes the only selected one. Click again or `Esc` → none.
- `↓` / `↑` move to the next / previous block in reading order (headings included), scrolling the page so the frame is centred.
- Clicking the page outside any frame deselects. Text on the page is not selectable in v1 (the overlay takes the clicks).

### 8.2 What was read

When a block is selected, a small **read-out** opens under its frame (above it if there is no room), 360px wide max, white, radius 8px, shadow `0 8px 24px rgba(0,0,0,.18)`:
- first line: id, nature pill (§8.3), and "p. 4–5" when it spans pages;
- then the block's **captured text** in the document font (Georgia 13px, line-height 1.6) — the exact string the tool will work with.

This is the trust check: the reader compares, at a glance, the frame on the original and the text the tool took from it. It closes on `Esc`, on deselect, or when another block is selected. It is not a side panel: it belongs to the frame and moves with it.

### 8.3 Reclassify

- On hover and on selection, a **nature pill** shows beside the chip: "Requirement ▾" / "Information ▾" / "Heading ▾" — 11px UI face semibold, `#4a5162`, background `rgba(0,0,0,.05)`, radius 6px, padding `2px 8px`. It is also in the read-out.
- Clicking it opens a menu with the three natures, the current one marked; choosing one changes the frame at once and marks the block `edited`. A block turned into a heading gets level 2.

### 8.4 Undo and confirmation

A reclassification is applied at once and confirmed by a toast at the bottom ("SRM-00012 → Information") with **Undo**. `Ctrl/⌘+Z` undoes the last one; one level is enough in v1.

### 8.5 Zoom and scroll

- **Fit width** (default), **100%**, and `+` / `−` in 25% steps (50%–300%). Frames, bars, ids and chips follow the scale; label sizes do not.
- Zooming keeps the selected block — or the page at the top of the view — in place.
- Only the pages near the viewport are rendered (two before, two after); others are placeholders of the right size, so a 300-page PDF scrolls smoothly and the scrollbar is true from the start.

### 8.6 Control strip (prototype only)

A single bar above the pages — not part of what this spec describes, only what the prototype needs to run: **Open PDF**, sentences setting (As in the source / Split), **Show ignored areas**, zoom, a count ("84 pages · 1 412 blocks · 389 requirements · 23 to check"), **Export JSON**.

## 9. Export

**Export JSON** downloads the data model of §6 (`<title>.segmented.json`): blocks with their text, nature, flags and areas, and the ignored areas. Reloading it with the same PDF restores the view and every reclassification.

## 10. Build constraints

- One self-contained HTML file, no build step. pdf.js (script and worker) from cdnjs is the only external dependency. The worker does not load from `file://` in every browser: serve the file over `http://localhost` (any static server) and say so in the page if the worker fails.
- Light theme only. The UI face for labels — Alstom (DEC-115), Noto Sans from Google Fonts where it isn't embedded; Georgia for the read-out text.
- Capturing a **200-page** PDF finishes in under 20 seconds on a laptop, the progress line moving throughout. Rendering is lazy (§8.5).
- Hover and selection update the overlay only — never re-render a page canvas.

## 11. Acceptance

- DV-T01: every page shows exactly as in a PDF reader — same layout, fonts, tables, figures; nothing is re-typeset.
- DV-T02: each frame covers exactly the text of its block, at every zoom level from 50% to 300%.
- DV-T03: a running header and page numbers repeated on every page produce no block and show as hatched ignored areas; hiding them removes the hatch.
- DV-T04: a paragraph continuing on the next page is one block with two frames that highlight together.
- DV-T05: "require-" / "ments" across two lines reads "requirements" in the read-out; the frame covers both lines.
- DV-T06: "2.4.1 Commercial speed" is a Heading of level 3; "2.4.1 The Contractor shall provide a speed of 80 km/h." is a Requirement.
- DV-T07: "The system SHALL log every event.", "The Contractor will provide…", "Access should be restricted…", "The cabinet is to be sealed." and "Le système doit journaliser chaque événement." are Requirements; "The objective of this document is to…" is Information and is not dimmed.
- DV-T07b: by default a paragraph of three sentences gives three blocks; "e.g. the OCC" and "99.7%" never end a sentence.
- DV-T08: a block with "The Contractor shall… The Supplier must…" is framed in red dashes, chip "Check boundaries".
- DV-T09: selecting a block opens the read-out with its captured text under the frame; `Esc` closes it.
- DV-T10: reclassifying a Requirement to Information changes its frame at once (dashes gone, margin bar shown) and Undo restores it.
- DV-T11: there is no control to cut, merge or resize a block.
- DV-T12: a scanned page is shown with the OCR banner and no frame.
- DV-T13: a 300-page PDF scrolls without lag; only nearby pages are rendered.
- DV-T14: the exported JSON reloaded with its PDF gives the same frames, natures and ids.

## 12. Out of scope (v1)

- Correcting the cut by hand — split, merge, moving a block's boundary (the maquette's Segmentation mode). The reader sees the cut and reclassifies; re-cutting stays in the capture.
- Everything around the pages in the maquette: toolbar, filters and search, navigation, detail panel, review table, compare mode, redaction, comment markers, "Unassigned" badges, statuses other than the default requirement look, allocation of any kind.
- Re-typesetting the document (the maquette's current view) — this prototype replaces it for reading, it does not reproduce it.
- OCR of scanned pages; recognising tables, figures and equations as such (their text is captured as lines, their drawing is visible because the page is the original); two-column reading order; drawing a new block by hand over text that was not captured (every text line belongs to a block or an ignored area, so there is nothing uncaptured to draw — revisit if §4.2 turns out to drop real text).
- Other inputs (`.docx`, pasted text). AI classification — v1 uses the rules of §5; the capture engine can replace them without changing §6–§8.

## 13. Decided (2026-09-30)

1. **Keywords.** `will`, `should` and `is to be` count as obligations, like `shall` and `must` (§5). Expect more requirements, including descriptive sentences written in the future tense — reclassifying them is the reader's check. French equivalents of `will` / `should` (`sera`, `devrait`) are **not** added: nobody asked, and `sera` is too common.
2. **Default cut.** One block per sentence (§4.5). "As in the source" stays available.
3. **Test documents.** The prototype is tried on PDFs the user provides, not on the maquette's capture set. What breaks on them (two columns, landscape annexes, ruled tables) decides what layout handling comes next.
4. **Where it goes.** If the prototype convinces, the original-PDF view **replaces** the Allocation screen's Document view. Compare keeps a text form, since a word diff between versions needs text — how Compare looks then is to be designed separately.
