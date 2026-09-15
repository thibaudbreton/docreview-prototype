> **Consolidation des réponses utilisateur :** variantes Turnkey/SIG/Mainline/RSC, pilote jusqu’à validation d’allocation, décisions DEC-001 à DEC-026 intégrées. Référence : [docs/current](current/README.md). Vérifications documentaires ; aucun test d’application exécuté.

> **Revue documentaire manuelle — 8 septembre 2026.** Référence consolidée : [docs/current](current/README.md). Audit de code ciblé, liens actifs vérifiés, anciennes specs archivées intégralement. Arbitrages utilisateur intégrés au fil des réponses ; édition non entièrement approuvée pour implémentation. Aucune routine automatique exécutée.

# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-09-15T08:02Z (covered commits from `6221a15` through
  `31a4b58`, the "fix-multi-activity-manager" merge: 24 substantive
  prototype commits implementing DEC-028 through DEC-039, plus
  `4b59426` landing the previous run's own DOC-HEALTH.md update).
- Findings this run:
  - **Opened #20.** Commit `22d651b` ("compliance model — two verdicts,
    no Allocation lock, read-only column") collapses the compliance
    scale from three internal values to two and removes the
    requirement-level lock mechanism entirely, citing DEC-028/031/039.
    Those decision IDs don't exist anywhere in `docs/` — both
    `docs/current/OPEN-QUESTIONS.md` and `docs/decisions/DECISIONS.md`
    stop at DEC-026 — and the change directly reverses two decisions
    that *are* on record with real citations and reasoning:
    `docs/current/COMPLIANCE.md`/`DOMAIN.md`/`PLATFORM.md` (DEC-001/024,
    three internal values), `docs/current/ACCESS.md`/`LIFECYCLE.md`
    (DEC-013/014/016, the lock), and `docs/decisions/DECISIONS.md` D6/D8
    (the lock-exclusion rule and the explicit, reasoned rejection of a
    two-value collapse). `docs/tickets/TICKET-two-pass-allocation.md`
    also specifies the lock's design rationale in detail and isn't
    marked superseded. Touches core domain behavior and reverses a
    previously-deliberated decision rather than just renaming something,
    so per the routine's rule this went to an issue, not a direct spec
    edit — `docs/current/COMPLIANCE.md` and friends are unchanged.
  - The rest of this batch (DEC-029/030/032-036: Allocation/Compliance/
    Contributor vocabulary, the manager+expert merge into "contributor,"
    activity-list unification across Compliance/Q&A/Casting) matches
    what `docs/current/*.md` already described as the target state
    (`ACCESS.md:33`, `ALLOCATION.md:36`, `DOMAIN.md:29`, `README.md:21`
    already treat `manager`/`expert` as superseded code-level residue,
    not current truth) — no drift found there, nothing to flag or edit.
  - **#12 still open, unaddressed**, unchanged since 2026-08-30.
    Re-checked, not re-flagged.
  - **#15 and PR #14 unchanged** since the previous run's comments
    (both still show 2026-09-08T22:06 as their last activity — no new
    movement). Re-checked, not re-flagged.
- Baseline for the next run: commits after `31a4b58` (2026-09-15T08:02Z),
  and #12 (still open, 2026-08-30), #15 (still open, 2026-09-07), PR #14
  (still open, conflicting), and #20 (opened this run, needs a human
  decision on DEC-028/031/039 before any spec edit) — check whether any
  have moved before re-flagging.
