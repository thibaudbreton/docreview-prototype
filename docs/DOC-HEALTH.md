# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-09-01T22:02Z (covered commits from `301343d` through
  `c4d246b`)
- Findings this run:
  - `301343d` ("remove casting from the creation flow") implements
    `TICKET-tender-creation-rework.md` and already rewrote
    `SPEC-project-creation.md` (five-step wizard with casting →
    four-step wizard, casting replaced by an optional project-management-
    team step) and added a dated correction to `SPEC-domain-model.md` §6
    (superseding the "activity manager assigned synchronously at creation"
    bullet) in the same commit. Checked both specs against the commit's
    described behaviour line by line — no stale references to casting, a
    five-step flow, or synchronous activity-manager assignment remain. No
    action needed.
  - `e686af7` ("seed COMPONENTS.md inventory and CLAUDE.md manifest
    rules", PR #13) adds `COMPONENTS.md` and its maintenance rules in
    `CLAUDE.md`. This is process/tooling documentation, not a spec or user
    story describing product behaviour — out of scope for this routine.
  - Issues #10, #11, #12 (opened by the previous run) are all still open
    and unaddressed. Per the previous run's note, re-checked rather than
    re-flagged: none of this window's commits touch the retired
    expert-space specs, add a spec for `documents.html`, or resolve the
    stray `docs/` files, so they stand as-is.
  - No new GitHub issues or PRs opened in this window besides #13 itself
    (already accounted for above). No Linear access configured for this
    repo. No `docs/decisions/` changes in this window.
- Baseline for the next run: commits after `c4d246b` (2026-09-01T10:14Z),
  and the 3 issues opened 2026-08-30 (#10, #11, #12), still open — check
  whether they've been resolved before re-flagging.
