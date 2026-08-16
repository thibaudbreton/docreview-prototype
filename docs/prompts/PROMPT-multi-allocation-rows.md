# Claude Code prompt — Expandable multi-allocation rows (PROTOTYPE / UI-only)

> Paste this as the task. Context: the existing **throwaway prototype** (5 source HTML files + `build_merge.py`; review screen in `revue-documentaire.html`). **There is no backend.** This is for **user testing the UI only** — the user will be able to manipulate the rows, but nothing is computed. See `SPEC-domain-model.md` for the concepts (branches, compliance scale) and `SPEC-review-table.md` for the table intent — but do NOT build the real domain logic.

---

## What this is (and is NOT)

A requirement can have **several allocations in parallel** — one "branch" per typology, each with its own manager, expert, branch status and compliance. The Requirement Manager needs to **follow and manipulate** these branches in the review table.

Build **Option B — expandable rows**: a **consolidated** row by default that **expands into one sub-row per branch**.

**This is UI-only, for a moderated user test:**
- **Do NOT compute anything.** No derivation of status, no "most restrictive wins" calculation, no cascade. The consolidated values are **written by hand in the demo data**.
- **Manipulation = local visual feedback, not logic.** When the user edits a branch cell (e.g. changes an expert), update that cell's display and give immediate feedback. Do **not** recompute the parent from the branches. If you want the parent to *appear* to react for a specific demo path, hard-code that single scripted response — but keep it dumb.
- Keep it **light and disposable** — this proto is thrown away and rebuilt in the target stack later. Do not add a data layer.

---

## Demo data (hand-authored, pre-consolidated)

In `revue-documentaire.html`, give **2–3 requirements** a `branches` array where **every value is written explicitly**, including the consolidated values shown on the parent row. Nothing is derived.

```
requirement = {
  ... existing fields ...,
  branches: [
    { typology, manager, expert, branchStatus, compliance },
    ...
  ],
  // consolidated values, WRITTEN BY HAND (not computed):
  rollupStatus,        // what the collapsed row shows
  rollupCompliance,    // "compliant" | "rnd_needed" | "not_compliant" | "pending"
  blockingBranch,      // index or label of the branch to surface as "what's blocking"
}
```

Author at least one rich example: a **Turnkey** requirement with **3 branches** (e.g. SIG & Urban, Mainline Wayside, Safety) where:
- one branch is **answered / not_compliant**,
- one is **awaiting** (compliance pending),
- one is **reassignment_needed**,
- and the hand-written `rollupCompliance` is **"pending"** (because not everyone answered) with `blockingBranch` pointing at the reassignment one.

Keep all other requirements single-branch (no `branches` array, or a 1-element one) so they render exactly as today.

## The collapsed row (default)

- Show a **caret + "×N" badge** only when there is more than one branch. Single-branch rows are unchanged — no caret, no visual regression.
- **Manager / Expert cells:** show a muted **"Multiple (N)"**.
- **Status cell:** show `rollupStatus` (the hand-written value).
- **Compliance cell:** show `rollupCompliance`, with a **clearly distinct "Pending" state** — it must NOT look like a decided verdict. This is the single most important visual point: a pending requirement must never read as "Not compliant decided".
- **Blocking hint:** surface `blockingBranch` compactly (small marker / icon + tooltip, e.g. "Safety — reassignment needed"). The RM's job is spotting the stuck branch at a glance.

## The expanded state (click the caret)

Insert **one sub-row per branch** directly under the parent (reuse the existing collapsible-group pattern in `buildVRows()` / `VROWS`):

- Each sub-row shows: **typology**, **Manager** (editable inline), **Expert** (editable inline), **branch status**, **branch compliance** (editable inline).
- Sub-rows are indented / tinted so they read as children, not standalone requirements.
- **Editing a branch cell** updates that cell only (local visual change + a toast/feedback). No recomputation of the parent. (Optional: if you want a specific scripted demo where the parent visibly reacts, hard-code just that one path and comment it clearly as scripted.)
- Expansion state lives in `state` (a Set of expanded requirement ids), survives re-render, and is cleared by reset-demo.

## Implementation notes (fit the existing code)

- Add a `"branch"` row type to `VROWS`. When a requirement id is in the expanded set, push its branch rows right after its `"row"` entry in `buildVRows()`.
- Render `"branch"` rows in `renderReview()`'s `rowHTML()`; bind their inline editors in `bindVRows()`, reusing the existing manager / expert editor patterns and the status/compliance controls.
- Apply this only on the **normal full-render path**. In the scale-test path (`BIG.on`, windowed 12k rows) keep rows consolidated / non-expandable — synthetic rows stay single-branch.
- Keep nature checks on `blockNature(b)`.
- Single-branch requirements must be untouched visually and behaviourally.

## Acceptance criteria

- Single-allocation requirements look/behave exactly as today (no caret).
- Multi-allocation requirements show caret + "×N", the hand-written rollup status, and a **Pending** compliance that is visually distinct from a real verdict.
- Clicking the caret reveals one editable sub-row per branch; editing a branch cell updates that cell with feedback (no cascade required).
- The blocking branch is visible from the collapsed row.
- Reset-demo collapses all and restores the seeded branches.

## Build & verify (unchanged workflow)

- Edit the **source** files only (`revue-documentaire.html`); never the merged file.
- `python3 build_merge.py`.
- Verify: `node --check` on the changed screen's last `<script>`; each base64 blob decodes as UTF-8; **0 dead `href="*.html"` links**; a quick **jsdom** check (expand pushes N branch rows; editing a branch cell updates it; collapsed row shows the hand-written rollup + Pending state). Puppeteer does not work here — use jsdom.
- Copy changed sources next to `docreview-app.html` in the output.
