> **Consolidation des réponses utilisateur :** variantes Turnkey/SIG/Mainline/RSC, pilote jusqu’à validation d’allocation, décisions DEC-001 à DEC-026 intégrées. Référence : [docs/current](current/README.md). Vérifications documentaires ; aucun test d’application exécuté.

> **Revue documentaire manuelle — 8 septembre 2026.** Référence consolidée : [docs/current](current/README.md). Audit de code ciblé, liens actifs vérifiés, anciennes specs archivées intégralement. Arbitrages utilisateur intégrés au fil des réponses ; édition non entièrement approuvée pour implémentation. Aucune routine automatique exécutée.

# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- **Last run:** 2026-09-27, covering commits `ccf3bb4..e7dbc91` — the merge
  of the long-lived `custom-columns` branch (35 commits, dated 2026-09-22
  through 2026-09-25, carrying DEC-063 through DEC-085). This branch forked
  before the 2026-09-23 run and only landed on `main` now, so none of it had
  been checked before.

## Updated

Each substantive commit in this batch already touched the matching
`docs/current/*.md` file in the same commit (the repo's established
discipline held). This run verified those additions against the actual code
diffs and found five small drifts, all fixed directly — none required a
product decision, only reconciling a doc with something already shipped and
explained elsewhere in the same corpus (a commit message, a `COMPONENTS.md`
entry, or a later commit in the same batch):

- **`docs/current/LIFECYCLE.md` — duplicate ID.** `82ab34e` introduced
  `LIFE-T10` through `LIFE-T13` for the new per-document Compare/Versions
  feature, colliding with the pre-existing `LIFE-T10` ("un retraitement SIG
  ne lance pas la passe 1 Turnkey"). Renumbered the new block to
  `LIFE-T11`–`LIFE-T14`; nothing else in the corpus referenced the old
  numbers.
- **`docs/current/ALLOCATION.md` — stale re-run control placement.**
  `f909cb7` documented the re-run control as living "on every Turnkey
  system card"; `920072e`, the same day, removed it from those cards again
  (kept only in the system's own detail view and the single-system/
  contributor headers) but never touched the doc. `COMPONENTS.md`'s own
  "Re-run Control" entry already recorded the reversal ("removed the same
  day at the user's request"). Corrected the "Où se trouve le contrôle"
  paragraph and `ALLOC-T23` to match.
- **`docs/current/COMPLIANCE.md` — shortcuts reinstated, not reflected.**
  `f6bdf9e` (DEC-081/CONF-025) removed all displayed keyboard-shortcut
  hints from Compliance; `5ba326f`, later the same day, added them back on
  demand via a "⌨ Shortcut Help" popover (also on Allocation) — confirmed
  by `COMPONENTS.md`'s "Shortcut Help" entry. CONF-025 read "no shortcuts
  displayed" until this run; added CONF-029 to record the reinstatement and
  cross-referenced it from CONF-025.
- **`docs/current/ALLOCATION.md` and `docs/current/COMPLIANCE.md` —
  DEC-085 had no rule entry.** Every other substantive DEC in this batch
  got both an `OPEN-QUESTIONS.md` line and a numbered rule in the owning
  screen file(s); DEC-085 (selection shortcuts, next-action jump,
  undo — spans both Allocation and Compliance) only got the
  `OPEN-QUESTIONS.md` line. Added `ALLOC-023`/`ALLOC-T31` and
  `CONF-030`, transcribing DEC-085's own text (no new decision made, just
  giving it the rule-ID home the rest of the batch already has).
- **`docs/current/CUSTOM-COLUMNS.md`** — line under "Conséquences de la
  portée" called the Allocation/Compliance duplication "à confirmer quand
  Compliance sera construit"; Compliance's own custom columns shipped in
  the same batch (`f6bdf9e`, DEC-081), a few lines below in the same file.
  Reworded as confirmed fact.
- **`docs/current/README.md`** — "Les décisions utilisateur DEC-001 à
  DEC-027" was stale (the registry now runs to DEC-085) and actively
  misleading, since a reader could take it as a real ceiling. Updated the
  range and linked directly to `OPEN-QUESTIONS.md`.

User stories, checked against the same batch (`docs/stories/`):

- **"Finalize the allocation"** described a milestone (`5019c2b`/DEC-084)
  removed this batch — no such button, modal, or gate exists any more.
  Rewritten as "Validate allocation per requirement", matching the
  documented `ALLOC-022` behavior (validate per requirement, panel always
  shows the next step, register export moved to the Export panel).
- **"Chase overdue contributors"** — DEC-078 removed the "overdue" status,
  pill and filter from Compliance entirely ("an assignment waiting on its
  contributor shows its age, and that is all", per the code comment).
  Renamed to "Chase slow-to-answer contributors" and reworded the
  acceptance criteria to drop the pill/threshold framing and the
  now-nonexistent "remind everyone overdue at once" action (only
  per-assignment, per-contributor, and bulk-selection reminders remain).

## Needs a human

- **#20 (compliance model: two verdicts + no lock vs. every spec still
  documenting three + a lock) — still open, still not ours to resolve.**
  New evidence this run, not a new discrepancy: DEC-078 through DEC-081
  (Compliance's document-structure rework and its new contributor decision
  panel) build substantially further on the disputed two-verdict/no-lock
  model — a queue-driven panel with one primary action ("Compliant en un
  geste, Not compliant en deux"), no R&D Needed option, no lock/unlock
  anywhere in the new UI. `COMPLIANCE.md` itself already carries both
  sides side by side (its own intro table and CONF-003/005/006/007/013/014
  still assert three internal values and a lock; CONF-022–030 describe a
  screen with neither) — this is not new, but the gap keeps widening as
  real product work lands on the unresolved side. Added a comment to #20
  consolidating this. Not editing `COMPLIANCE.md`/`DOMAIN.md`/`ACCESS.md`/
  `LIFECYCLE.md`/`PLATFORM.md` or `docs/decisions/DECISIONS.md` D6/D8
  myself — same reasoning as every prior run: this reverses a previously
  reasoned decision, not a naming drift.
- **Three Compliance user stories need a full rewrite, not a patch** (out
  of scope for a direct fix this run — each is restructured across
  several acceptance criteria by DEC-073/078/079/080/081/083, not a single
  stale line):
  - *"Track consolidation across the tender"* (`docs/stories/
    STORIES-extracted-from-prototype.md`, "Compliance" section) — still
    describes overdue/outdated-version pills, a "Sort by ... Needs my
    action" toggle, none of which exist post-DEC-078/083.
  - *"Navigate by section or by contributor"* — the By-section/By-
    contributor toggle and the separate Document view/tab it describes
    are gone (DEC-078 default document order; DEC-080 turns the Document
    resource tab into Q&A; DEC-081 drops the toggle entirely).
  - *"Render a verdict as a contributor"* — superseded wholesale by the
    new queue-driven decision panel (`SPEC-compliance-decision-panel.md`,
    DEC-079/080/081): different primary/secondary action structure, Set
    aside, Ask the client, Not mine, Similar/REX/Chat resources, none of
    which the current story mentions.
  - *"A new document version invalidates prior work"* — its Compliance
    leg ("flagged 'outdated version', filterable") no longer holds
    (DEC-078); the wider Versions/Compare model it should describe instead
    is the new `LIFE-012`–`LIFE-015`.

## Still open

- **#12** (stray/duplicate files under `docs/` from manual uploads) —
  unaddressed since 2026-08-30. No commit this run touches `docs/Faire`,
  `docs/SPEC-qa-screen.md`, `docs/TICKET-casting-screen-redesign.md`, or
  `docs/USER-TEST-session-3_2.md`. Re-checked, not re-flagged.
- **#15** (language & translation pipeline-timing sign-off) and **PR #14**
  (its proposed doc fix) — both still open, no new commits or comments
  since 2026-09-08. No commit this run touches `docs/specs/
  SPEC-translation.md` or `TICKETS-prototype-batch6.md`. Re-checked, not
  re-flagged.
- Noted, not acted on: PRs #17/#18/#19/#22/#25/#26 (TH1 padding fix
  duplicates, duplicate-branch blocker) predate this run's window and
  touch neither specs nor decisions.

## Verified consistent

All 35 non-merge commits in `ccf3bb4..e7dbc91` were checked (code diff
against the same commit's `docs/current`/`COMPONENTS.md` diff, or against
the rest of the corpus where no doc was touched):

`dd816be` (DEC-063 brand), `9f677cf` (DEC-064–068 custom columns),
`cdce5a9` (keyboard nav reaches custom columns), `82ab34e` (DEC-069–072
gap-per-document, beyond the ID collision above), `5410006` (DEC-073
headings/info no status), `d8937b5` (DEC-074 Nature vs. Class, incl. its
`KEYS.md` cross-edit), `41bbcef` (DEC-075 re-run offer), `e808e7b`
(DEC-076 delete OBS/system to zero), `daaa04e` (add-system search picker),
`3a5f5f5` (DEC-077 merge TK OBS into System), `53056db` (DEC-078
Compliance restructure), `b19eadf` (DEC-079 contributor decision panel +
new spec file), `dd4b8fd` (DEC-080 panel adjustments — self-documents its
own deviation from the spec, which is healthy, not a gap), `54fb4cf`
(DEC-082 external partners, both `ALLOCATION.md` and `COMPLIANCE.md`
covered), `e5b34f5` (DEC-083 header sort, incl. its `CUSTOM-COLUMNS.md`
fix), `5019c2b` (DEC-084, beyond the stories fix above). Pure-UI/polish
commits with no `docs/current` touch and correctly none needed —
`4bedc2a`, `f2129b1`, `f8aa992`, `171651e`, `aac89b1`, `269d835`,
`3a66009`, `ec7e36d`, `083e9a3`, `0e1af9e`, `73efa97`, `0ae2983`,
`49ae3a3` — each checked for silently-changed documented behavior and
logged correctly in `COMPONENTS.md`. `5b6c11e` is the previous run's own
doc-landing commit, not new content.

No new Linear tickets, GitHub issues, or PRs since the last run — checked
`list_issues`/`list_pull_requests`; #12/#15/#20 and PR #14 are unchanged.

---

## Run log

- 2026-09-27 — examined `ccf3bb4..e7dbc91` (35 commits, DEC-063–085).
  Fixed a duplicate ID (`LIFECYCLE.md`), a stale UI-placement claim and a
  stale "no shortcuts" claim in `ALLOCATION.md`/`COMPLIANCE.md`, added the
  missing DEC-085 rule entries, a stale "to confirm" caveat in
  `CUSTOM-COLUMNS.md`, and the stale DEC-001–027 range in `README.md`.
  Rewrote 2 user stories made wrong by this batch (Finalize-allocation
  removal, overdue-status removal); flagged 3 more Compliance stories and
  a Versions story as needing a full rewrite rather than a patch. Added a
  consolidating comment to #20 (compliance model still unresolved, gap
  widening). #12/#15/PR #14 re-checked, unchanged, not re-flagged.
- 2026-09-23 — see previous entry (superseded above); the 2026-09-16 and
  2026-09-17 entries before it are further back in this file's git
  history, not repeated here per the routine's "replace, don't append to
  the body" rule (the run log itself remains append-only).
