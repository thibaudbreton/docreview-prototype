# Doc Health

Tracks the last completed run of the "Keep specs current" scheduled routine
(checks `docs/` specs and user stories against recent decisions, and either
fixes unambiguous drift directly or opens a GitHub issue for anything
ambiguous — see the routine's prompt for the full procedure).

- Last run: never (seed file — routine had no repository attached until now)
- Baseline: commits before 2026-08-20T08:31Z are not yet covered by an
  automated pass; the first real run should treat that timestamp as its
  starting point rather than scanning the full project history.
