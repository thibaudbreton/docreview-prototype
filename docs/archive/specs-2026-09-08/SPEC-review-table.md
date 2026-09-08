# Spec — Review Table (iSenS / DocReview)

> Reference spec for the review table — the core screen of the tool. Describes what the table must let users do, for whom, and why. Target-state description; during the test phase, implement the minimum credible version and keep the robust implementation for the target stack. Points marked _(to validate)_ are hypotheses, not settled facts.

---

## 1. Role in the product

The review table is the **operational core** of the tool. It is where the Requirement Manager turns an AI-captured tender (AO) into a set of requirements that are verified, characterised, assigned and validated.

Today this work is partly done in **Excel**: users export the requirements, process them in a spreadsheet (because they are fast there), then re-import. This detour is both **friction** (one more tool in the workflow) and a **source of errors** (every export/re-import can corrupt or desynchronise the data).

**The value proposition of the table is therefore not "match Excel". It is to remove the Excel detour** — deliver the same manipulation speed directly inside the tool, so users never need to leave it. Anything that would force them to re-export to Excel is a design failure.

---

## 2. Guiding principle

**"The speed of a spreadsheet, the structure of a document."**

- **Spreadsheet speed** — selection, editing, filtering and sorting must be as immediate as in Excel, by keyboard and mouse, with no latency and without opening a panel for each change.
- **Document structure** — unlike Excel, the table preserves the thread of the AO (heading hierarchy, document order), because requirements about the same topic follow one another in the document — which is what makes range selection meaningful.

This is **not** a free-form spreadsheet: columns, values and business rules are constrained (see non-goals).

---

## 3. Jobs-to-be-done

The table is used at **several points** in the process, by the same person, with different intents. The three main ones, in order of appearance:

1. **Handle uncertain cases first.** On opening, the user comes to check what **the AI struggled to characterise** (low confidence, "to review" statuses). These cases must be **isolated immediately** and corrected one by one.
2. **Sweep and verify assignments, fast.** The user then goes down the whole document to make sure **everything is correctly assigned** — but quickly. Because requirements on the same topic (hence the same expert) **follow one another in the document**, the user must be able to **select a range by dragging** and apply a settings change in one go.
3. **Correct and validate in series.** Reclassification (Information / Requirement), characterisation changes, reassignment, validation — all in bulk when several rows share the same change.

---

## 4. Required capabilities

### Selection
- Multi-select with click / Ctrl / Shift (range).
- **Drag selection** (drag across a range of rows) — essential, because requirements on the same topic follow one another.
- Select all in the current filtered view.

### Editing
- **Inline editing** of every editable field directly in the cell (Class, Activity, Type, Manager, Expert, Status), without going through the detail panel.
- **Inline reclassification** Information / Requirement directly in the table (a requirement reclassified as Information disappears cleanly from the table, which lists requirements only).
- **Bulk actions** on the selection: apply one value (expert, manager, activity, status, classification) to all selected rows at once.

### Filtering
- **Exhaustive per-column filters** (Excel-style) on every field, in addition to global filters — to quickly find the rows that need action.
- A dedicated **"uncertain cases" filter** (low AI confidence / to review) surfaced prominently, since that is the first job.

### Sorting
- **Per-column sorting**, essential. By status, section, expert, etc.
- **Document order** remains the default sort (the AO thread) and must always be restorable.

### Visibility & readability
- **Show / hide / collapse columns** to fit the view to the task at hand.
- **Retractable side panels** (navigation, detail) to maximise the table area.
- Requirements **readable in full** (wrapping text, tall-enough rows) — reading must stay comfortable even in dense mode.
- **Visible document structure**: section titles / sub-headings woven into the table thread, to follow the AO.

### Navigation
- Keyboard navigation (at minimum between rows; ideally between cells, Excel-style) — to be evaluated against test feedback.

---

## 5. Constraints & non-goals

- **Real volume: 500 to 10,000+ requirements.** The table must stay fluid at this scale — designed for both **comfortable reading** and **mass processing**. Performance at 10k is not optional (implies virtualisation and indexed filter/sort in the target stack).
- **HITL preserved.** The AI proposes, the human validates. No bulk action may bypass validation checkpoints; validation stays a conscious act.
- **Not a free-form spreadsheet.** No formulas, no arbitrary columns, no free text where a constrained value is expected. Editable fields are those of the business model, with their allowed values.
- **Allocation validation may belong to a distinct role** _(to validate)_. The Requirement Manager runs the whole process, but **validating assignments may be the responsibility of a product-line requirements specialist**. The table should be able to reflect this split (who assigned vs who validates) without forcing it.
- **Cross-cutting goal: they must never fall back to Excel.** Any gap that would send them back there is a priority to close.

---

## 6. Success criteria (measurable in testing)

- The user handles uncertain cases **without having to search** for them (the first job is immediate).
- A series correction (e.g. reassign 12 requirements on the same topic) takes **one selection gesture + one change**, not twelve.
- On a realistic document (several hundred rows), the user **does not ask to export to Excel** to go faster.
- The table stays **usable and fluid** on an AO of several thousand requirements.
- A user accustomed to Excel **recovers their reflexes** (select, filter, sort) with no noticeable relearning.

---

## 7. Notes for implementation

- **Two levels, kept distinct.** This spec describes the target. For the test-phase prototype (vanilla, disposable), implement the minimum credible version; keep the robust implementation (virtualisation, indexed filters/sort, drag-select) for the target stack, after concept validation and stack confirmation with the dev lead.
- **`blockNature`, not raw `kind`.** Any table/panel logic that distinguishes requirement / information / image must key on the block's nature, so an image classified as a requirement behaves like one.
- **Open question to resolve in discovery:** the distinct role for allocation validation (§5) is a hypothesis phrased as "may" — confirm before hard-coding it into the UI.
