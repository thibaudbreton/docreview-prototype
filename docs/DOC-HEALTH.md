> **Consolidation des réponses utilisateur :** variantes Turnkey/SIG/Mainline/RSC, pilote jusqu’à validation d’allocation, décisions DEC-001 à DEC-026 intégrées. Référence : [docs/current](current/README.md). Vérifications documentaires ; aucun test d’application exécuté.

> **Revue documentaire manuelle — 8 septembre 2026.** Référence consolidée : [docs/current](current/README.md). Audit de code ciblé, liens actifs vérifiés, anciennes specs archivées intégralement. Arbitrages utilisateur intégrés au fil des réponses ; édition non entièrement approuvée pour implémentation. Aucune routine automatique exécutée.

# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-10-20T22:11Z (covered commits `40a06a6..f95d616`, the tool
  rename to "Smart Req." — the 2026-10-14 run's window ended at `40a06a6`).
- Findings this run:
  - `c4d7e3b` / `4bf3926` (rename SRM / Smart Requirement Manager →
    "Smart Req.") updated the README, stories and prompts in the same
    commit but missed four tool-name mentions: `current/ACCESS.md` ACC-010,
    `current/QA.md` QA-003, `stories/15-configuration.md` (story 5, l.181)
    and the `GLOSSARY.md` title. Renamed directly (pure naming, no
    behaviour). Left as is on purpose: `SRM-` requirement ID prefix
    (a data convention, not the tool name), `AUDIT.md` (dated snapshot,
    folder SRM-PROTO), `archive/`, `gap/`, reports.
  - #20, #15, #12 still open; no commit in the window touches their
    files. Not re-flagged. PRs #27, #29-#35 (earlier doc-health runs) are
    still unmerged.
- Baseline for the next run: commits after `ccf3bb4` (2026-09-23T22:09Z),
  and #12 (still open, 2026-08-30), #15 (still open, 2026-09-07) plus
  PR #14 (still open, conflicting), and #20 (still open, 2026-09-15,
  last comment 2026-09-21) — check whether `COMPLIANCE.md`, `DOMAIN.md`,
  `ACCESS.md`, `LIFECYCLE.md`, `PLATFORM.md`, or `DECISIONS.md` D6/D8 have
  been brought in line with DEC-028/031/039 before re-flagging, and close
  #20 once they have.
