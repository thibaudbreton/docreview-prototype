> **Consolidation des réponses utilisateur :** variantes Turnkey/SIG/Mainline/RSC, pilote jusqu’à validation d’allocation, décisions DEC-001 à DEC-026 intégrées. Référence : [docs/current](current/README.md). Vérifications documentaires ; aucun test d’application exécuté.

> **Revue documentaire manuelle — 8 septembre 2026.** Référence consolidée : [docs/current](current/README.md). Audit de code ciblé, liens actifs vérifiés, anciennes specs archivées intégralement. Arbitrages utilisateur intégrés au fil des réponses ; édition non entièrement approuvée pour implémentation. Aucune routine automatique exécutée.

# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-09-08T00:00Z (covered commits from `31eb00a` through
  `6221a15`, i.e. one substantive commit: `7f50eda`). This entry was
  drafted the same day in PR #16, which sat unmerged for six days; landed
  directly on 2026-09-14 after re-confirming nothing below had moved in
  the meantime (see the 2026-09-14 note at the end of this entry).
- Findings this run:
  - `7f50eda` ("docs: consolidate specs into docs/current, archive
    originals") is a manual documentation review, not a ticket/issue/PR
    describing a product decision, and not this routine's own commit —
    its message says so directly, and its own two-paragraph preamble at
    the top of this file states the edition is "not fully approved for
    implementation." Treated it as in scope anyway because it rewrote the
    entire spec corpus this routine checks against, and it bears directly
    on two open issues from the previous run.
  - **Closed #10 and #11.** Both were about live specs describing things
    that no longer match the shipped app (stale Expert Space references;
    no spec for `documents.html`). `docs/specs/*.md` is now pointer stubs
    into `docs/current/`, so the specific stale text both issues quoted
    no longer exists as current truth — `docs/current/README.md` states
    directly that Expert Space isn't in the active-screens list, and
    `docs/current/LIFECYCLE.md` (LIFE-004, LIFE-006/007) covers
    `documents.html`'s functional rules, just in a rule-based shape
    rather than the old screen-walkthrough format. Commented on each with
    the specific citations before closing — this was a factual check
    (does the coverage gap still exist), not a judgment call.
  - **Did not close #15.** `docs/current/AI.md` (AI-003) and
    `docs/current/LIFECYCLE.md` (LANG-001/002) now give one consistent
    answer to the pipeline-timing question — matching what the lot-1/3/4
    commits actually shipped, and the three-way contradiction in the old
    `SPEC-translation.md` is gone along with the file itself. But the
    consolidation's own "not fully approved for implementation" line
    means the human sign-off the batch-6 ticket required still isn't on
    record anywhere (no `docs/decisions/` entry). Commented on #15 with
    both facts and left it open for a human to confirm the sign-off
    before closing. Also flagged PR #14 in the same comment: it edits the
    now-archived `SPEC-translation.md` directly and has real merge
    conflicts against `main` as of this run — superseded either way.
  - **#12 still open, unaddressed** (`docs/Faire`,
    `docs/SPEC-qa-screen.md`, `docs/TICKET-casting-screen-redesign.md`,
    `docs/USER-TEST-session-3_2.md` all still present, untouched by
    `7f50eda`). Re-checked, not re-flagged.
- 2026-09-14 note: no commits landed on `main` after `6221a15` in the
  interim (`git log 6221a15..HEAD` is empty), and #12, #15, and PR #14
  are all still open/unresolved exactly as described above — re-checked
  rather than re-flagged. PR #16 (which had carried this update since
  2026-09-08) is superseded by this direct commit and should be closed.
- Baseline for the next run: commits after `6221a15` (2026-09-08T14:54Z),
  and #12 (still open, 2026-08-30) plus #15 (still open, 2026-09-07) and
  PR #14 (still open, conflicting) — check whether any have moved before
  re-flagging.
