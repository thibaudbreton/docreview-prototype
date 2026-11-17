> **Consolidation des réponses utilisateur :** variantes Turnkey/SIG/Mainline/RSC, pilote jusqu’à validation d’allocation, décisions DEC-001 à DEC-026 intégrées. Référence : [docs/current](current/README.md). Vérifications documentaires ; aucun test d’application exécuté.

> **Revue documentaire manuelle — 8 septembre 2026.** Référence consolidée : [docs/current](current/README.md). Audit de code ciblé, liens actifs vérifiés, anciennes specs archivées intégralement. Arbitrages utilisateur intégrés au fil des réponses ; édition non entièrement approuvée pour implémentation. Aucune routine automatique exécutée.

# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-11-17T22:00Z (covered commits from `ccf3bb4` through
  `3c07d9f`, 139 commits). The runs from 09-27 to 10-20 never landed:
  their PRs (#27, #29–#36) were closed unmerged and without comment in
  one cleanup on 2026-11-17. So this run starts from the last landed
  baseline. Those runs found
  `docs/current` in step for DEC-063–125; this run re-checked that span
  briefly and looked closely at everything after 2026-10-14
  (`c4d7e3b`..`3c07d9f`). Linear could not be reached (connector refused
  by the proxy); GitHub issues and PRs were checked.
- Consistent, no action needed: nearly every decision in the range
  landed in its spec in the same commit — DEC-126 vocabulary (`d500869`),
  Administration DEC-137 (`5e346fb`, `a369225`), Settings DEC-138
  (`ec800ec`), the notification plan DEC-127–136 (`10b4aa0`, `f7a5b51`,
  new `docs/current/NOTIFICATIONS.md`), the creation processing panel
  (`59f9466`, stories/02). The micro-animations (`f400b62`..`0ec0ebe`),
  the chevron + count control (`b2cc6a0`) and the header full stop
  (`4bf3926`) are visual only. Showing the tender chat again (`57d4918`,
  `1277fa1`) is a demo choice and does not contradict "REX/Chat out of
  V1" (DEC-021). The unsaved-work prompt in `1356e23` protects the
  prototype only (it stores nothing), so no spec change.
- Fixed directly (low risk, factual):
  - Tool rename to "Smart Req" (`c4d7e3b`): four references to "SRM" as
    the tool name were left over — `docs/current/ACCESS.md` ACC-010,
    `docs/current/QA.md` QA-003, `docs/stories/15-configuration.md`
    (issuer channel, criterion 5) and the `docs/GLOSSARY.md` title.
    Changed to "Smart Req". (The 10-20 run, PR #36, made the same fix;
    it was closed in the cleanup above, with no review comment.) Requirement IDs
    (`SRM-00001`…) keep that prefix, as the rename commit says.
  - `docs/stories/16-transverse.md` US-X-08, mockup gap note: it said no
    file is produced. Since `1356e23` the CSV export writes a real file
    (the table as it stands). The note now says only the CSV is really
    written and the other formats are only announced.
  - `docs/stories/06-tables.md` US-TAB-18, mockup gap note: it said only
    the PIC cell assignment could be undone in Allocation. Since `1356e23`
    every Allocation correction can be undone (ABS/PBS, roles, people,
    nature/class, bulk actions including delete), and leaving the screen
    asks for confirmation first. The note now describes that. The story's
    Conversation list of undoable actions was **not** extended: that is a
    product decision, not a doc fix.
- Open issues re-checked:
  - **#20 still open.** No commit in the range brings `COMPLIANCE.md`
    (intro table, CONF-003/005/006/007/013/014, the transition table,
    CONF-T05/T06), `DOMAIN.md`, `ACCESS.md` ACC-011, `LIFECYCLE.md`,
    `PLATFORM.md` or `docs/decisions/DECISIONS.md` D6/D8 in line with
    DEC-028/031/039. Last comment 2026-10-14. Re-checked, not re-flagged.
  - **#12** (2026-08-30) and **#15** (2026-09-07) still open, no change;
    no commit touches the files they cite. #28 was closed on 2026-10-14.
  - Open PR #38 (TH1 padding) touches no spec. Noted, not acted on.
- Baseline for the next run: commits after `3c07d9f` (2026-11-17), plus
  #12, #15 and #20. Close #20 once the compliance specs follow
  DEC-028/031/039.
