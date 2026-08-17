# Glossary

Produced as Phase 1 of `docs/tickets/TICKET-vocabulary-alignment.md` (once moved there — see Phase 2). Defines every term used across the SRM corpus, flags which ones replace an earlier, wrong (team-invented rather than user-spoken) label, and lists the terms deliberately left alone because it isn't yet confirmed which side of that line they're on.

**Chosen phrasing for "an activity allocated to a requirement":** ​**allocated activity**. Used consistently below and, from Phase 2 onward, throughout the live corpus in place of "branch."

---

## Renamed terms

### Activity
*Replaces: typology / typologie.*
The categorisation dimension used to route a requirement to the team responsible for it (e.g. Signalling, Mainline, Power Supply, Civil Works). Activities can nest to arbitrary depth — a child activity's parent field points to another activity, or is null at the root. The nesting affects **permissions only**: a manager or expert assigned to a parent activity automatically gets view + modify rights on every descendant activity's requirements, recursively; it has no effect on characterisation, allocation, or compliance consolidation, which happen exactly as if the hierarchy didn't exist.

### Sub-activity
*Replaces: sub-typology.*
A child activity in the activity hierarchy above. Same permissions-only semantics — a sub-activity's requirements are characterised/allocated/consolidated with no inheritance from the hierarchy; only who can see and act on them changes.

### Allocated activity
*Replaces: branch.*
One activity allocated to a specific requirement — not a new concept distinct from Activity, but an Activity in its "allocated to this requirement" state. Carries its own manager, expert, progress status, and — once answered — a compliance verdict. A single-activity requirement has exactly one allocated activity; a multi-activity requirement has one per activity assigned to it. "Branch" was a team invention; nobody outside the team ever called this anything.

### Activity Manager
*Replaces: Branch Manager.*
The person responsible for a given allocated activity: assigning or reassigning its expert, tracking the response, and being the first stop when an expert raises a reassignment request. Already the term used naturally when describing the AS-IS workflow.

### Type
*Replaces: Nature (the title/information/requirement attribute).*
The category assigned to a captured block — **Heading**, **Information**, or **Requirement** — either by the AI or corrected by a human. Matches the column name used in the real capture files; "Nature" was never a term anyone outside the team used.

### Heading
*Replaces: title (as a Type value).*
A Type value marking a block as a section or document heading rather than a requirement or an information block. Confirmed before this ticket; listed here only so the glossary stays complete.

### *(deleted, not renamed)* Container
*Was: the image container/folder model.*
Dropped, not renamed — a dead concept, superseded by the current one-requirement-row-per-image model (an image auto-creates one requirement row; the user can duplicate that row for an image holding several requirements). Recorded as decision D4 in `docs/decisions/DECISIONS.md` and, where it appears in already-archived tickets, left untouched there (see "Archived documents," below).

### Derived from "allocated activity"

These follow from the rename above, not from mechanical substitution:

- **Allocated-activity sub-row** *(replaces: Branch Sub-row)* — the sub-row in the review/follow-up tables showing one requirement's allocated activity; shown whenever a requirement carries more than one.
- **Allocated-activity section** *(replaces: Branch Section)* — the retractable section in a detail panel showing one allocated activity's manager, expert, status and compliance.
- **Allocated-activity status** *(replaces: branch status)* — the progress axis of one allocated activity: Proposed → Assigned → Awaiting answer → Awaiting Q&A → Reassignment needed → Answered. Kept distinct from compliance (the result axis, meaningful only once Answered) — the two must never be conflated.

---

## Terms confirmed correct — unchanged

Listed for completeness, since the glossary should define every term in use, not only the renamed ones.

- **Compliance** — the per-allocated-activity verdict once answered: Compliant / R&D Needed / Not compliant.
- **Compliance matrix** — the consolidated, per-requirement compliance view assembled from every requirement's allocated activities, exported to the client.
- **ABS / PBS / OBS** — the three assignment dimensions (product / activity / organisation breakdown structure) an allocation is derived from.
- **REX** — prior-experience references surfaced to an expert for a given requirement.
- **Q&A** — the clarification-question loop between the team and the tender issuer, distinct from the internal reassignment loop.
- **Capture** — the AI step that segments a source document into blocks.
- **Characterisation** — the AI/human step that assigns each captured block a Type, Class, and Activity.
- **Allocation** — the AI/human step that assigns a requirement's allocated activity to a manager and expert (ABS/PBS/OBS).
- **Gap analysis** — the diff computed between two document versions, surfaced when a new AO version arrives.
- **Product line** — a project-level classification (e.g. Signalling & Urban, Rolling stock, Services, Systems).
- **Turnkey** — the most complex/variable activity value, spanning multiple systems on one requirement.
- **Information** — a Type value: a block that carries no requirement content and no allocation/compliance/status fields at all.
- **Requirement** — a Type value: a block that goes through characterisation, allocation, and compliance.
- **Expert** — the person who renders a compliance verdict on an allocated activity.
- **VIP** — a read-only role, dashboard/KPI visibility only.
- **Admin** — the unrestricted-access in-tool role.
- **Requirement Manager** — a job title used by the client's own teams (AS-IS), **not** the name of an in-tool role — do not confuse it with any specific SRM permission role (e.g. Project Manager, Activity Manager).
- **Bid Manager** — an AS-IS job title, kept as-is; its relationship (if any) to a specific in-tool role is not established.
- **Project Manager** — the in-tool role with full access to their assigned project, including locking/unlocking compliance verdicts and approving reassignment/reallocation requests.

---

## Open questions — deliberately NOT renamed

Per the ticket: renaming these on a guess would be worse than leaving the current inconsistency. Left exactly as found, and listed here so they stay visible rather than silently forgotten.

- **Casting** — possibly a team invention; the client's own teams may say something closer to "team constitution," or simply refer to the TLW (unexplained acronym in the source ticket — not expanded here since guessing would misrepresent it as confirmed).
- **Class** *(Technical / Non-technical)* — unclear whether this is the real column name used in capture files, unlike Type, which is confirmed.
- **The status-progression values** — the source ticket names them "Incomplete / Doubt / To validate / Valid," and flags that "Valid" collides with a separate final "Validated" state. **This doesn't match what's actually implemented**: `docs/specs/SPEC-domain-model.md` §8.2's current, shipped vocabulary is **Incomplete → To review → To validate → Allocated** — neither "Doubt" nor "Valid"/"Validated" appears in the live model. This is the same discrepancy already flagged during the docs-cleanup task (see `docs/CLEANUP-REPORT.md`, item 4) — recorded again here rather than assumed resolved, since this ticket's own list still uses the older names. Neither the ticket's names nor the domain model's names are renamed here; a human needs to reconcile which is current before anything gets touched.
- **Reassignment** — the three underlying cases (right activity/wrong person; wrong activity; activity doesn't apply here) were described in plain language during requirements gathering; the label "reassignment" itself was never confirmed as the client's own word.
- **Tender vs. RFP** — both appear across the corpus with no single decision recorded; needs its own pass once decided, separate from this ticket.

## Archived documents

Per the ticket: documents already in `docs/archive/` are historical records and are **not** renamed in Phase 2 — rewriting them would destroy the trail of what was actually said at the time. Where an archived document uses "branch," "typology," "Nature," or "container," that reflects the vocabulary in use when it was written, not an error to fix.
