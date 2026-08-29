# User test — session 3

Session with a requirement management user. Focus on the first half of the flow (project creation → review → allocation), with a shorter pass over expert review and follow-up.

**Overall reception:** good satisfaction on the UI, assessed as clear. No usability blockers surfaced. The qualifier is that it needs a full-scale test on real volume — **possible early October with a Dublin tender, scoped up to allocation and no further.**

---

# Part 1 — Findings

## 1.1 Model changes

Two findings change the domain model rather than the interface. Everything else in this report is downstream of them.

### One responsible person per requirement, not two

There is no need for both a manager and a responsible expert. **Allocation resolves to one person, and that person owns the requirement.**

This overrides the previous model, which assigned one manager *and* one expert per activity on every requirement.

Consequences:
- The detail panel showed both roles per allocated activity — one becomes redundant.
- Reassignment "right activity, wrong person" still holds, but there is only one person to change.
- Casting no longer needs to guarantee a manager *and* an expert per activity — it needs to guarantee **someone**.
- "Who is this waiting on" becomes unambiguous on the follow-up screen.

### No action boundary between experts and bid managers

Within their own activity, experts and bid managers can do the same things. **The role is not a permission boundary.**

Consequences:
- The compliance screen must be **directly accessible to non-project-manager roles**.
- **Every screen filters by activity** for any user attached to one. Scope comes from the activity, not the role.
- The split between the expert workspace and the manager follow-up view is now about what each needs to **see**, not what they're **allowed to do**.

The boundary that survives is **project manager vs. activity-attached user** — not manager vs. expert.

## 1.2 Allocation rules by system

**For Turnkey, the expected outcome of allocation is the activity itself** — the OBS *is* the activity, unlike the other systems which resolve down to a person.

They also want to **select an expert afterwards**. Confirmed in scope: the other systems need person-level resolution anyway, so the capability exists regardless. For Turnkey it's an **additional step on top** of the activity decision, not a replacement for it.

Consistent with Turnkey being the umbrella system drawing on all the others — and further confirmation that allocation rules genuinely vary by system rather than being one rule with an exception.

## 1.3 Project creation

- **"Tender reference" is called `BO-ID`.**
- **Product Line has no list at all** — needs every system: Turnkey, RCS, SIG, INFRA and the rest.
- **Region must use the real acronyms.** They exist and need collecting; improvise for now.

## 1.4 Review table

- **The ID must be stable regardless of content type** — headings, information and requirements share one identifier scheme. Today it's per category.
- **A document can be added mid-project**, with the AI run on it afterwards. The project isn't sealed at creation.
- **Export must work per document**, not only for the whole tender.
- **Columns must be reorderable**, and must be able to **disappear entirely** — collapsing isn't enough.
- **Filtering needs a rule builder**, not more presets — see 1.6.

## 1.5 Expert review & follow-up

- **The compliance comment must be visible at a glance**, next to the verdict. Today the verdict shows and the comment sits behind an interaction — but for anyone reviewing or following up, the reasoning matters as much as the value.

## 1.6 Needs its own design pass

**Advanced filters — a rule builder.** The target is closer to Excel's advanced filters: the user composes a **list of conditions**, combined, rather than picking from a fixed set. This is a distinct feature from today's per-column filter chips, not an extension of them, and deserves specifying properly.

**Turnkey's expert selection**, layered on top of activity-level allocation.

## 1.7 Still open

**What happens when the casting has nobody matching an activity** present in the document. This gap is a direct consequence of the reorganisation in 1.1 — the model has always assumed casting covers every activity in the document, and this is the first sign it won't.

**Partial answer since:** the project management team has no scope restriction, so uncovered requirements fall to them by default. That removes the dead end — work can proceed regardless. What remains open is whether that's the intended resolution or merely a safety net, and whether anything should actively flag uncovered activities rather than letting them sit with the PM team unnoticed. Still worth the session with more experts.

## 1.8 Raised, deliberately not tackled

A review document — a document whose purpose is to review another. Noted, no action.

---

# Part 2 — Prototype to-do

Ordered so the quick, self-contained items come first. Formatted for the nightly routine.

- [ ] **Rename "Tender reference" to `BO-ID`** on the project creation screen.

- [ ] **Populate the Product Line list** with the full set of systems — Turnkey, RCS, SIG, INFRA and the others. Currently there is no choice to make.

- [ ] **Add region acronyms** to the region selector. The real ones aren't collected yet — use plausible placeholders and mark them clearly as such in a code comment, so they're not mistaken for confirmed values.

- [ ] **Make the row ID independent of content type.** One identifier scheme across headings, information and requirements, instead of the current per-category numbering. A row keeps its ID when its type is corrected.

- [ ] **Blocked state on "Ask the client" once the question deadline has passed.** In the compliance step, the ask-the-client action shows a blocked state when the tender's question cut-off date is behind us, stating why rather than just greying out. The project manager can still push a question through — a late question negotiated with the client is a real situation, and a hard block would just get worked around. If no cut-off date is set, the action behaves normally with no indicator.

- [ ] **Show the compliance comment inline** with the verdict, in the review table and on the follow-up screen — visible without opening anything.

- [ ] **Allow full column removal, not just collapse.** The column visibility menu should be able to take a column out of the table entirely.

- [ ] **Allow column reordering** by the user.

- [ ] **Keep the active cell in view when navigating.** The scroll should follow the selected cell — vertically when moving between rows, and horizontally when moving between columns, so the active cell never ends up off-screen. Applies to keyboard navigation and to any programmatic selection change.

- [ ] **Add per-document export.** Export currently covers the whole tender; it must also work for one document at a time.

- [ ] **Allow adding a document mid-project**, with the AI pipeline runnable on it after the fact. The project isn't sealed at creation.

- [ ] **Make the compliance screen reachable by activity-attached users**, not only the project manager.

- [ ] **Collapse allocation to a single responsible person.** Remove the manager/expert pair per activity from the detail panel, the follow-up screen and the casting screen; allocation designates one person who owns the requirement. **Larger than the others and touches several screens** — if it can't be completed cleanly in one pass, leave it unchecked with a blocker note rather than committing a half-change.

<!--
Not in this list, deliberately:
- advanced filter rule builder → needs its own spec first (1.6)
- Turnkey expert selection → needs its own spec first (1.6)
- casting with no matching person → undecided (1.7)
- review document edge case → out of scope (1.8)
-->
