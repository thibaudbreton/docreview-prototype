# SPEC — External partner companies on Turnkey tenders

> Status: v1 scope agreed. Applies to Turnkey tenders only for now.

## 1. The principle: the Turnkey OBS list is not the model's label set

On a Turnkey tender, pass 1 (the Turnkey model) outputs an **OBS, and that OBS is a system** — the system (activity) the requirement is distributed to, before that system's own model runs pass 2.

An external partner company takes the place of a system on part of the scope. So it belongs **at the same level as the systems: in the Turnkey OBS list**.

Two lists must not be confused:

| | The Turnkey model's label set | The Turnkey OBS list in the UI |
|---|---|---|
| What it is | The closed set of systems the model can predict | The systems a requirement can be assigned to at pass 1 |
| Who owns it | The model | The tender configuration |
| Can it be extended per tender? | **No** | **Yes** |

The model's label set is closed by design and protected by test cases — "Verify Predicted Labels Are Only From [Model] Label Set" and "Verify Invalid or Unsupported Label Is Not Generated". So **no temporary system can be indexed on the model**. The model never predicts the partner; a human assigns it.

## 2. What to build in v1

**2.1 Add a system to the Turnkey OBS list, from the settings**
- In the tender settings, the PM can add a system to the Turnkey OBS list.
- Available on **Turnkey tenders only** for now.
- Field: name of the partner. Nothing else in v1.
- The added system then appears in the Turnkey OBS list everywhere it is used: allocation screen, detail panel, filters.

**2.2 Distinguish added systems visually**
- Added systems render in a **different colour** from the model's systems, everywhere the list appears.
- The colour means one thing: *this system does not come from the model* — the AI never predicted it, and the partner is not in the tool.
- A tooltip states it plainly: added for this tender, not part of the model.

**2.3 No pass 2 for an added system**
An added system has no allocation model and no teams. A requirement assigned to it stops at pass 1: no team-level OBS, no second nesting level under that branch.

## 3. The blocking case, and the v1 rule

Consolidation ("most restrictive wins") requires **every system branch to answer**. A branch assigned to a partner with no tool access would never answer, so the requirement would stay pending forever, with nothing on screen explaining why.

**v1 rule: the PM enters the compliance verdict on the partner's behalf**, at the system level.

- The PM fills the verdict from whatever the partner sent back (email, Excel, call).
- That verdict is the added system's verdict and consolidates with the other systems exactly like any other system verdict.
- No consolidation exemption, no new status, no "waiting for external partner" state in v1.

## 4. Sending the requirements to the partner

Nothing new to build. The filtered export already covers it (batch 6, "Export what the filters currently show").

1. PM filters the table on the added system.
2. PM exports what the filters show. The export states the row count and the active filter in plain language, so the PM checks the subset before it leaves the tool.
3. Partner answers off-tool.
4. PM enters the verdicts (see §3).

## 5. Deliberately not in v1

- **No tool access for the partner.** No account, no restricted view, no external login.
- **No new concept in the data model.** An added system is an entry in the tender's Turnkey OBS list, not a new object type.
- **No consolidation exemption.** The branch must be answered like any other system.
- **No re-import of the partner's answers.** The PM types them in (consistent with Excel/CSV re-import deferred to v2).
- **Nothing on the model side.** No temporary labels, no per-tender label set, no retraining.

## 6. Open

**6.1 Should the partner's verdict be marked as entered on someone's behalf?**
As written, the verdict looks like the PM's own judgement — three months later nobody can tell which verdicts came from a partner. Options:
- (a) Leave as is — simplest, loses the distinction.
- (b) Derive it: the branch is on an added system, already coloured differently, so the row explains itself. No new field.
- (c) An explicit marker on the verdict.

**Recommendation: (b).** Worth confirming.

**6.2 Who is shown as responsible for an added system's branch?**
An added system has no contributors, so the branch has a system but no person. In v1 the PM is de facto responsible (§3); the UI should say so rather than show an empty assignee.

**6.3 Should added systems be reusable across tenders?**
If the same partner comes back on the next Turnkey tender, the PM re-adds it. Acceptable in v1; a shared list of known partners is the v2 move.
