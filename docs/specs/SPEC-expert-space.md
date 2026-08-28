# SPEC — Expert Space

> **SUPERSEDED by the Compliance step on 2026-08-28.** Kept for reference. Do not build from this. See `TICKET-merge-expert-space-into-compliance.md`: there is no more expert space — the second workflow step is now `compliance.html`, serving both the project manager and contributors (the merged manager/expert role) from one screen. The reasoning behind the research panel (Document/REX/Chat) and the "Ask the client" naming risk survive the merge; the three-zone layout, the manager/expert role split, and the three-value compliance model below do not.
>
> **Reconciled during the docs cleanup (2026-08-16).** This file was moved into `docs/specs/` from outside the git repo (see `docs/INVENTORY.md`) and updated in place so it reads as current truth, per the two later ticket decisions below. The original wording and the history of what changed live in `docs/decisions/DECISIONS.md` (D8, D11) — this is not a silent rewrite. `expert-space.html` is built and shipped; this is no longer "a spec to validate."
>
> - The **compliance model** below now reflects `SPEC-domain-model.md` §9.2 (decision **D8** in the log): compliance is a **three-value** scale (Compliant / R&D Needed / Not compliant), not the two-value model originally described here. The original two-value wording was an explicit choice at the time this spec was written, later reversed once it was found to conflict with the rest of the domain model.
> - The **two-surface model** section below is new, added per `TICKETS-review-expert-batch4.md` (B11 — decision **D11**), which clarifies (not reverses) this spec's original access-restriction wording. **B11's UI is not yet built** — see the note in that section.

## What this is

The third instance of the same underlying pattern already used twice — **table + detail panel**, configured for a third audience. Requirement review (RM) and manager follow-up (B5) proved the pattern generalises; this is not a new screen type, it's a new configuration of an existing one.

## Why the shape is what it is — three real profiles, not one workflow

Field observation: an expert's work isn't homogeneous. Three distinct cases, and the UI must not force any of them through a detour built for another:

- **Fast** — the verdict is obvious, no research needed.
- **Slow** — needs research: REX and document context before a verdict can be reached.
- **Misrouted** — not actually this expert's subject; the real action is reassignment, not a verdict at all, and this is a real share of the flow, not an edge case.

Concretely: the verdict field and the research material (REX, document) must coexist in the same panel without an imposed step between them, and reassignment must be as visually prominent as rendering a verdict — not tucked behind a menu.

## List side (table)

Reuses the same building blocks as the other two table instances: **Requirement Row**, **Allocated-activity sub-row**, **Bulk Action Bar** (for batch status change), **Column Visibility Menu**, the existing filtering mechanism (confirmed scale: up to several hundred rows for one expert).

- **Access is a strict restriction, not a liftable filter.** An expert only ever sees requirements belonging to their activity — confirmed directly ("ne peut pas voir les autres"). This is unlike the manager follow-up view (B5), where filter-vs-restriction is still an open question — here it's settled. **This restriction applies to the table specifically — see "Two surfaces" below for how document reading differs.**
- The restriction scope includes **all descendant activities** in the hierarchy (see below), not just the expert's own activity.
- **New for this screen only:** a **Gap Chip shown directly in the row** — the expert needs to spot version changes without leaving the list. (Contrast: the manager follow-up view explicitly does *not* need this — the existing Versions tab is enough there. Same component, different placement, because the two audiences use it differently.)
- Batch status change on selected rows is already covered by reusing the Bulk Action Bar as-is.

## Two surfaces: the table decides, the document informs (B11)

**Not yet implemented — this section describes the intended design; the corresponding UI work is still open.**

Two different surfaces, two different rules — this is a decision surface vs. a context surface, not "full access" vs. "restricted access":

- **The table = only the expert's own requirements** (their own activity plus its descendant activities, per the restriction above). This is the **decision surface** — an expert can only act on what appears here.
- **The document = readable in full.** The whole tender document is available to read, so the expert has complete context. But they **cannot click into other requirements** and **cannot make decisions on them** from there. Reading only.

This clarifies rather than reverses the restriction stated above — the restriction was never wrong, it correctly described the table. What was missing is that full document reading sits alongside it, unrestricted.

The same model applies to Activity Managers on their own screen: their own requirements in the table, full document readable for context.

## Detail panel side — where the judgment actually happens

- **Characterisation and allocation** are shown **read-only**. The expert doesn't edit these — changing an allocation is the manager/project-manager's job (ticket B1).
- **REX linked to the requirement** — surfaced without an extra click, to support the "slow" profile directly.
- **Full RFP document accessible** — the whole document, not just an excerpt, consistent with the existing "expert reads the tender" step already in the workflow, and with the two-surface model above.
- **Three first-class actions, none hidden in a menu:**
  1. Render a verdict.
  2. Ask a question (existing Q&A flow — internal review before it's sent to the client, `awaiting_qa` status).
  3. Return the allocation (existing `reassignment_needed` flow, with a comment) — kept just as prominent as the verdict action.

### Verdict form

The compliance model is **three values: Compliant / R&D Needed / Not compliant** (canonical keys `compliant` / `rnd_needed` / `not_compliant`, per `SPEC-domain-model.md` §3.1 and §9.2).

- **Compliant** → a single free comment field.
- **R&D Needed** → its own comment field ("what R&D work is needed for compliance?"). This is a first-class, countable verdict, not text folded into the Compliant comment.
- **Not compliant** → a **Category** (closed list) + a **Topic** (free text).

The verdict form has a dedicated button per value — Compliant / R&D Needed / Not compliant — matching `expert-space.html`'s shipped `COMPLIANCE_LABELS`.

## Activity hierarchy — a permissions-only concept

A new piece of the domain model surfaced during this session:

- Activities can **nest**, to **arbitrary depth**.
- The nesting affects **permissions only** — it has **no effect** on characterisation, allocation, or compliance consolidation logic. A requirement's activity tag doesn't inherit or cascade anything from the hierarchy for those purposes.
- A manager **or** expert assigned to a **parent** activity automatically gets **view + modify** rights on every **descendant** activity's requirements.
- This is **additive**: a child activity can still carry its own directly-assigned manager/expert; the inherited parent access stacks on top of that, it doesn't replace it.
- This also refines ticket B5: whatever the filter-vs-restriction answer turns out to be there, a manager's "own team" scope must include their child activities, not just their own.
- Implementation scope: this hierarchy is implemented in `expert-space.html` only for the current prototype phase — see `SPEC-domain-model.md` §9.0.

## Resolved since this spec was first written

Both points originally marked open here are now resolved:

1. **Compliance export granularity — resolved by D8.** R&D Needed stays a structured, countable compliance value (not free text), so the export concern this point raised does not apply — the count is preserved by construction.
2. **Category list values — resolved.** `expert-space.html`'s `CATEGORY_LIST` is seeded with concrete values (Design & Engineering, Operations, Compliance, Integration, Performance & Validation, Other).

## Historical note — a correction that was itself later reversed

An earlier revision of this spec noted: *"The Compliance atom in Figma had 3 variants (Compliant / R&D needed / Not compliant). It's been reduced to 2 (Compliant / Not compliant) to match the model confirmed in this session."* That 3→2 reduction is what D8 (TF3) later reversed back to 3 — see the provenance note at the top of this file. Recorded here rather than deleted, per this corpus's no-silent-deletion rule.

## Follow-up — now current

- `SPEC-domain-model.md` has been updated with the activity hierarchy (permissions-only, arbitrary depth) — see its §9.
- `SPEC-backend-requirements.md` §12 (Access Control) should still be checked against the two-surface model (B11) once that UI is built — not yet done, tracked as open work in `docs/tickets/TICKETS-review-expert-batch4.md`.
