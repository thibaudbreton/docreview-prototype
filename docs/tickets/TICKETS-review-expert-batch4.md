# Tickets — Review table & Expert Space (batch 4)

> Continues numbering from `TICKETS-review-table-batch3.md` (B1–B7). Two of these **override earlier decisions** — flagged explicitly. Excel/CSV re-import is deliberately excluded here and will get its own dedicated spec.

---

## B8 — Show "information" rows and let users correct the AI's category

**The three categories are:** `heading` / `information` / `requirement`. "Heading" replaces the previous "title" wording — same thing, renamed. **Image is no longer a category** (see B9 — images are handled as requirement rows now, not a separate nature).

**What to build:**
- The allocation/document-review table must display **information** rows alongside requirements, not just requirements.
- The user can **correct the AI's categorisation** on any row, switching it between the three categories.
- **Information rows carry no other fields at all** — no typology, no allocation, no compliance, no status. The category is the only attribute they have.

**Transitions between categories — confirmed rules:**
- `information` → `requirement`: the row lands on status **Incomplete** automatically (nothing is filled in yet).
- `requirement` → `information`: any allocation already made on that requirement is **deleted**. This is destructive and irreversible for that allocation data.

**Worth flagging, not a blocker:** if an expert has already answered on a branch, switching the requirement to `information` deletes that work too. Consider a confirmation step for that specific case — the rule itself is confirmed, this is only about how abruptly it happens in the UI.

---

## B9 — New image model (replaces the container model entirely)

**This supersedes `SPEC-image-container-requirements.md`.** The container/folder model (image as a parent container, open by default, requirements typed inside it) is **dropped**. Delete that model from the spec.

**New model:**
- When an image is detected, the system **automatically creates one requirement row** attached to it. No container, no folder row, no nesting.
- The user can **duplicate that row** — the duplicate stays attached to the same image. This covers the case where an image is a table containing several requirements.
- **No sub-type declaration.** The user doesn't tag an image as "diagram" vs "table". Duplication is simply available; whether to use it is the user's judgement. (A diagram is a single requirement in practice; a table may warrant several — but the system doesn't enforce or ask.)
- **The user never types the requirement text.** In the table's text cell, show the **existing small image button** already used at that spot — not a text field to fill in.
- The AI still does not read images. It only detects that one is present and creates the row.

**Source fidelity still applies:** the image and the original document are never editable or deletable. Only rows added by duplication can be removed.

---

## B10 — Three reassignment reasons, with project-manager approval

**Reassignment is a request, not a direct action.** It can be raised by **either the Expert or the Branch Manager**, and in all cases it must be **approved by the Project Manager** before taking effect. This aligns the expert-side loop with B1 (which already routed manager-raised proposals to the PM) — both now follow the same approval path.

**Three reasons the requester picks from:**
1. **Right typology, wrong person** — the activity is correct, but this isn't the right expert for it. Resolution stays within the activity: another expert from the same team takes it.
2. **Wrong typology** — this requirement doesn't belong to this activity at all. Resolution reallocates it to a different typology.
3. **This activity doesn't apply here** — the branch shouldn't exist on this requirement at all. The requester is saying "nothing for us to do here."

**Also required:**
- Reassignment requests must be **tracked in the Activity feed** (the existing Activity tab / Activity Item molecule), like any other action.
- **A new table filter for requirements with a pending reassignment request.** This filter — and the corresponding status indicator — must **only appear when at least one such request exists**, not permanently occupy space in the filter bar.

**Reallocation is always a replacement, never a removal — enforce this.**
- When the manager reallocates, they **name another activity in place of the current one**. The data entered for the previous activity is deleted, but a new activity always takes its place.
- **A requirement can never have zero activities.** The system must enforce this: removing an activity without naming a replacement is not a permitted state.
- This applies to reason 3 as well — "this activity doesn't apply here" still resolves by naming whichever activity *does* apply, not by leaving the requirement unassigned.

---

## B11 — Full document readable; the table stays scoped to your own work

**Two different surfaces, two different rules.** This is the key distinction — it is not "full access" vs "restricted access", it's a **decision surface** and a **context surface**:

- **The table = only your own requirements.** For an Expert: their own activity plus its sub-activities (child typologies), nothing else. This is the **decision surface** — an expert can only act on what appears here.
- **The document = readable in full.** The whole tender document is available to read, so the expert has complete context. But they **cannot click on other requirements** and **cannot make decisions on them**. Reading only.

**This clarifies rather than reverses `SPEC-expert-space.md`.** The strict restriction stated there wasn't wrong — it correctly described the **table**. What was missing is that full document reading sits alongside it. Update the spec to state both surfaces explicitly rather than removing the restriction.

**For Branch Managers:** currently they only see their assigned requirements. Same model applies — their own requirements in the table, with the full document readable for context.

**Consequence for the specs:** `SPEC-expert-space.md` needs the two-surface distinction made explicit. `SPEC-backend-requirements.md` §12 (restricted view) should state that the restriction applies to the actionable table scope, not to document readability.

---

## Deliberately not in this batch

**Excel/CSV re-import** — the ability to export from SRM, work in Excel, and re-import the updated file back into the tool. Confirmed as wanted (deliberately keeping the door open for people who go work in Excel), but carries enough complexity to warrant its own dedicated spec rather than a line item here. Also intersects with the still-open DOORS import question.
