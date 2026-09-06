# Doc Health

Report of the last completed run of the "Keep specs current" scheduled
routine (`docs/prompts/PROMPT-specs-maintenance.md`): checks `docs/` specs
and user stories against decisions made in tickets, issues and PRs since
the previous run, and either fixes unambiguous drift directly or opens a
GitHub issue for anything ambiguous or that touches core behavior.

Rewritten each run per the routine's own Step 4; the append-only history of
what happened on each run lives in the **Run log** at the bottom.

## Updated

- **`docs/tickets/TICKETS-prototype-batch6.md`** — its last open item,
  "Language: original at capture, English in the tool, viewable in any
  language," was left unchecked with a blocker note by the previous run
  pending a product decision (does the AI pipeline run on the original
  text or a translation). That decision was made and shipped in this
  window, stated directly in the commit messages: `2b4b594` ("language &
  translation lot 1") states plainly *"SPEC-translation.md, decided: no
  translation-review gate (pipeline trusts the automatic translation and
  runs immediately...)"*, and `7e4ae81` ("lots 4 & 5") resolves the
  ticket's mid-project-document question the same way. All four surfaces
  (project creation, storage, detail panel, translation) landed across
  `2b4b594`, `ea2049f`, `900381f`, `7e4ae81`, plus polish commits
  `4022171`, `b607deb`, `3ef09ba`. Marked the item done, referencing all
  seven commits.
- **`docs/specs/SPEC-translation.md`** — added in `2b4b594` itself (so
  never reviewed by a prior run), and it turned out to be internally
  stale on arrival: its own §2 "Open" line and §7/§8's open questions
  still described the pipeline-timing question as unresolved even though
  the same commit that added the file had already decided it in the
  commit message quoted above, and §5's "no stale-work flagging"
  reasoning assumed the opposite sequencing from what was actually
  decided (work does not wait for translation review before running).
  Corrected all three spots in place — §2's mid-project-document
  question, §5's staleness reasoning, and §7/§8's open questions — dated
  2026-09-05 to match when the decision was actually made, with the
  superseded reasoning kept rather than deleted (matching this corpus's
  existing `SPEC-domain-model.md` §3.2/§4 dated-correction convention,
  rather than a silent rewrite).

## Needs a human

Nothing this run.

## Still open

- **Issues #10, #11, #12** (opened 2026-08-30 by a previous run) are all
  still open and unaddressed. Re-checked rather than re-flagged: none of
  this window's commits (`77fa82f`..`31eb00a`) touch the retired
  `expert-space.html`/`suivi-experts-et-versions.html` specs (#10), add a
  spec for `documents.html` (#11 — `documents.html` itself did change, in
  `7e4ae81`, but only to add a translation-export note, not to gain a
  spec), or touch the stray top-level `docs/` files (#12: `docs/Faire`,
  `docs/SPEC-qa-screen.md`, `docs/TICKET-casting-screen-redesign.md`,
  `docs/USER-TEST-session-3_2.md` — all predate this window, from
  `a4c4bbe`/`d0b2436`). They stand as-is.
- **`TICKET-two-pass-allocation.md`'s own "Open" section** — which
  activities beyond SIG/RSC have an allocation model, and the
  activity-level views it defers to a separate ticket. Both already
  marked open in the ticket itself; nothing built since assumes either is
  resolved, so restated here rather than acted on.

## Verified consistent

- **`TICKET-two-pass-allocation.md`** (commits `77fa82f`..`055f438`, lots
  1-6): already fully self-documenting — `055f438`'s own "lot 6" updated
  `SPEC-domain-model.md` §3.2/§4/§4.1/§5 and `SPEC-advanced-filters.md`'s
  field table in the same commit as the behaviour, matching the ticket's
  own "SPEC-domain-model.md needs correcting" instruction. Read both
  specs against the ticket's six definition-of-done items line by line —
  sequential PBS→ABS→OBS, per-level confidence, the two-level tree, the
  "applied twice, lock at the top only" consolidation rule, and the
  never-both-"OBS" table labelling are all present and match.
- **`SPEC-review-table.md`** against the same ticket, since it calls out
  table/row-expansion impact: not touched by this ticket, but it
  describes the table only at the JTBD/capability level (generic "Class,
  Activity, Type…" fields, no mention of OBS/ABS/PBS or expansion depth),
  so it doesn't actually assert anything the two-pass model contradicts —
  confirmed against `revue-documentaire.html`'s shipped `tkobs`/`obs`
  columns rather than left on inference. No update needed.
- The remaining ~14 commits in this window (UI/component refactors —
  shared `components.css`, universal `ui-select`/`ui-input`, flattened PM
  classification, filter-builder rework, toolbar/table polish — plus two
  isolated bug fixes, `c1a9681` and `29c7256`) are presentation changes or
  bug fixes with no product decision that a spec asserts otherwise.
- No new GitHub issues or PRs in this window (checked `list_issues` and
  `list_pull_requests` — nothing past PR #13, already accounted for by
  the previous run). No Linear access configured for this repo.

**Note for a human:** `docs/decisions/DECISIONS.md` wasn't updated this
run. Its own scope line says it indexes decisions that "changed a
previously-written spec or model"; the translation-timing fix above
corrects `SPEC-translation.md` against its own commit message, in the
same window the spec was created, rather than overturning an
already-published spec — judged out of that log's scope, but flagging
the call in case a future run should treat same-window self-corrections
differently.

---

## Run log

_(append-only, one line per run — do not rewrite past entries)_

- 2026-09-01T22:02Z — commits `301343d`..`c4d246b`. No spec changes
  needed (`301343d` and `e686af7` both already self-documenting or out of
  scope); issues #10/#11/#12 opened for pre-existing gaps.
- 2026-09-06T00:00Z — commits `77fa82f`..`31eb00a`. Updated
  `SPEC-translation.md` and `TICKETS-prototype-batch6.md` (see Updated,
  above); everything else in the window verified consistent or already
  self-documented; issues #10/#11/#12 re-checked, still open.

**Baseline for the next run:** commits after `31eb00a`
(2026-09-05T16:25:21+02:00), and issues #10, #11, #12 — check whether
resolved before re-flagging.
