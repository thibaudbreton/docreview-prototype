# SPEC — Expert follow-up

> Derived from the prototype's actual behaviour, per `docs/prompts/PROMPT-derive-specs-from-prototype.md`. Describes "Screen 2" (`#screen2`, `state.screen===2`) of `suivi-experts-et-versions.html` as built — the Follow-up half of the file; the Versions & Q&A half ("Screen 3") is `docs/specs/SPEC-versions-qa.md`. Split along the file's own `screen:2`/`screen:3` boundary and its two top-nav tabs, matching `HANDOVER.md`'s own "Expert follow-up + Versions & Q&A" description. Cross-references `docs/specs/SPEC-domain-model.md` (allocated activities, statuses, compliance) and `docs/specs/SPEC-review-table.md` (the shared table component) — does not restate either.

## 1. Purpose

The activity manager's/project manager's tracking view for expert responses: which assignments (allocated activities) are answered, waiting, blocked on the issuer, or bounced back for reassignment, and a consolidated per-requirement compliance read. Serves the manager's "where does this tender stand, and what needs me right now" question, and is the internal (non-issuer-facing) half of the Q&A loop.

## 2. Actors

- **An activity manager**, the primary user — the "Viewing as" selector (see §6) simulates whichever manager is currently using the screen, defaulting to the first seeded manager and scoping the table to their own team by default.
- **The project manager**, implicitly, since nothing here is actually gated by role — anyone can switch "Viewing as" to any manager or lift the own-team scope.
- **Experts** never use this screen directly — their actions (answering, raising a question, returning an assignment) arrive as already-updated allocated activity state, either hand-seeded or pushed here from `expert-space.html` via the shared reassignment-request mailbox (§8).

## 3. Entry points

- The "Follow-up" tab in the shared screen-nav, present in this file's own header — always open (TE2; no longer gated on Allocation being finalized).
- The Dashboard's "Expert follow-up" phase card (`SPEC-dashboard.md` §6).
- The Dashboard's overdue-response attention item and Q&A-related attention items route here directly.

From here: the "Versions & Q&A" tab (`SPEC-versions-qa.md`); "↪ Reassign" jumps within this same screen; "⇗ Escalate to client Q&A" moves an allocated activity into this screen's own Q&A-register view (not into Screen 3 — see §6).

## 4. Layout

- **Header** (shared) — logo, breadcrumb, screen-nav (Follow-up / Versions & Q&A), a 3-way mode switch (Table / Document / Q&A) scoped to this screen only, notification bell, Export button, Configuration icon, avatar.
- **Triage bar** — a consolidation progress readout, 6 status quick-filter pills (answered / awaiting answer / awaiting Q&A / reassignment needed / overdue / outdated version), a clear-filter button, a "remind all overdue" button, a By-section/By-expert nav toggle, and keyboard-shortcut hints.
- **Left nav** (collapsible) — either a document/section hierarchy (grouped by source document, then section, then requirement) or a per-expert card list, depending on the nav toggle.
- **Center** — one of three views (Table / Document / Q&A register), switched by the header's mode switch.
- **Right detail panel** (collapsible) — the selected requirement/allocated activity's full detail, in three tabs (Assignment / Activity / Requirement).
- **Bulk action bar** — appears once ≥1 row is selected in Table view.

## 5. Data displayed

All from `REQS`, a **allocated-activity-level** array (`SPEC-domain-model.md` §1): each requirement carries one or more allocated activities, each with its own activity, manager, expert, status (`proposed`/`assigned`/`awaiting_answer`/`awaiting_qa`/`reassignment_needed`/`answered`), and — only once answered — a compliance verdict (`compliant`/`rnd_needed`/`not_compliant`). `EXG-003` (3 allocated activities) and `EXG-007` (2 allocated activities) mirror the same multi-activity requirements seeded on the Allocation screen, so both screens tell the same story.

- **Triage bar** — consolidated-count/total and a progress fill (per requirement, computed by `consolidate()`); 6 live pill counts (per allocated activity, except the outdated-version count which is per requirement).
- **Nav, by section** — grouped by source document (2 documents, mirroring the Allocation screen's own document set) then section then requirement, each item showing a compliance/pending dot and, for multi-activity requirements, an allocated-activity-count badge; items not matching the active filter are dimmed rather than hidden.
- **Nav, by expert** — one card per expert: answered/pending/blocked allocated activity counts, a mini progress bar, and (if any allocated activity is overdue) an overdue-count-plus-silence-duration line.
- **Table view** — one row per requirement (allocated activities collapse into "Multiple (N)" cells unless a filter narrows to specific allocated activities, in which case matching allocated-activity sub-rows expand beneath their parent), columns: ID, requirement/assignment text, activity, expert, manager, status, last follow-up date, age in days. A single consolidated status pill per row: the verdict once answered, a distinct "Pending" pill (with an allocated-activity-remaining count for multi-activity rows) while incomplete, or a "⛔ Reassignment needed" chip when that's what's blocking.
- **Document view** — a read-only paper-styled rendering of every requirement grouped by section, each tagged with its consolidated compliance/pending state.
- **Q&A register view** — see `SPEC-followup.md` §6's own description below; this is the same screen's third mode, not the separate Screen-3 issuer-facing view.
- **Right panel** — the selected allocated activity's assignment (expert, manager, status), and one of three tab bodies: Assignment (response note + evidence + escalate action, or the Q&A/reassignment-specific UI described in §6, or a "waiting" state with a remind action), Activity (a synthesized timeline of that allocated activity's own status history), or Requirement (frozen characterisation/allocation summary plus the read-only source passage).

## 6. Interactions

- **Filter by triage pill** — click toggles that status filter on/off; only one active at a time. *Implemented.*
- **Switch nav grouping** (By section / By expert) — re-renders the left nav. *Implemented.*
- **Switch view** (Table / Document / Q&A) — swaps the center pane; the header's Export button and mode switch itself stay visible only in Follow-up. *Implemented.*
- **Select a requirement or allocated activity** (nav item, table row, document block, expert card) — opens it in the right panel, defaulting to whichever allocated activity is blocking consolidation. *Implemented.*
- **"Viewing as" + "My team only"** — switches which manager's allocated activities are the default scope; the chip's ✕ lifts the scope to show every team, same mechanism as any other column filter (`SPEC-domain-model.md` §7's B5 resolution: a liftable UI default, not an access restriction). *Implemented.*
- **Search / filter by expert or activity / sort / "needs my action"** — client-side filters and sort orders over the same row set; "needs my action" surfaces reassignment requests plus allocated activities the issuer just unblocked. *Implemented.*
- **"What needs you now"** — a standing summary of the three manager to-dos (reassignments, questions ready to send, just-unblocked allocated activities), each clickable straight into the matching filtered view. *Implemented.*
- **"Compliance matrix complete" banner** — shown once every requirement is consolidated, linking to Export; otherwise shows a remaining count. *Implemented.*
- **Bulk-select rows, "Show only selected," "Send reminder," "Reassign expert"** — the shared table-engine (`table-engine.js`) bulk mechanics, this screen's own action set. "Send reminder" stamps `lastFollowup="Today"` on every awaiting-answer allocated activity of each selected requirement; "Reassign expert" jumps to the first selected row's detail panel rather than acting in bulk (a single-row action, entry point only). *Implemented.*
- **Keyboard** — J/K (aliases for Up/Down row navigation via the shared active-cell mechanism), R (remind, on the selected allocated activity), Q (escalate to Q&A, on the selected allocated activity) — active only in Table view. *Implemented.*
- **Reminder (single allocated activity or bulk)** — a toast confirming who was reminded; **represented/backend-dependent** — no real email is sent (`SPEC-backend-requirements.md` FR7).
- **Reassign an allocated activity in `reassignment_needed`** — pick a new manager/expert, allocated activity returns to `awaiting_answer` at age 0; if the allocated activity's reassignment originated as a live request from Expert Space (not the hand-seeded comment), the shared mailbox entry is marked `approved`. *Implemented*, the internal loop (`SPEC-domain-model.md`'s T5/reassignment-needed state) — stays inside the company, distinct from the Q&A loop below.
- **Escalate an allocated activity to Q&A** (from an answered allocated activity's detail, or the `Q` shortcut) — creates a new draft question in *this screen's own* Q&A register (not Screen 3), and if a specific allocated activity is targeted, moves it to `awaiting_qa`. *Implemented.*
- **Q&A register — send batch to issuer** — every draft/internal-review question moves to `sent`. *Implemented*, still entirely internal to this screen; nothing here contacts a real issuer (that handoff is represented on Screen 3 — see `SPEC-versions-qa.md`).
- **Q&A register — upload answer dossier & match** — simulates matching every already-`sent` question to its blocking allocated activity(es), moving each matched allocated activity from `awaiting_qa` back to `awaiting_answer` at age 0. **Represented/backend-dependent**: the matching step itself is explicitly simulated in the code (a comment states as much) — every sent question is simply treated as answered and matched by its already-known allocated activity link, not by any real question/answer text matching (`SPEC-backend-requirements.md` doesn't specify this pipeline in detail; the domain model's T8 describes the intended behaviour this simulates).
- **Q&A register — merge suspected duplicate questions** — an AI-detected duplicate pair (hand-seeded, always the same two questions in this build) can be merged or kept separate; merging carries over the allocated activity link the merged-away question was blocking. **Represented/backend-dependent** — the "detection" is a fixed seed condition, not a live similarity check.
- **Nav/detail panel collapse** — independent collapse toggles for the left nav and right panel. *Implemented*, same pattern as the Allocation screen.
- **Header "Export"** — generates a single fixed-name file ("Compliance register STB-2026_qualification.xlsx generated"), followed 800ms later by a toast summarizing non-compliant and still-pending counts computed live from `REQS`. **Represented/backend-dependent** — no real file is produced (`SPEC-backend-requirements.md` FR29). Distinct from the Allocation screen's own Export, which offers a modular step×format picker (`SPEC-review-table.md`) — this screen's Export is a single fixed action with no options, not a smaller instance of the same component.

## 7. States

- **Empty table** — "No assignment matches the current view." when every allocated activity is filtered out.
- **Empty nav groups** — implicit; a section with a fully-filtered-out requirement list still shows its dimmed entries rather than disappearing (dimming, not hiding, is deliberate — see §8).
- **No selection** (right panel) — an icon, "No assignment selected," plus the same consolidated/overdue counts shown in the triage bar.
- **Per-allocated activity detail states** — answered (verdict + note + escalate action), awaiting Q&A (blocked-on-issuer note + link to the register), reassignment needed (the reallocation form), and waiting (a plain "no response yet" note + remind action) are each fully designed, not stubs.
- **Q&A register — empty batch** — "Nothing waiting — every raised question is already with the issuer."
- **Loading / error** — not present; nothing here depends on a request that could fail.

## 8. Business rules

- **Status (progress) and compliance (result) are two separate axes** — `awaiting_qa` is a progress state, never itself a verdict, and it blocks consolidation exactly like `awaiting_answer` does (`SPEC-domain-model.md` §2–§3).
- **Consolidation is derived, not hand-written** — unlike the Allocation screen's rollup, this screen computes `consolidate(r)` live: pending until every allocated activity is `answered`, then the most restrictive verdict wins (`CMP_ORDER`). This screen is the one place in the corpus where the multi-activity rollup is genuinely computed rather than seeded.
- **The two loops must never be confused**: reassignment (`reassignment_needed`) is internal — it never leaves the company, and its resolution is picking a new manager/expert; the Q&A loop (`awaiting_qa`) is external — its resolution runs through the register and, eventually, the issuer (Screen 3). Distinct visuals (a warning chip vs. a blocked-note panel) and distinct actions enforce this.
- **A question is a first-class object linked to an allocated activity** (`branchRefsOfQ`), not free text attached to a status — a merged duplicate carries its blocking link over via `extraBranches` so no allocated activity is silently orphaned from having a question to unblock it.
- **"Needs my action" is a specific, bounded set**: reassignment requests, plus allocated activities whose blocking question was just answered and are now back with the expert — not every open item, just the ones the manager, specifically, must act on next.
- **Dimming, not filtering, in the nav** — a requirement that doesn't match the active filter stays visible (dimmed) in the section/document nav rather than disappearing, so the document structure itself is never broken up by a filter; the table view, by contrast, does remove non-matching rows entirely. This is a deliberate difference between the two views, not an inconsistency to reconcile.

## 9. Non-functional

Table rendering, filtering, and the active-cell keyboard navigation reuse `table-engine.js`, the same shared mechanism as the Allocation screen — no separate performance characteristics are introduced here; the row count in this build (14 requirements, ~17 allocated activities) is far below anything that would exercise virtualisation (which this screen doesn't have at all — only the Allocation screen's scale-test path does; see `SPEC-review-table.md`).

## 10. Placeholders & gaps

- **Notification bell and avatar are unwired**, same cross-screen pattern noted in `SPEC-dashboard.md` §10.
- **"Show only selected" plus a bulk "Reassign expert" click doesn't actually reassign anything in bulk** — it jumps to the first selected row's own single-activity reassignment form. The button's label ("Reassign expert") doesn't distinguish this from a true bulk action; a user could reasonably expect all selected rows to be reassignable at once. This may be intentional scope (reassignment is inherently a per-activity judgment call, not a batchable one) rather than an unfinished feature — flagged rather than assumed.

## 11. Open points

- The **duplicate-question AI-detection** is always the same fixed pair in this build; there's no way to tell from the code alone whether a real implementation would detect duplicates continuously (as new questions are raised) or only in a batch pass — not specified anywhere in the corpus.

Note: an earlier draft of this section asked whether "send batch to issuer" is meant to connect to Screen 3's Issuer-responses list — it does. Both this screen's Q&A register and `SPEC-versions-qa.md`'s Issuer-responses list read and write the same in-memory `QA` array; a question sent from here genuinely appears there, and recording an issuer answer there genuinely unblocks the allocated activity here. See `SPEC-versions-qa.md` §8.
