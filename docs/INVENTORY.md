# Documentation corpus inventory

Produced as Step 1 of the docs cleanup (see `docs/prompts/PROMPT-specs-cleanup.md` once moved). Lists every `.md` file found across the repo and the scattered locations the corpus turned out to live in (`~/Desktop`, `~/Downloads`), before any file was moved, renamed, or edited. Ages are apparent — from filesystem mtimes / git history, not confirmed authorship dates.

**Scope note:** the corpus is materially bigger than `SRM-PROTO/SPECS/` — 28 files total, spread across three locations. Nothing outside the git repo was previously tracked or backed up anywhere.

---

## A. Already in the repo (`SRM-PROTO/`)

| File | Subject | Apparent age | Overlaps / notes |
|---|---|---|---|
| `HANDOVER.md` | Project context, architecture, screen inventory, conventions for picking up the prototype cold | Continuously updated through 2026-08-13 (last touched by the automated ticket routine's TG1) | Living document, source of truth for "what is this repo." No overlap — nothing else covers this ground. |
| `README.md` | Same role as HANDOVER.md but shorter/public-facing | Updated alongside HANDOVER.md, through 2026-08-13 | Partial content overlap with HANDOVER.md by design (both describe the six screens) — not a contradiction, a summary/detail pair. |
| `SPECS/SPEC-domain-model.md` | The domain model: casting, branches, typology hierarchy, status vocabulary, compliance scale — continuously amended as tickets land (§9.2 is the newest section, TF3) | Oldest sections from early batch work; newest (§9.2) from 2026-08-13 | Central reconciliation target. Directly overlaps/contradicts `SPEC-expert-space.md` (compliance scale) and `SPECS.md` (backend requirements) — see Step 2 findings below. Cites `SPEC-backend-requirements.md` and `SPEC-expert-space.md` by name; §9.1 claims neither survives anywhere — **now known to be inaccurate**, see §C. |
| `SPECS/SPEC-review-table.md` | Target-state UX spec for the review/allocation table | Not recently amended relative to the domain model — reads as an earlier, stable document | Describes some behaviour still marked "(to validate)" as open — not fully overtaken by tickets. |
| `SPECS/TICKETS-continuity-fixes.md` | Ticket queue (groups TA–TG) for dashboard/finalize/data-wiring continuity bugs | All items now checked `[x]`, most recent 2026-08-13 | Functions as a de facto decisions log already — every ticket has a written resolution. Primary source for Step 3 (`docs/decisions/DECISIONS.md`). |
| `SPECS/TICKETS-followup-workflow.md` | Sequenced tickets (T1–T12) building the manager-side follow-up screen | Base content matches the Downloads copy; this copy carries one additional inline edit (T2's compliance line struck through, pointing to `SPEC-domain-model.md` §3.1) dated with the TD1 ticket | **Near-duplicate of `Downloads/TICKETS-followup-workflow.md`** — this repo copy is strictly newer (has the TD1 correction the Downloads copy lacks). Confirmed by diff: single-line difference, no other divergence. |

## B. Desktop

| File | Subject | Apparent age | Overlaps / notes |
|---|---|---|---|
| `PROMPT-specs-cleanup.md` | The one-off documentation reorganization prompt driving this exact cleanup | 2026-08-16 (today) | Tooling, not corpus content — belongs in `docs/prompts/` once this task is done. |
| `PROMPT-specs-maintenance.md` | Companion **recurring** routine prompt, assumes this one-off cleanup already ran; keeps `docs/` healthy going forward | 2026-08-16 (today) | Tooling, not corpus content — `docs/prompts/`. References `docs/DOC-HEALTH.md`, a file this cleanup does not produce (that's the maintenance routine's own job on its first run). |
| `SPECS.md` | "Backend SRM — Feature Specification": full production/backend requirements doc — 5 user-story roles, 29 functional requirements, performance/scale targets, integration requirements (DOORS, SSO, Q&A) | Undated internally; filesystem mtime 2026-08-10 | **Byte-identical to `Downloads/SPECS.md`** (confirmed via diff — zero output). Very likely the missing "`SPEC-backend-requirements.md`" that `SPEC-domain-model.md` §9.1/§9.2 and other tickets cite by name and describe as unrecoverable — see §C for why this can only be stated as "very likely," not confirmed identical. **Contains the real client company name twice — scrub before any copy leaves this file's original location.** |

## C. Downloads

| File | Subject | Apparent age | Overlaps / notes |
|---|---|---|---|
| `SPECS.md` | Duplicate of the Desktop copy above | mtime 2026-08-10 | Byte-identical to Desktop copy (diff confirmed empty). Same confidentiality note applies. |
| `AS-IS-workflow-map.md` | Pre-SRM workflow interview guide: roles, casting, capture, characterisation, expert review, consolidation, export today — heavily tagged `[A]/[B]/[?]` for confidence | mtime 2026-08-07 | Research category — evidence, not a spec. No client name found. Several of its "open questions" are now closed by later specs/tickets (see Step 2). |
| `DEBRIEF-user-interview.md` | User interview debrief: 8 numbered findings + interviewee profile | mtime 2026-08-06 | Research category. **Several of its findings are already implemented** in the prototype (rename Document Review→Allocation; four-value status split; Excel-parity filter/Enter behaviours) — this file is the *source* of decisions now recorded elsewhere, not itself superseded. No client name found. |
| `PERSONAS-srm-roles.md` | Three personas (fictional names), explicit confidentiality note already applied | mtime 2026-08-07 | Research category. Self-consistent, no client name — a model example of the confidentiality rule done right. |
| `PITCH-SRM.md` | 12-slide pitch deck content | mtime 2026-07-31 | Business/sales collateral, not functional documentation — doesn't map cleanly to any of the seven target `docs/` folders. Explicit internal confidentiality note; no client name found in content. See CLEANUP-REPORT for disposition. |
| `PITCH-SRM-slides.md` | Companion visual-direction/storyboard doc to `PITCH-SRM.md` | mtime 2026-07-31 | Same disposition question as `PITCH-SRM.md`. No client name found. |
| `SPEC-Design tokens.md` (note: space in filename) | Build prompt for colour/type/spacing/radius design tokens (full CSS variable blocks, dark+light) | mtime 2026-08-04 | This is a **build prompt fed to Claude Code**, not a living spec, despite the `SPEC-` prefix — work is already complete (see HANDOVER.md's rebrand entries). Belongs in `docs/prompts/`, renamed for consistency and to drop the filename's space. Superset of `SPEC-brand-colors.md` (same palette, plus typography/spacing/radius). |
| `SPEC-brand-colors.md` | Build prompt for the brand colour palette only | mtime 2026-08-03 | Subset of `SPEC-Design tokens.md` (colours only, same source palette, same structure) — earlier iteration. Also a completed build prompt, not a living spec. |
| `SPEC-expert-space.md` | Design spec for the Expert Space screen: typology hierarchy, compliance model, two open questions | mtime 2026-08-06 | **Confirmed direct contradiction** with `SPEC-domain-model.md` §9.2 on the compliance scale (two-value vs. three-value — see Step 2). Also self-describes as "a spec to validate, not yet a build prompt." Cites `SPEC-backend-requirements.md §11` and `§12` — see the `SPECS.md` entry above. |
| `PROMPT-filter-selection-keyboard-nav.md` | Build prompt: Filter-to-Selection + keyboard row navigation on the review table | mtime 2026-08-06 | Tooling/prompt category. `TICKETS-manager-features-batch2.md` (B5) explicitly widens this prompt's scope from one screen to shared table behaviour — read together. |
| `PROMPT-multi-allocation-rows.md` | Build prompt, Option B (full derivation logic) for expandable multi-allocation rows | mtime 2026-07-30 | **Two near-duplicate prompts for the same feature** — see next row. This one specifies real derivation/computation logic ("not UI-only"). |
| `PROMPT-multi-allocation-rows_1.md` | Build prompt, same feature, explicitly UI-only / no derivation, hand-authored consolidated values | mtime 2026-07-30 (same day) | The `_1` suffix and stated scope ("PROTOTYPE / UI-only... do NOT build the real domain logic") strongly suggest this is the **revised** version that superseded the first — a narrower, prototype-appropriate scope replacing a heavier one. Matches what was actually built (hand-authored branches, no derivation engine) per completed task #17 in the working task list. Treat `PROMPT-multi-allocation-rows.md` as superseded by `PROMPT-multi-allocation-rows_1.md`. |
| `PROMPT-nightly-ticket-routine.md` | Scheduled-routine prompt: works a `NIGHTLY-TICKETS.md` queue file by exact filename | mtime 2026-08-13 | **Two near-duplicate prompts for the same routine** — see next row. Neither `NIGHTLY-TICKETS.md` file exists anywhere in the corpus found. |
| `PROMPT-nightly-ticket-routine_1.md` | Same routine, revised to locate the queue file **by heading** (`# Tickets — Continuity & consistency fixes`) rather than by filename, plus a stricter checkbox-format guard | mtime 2026-08-13 (same day) | This matches the file that was actually used this session (`SPECS/TICKETS-continuity-fixes.md`, found and worked by the separate automated routine described in the session's own findings). The `_1` copy is the version consistent with what actually ran — treat `PROMPT-nightly-ticket-routine.md` as superseded by `PROMPT-nightly-ticket-routine_1.md`. |
| `PROMPT-roadmap-slide-claude-design.md` | Claude-Design prompt for a single pitch-deck roadmap slide | mtime 2026-07-31 | Tooling/prompt category, paired with the pitch deck content above. |
| `TICKETS-manager-features-batch2.md` | Tickets S1/S2/B1–B5 (role badge, hide capture-correction, allocation-change proposal, async casting, compliance lock, team management screen, table reuse on follow-up) | mtime 2026-08-07 | Matches completed work (tasks #67–#82 in the working history: B1, B2, B3, B4 all implemented; B5's table-reuse is reflected in the retractable-panel/shared-table work this session). Flags two spec updates needed (casting async, locked-compliance exemption) — both already applied to `SPEC-domain-model.md` per the working history. |
| `TICKETS-followup-workflow.md` | Same file as the repo copy in §A, one edit older (lacks the TD1 strikethrough correction) | mtime 2026-08-02 | Confirmed via diff: single-line difference only. The repo copy (§A) is authoritative; this copy is a stale earlier draft, not a genuine second source. |
| `TICKET-wire-capture-data.md` | The real-RFP-data wiring ticket (`import_capture.py`/`data.js` → `revue-documentaire.html`) | mtime 2026-08-13 | Matches the ticket already implemented this session (tasks #117–#122). No conflicting content found against the version worked from. |
| `TICKETS-review-expert-batch4.md` | Tickets B8–B11 (information rows, new image model, three-reason reassignment with PM approval, two-surface Expert Space model) | mtime 2026-08-12 | B8–B10 implemented (tasks #101–#108). **B11 not yet implemented** (tasks #109–#110 still pending) — this ticket explicitly says it "clarifies rather than reverses `SPEC-expert-space.md`" and names the exact two files needing the update (`SPEC-expert-space.md`, `SPEC-backend-requirements.md` §12). |

## Referenced but not found anywhere in the corpus

- **`SPEC-review-table-batch3.md`** — `TICKETS-review-expert-batch4.md` opens with "Continues numbering from `SPEC-review-table-batch3.md` (B1–B7)." No file by this name (or containing B1–B7 review-table tickets under any name) was found in the repo, Desktop, or Downloads. Its content may be fully absorbed into `SPECS/SPEC-review-table.md` and `HANDOVER.md`'s task history, but this can't be confirmed — flagged as a gap, not resolved by assumption.
- **`NIGHTLY-TICKETS.md`** — both nightly-routine prompts (`PROMPT-nightly-ticket-routine.md` / `_1.md`) reference a queue file by this name. It does not exist anywhere in the corpus. The `_1` revision's own fallback (locate by heading instead) is presumably *why* it was written — the exact-filename version broke once the queue was renamed/restructured into `TICKETS-continuity-fixes.md`.
- **`SPEC-image-container-requirements.md`** — named in `TICKETS-review-expert-batch4.md` (B9) as the spec being superseded ("This supersedes `SPEC-image-container-requirements.md`. ... Delete that model from the spec."). No file by this name exists anywhere in the corpus — either it was deleted per that instruction, or it never existed as a standalone file (its content may have lived inside an earlier, now-overwritten revision of `SPEC-domain-model.md` or `SPEC-review-table.md`). Flagged as a gap.

---

## Summary counts

- 6 files already in the repo
- 3 files on Desktop (1 is this cleanup's own prompt)
- 19 files in Downloads
- **28 files total**, of which:
  - 2 byte-identical duplicate pairs (`SPECS.md` ×2; near-duplicate `TICKETS-followup-workflow.md` ×2 differing by one line)
  - 2 revised-superseded-by-`_1` prompt pairs (`PROMPT-multi-allocation-rows*`, `PROMPT-nightly-ticket-routine*`)
  - 1 confirmed content contradiction requiring reconciliation (`SPEC-expert-space.md` vs. `SPEC-domain-model.md` §9.2)
  - 1 subset/superset prompt pair (`SPEC-brand-colors.md` ⊂ `SPEC-Design tokens.md`)
  - 3 files referenced by name elsewhere in the corpus but not found anywhere (`SPEC-review-table-batch3.md`, `NIGHTLY-TICKETS.md`, `SPEC-image-container-requirements.md`)
  - 2 files containing the real client company name, requiring scrubbing before reuse (`SPECS.md` ×2, same file)
