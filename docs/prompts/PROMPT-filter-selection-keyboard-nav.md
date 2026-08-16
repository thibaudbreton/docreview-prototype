# PROMPT — Table: Filter to Selection & Keyboard Row Navigation

> Paste into Claude Code. Scope: `revue-documentaire.html` (the review table screen) only. **Prototype / UI-only** — no backend calls, no derivation logic beyond interaction behaviour. Edit the **source** file, then run `build_merge.py` to regenerate the merged app, then verify with `node --check` on any touched script and the existing jsdom dead-link check (must stay at 0 dead hrefs).

---

## Feature 1 — Filter to Selection

**What it does:** the reviewer selects a scattered set of requirements (existing row checkboxes — not necessarily contiguous), then narrows the table to show only those rows, to work on that working subset without scrolling through the rest.

**Interaction:**
- New button in the existing **Bulk Action Bar**: **"Show only selected"**. Disabled when 0 rows are selected.
- Activating it switches the table into a **filtered view**: a persistent banner replaces the normal toolbar area — *"Showing 10 of 1,204 requirements — selected"* with a **"Show all"** button to exit.
- Rows stay in their original **document order** inside the filtered view (not selection order) — consistent with source fidelity elsewhere in the tool.
- Checkboxes remain checked; the Bulk Action Bar stays available on this reduced set (you can still bulk-assign, validate, etc. on just this subset).
- Exiting via "Show all" restores the full table exactly as it was, including any prior sort/scroll position.

**Open decision — interaction with existing column filters.** Default proposed: activating "Show only selected" **suspends** any active column filters (they're not lost, just not applied while filter-to-selection is on) and restores them when you click "Show all". Combining scattered selection with column filters at the same time risks producing a confusing, hard-to-reason-about result — flag if you'd rather they compose (AND together) instead.

**Open decision — multi-allocation rows.** If a selected row is a **branch sub-row** (from the multi-allocation expandable pattern), default proposed: show its **parent requirement row for context**, expanded to reveal only the selected branch(es) — not all branches. Flag if you'd rather show the branch in isolation, without the parent row.

**Scale note (flag only, not to build now):** in the prototype this filters whatever is currently rendered/loaded client-side. At real scale (10k+ requirements, per `SPEC-backend-requirements.md` §5), a scattered selection may span rows the client hasn't fetched — production would likely need a "fetch by ID list" backend call rather than a pure client-side filter. Worth keeping in mind for the backend spec later; doesn't block the prototype.

---

## Feature 2 — Keyboard Row Navigation

**What it does:** arrow keys move focus row by row, keeping the same column — the standard spreadsheet "active cell" behaviour.

**New concept needed:** an **active cell** (row × column), visually distinct from row selection (the checkboxes). This doesn't exist yet in the prototype and needs a visible focus indicator — reuse the same **accent-coloured focus ring** already used on Text Input's Focus state, applied at the cell level.

**Interaction:**
- **Up / Down** — move the active cell to the same column, previous/next **visible** row (i.e. whatever's currently rendered, respecting current sort/filter — including a Filter-to-Selection view if one is active). Auto-scrolls the target row into view if it's outside the viewport.
- **Left / Right** — move the active cell to the adjacent column, same row. *(You only asked for vertical navigation — this is a natural extension since you're already tracking column focus. Flag if you'd rather skip it and keep Left/Right for something else, e.g. text-cursor movement only.)*
- **Traversal includes expanded rows.** If a multi-allocation parent is expanded, Up/Down step through its visible branch sub-rows too, in the order they're displayed on screen.
- **Checkbox column.** When the active cell is on the checkbox column, **Space** toggles that row's selection.

**Open decision — interaction with edit mode.** Arrow keys should only navigate rows when the active cell is **not** currently being edited. Default proposed (standard spreadsheet convention):
- While a cell is in **Editing** state (per the Editable Cell molecule), arrow keys move the **text cursor inside the input**, they do not change rows.
- **Escape** cancels the edit and returns focus to the cell (no row change).
- **Enter** confirms the edit **and** moves the active cell down one row, same column — lets you type down a column quickly, like a spreadsheet.

Flag if you'd rather Enter just confirm-in-place without moving, or if arrow keys should always navigate rows even mid-edit (less standard, but simpler to build).

---

## Build & verify

1. Edit `revue-documentaire.html` only.
2. Run `build_merge.py`.
3. `node --check` on the last touched script block.
4. Run the jsdom dead-link checker — 0 dead hrefs required.
5. Copy the rebuilt `docreview-app.html` to the outputs location as usual.

## Open decisions to confirm (summary)

1. Filter-to-selection vs. existing column filters — **suspend** (proposed) or **compose**?
2. Filter-to-selection on a selected branch sub-row — show **parent row for context** (proposed) or **isolated branch only**?
3. Left/Right column navigation — **build it** (proposed) or **skip it**?
4. Enter during edit mode — **confirm + move down** (proposed) or **confirm in place**?
