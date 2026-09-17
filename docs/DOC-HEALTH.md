> **Consolidation des réponses utilisateur :** variantes Turnkey/SIG/Mainline/RSC, pilote jusqu’à validation d’allocation, décisions DEC-001 à DEC-026 intégrées. Référence : [docs/current](current/README.md). Vérifications documentaires ; aucun test d’application exécuté.

> **Revue documentaire manuelle — 8 septembre 2026.** Référence consolidée : [docs/current](current/README.md). Audit de code ciblé, liens actifs vérifiés, anciennes specs archivées intégralement. Arbitrages utilisateur intégrés au fil des réponses ; édition non entièrement approuvée pour implémentation. Aucune routine automatique exécutée.

# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-09-17T10:05Z (covered commits from `6221a15` through
  `d21eb23`, 50 commits total). Two earlier runs on this same window sat
  unmerged as PR #21 (2026-09-15, covered `6221a15..31a4b58`) and PR #23
  (2026-09-16, covered `6221a15..dc3577e`); #21 was already superseded by
  #23 and closed. This run's findings fold both in and cover the
  remaining `dc3577e..d21eb23` (14 commits, all 2026-09-17), so PR #23 is
  now superseded in turn and should be closed.
- Findings this run:
  - The `fix-multi-activity-manager` batch (DEC-028–DEC-039 vocabulary,
    the dashboard Statistics rework, DEC-040–DEC-057 allocation re-run and
    OBS/ABS/PBS work, the DEC-044 standalone SIG tender, the DEC-045
    "activity"→"system" rename) is, with one exception below, **doc-synced
    in the same commits that shipped it** — `docs/current/ALLOCATION.md`,
    `DOMAIN.md`, `OPEN-QUESTIONS.md` and `TENDER-PROFILES.md` all gained
    their DEC-040–057 entries alongside the code (`a6aeb84`, `7e9b462`,
    `b851a7a`), and `d72a2a9` swept the DEC-045 rename through every
    `docs/current` file the same day it applied it to the prototype.
    Spot-checked `DOMAIN.md`, `ALLOCATION.md` and `OPEN-QUESTIONS.md`
    against the shipped behavior (multi-OBS consolidation, requirement-
    level re-run granularity, OBS-is-an-organisation) — consistent, no
    action needed.
  - **#20 (compliance model reversal) — updated, not closed.** `a6aeb84`
    (2026-09-17, 10:19) landed DEC-027–050 into
    `docs/current/OPEN-QUESTIONS.md` with real, sourced citations,
    including DEC-028/031/039 — the exact IDs #20 flagged as not existing
    anywhere. DEC-031 states directly "Remplace DEC-001" and "DEC-024 sans
    objet", and DEC-028 states the Allocation lock disappears, so the
    citation problem that was #20's original objection is resolved. But
    the five spec files #20 cited as still asserting the old model —
    `docs/current/COMPLIANCE.md` (§ intro, CONF-001/003/004/005/006/014,
    the state table, CONF-T03/T08/T09/T11/T13/T15), `DOMAIN.md` (DOM-009),
    `ACCESS.md` (ACC-011 and the permissions table), `LIFECYCLE.md`
    (LIFE-007, LIFE-T05), and `PLATFORM.md` (the compliance-profile row)
    — are **unchanged**, still describing three internal verdicts and a
    requirement-level lock, still citing DEC-001/013/014/016/024 as if
    current. `docs/decisions/DECISIONS.md` D6/D8 (the original reasoned
    write-ups for the lock exclusion and the three-verdict scale) are also
    not annotated as superseded. This is exactly the core-domain-behavior
    case the routine's own rule routes to a GitHub issue rather than a
    direct edit — five interlinked spec files plus the decision log, not
    a renamed field — so left it to a human rather than rewriting it
    myself, especially with the same human mid-session on these very
    files today. Commented on #20 with the specific line references
    rather than opening a duplicate issue, since #20 already covers this
    discrepancy.
  - **#12 still open, unaddressed** (`docs/Faire`,
    `docs/SPEC-qa-screen.md`, `docs/TICKET-casting-screen-redesign.md`,
    `docs/USER-TEST-session-3_2.md` all still present). Re-checked, not
    re-flagged.
  - **#15 still open, PR #14 still open.** No commits in this window touch
    `docs/specs/SPEC-translation.md`, `TICKETS-prototype-batch6.md`, or
    add a `docs/decisions/` entry for the pipeline-timing sign-off.
    Re-checked, not re-flagged.
- Baseline for the next run: commits after `d21eb23`
  (2026-09-17T10:05Z), and #12 (still open, 2026-08-30), #15 (still open,
  2026-09-07) plus PR #14 (still open), and #20 (still open,
  2026-09-15, updated 2026-09-17) — check whether `COMPLIANCE.md`,
  `DOMAIN.md`, `ACCESS.md`, `LIFECYCLE.md`, `PLATFORM.md` or
  `DECISIONS.md` D6/D8 have been brought in line with DEC-028/031/039
  before re-flagging, and close #20 once they have.
