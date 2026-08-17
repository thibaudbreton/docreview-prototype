# Claude Code prompt — Expandable rows for multi-allocation requirements (Option B)

> SUPERSEDED by `docs/prompts/PROMPT-multi-allocation-rows.md` (the revised, UI-only version) on 2026-07-30. Kept for reference. Do not build from this — this version specifies real derivation logic, which is not what was built; see `docs/decisions/DECISIONS.md` (D1).

> Paste this as the task. It assumes the existing prototype (5 source HTML files + `build_merge.py`, review screen in `revue-documentaire.html`) and the specs `SPEC-domain-model.md` and `SPEC-review-table.md`. Read those two specs first for the model and the table intent.

---

## Goal

In the review table, a requirement can now have **several allocations in parallel** (one "branch" per typology — see `SPEC-domain-model.md` §2.2). The Requirement Manager must be able to **follow all branches of a requirement** without losing the clean "one row = one requirement" reading.

Implement **Option B — expandable rows**: each multi-allocation requirement shows a **consolidated** row by default and **expands into one sub-row per branch** on demand.

Keep single-allocation requirements behaving exactly as they do today.

---

## Part 1 — Data model (do this first)

Introduce a `branches` array on requirements. A branch is one line of responsibility:

```
branch = {
  id,               // unique within the requirement
  typology,         // the typology this branch covers (one of the TYPO values)
  manager,          // manager id (Bid-team person who handles the OBS) — editable
  expert,           // expert/OBS id (person who returns the verdict) — editable
  branchStatus,     // "proposed" | "assigned" | "awaiting" | "reassignment_needed" | "answered"
  compliance        // null (pending) | "compliant" | "rnd_needed" | "not_compliant"
}
```

Rules:
- **Normalize:** treat every requirement as having `branches`. A single-allocation requirement has exactly **one** branch (mirror its current `manager` / `alloc` / status into that single branch). A multi-allocation requirement has one branch per typology.
- Do **not** delete the existing single-value fields yet if other code depends on them; instead make the branch array the source of truth and keep the row cells reading from the consolidated derivation (Part 2). Refactor callers progressively.
- Seed **2–3 multi-branch requirements** in the demo data so the feature is visible (e.g. one Turnkey requirement with 3 branches: SIG & Urban, Mainline Wayside, Safety — with different branch statuses and compliances, including at least one branch still **pending** and one in **reassignment_needed**). Keep the rest single-branch.

## Part 2 — Consolidation (derived values)

Add helper functions that derive the requirement-level values from its branches. Follow `SPEC-domain-model.md` §5–§6 exactly:

- **Derived status** — from the branch statuses (e.g. any branch `reassignment_needed` → requirement shows `reassignment_needed`; else if any branch not `answered` → `awaiting_compliance`; etc.).
- **Derived compliance** — **most restrictive wins**: `not_compliant` > `rnd_needed` > `compliant`. BUT the overall compliance stays **pending** until **every** branch has answered (no branch with `compliance === null`). Single branch → that branch's value is the requirement's value, no derivation.
- **Blocking branch** — expose which branch is holding things up (the one in `reassignment_needed`, or the longest `awaiting`, or the most restrictive answered branch). This drives the "what's blocking" hint (Part 3).

These derivations must be **pure** (compute from branches, never store a stale copy) and must re-run whenever a branch changes.

## Part 3 — The consolidated row (collapsed state)

The default row keeps **one row = one requirement**. On a multi-branch requirement:

- Show a **caret / expander** and a small **"×N" badge** (N = number of branches) — only when `branches.length > 1`. Single-branch rows get no caret and look exactly as today.
- **Class / Typology cells:** typology shows the set of branch typologies (existing multi-tag display is fine).
- **Manager / Expert cells:** show a muted **"Multiple (N)"** rather than a single value (editing happens per branch when expanded).
- **Status cell:** show the **derived** status.
- **Compliance:** show the **derived** compliance, with a **visually distinct "Pending" state** when not all branches have answered — a pending requirement must NOT look like a rendered verdict. This is critical: never show "Not compliant" as if decided while a branch is still pending.
- **Blocking hint:** surface the blocking branch compactly (e.g. a small marker "Safety — reassignment needed" or an icon with tooltip). The RM's real job is spotting which branch is stuck, not admiring all of them.

## Part 4 — The expanded state (sub-rows)

Clicking the caret expands the requirement into **one sub-row per branch**, inserted directly under the parent (like the existing collapsible group pattern):

- Each sub-row shows: the **typology** of the branch, **Manager** (editable inline), **Expert** (editable inline), **branch status**, **branch compliance** (editable inline).
- Sub-rows are visually indented / tinted so they read as children of the parent, not as independent requirements.
- Editing any branch field **re-derives** the parent row immediately (status, compliance, blocking hint update live).
- The parent row stays visible above its expanded children.
- Expansion state lives in `state` (a Set of expanded requirement ids), survives re-render, and is cleared by reset-demo.

Implementation note: this fits the existing `buildVRows()` / `VROWS` model — add a new row type `"branch"` and, when a requirement is expanded, push its branch rows right after its `"row"` entry. Render them in `renderReview()`'s `rowHTML()` and bind their inline editors in `bindVRows()`, reusing the existing manager/expert/compliance editor patterns.

## Part 5 — Constraints (do not break these)

- **HITL preserved** — editing a branch is a human validation; no bulk action may auto-consolidate a verdict. Consolidation is computed, never auto-confirmed.
- **Single-allocation unchanged** — requirements with one branch must render and behave exactly as before (no visual regression, no caret).
- **Full-render path only** — expansion applies to the normal full-render table. In the scale-test path (`BIG.on`, windowed 12k synthetic rows), keep rows consolidated only (no expansion). Synthetic rows can stay single-branch.
- **`blockNature`, not raw `kind`** — keep any nature checks on `blockNature(b)` so image-as-requirement keeps working.
- **Bulk edits** — when a bulk action sets e.g. an expert, define and document the behavior on multi-branch rows (recommended: bulk applies to single-branch rows only, and multi-branch rows are edited per branch — but confirm the intended behavior in a comment).
- **Keep it readable at scale** — expanding many requirements at once should not tank the full-render path; if needed, only allow a reasonable number expanded or lazily render sub-rows.

## Part 6 — Acceptance criteria

- A single-allocation requirement looks and behaves exactly as today (no caret, inline edits work).
- A multi-allocation requirement shows a caret + "×N", a derived status, and a derived compliance that reads **Pending** until all branches answered.
- Expanding shows one sub-row per branch with editable manager / expert / compliance; editing a branch updates the parent's derived values live.
- The blocking branch is visible from the collapsed row.
- Derived compliance follows most-restrictive-wins, and never shows a verdict while a branch is pending.
- Reset-demo collapses everything and restores seed branches.

## Part 7 — Build & verify (unchanged workflow)

- Edit the **source** files (`revue-documentaire.html` for the table; seed data there). Never edit the merged file.
- Run `python3 build_merge.py`.
- Verify: `node --check` on the last `<script>` of the changed screen; confirm each base64 blob decodes as UTF-8; confirm **0 dead `href="*.html"` links**; use **jsdom** for behaviour (assert: derived compliance is Pending with one null branch; most-restrictive wins when all answered; expand pushes N branch rows; editing a branch re-derives). Puppeteer does not work here (no Chromium) — use jsdom.
- Copy changed sources next to `docreview-app.html` in the output.

---

## Reminder on scope

This is a heavier feature and touches the data model. If the prototype is still in the **user-testing phase**, consider whether the lighter **Option A** (consolidated row + branch list in the right-hand detail panel) is enough to learn from users first — Option B is the target-state pattern and is best built robustly in the target stack. Build B here only if you specifically want to test in-table branch editing.
