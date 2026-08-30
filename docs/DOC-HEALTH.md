# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: 2026-08-30T14:00Z (covered commits from `f95ef53` through
  `32b1f69`)
- Findings this run:
  - Most of this window's spec work was already done self-consistently by
    the implementing commits themselves: `SPEC-team-management.md` was
    rewritten in step with `TICKET-casting-screen-redesign.md`;
    `SPEC-expert-space.md` and `SPEC-versions-qa.md` got correct
    `SUPERSEDED` headers per `TICKET-merge-expert-space-into-compliance.md`
    / `TICKET-three-support-screens.md`; `SPEC-domain-model.md` §7 and
    `SPEC-followup.md` picked up matching correction notes;
    `SPEC-advanced-filters.md` shipped with its implementation in one
    commit; `GLOSSARY.md` correctly reflects the `contributor` vocabulary
    correction. No action needed on any of these.
  - `qa.html`'s two later polish commits (`b70c270` dropping the "Internal
    review" status, `13fb3be` restructuring the panel layout) don't
    contradict `SPEC-qa-screen.md` — that spec never asserted specific
    status enumerations or panel layout, only behaviour. No drift.
  - **Opened 3 GitHub issues, no spec edits** — everything found this run
    was either core-behavior-touching or ambiguous, per the routine's own
    rule (unambiguous/low-risk → edit directly; ambiguous/core → flag).
    Nothing found qualified as unambiguous/low-risk:
    - **#10** — `SPEC-domain-model.md` §9, `SPEC-dashboard.md`,
      `SPEC-configuration.md` and `SPEC-home.md` still describe the retired
      `expert-space.html` / `suivi-experts-et-versions.html` as current
      (the dashboard phase-rail description in particular predates the
      three→two-step rework in `5902b31`). `SPEC-expert-space.md` and
      `SPEC-followup.md` already got correct supersede headers; these
      didn't.
    - **#11** — no spec exists at all for the new `documents.html`
      ("Documents & versions") screen from `TICKET-three-support-screens.md`
      (shipped in `42f0a39`), unlike its sibling `qa.html` which got
      `SPEC-qa-screen.md`.
    - **#12** — stray files under `docs/` from two apparent manual-upload
      commits (`d0b2436`, `a4c4bbe`): an empty `docs/Faire`, two exact
      duplicates of properly-located spec/ticket files, and
      `docs/USER-TEST-session-3_2.md`, which is *not* identical to the
      canonical `docs/research/USER-TEST-session-3.md` — it carries extra
      content (a fuller §1.7 answer, one extra to-do item) not present in
      the canonical copy. Flagged for human triage rather than deleted,
      since it's unclear which copy is authoritative.
  - No open GitHub issues or PRs existed before this run (checked
    `list_issues`/`list_pull_requests`); no Linear access configured for
    this repo. No `docs/decisions/` changes in this window.
- Baseline for the next run: commits after `32b1f69` (2026-08-30T15:22Z),
  and the 3 issues opened this run (#10, #11, #12) — check whether they've
  been resolved before re-flagging.
