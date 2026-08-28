# Ticket — Align vocabulary with the users' own terms

> **Not for the unattended nightly routine.** A corpus-wide rename needs a human reviewing the diff — see "Why this shouldn't run unattended" at the end. Run it as a supervised task, on a branch, one phase per commit.
>
> **Correction (2026-08-28), per `TICKET-merge-expert-space-into-compliance.md`:** the `Branch Manager → Activity Manager` row below is **void**. `Activity Manager` is no longer the target — `expert` and `(activity) manager` have since merged into one in-tool role, **contributor**, and that's what `Branch Manager` (and any other manager/expert role reference) becomes instead. Also void: `expert` is no longer "confirmed correct — leave untouched" as an in-tool role name (it still may appear correctly as a real-world job title/subject-matter sense outside the tool). Everything else on this page — `typology → activity`, `sub-typology → sub-activity`, `branch → activity`, `Nature → Type`, `title → heading`, `container` deletion — is unaffected and still pending.

## Why

Several terms in the corpus are ours, not the users'. They were reasonable working labels, but they now appear in specs, tickets, user stories, the prototype and the Figma library — and every day they stay, they spread further and make the documentation read as if it were describing a different product than the one users talk about.

## Confirmed renames

| Current | Correct | Notes |
|---|---|---|
| typology / typologie | **activity** | The users' own word. Appears constantly — expect the highest hit count. |
| sub-typology | **sub-activity** | Same hierarchy, same permissions-only semantics (parent grants access to descendants). |
| **branch** | **activity** (as allocated to a requirement) | Our invention. Nobody said "branch". A "branch" was only ever *an activity allocated to a requirement* — so it collapses into `activity`, it doesn't get a new name. |
| Branch Manager | ~~Activity Manager~~ **contributor** | **Void, see the correction note at the top of this ticket.** Was "already the term used naturally when describing the AS-IS" — no longer the target since manager and expert merged into one in-tool role. |
| Nature *(the title/information/requirement attribute)* | **Type** | This is the column name in the real capture files. |
| title *(as a Type value)* | **heading** | Already confirmed. |
| container *(image model)* | — *(delete)* | Dead concept, superseded by the one-row-per-image model. Remove, don't rename. |

### Derived names that follow from `branch → activity`

These all need rethinking rather than mechanical substitution, since "branch" is disappearing as a concept:

- `Branch Sub-row` → the sub-row showing one allocated activity
- `Branch Section` → the retractable section per allocated activity in the detail panel
- `branch status` → the status of an allocated activity
- Phrases like "the branch goes to Awaiting Q&A" → "the allocated activity goes to Awaiting Q&A"

**Pick one consistent phrasing** for "an activity allocated to a requirement" before starting, and use it everywhere. Note the chosen phrasing at the top of the glossary.

## Deliberately NOT in scope — still to confirm

Do **not** rename these. They may be our labels or the users', and it hasn't been established which:

- **casting** — possibly ours; the users may say something closer to "team constitution", or just refer to the TLW.
- **Class** *(Technical / Non-technical)* — unclear whether this is the real column name.
- **The four status values** *(Incomplete / Doubt / To validate / Valid)* — proposed names, no confirmed equivalents. Note that "Valid" still collides with the final "Validated" state, an unresolved question.
- **reassignment** — the three cases were described in plain language; the label itself is unconfirmed.
- **tender vs RFP** — both are in use across the corpus. Needs one decision, then a separate pass.

Leaving these alone is correct. Renaming them on a guess would be worse than the current inconsistency.

## Terms confirmed correct — leave untouched

compliance, compliance matrix, ABS / PBS / OBS, REX, Q&A, capture, characterisation, allocation, gap analysis, product line, Turnkey, information, requirement, VIP, admin, Requirement Manager *(as a job title, not an in-tool role)*, Bid Manager, Project Manager.

~~expert~~ — **void, see the correction note at the top.** No longer correct as an in-tool role name — merged into **contributor**. May still appear correctly as a real-world job title/subject-matter sense (e.g. "subject-matter expert") outside the tool.

## Phases

**Phase 1 — Glossary first.** Create `docs/GLOSSARY.md`: every term, its definition, and any former name it replaces. This becomes the reference for the rest of the work, and for future sessions. Commit it before touching anything else.

**Phase 2 — Documentation.** Specs, tickets, user stories, personas, journeys, workflow maps. Where a document is archived/superseded, **leave it alone** — archived documents are historical records and rewriting them destroys the trail.

**Phase 3 — Prototype.** Source HTML files: UI copy, comments, variable and function names, data keys. Then rebuild and run the usual verification (`build_merge.py`, `node --check`, jsdom link check, zero dead hrefs).

**Phase 4 — Figma.** Component names in the design system: `Branch Sub-row`, `Branch Section`. Not urgent, but they'll drift out of sync with the code otherwise.

## Why this shouldn't run unattended

A naive find-and-replace on **"branch"** would hit things that have nothing to do with the domain: git branch references, CSS class names, code comments about control flow, possibly library code. Same risk with "type", which is a reserved-ish word in any codebase.

So: **review each match rather than replacing globally**, and keep each phase in its own commit so the diff stays readable.

## Definition of done

1. `docs/GLOSSARY.md` exists and defines every term, including former names.
2. No confirmed-wrong term remains in any live (non-archived) document.
3. The prototype builds and verifies clean; UI copy uses the corrected terms.
4. The out-of-scope terms above are untouched, and still listed as open questions somewhere visible.
