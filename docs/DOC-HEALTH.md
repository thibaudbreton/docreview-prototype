> **Consolidation des réponses utilisateur :** variantes Turnkey/SIG/Mainline/RSC, pilote jusqu’à validation d’allocation, décisions DEC-001 à DEC-026 intégrées. Référence : [docs/current](current/README.md). Vérifications documentaires ; aucun test d’application exécuté.

> **Revue documentaire manuelle — 8 septembre 2026.** Référence consolidée : [docs/current](current/README.md). Audit de code ciblé, liens actifs vérifiés, anciennes specs archivées intégralement. Arbitrages utilisateur intégrés au fil des réponses ; édition non entièrement approuvée pour implémentation. Aucune routine automatique exécutée.

# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-09-21T07:41Z (covered commits from `6221a15` through
  `314d2a5`, 55 commits total — the full `fix-multi-activity-manager` and
  `obs-allocations-merge` window). Two prior runs over parts of this same
  window had already landed as unmerged PRs and were closed as superseded
  — #21 (2026-09-15, `6221a15..31a4b58`) and #23 (2026-09-16,
  `6221a15..dc3577e`) — and a third, PR #24 (2026-09-17,
  `6221a15..d21eb23`), sat open and unmerged for four days. PR #24's
  findings were re-checked against the current tree, nothing in them had
  moved, so they're folded in below rather than re-derived, and PR #24 is
  closed by this entry rather than landed separately — the same call the
  2026-09-08 run made after PR #16 sat six days, now sharper: the nightly
  ticket routine (`docs/archive/TICKETS-continuity-fixes.md`, run
  independently of this one) hit the identical problem from its own side
  this week and named the root cause directly — nothing merges either
  routine's branches into `main`, so one more PR here just repeats PR
  #16/#21/#23/#24's fate. Landing this run's update directly, as the last
  three landed updates have.
- Findings this run:
  - `6221a15..d21eb23` (50 commits, carried over from PR #24): the
    `fix-multi-activity-manager` batch — DEC-028–039 vocabulary, the
    dashboard Statistics rework, DEC-040–057 allocation re-run and
    OBS/ABS/PBS work, the DEC-044 standalone SIG tender, the DEC-045
    "activity"→"system" rename — is doc-synced in the same commits that
    shipped it (`a6aeb84`, `7e9b462`, `b851a7a`, `d72a2a9` all touch
    `docs/current/` alongside the code they document). Spot-checked
    `DOMAIN.md`, `ALLOCATION.md`, `OPEN-QUESTIONS.md` against shipped
    behavior — consistent, no action needed.
  - `d21eb23..314d2a5` (5 commits, 2026-09-21, this run's own window):
    same pattern holds — `1982965` (DEC-060, the allocation panel) and
    `132eef3` (DEC-061/062, the real PBS/OBS/ABS keys) each update
    `docs/current/ALLOCATION.md`/`DOMAIN.md`/`OPEN-QUESTIONS.md`/`KEYS.md`
    in the same commit as the code; `b3a195d` (DEC-049, the four standing
    defects) updates `OPEN-QUESTIONS.md`/`PLATFORM.md`/`TENDER-PROFILES.md`
    likewise. Spot-checked all three against the code — consistent, no
    action needed.
  - **#20 (compliance model reversal) — still open, still not ours to
    close.** Unchanged since PR #24's 2026-09-17 check: DEC-028/031/039
    still carry real citations in `OPEN-QUESTIONS.md` (resolving the
    issue's original "these IDs don't exist" objection), but
    `COMPLIANCE.md`, `DOMAIN.md`, `ACCESS.md`, `LIFECYCLE.md`, and
    `PLATFORM.md` still assert three internal verdicts and a
    requirement-level lock, and `DECISIONS.md` D6/D8 are still
    unannotated. New this run: `7978837` ("Compliance panel: one verdict
    at the top...") added `COMPLIANCE.md` CONF-016–021, a new section on
    panel layout that states the two-verdict/no-lock reality in passing
    ("le verdict interne est énoncé en toutes lettres dessous, comme
    contexte, pas comme titre concurrent" — one verdict shown, not a
    locked final one) — consistent with the reversal, but appended
    alongside the still-unreconciled CONF-005/006/007/013/014 lock
    language rather than replacing it, so the contradiction #20 describes
    now sits inside one file's own sections, not just across files. Still
    five interlinked spec files plus the decision log describing core
    domain behavior — routed to a human per the routine's own rule, same
    as the last two runs. Commented on #20 with the new citation.
  - **#12 still open, unaddressed** (`docs/Faire`,
    `docs/SPEC-qa-screen.md`, `docs/TICKET-casting-screen-redesign.md`,
    `docs/USER-TEST-session-3_2.md` all still present). Re-checked, not
    re-flagged.
  - **#15 still open, PR #14 still open.** No commit in `6221a15..314d2a5`
    touches `docs/specs/SPEC-translation.md`,
    `TICKETS-prototype-batch6.md`, or adds a `docs/decisions/` entry for
    the pipeline-timing sign-off. Re-checked, not re-flagged.
  - Noted, not acted on: `docs/archive/TICKETS-continuity-fixes.md` picked
    up a `2026-09-21 (nightly routine)` entry from a separate scheduled
    routine (ticket-queue work, not specs/decisions) — a different file
    and a different remit from this one, left untouched.
- Baseline for the next run: commits after `314d2a5` (2026-09-21T07:41Z),
  and #12 (still open, 2026-08-30), #15 (still open, 2026-09-07) plus
  PR #14 (still open, conflicting), and #20 (still open, 2026-09-15,
  updated 2026-09-21) — check whether `COMPLIANCE.md`, `DOMAIN.md`,
  `ACCESS.md`, `LIFECYCLE.md`, `PLATFORM.md`, or `DECISIONS.md` D6/D8 have
  been brought in line with DEC-028/031/039 before re-flagging, and close
  #20 once they have.
