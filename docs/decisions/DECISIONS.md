# Decisions log

Append-only. Each entry: what was decided, what it replaced (if anything), why (when known — "reason not recorded" is used rather than invented), and where the full detail lives. This log indexes decisions that **changed a previously-written spec or model**; day-to-day feature build tickets that didn't overturn anything stay in their own ticket files rather than being duplicated here (see `docs/tickets/` and `docs/archive/`).

Ordered chronologically, oldest first, by apparent build order (not always exact calendar dates — see `docs/INVENTORY.md` for the age evidence behind each entry).

---

### D1 — Multi-allocation rows: UI-only, no derivation engine (supersedes the Option-B derivation prompt)
**What:** the expandable multi-allocation-rows feature was built with hand-authored consolidated values (`rollupStatus`, `rollupCompliance`, `blockingBranch` all written directly in seed data), not computed by a derivation engine.
**Replaced:** an earlier build prompt (`PROMPT-multi-allocation-rows.md`) that specified real "most restrictive wins" derivation logic running against a `branches` array.
**Why:** the revised prompt (`PROMPT-multi-allocation-rows_1.md`) states this explicitly — the prototype is disposable and for UI-only user testing; computing real derivation is target-stack work, not prototype work.
**Source:** `PROMPT-multi-allocation-rows_1.md`; implemented per the working task history (branches demo data, expandable sub-rows).

### D2 — Rename Document Review → Allocation; four typology-hierarchy phases
**What:** the "Document review" phase/screen concept was renamed "Allocation" everywhere in the UI, and the "Fully manual" preset was removed from project creation.
**Replaced:** the original "Document review" naming.
**Why:** user-interview finding — the name didn't match how users described the activity.
**Source:** `DEBRIEF-user-interview.md` finding; ticket 3 in `SPECS/TICKETS-continuity-fixes.md`.

### D3 — Status vocabulary split into two axes: characterisation/allocation progression vs. compliance
**What:** requirements now carry a 4-value progression status — **Incomplete → To review → To validate → Allocated** — separate from the compliance axis (`compliant`/`rnd_needed`/`not_compliant`).
**Replaced:** an earlier single conflated "status" notion that mixed AI-confidence and workflow state.
**Why:** user-interview finding — AI-confidence and workflow-status need to be visually and structurally separate.
**Source:** `DEBRIEF-user-interview.md` finding; `SPECS/SPEC-domain-model.md` §8.2 (B6/B7 tickets).
**Note:** the exact labels are **Incomplete / To review / To validate / Allocated** — not "Doubt" or "Valid." Any document using those older informal names is describing this same model with stale wording.

### D4 — Image model: auto-created requirement row, container model dropped
**What:** an image now auto-creates **one requirement row** attached to it; the user can duplicate that row for images containing several requirements (e.g. tables). No sub-type declaration, no container/folder.
**Replaced:** the earlier container/folder model — an image as a parent container, open by default, with typed requirements nested inside it.
**Why:** reason not recorded in the surviving corpus beyond "supersedes" — the ticket states the replacement directly without elaborating the original container model's shortcomings.
**Source:** `TICKETS-review-expert-batch4.md` (B9): *"This supersedes `SPEC-image-container-requirements.md`. ... Delete that model from the spec."*
**Note:** `SPEC-image-container-requirements.md` was not found anywhere in the corpus during this cleanup — either already deleted per this instruction, or its content never existed as a standalone file. `SPECS/SPEC-domain-model.md` and `SPECS/SPEC-review-table.md` currently contain no trace of the container model, confirming the new model is what's actually live.

### D5 — Casting becomes async and ongoing, not one-shot (B2)
**What:** the project manager assigns branch managers per activity at project creation; each branch manager then fills in their own experts **asynchronously, at their own pace**, via an email-notified flow. The project dashboard shows a completion-progress indicator for this step.
**Replaced:** the original domain-model decision that casting is filled in one pass at project creation.
**Why:** accepted trade-off — delaying the start of analysis is intended, not a bug to design around.
**Source:** `TICKETS-manager-features-batch2.md` (B2), explicitly flagged there as overriding the prior decision; applied to `SPECS/SPEC-domain-model.md`.

### D6 — Locked compliance is excluded from "most restrictive wins" consolidation (B3)
**What:** when a project manager overrides and locks a compliance verdict, that branch's locked value is excluded from cross-branch consolidation — otherwise another branch's later answer could silently override an explicitly locked verdict.
**Replaced:** nothing directly, but required a small addition to the compliance-consolidation rule in the domain model (an unstated edge case became stated).
**Why:** stated directly in the ticket — without the exclusion, locking would be defeated by consolidation.
**Source:** `TICKETS-manager-features-batch2.md` (B3); `SPECS/SPEC-domain-model.md` compliance-model section.
**Still open (not resolved here):** whether the project manager can unlock a verdict later. Ship was lock-only; do not build an unlock path until confirmed.

### D7 — Typology hierarchy is a permissions-only concept, scoped to Expert Space only for this build (TF2)
**What:** typologies can nest to arbitrary depth for **permission cascade** only (a manager/expert on a parent typology gets view+modify on descendants) — it has no effect on characterisation, allocation, or compliance consolidation. Implemented in `expert-space.html` only; the other three screens keep an independently-authored flat typology vocabulary.
**Replaced:** nothing prior — this is the first explicit statement of the hierarchy's scope and limits.
**Why:** extending the hierarchy to all four screens (plus `dashboard-et-config.html`'s team-scoping) is a real feature addition across four files' data models, judged out of scope for this prototype phase.
**Source:** `SPECS/SPEC-domain-model.md` §9, §9.0.

### D8 — R&D Needed stays a first-class, countable compliance value, including at expert entry (TF3)
**What:** the expert verdict form has **three** buttons — Compliant / R&D Needed / Not compliant — matching the canonical 3-value scale (`compliant`/`rnd_needed`/`not_compliant`) already implemented structurally in the review table and follow-up screens.
**Replaced:** an earlier, explicitly self-contradictory state of `SPECS/SPEC-domain-model.md` §9 that simultaneously asserted the expert verdict form was "already final at two values: Compliant / Not compliant" while calling R&D Needed's status "still open." **This also supersedes `SPEC-expert-space.md`'s two-value compliance description** ("compliance has exactly two real values: Compliant / Not compliant... R&D Needed is NOT a status... this was an explicit choice, not an omission") — see the discrepancy noted below.
**Why:** stated directly in the resolution — a rail-tender compliance matrix commercially needs to distinguish "compliant as-is" from "compliant pending R&D investment," which only a countable value serves; the two-value form would have made the review table and follow-up screens' already-shipped structured handling of `rnd_needed` pointless downstream.
**Source:** `SPECS/SPEC-domain-model.md` §9.2 (TF3), which narrates the self-contradiction and its resolution directly.

> **⚠ Flag — this decision conflicts with an assumption in the cleanup task's own brief.** The prompt driving this cleanup (`docs/prompts/PROMPT-specs-cleanup.md`) lists as a "known case to verify": *"'R&D needed' is no longer a compliance value — compliance has exactly two: Compliant / Not compliant."* That is the **opposite** of what actually happened. TF3 (recorded directly above, in `SPEC-domain-model.md` §9.2, with explicit reasoning) resolved the question the other way, and the shipped code (`expert-space.html`'s three-button verdict form, `COMPLIANCE_LABELS`, `CMP_ORDER`) matches the three-value outcome, not the two-value one. Per the cleanup prompt's own resolution rule ("an explicit statement, or a later file that contradicts an earlier one" outrank a filename-similarity guess), TF3 is the clearly-later, clearly-reasoned, code-matching side — so this decisions log treats **three values (with R&D Needed countable) as current truth**, and `SPEC-expert-space.md`'s two-value description is archived as superseded (see `docs/archive/`). This isn't this cleanup resolving a live product question by picking a side; TF3 already resolved it before this cleanup started. What's being flagged here is that the cleanup brief's own premise on this specific point was stale.

### D9 — Information rows carry no fields beyond their category; category is user-correctable (B8)
**What:** the allocation table shows `heading` / `information` / `requirement` rows (heading replaces "title," same thing renamed). Information rows have no typology, allocation, compliance, or status — category is their only attribute. Users can reclassify any row between the three categories; `information → requirement` lands on `Incomplete`; `requirement → information` deletes any existing allocation.
**Replaced:** an implicit assumption that only requirement rows appear in the table.
**Why:** reason not recorded beyond the ticket's own statement of the rule.
**Source:** `TICKETS-review-expert-batch4.md` (B8).

### D10 — Reassignment is a request from either side, always PM-approved, three fixed reasons (B10)
**What:** either the Expert or the Branch Manager can raise a reassignment request (right typology/wrong person; wrong typology; activity doesn't apply here); all routes require Project Manager approval before taking effect. Reallocation is always a replacement — a requirement can never end up with zero activities.
**Replaced:** the earlier B1 ticket, which routed only manager-raised proposals to the PM; this generalizes the same approval path to expert-raised requests too (aligning, not overriding, B1).
**Why:** stated directly — "aligns the expert-side loop with B1... both now follow the same approval path."
**Source:** `TICKETS-review-expert-batch4.md` (B10).

### D11 — Two-surface model for Expert Space: table = own work only, document = fully readable (B11)
**What:** the table (decision surface) stays scoped to the expert's own typology + descendants; the source document (context surface) is readable in full, with no click-through to act on other requirements.
**Replaced/clarifies:** `SPEC-expert-space.md`'s original strict-restriction statement is confirmed correct for the table, but incomplete — it didn't address document readability at all.
**Why:** stated directly — "this clarifies rather than reverses `SPEC-expert-space.md`."
**Source:** `TICKETS-review-expert-batch4.md` (B11).
**Status: not yet implemented.** This decision is recorded as the intended design; the corresponding build (two-surface UI in `expert-space.html`) and the spec updates to `SPEC-expert-space.md` and the backend-requirements doc's restricted-view section are still open work (see `docs/tickets/`).

### D12 — Dashboard KPIs, overdue alert, and Finalize modal computed from live data, not hardcoded (TB1–TB5)
**What:** dashboard KPI numbers, the "expert responses overdue" alert, and the Finalize allocation modal are all derived from the actual seeded requirement/branch data (`REVIEW_REQS`, `FOLLOWUP_REQS`, `OVERDUE_BRANCHES`, `SECTIONS`) instead of being hand-typed into the markup.
**Replaced:** hardcoded KPI/alert/modal markup that could silently drift from the demo data it was supposed to reflect.
**Why:** continuity/consistency bug fixes — the hardcoded numbers had already drifted from the seeded data (e.g. a false "2 experts overdue" alert with no actual overdue branches in the data).
**Source:** `SPECS/TICKETS-continuity-fixes.md`, groups TB (full per-ticket detail lives there — this entry only indexes that it happened, since the ticket file already carries the complete write-up).
**Note on a real bug caught mid-flight:** an early implementation of the response-rate KPI computed 6/16 = 37.5%; the correct denominator is 15 branches (one requirement has 3 branches, one has 2, the rest have 1 each), giving 6/15 = 40%. Corrected in the same ticket group.

### D13 — Compliance canonical keys and wording (TD1)
**What:** the canonical compliance keys are `compliant` / `rnd_needed` / `not_compliant`, with `SPEC-domain-model.md` §3.1 as the single source for the wording.
**Replaced:** ad hoc wording in earlier ticket text (e.g. `TICKETS-followup-workflow.md` T2 originally spelled out "Compliant / Compliant with R&D / Non compliant" inline).
**Why:** reason not recorded beyond consolidating to one canonical source instead of restating the scale in every ticket.
**Source:** `SPECS/SPEC-domain-model.md` §3.1; cross-referenced (with a strikethrough correction) from `SPECS/TICKETS-followup-workflow.md` T2.

### D14 — Real RFP capture data replaces synthetic seed data, with a hand-set demo status distribution
**What:** the review table is fed from `window.SRM_DATA` (built by `import_capture.py` from the real `.xlsx` captures) when present, falling back to `buildBigData(n)`'s synthetic generator when absent. Per-row characterisation/allocation values have no captured equivalent and are not invented; for the imported rows actually used in the demo, a hand-set distribution was applied on top for demo purposes (roughly 80% "To validate" at high AI confidence, 18% "To review," the remainder "Incomplete").
**Replaced:** the table's prior sole reliance on `buildBigData(n)`'s fabricated rows for demo content.
**Why:** user testing should run on genuine tender content, not generated placeholder text; the demo status distribution was requested separately to make the workflow's status filters demonstrable without overstating what the (real, but uncharacterised) capture data actually contains.
**Source:** `TICKET-wire-capture-data.md`; applied via `buildDataFromCapture()` / `applyCaptureDemoStatuses()` in `revue-documentaire.html`.

---

## Discrepancies noted but not resolved here (need a human)

- **"One user-stories file supersedes an earlier sample"** — a known case named in `docs/prompts/PROMPT-specs-cleanup.md`, but no matching pair of files was found anywhere in the corpus during the Step 1 inventory. The only "user stories" content found is a single, non-duplicated section inside `SPECS.md` (5 roles). This known case could not be verified against any actual file and is not acted on.
- **`SPEC-review-table-batch3.md`** — referenced by `TICKETS-review-expert-batch4.md` as the ticket file B1–B7 continue numbering from. Not found anywhere in the corpus. Its content may be fully absorbed into `SPECS/SPEC-review-table.md`, but this is not confirmed.
- **`NIGHTLY-TICKETS.md`** — referenced by both nightly-routine prompts as the queue file they read from. Not found anywhere in the corpus; the actual ticket queue that was used (`SPECS/TICKETS-continuity-fixes.md`) is located by a different mechanism (heading match) in the revised prompt, suggesting the filename-based queue was abandoned at some point without a recorded reason.
