# SPEC — Risks module

> Status: v1 scope agreed, with open points in §12.
> Written without seeing the current Risks page in the prototype. The prototype remains ground truth: where it already differs, reconcile against it rather than this file.
> Partly supersedes `SPEC-internal-external-compliance.md` (see §10).

> **Reconciled with the prototype and arbitrated on 2026-09-30 (DEC-105 to DEC-112). Where this file and the decisions differ, the decisions win:**
> - §1 "no PM override" — **the PM can correct a derived external compliance**, with a mandatory, visible reason, revertible (DEC-106).
> - §2.2 Risk logging per activity — **not in v1**: a risk is expected on every Not compliant, SIG included (DEC-109).
> - §3.3 Category + Topic — Turnkey only, as written; the prototype asked for them on every tender and is aligned (DEC-107).
> - §12.1 — **not blocking**: the verdict saves; a missing strategy or risk flags the assignment ("Strategy missing" / "Risk missing"); without a strategy, external stays Pending (DEC-108).
> - §12.2 — **the strategy list starts empty**; the PM writes it (DEC-110). Demo tenders carry one.
> - §12.3 and §12.4 — as recommended (DEC-111).
> - §5 IDs — requirements are `SRM-` / `L4-` in the prototype; risks are `RSK-00001`.
> - **DEC-113 (same day, supersedes parts of the above):** a risk is only its justification — the three answers of the template, entered as three fields — and its links. **No weight, no Open/Closed status, no comments, no merge**: the risk work is done outside the tool. §4.1 stands (pick an existing risk first, create one only if none fits). §4.2's weight, §5's Weight/Status/Comments, §6.1's matrix, §6.3's comment feed, §6.4 entirely, and §9's "Risks by weight" and "Weight × strategy" are dropped; the Risks page is the list of risks with their justification and linked requirements; §12.3 is moot.

## 1. Principle

Every non-compliance must be traceable to a risk, and risks are **reused**, not created once per requirement. In practice, a few hundred non-compliant requirements end up pointing at roughly half as many risks.

The whole module rests on one extra gesture in the compliance flow: **after Not compliant, the responsible picks a gap strategy and links a risk — an existing one first, a new one only if nothing fits.** The register, the matrix and the dashboard stats are all derived from that gesture. Nothing else has to be filled anywhere.

**Ownership:** the compliance responsible of a requirement (the person designated by allocation) owns it from start to end — internal compliance, gap strategy, and therefore external compliance. There is no lock and no PM override.

## 2. Configuration (per tender)

**2.1 Gap strategies — written for each tender**
- The PM defines the tender's strategy list in the tender settings.
- Each strategy has two fields: **name**, and **external result** — the external compliance it produces: `Compliant` / `Not compliant` / `Pending`.
- Example of what a tender's list typically looks like (not a fixed list):

| Strategy | External result |
|---|---|
| Declare NC in offer | Not compliant |
| Request adjustment | Pending |
| Change to reach compliance | Compliant |
| Keep as a gap | Compliant |

- A strategy that is in use cannot be deleted, only renamed.

**2.2 Risk logging per activity**
- Each activity has a **Risk logging** setting, on by default.
- Off for SIG.
- When off, Not compliant still requires a gap strategy (external compliance depends on it) but no risk is linked.

## 3. The compliance flow (contributor)

Unchanged up to the verdict. After **Not compliant**, the decision panel shows, in this order, inline (no modal):

1. **Gap strategy** — a list of the tender's strategies. Once picked, a read-only line states the consequence: *"Declared to the client: Compliant"*.
2. **Risk** — only if the activity has risk logging on (§2.2). See §4.
3. **Category + Topic** — Turnkey only, unchanged.

One primary action, as before (`SPEC-compliance-decision-panel.md` §3).

## 4. Linking a risk

**4.1 Existing risks first**
The Risk step opens on a list of the tender's existing risks, ordered:
1. risks already linked to requirements under the **same heading** (chapter),
2. then risks linked in the **same activity**,
3. then the rest.

Each suggestion shows its ID, the first line of its description, its weight, and **how many requirements it's already linked to**. A text search filters the list. One click links it.

**4.2 New risk, second**
A **New risk** action below the list opens an inline form:
- **Description**, pre-filled with the three-sentence template:
  *There is a risk that… / The risk is caused by… / The direct impact of the risk will be…*
- **Weight**: Negligible / Low / Medium / High — four buttons.

Saved risks are immediately linked and immediately available to everyone else on the tender.

**4.3 Several risks**
A branch can link one or more risks (chips, removable). One is the normal case.

## 5. The risk object

| Field | Notes |
|---|---|
| ID | `RSK-00001`, same convention as `REQ-` / `H-` / `INF-` |
| Description | Three-sentence template |
| Weight | Negligible / Low / Medium / High |
| Status | Open / Closed |
| Activity | Activity of the requirement it was created from; a risk linked across activities lists all of them |
| Created by | The contributor who created it |
| Linked requirements | Derived, never typed |
| Comments | Dated feed (author, date, text) |

**The strategy is not on the risk.** It is on each requirement's verdict (§3). Two requirements can share the same risk with different strategies — one declared non-compliant, the other kept as a gap. This is what keeps each responsible in control of their own requirement end to end: editing a shared risk never changes someone else's external compliance.

**Editing a shared risk:** description and weight can be edited by the creator and by the PM team. Others link, comment, or create their own risk if they disagree.

## 6. The Risks page

A tender-level module, alongside Q&A, Documents & versions and Casting.

**6.1 Matrix — top of the page**
Weight × strategy, counting links (requirement–risk pairs). Rows: High / Medium / Low / Negligible. Columns: the tender's strategies, plus Total. Clicking a cell filters the register below.

**6.2 Register**
Table of risks: ID, description, weight, status, activity, **linked requirements count** (click → Compliance table filtered on this risk), last comment date.
Advanced filters and filtered export, as on every table.

**6.3 Detail panel**
Clicking a risk opens: the full risk, its linked requirements (each with its strategy and responsible), and the comment feed.

**6.4 Actions**
- **Close / reopen** — creator or PM team. Closed risks stay linked and stay in the register.
- **Merge** — PM team. Select two or more risks, keep one; all links move to the kept risk; the others are deleted with a trace in the kept risk's comments. Needed because duplicates will happen despite the suggestions.

## 7. Compliance table and requirement detail

- A **Risk** column showing the linked risk IDs as chips, clickable to the risk.
- A **Strategy** column.
- **External compliance** stays a column but is read-only (§8).

## 8. External compliance is derived

- Internal Compliant → external Compliant. No strategy, no risk.
- Internal Not compliant → external = the chosen strategy's external result.
- Nobody types external compliance.

**Consolidation** follows the existing rule, per axis:
- internal as today;
- external: **Not compliant wins, Pending propagates**, otherwise Compliant.

A requirement with several branches can therefore carry several strategies and several risks; the requirement row lists them all.

## 9. Dashboard

| Stat | Computation | Display |
|---|---|---|
| **% NC logged** | NC branches with ≥ 1 linked risk ÷ NC branches, on activities with risk logging on | Added to the existing progress sequence: % identification → % assigned → % internal compliance → **% NC logged** → % external compliance |
| **Open risks** | Count of risks with status Open | Big number, with total alongside |
| **Risks by weight** | Count per weight level | Horizontal bar |
| **NC by strategy** | NC branches per strategy | Horizontal bar |
| **Weight × strategy** | Same as §6.1 | Compact table, each cell links to the filtered register |

## 10. Impact on existing specs

- **`SPEC-internal-external-compliance.md`**
  - The lock is removed (already removed from the prototype).
  - External compliance is no longer set by the PM: it is derived from the gap strategy, chosen by the compliance responsible.
  - The rule "risk field mandatory when internal Not compliant + external Compliant" (§2, §4) is replaced by risk linking on every Not compliant (§3–§4).
  - The case "internal Compliant + external Not compliant" (§5) can no longer occur.
  - Two axes (§1) and per-axis consolidation (§6) still apply.
- **`SPEC-compliance-decision-panel.md`** — the Not compliant path gains the Strategy and Risk steps.
- **`SPEC-dashboard-statistics.md`** — gains the stats in §9.
- **Turnkey Category + Topic** — unchanged, still Turnkey only.

## 11. Not in v1

- Over compliant as an internal value.
- Savings and Opportunities (risk type only in v1).
- Amounts: risk exposure, contingency provision.
- AI suggestion of similar risks (v1 orders suggestions by heading and activity only).
- Region approval on specific strategies.
- Risk reuse across tenders, and transfer to the project phase.

## 12. Open

1. **Is a missing risk blocking?** Recommendation: the Not compliant verdict saves, but the requirement stays *Incomplete* until a risk is linked. If it were blocking, % NC logged would always read 100% and tell nobody anything.
2. **Strategy list at tender creation**: empty, or pre-filled with a default set the PM edits? Recommendation: pre-filled with the four in §2.1, fully editable.
3. **Who may close a risk**, and does closing mean anything for the linked requirements? Recommendation: creator or PM team; no effect on the requirements.
4. **Changing a strategy's external result after use**: does it recompute every linked requirement's external compliance silently? Recommendation: yes, with a confirmation stating how many requirements change.
