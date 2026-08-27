# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-08-27T12:00Z (covered commits from `6bfb87c` through
  `f95ef53`)
- Findings this run:
  - `fd5d084` ("implement SPEC-dashboard-statistics.md") added the spec and
    its implementation in the same commit — self-consistent, no drift to
    reconcile. Its hand-authored metrics (1.1, 1.6/2.3, 2.4) match the
    spec's own "Data gaps" section, which already flags them as not yet
    backed by real tracking.
  - `9e10bca`/`e4b9835` (`TICKET-ai-uncertainty-display.md`, per-field AI
    confidence driving row status) resolves the ticket's one open question
    — "To review" is the existing `doubt` status, not a new fifth state —
    but `SPEC-domain-model.md` §8.2 already documented exactly this
    (vocabulary, rename, per-field doubt) from an earlier session
    (`9ebda8f`, predates this window). Checked line by line against the
    implementation commit's description: no drift, no edit needed.
  - `e278a2a`/`70a6f3a`/`f95ef53` (accent-colour token cleanup, bulk-action-bar
    redesign propagated to Expert Space and Follow-up) is a pure visual/CSS
    fix — no spec asserts a specific bulk-bar layout or accent literal, only
    that the shared Bulk Action Bar component is reused. No drift.
  - No open GitHub issues or PRs since the previous run (checked
    `list_issues`/`list_pull_requests`); no Linear access configured for
    this repo. No `docs/decisions/` changes in this window.
  - No spec edits made, no GitHub issues opened — nothing ambiguous or
    out of sync was found.
- Baseline for the next run: commits after `f95ef53` (2026-08-27T11:46Z).
