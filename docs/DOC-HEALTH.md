> **Consolidation des réponses utilisateur :** variantes Turnkey/SIG/Mainline/RSC, pilote jusqu’à validation d’allocation, décisions DEC-001 à DEC-026 intégrées. Référence : [docs/current](current/README.md). Vérifications documentaires ; aucun test d’application exécuté.

> **Revue documentaire manuelle — 8 septembre 2026.** Référence consolidée : [docs/current](current/README.md). Audit de code ciblé, liens actifs vérifiés, anciennes specs archivées intégralement. Arbitrages utilisateur intégrés au fil des réponses ; édition non entièrement approuvée pour implémentation. Aucune routine automatique exécutée.

# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-09-16T09:15Z (covered commits from `6221a15` through
  `dc3577e`: the "fix-multi-activity-manager" merge, 29 substantive
  prototype commits across two sessions — 24 on 2026-09-10/15 citing
  DEC-028 through DEC-039, plus 5 more on 2026-09-16 reworking the
  dashboard Statistics panel). This entry lands directly, superseding
  PR #21, which drafted the 2026-09-15T08:02Z half of this update and
  sat unmerged for a day; nothing it found had moved in the meantime, so
  its findings are folded in below rather than re-derived.
- Findings this run:
  - **Opened #20** (2026-09-15, still open). Commit `22d651b`
    ("compliance model — two verdicts, no Allocation lock, read-only
    column") collapses the compliance scale from three internal values
    to two and removes the requirement-level lock entirely, citing
    DEC-028/031/039 — IDs that don't exist in `docs/current/OPEN-QUESTIONS.md`
    or `docs/decisions/DECISIONS.md` (both stop at DEC-026), while the
    change reverses decisions that *are* on record with real citations:
    DEC-001/024 (three internal values — `COMPLIANCE.md:14`,
    `DOMAIN.md:23`, `PLATFORM.md:36`) and DEC-013/014/016 (the lock —
    `ACCESS.md` ACC-011, `LIFECYCLE.md` LIFE-007, `DOMAIN.md` DOM-009),
    plus `DECISIONS.md` D6/D8's explicit, reasoned rejection of exactly
    this collapse. Reverses a previously-deliberated decision rather than
    renaming something, so this went to an issue, not a direct edit —
    `docs/current/COMPLIANCE.md` and friends are unchanged.
  - The rest of the 2026-09-10/15 batch (DEC-029/030/032-036:
    Allocation/Compliance/Contributor vocabulary, the manager+expert
    merge into "contributor," the shared 16-code activity list across
    Compliance/Q&A/Casting, "typology"→"activity" copy) matches what
    `docs/current/*.md` already described as the target state
    (`ACCESS.md:33`, `ALLOCATION.md:36`, `DOMAIN.md:29`, `README.md:21`
    already treat manager/expert as superseded code-level residue; no
    remaining "typolog*" hits in `docs/current`) — no drift, no edit.
  - **Commented on #20, not a new issue**, for the 2026-09-16 dashboard
    batch (`d2793d2`, `633685b`): `d2793d2` cites **DEC-029** again to
    justify restructuring Statistics into one tab per canonical step, and
    `633685b`'s commit message cites **DEC-036**'s perimeter merge as the
    reason a Team-casting badge regressed — both are the same undefined
    DEC-IDs #20 already flags, now driving a second area of the product.
    Folded into #20 as more evidence rather than opened separately, since
    the root cause (phantom DEC citations) is identical.
  - **No spec written for dashboard/Statistics itself** — `docs/current`
    has no reading-map row for it (`README.md:27-41`) and `AUDIT.md:20`
    already recorded on 2026-09-08 that the old dashboard/KPI specs were
    deliberately left archived rather than consolidated. `d2793d2`/`6953e2b`/
    `633685b`/`9fad58e`/`a568853` are further work inside that
    already-acknowledged gap, not new drift against a current claim — so
    nothing to fix or flag beyond the DEC-029/036 citations above.
  - **#12 still open, unaddressed**, unchanged since 2026-08-30.
    Re-checked, not re-flagged.
  - **#15 and PR #14 unchanged** since the previous run's comments (both
    still show 2026-09-08T22:06 as last activity). Re-checked, not
    re-flagged.
  - PR #21 (carried the 2026-09-15 half of this update since then) is
    superseded by this direct update and should be closed.
- Baseline for the next run: commits after `dc3577e` (2026-09-16T09:04Z),
  and #12 (still open, 2026-08-30), #15 (still open, 2026-09-07), PR #14
  (still open, conflicting), and #20 (open, now covering both the
  compliance-model reversal and the dashboard's DEC-029/036 citations) —
  check whether any have moved before re-flagging.
