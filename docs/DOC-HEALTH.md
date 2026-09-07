# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-09-07T00:00Z (covered commits from `c4d246b` through
  `31eb00a`)
- Findings this run:
  - `TICKET-two-pass-allocation.md`'s implementation (`77fa82f` ...
    `055f438`, "two-pass allocation" lots 1-6) corrected
    `SPEC-domain-model.md` (new §3.2, dated corrections to §4/§4.1/§5) and
    `SPEC-advanced-filters.md`/`GLOSSARY.md` in the same commit as the code
    (`055f438`). Checked the diff against the ticket's definition-of-done
    line by line — sequential PBS→ABS→OBS, per-level confidence, two-level
    tree, consolidation applied twice with the lock at the top only, and
    the old crossed-derivation/single-level framing all correctly
    superseded rather than silently overwritten. `SPEC-review-table.md`
    doesn't name ABS/PBS/OBS at all, so it wasn't left stale by this
    change. No action needed.
  - **Opened issue #15**: the "language & translation" work (`2b4b594`,
    `900381f`, `7e4ae81` — lots 1, 3, 4, 2026-09-05) implements the
    feature that `TICKETS-prototype-batch6.md` had explicitly left
    **blocked**, on the grounds that whether the AI pipeline runs on the
    original text or a translation "has to be answered by a human" first.
    The lot-1 commit message states this was "decided" (no review gate,
    pipeline trusts translation and runs immediately) and lot-3/lot-4
    commit messages both refer back to that decision — but
    `SPEC-translation.md` §7/§8 still lists the same question as **open**
    ("Needs deciding... this is the one that matters"), while its own §5
    still asserts a no-staleness guarantee that the lot-1 message says "no
    longer holds." Three inconsistent answers in one document, and no
    `docs/decisions/` record of the call being made. This is the
    architectural fork the ticket said only a human should resolve, not a
    wording drift — flagged rather than edited, per the routine's own
    ambiguous/core-behaviour rule. Spec left untouched pending the
    decision.
  - Issues #10, #11, #12 (opened 2026-08-30) are all still open and
    unaddressed. Re-checked rather than re-flagged: none of this window's
    commits touch the retired expert-space specs, add a spec for
    `documents.html`, or resolve the stray `docs/` files.
  - `e686af7`/PR #13 (component manifest) and this window's UI-only
    prototype fixes (SSO dropdown, filter builder rework, header identity,
    export scoping, etc.) don't describe product decisions a spec or user
    story needs to track — out of scope for this routine.
- Baseline for the next run: commits after `31eb00a` (2026-09-05T16:25Z),
  and issue #15 (opened this run) plus #10/#11/#12 (2026-08-30), all
  still open — check whether any have been resolved before re-flagging.
