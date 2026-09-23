> **Consolidation des réponses utilisateur :** variantes Turnkey/SIG/Mainline/RSC, pilote jusqu’à validation d’allocation, décisions DEC-001 à DEC-026 intégrées. Référence : [docs/current](current/README.md). Vérifications documentaires ; aucun test d’application exécuté.

> **Revue documentaire manuelle — 8 septembre 2026.** Référence consolidée : [docs/current](current/README.md). Audit de code ciblé, liens actifs vérifiés, anciennes specs archivées intégralement. Arbitrages utilisateur intégrés au fil des réponses ; édition non entièrement approuvée pour implémentation. Aucune routine automatique exécutée.

# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-09-23T22:09Z (covered commits from `314d2a5` through
  `ccf3bb4`). Most of that range is the previous run landing and a
  same-day reconciliation merge (`c07f072`, `db8fa39`, `ccf3bb4`) that
  touch only this file — already accounted for by the 2026-09-21 entry
  below, not re-derived. The only new content is two commits from the
  `nature-field-placement` branch, merged via `db8fa39`.
- Findings this run:
  - `9435d3f` ("Nature goes above the qualification block, and its label
    is a label again", DEC — repositions the Nature field above the
    derivation chain on both the manager panel and the contributor view
    in `revue-documentaire.html`, and moves its explanation out of the
    label into a hint line) updates `docs/current/ALLOCATION.md` (ALLOC-017
    gains a "Où elle se place" paragraph) in the same commit as the code.
    Checked the diff against the doc addition line by line — order,
    label text, and hint placement all match what shipped. Consistent,
    no action needed.
  - `b2ac7af` ("Advanced capture settings in the project configuration")
    adds four conversion settings (conversion range, table conversion
    format, sentences in paragraphs, equation format) to
    `dashboard-et-config.html`, renames the "AI & segmentation" section
    to "Capture & segmentation", and wires the table-format →
    granularity dependency and the specific-pages field — all in the
    same commit as new `docs/current/CAPTURE.md` (CAPT-T01–T04) and the
    `docs/current/README.md` index entry. Checked the code diff against
    CAPTURE.md's description of the section rename, field order, and the
    two open questions it flags (granularity-vs-Image, whether settings
    can change post-capture) — matches. Consistent, no action needed.
  - **#20 (compliance model reversal) — still open, still not ours to
    close.** No commit in `314d2a5..ccf3bb4` touches `COMPLIANCE.md`,
    `DOMAIN.md`, `ACCESS.md`, `LIFECYCLE.md`, `PLATFORM.md`, or
    `DECISIONS.md`. Confirmed via the issue thread that the only comment
    since the last run's check is that run's own citation comment
    (2026-09-21T22:05Z) — nothing has moved. Re-checked, not re-flagged.
  - **#12 still open, unaddressed.** No commit this run touches
    `docs/Faire`, `docs/SPEC-qa-screen.md`,
    `docs/TICKET-casting-screen-redesign.md`, or
    `docs/USER-TEST-session-3_2.md`. Re-checked, not re-flagged.
  - **#15 still open, PR #14 still open and still conflicting**
    (`mergeable_state: dirty`, no new commits or comments since
    2026-09-08). No commit this run touches
    `docs/specs/SPEC-translation.md`, `TICKETS-prototype-batch6.md`, or
    adds a `docs/decisions/` entry for the pipeline-timing sign-off.
    Re-checked, not re-flagged.
  - Noted, not acted on: PR #24 (superseded, per the last run) is closed;
    two unrelated open PRs, #25 and #26 (duplicate unmerged branches,
    TH1), predate this run's window and touch neither specs nor
    decisions — left untouched.
- Baseline for the next run: commits after `ccf3bb4` (2026-09-23T22:09Z),
  and #12 (still open, 2026-08-30), #15 (still open, 2026-09-07) plus
  PR #14 (still open, conflicting), and #20 (still open, 2026-09-15,
  last comment 2026-09-21) — check whether `COMPLIANCE.md`, `DOMAIN.md`,
  `ACCESS.md`, `LIFECYCLE.md`, `PLATFORM.md`, or `DECISIONS.md` D6/D8 have
  been brought in line with DEC-028/031/039 before re-flagging, and close
  #20 once they have.
