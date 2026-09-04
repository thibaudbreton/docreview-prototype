# Ticket — Two-pass allocation model

> Replaces the single-pass allocation the prototype implements today. This is a structural change, not an adjustment: it changes how many allocation levels exist, in what order the fields are derived, and what happens when no model exists for an activity.

## What changes

### 1. Turnkey adds a distribution pass in front

A **Turnkey** tender runs **two passes**:

**Pass 1 — distribution across activities.** Characterisation feeds a single-dimension decision:
- **Non-technical → ABS**
- **Technical → PBS**

That dimension produces the **TK OBS, which is an activity** (SIG, RSC, INFRA…). The TK OBS then **routes the requirement into that activity's own allocation model**.

**Pass 2 — the activity's own model**, which resolves down to a team and then a person.

**Every other tender type skips pass 1 entirely.** A SIG tender is already scoped to SIG, so characterisation feeds straight into the SIG model. Nothing to distribute.

**Why only some activities have a model:** SIG and RSC are large enough to be tender types in their own right, so their allocation models were built for those standalone tenders. Turnkey reuses them when it routes there. Activities that never stand alone as a tender have no model — see §3.

### 2. The chain is sequential, not crossed

**`PBS → ABS → OBS`.** Each step derives from the previous one.

This corrects a long-standing assumption in the corpus, which described allocation as `ABS × PBS → OBS`. It was wrong. Consequences:

- The detail panel must present them **in derivation order**, not as three equivalent fields.
- Correcting the PBS invalidates what follows. The interface should make that consequence visible rather than leaving stale downstream values sitting there looking valid.
- `SPEC-domain-model.md` needs correcting.

At pass-2 level, the **OBS is a team or service** — matching the perimeter values in the real casting file (DBM, Risk, BTM, Wayside…). This closes the loop with casting: pass 2's OBS is what casting staffs.

### 3. Activities without a model — a normal state, not an error

**Most activities have no allocation model.** SIG and RSC do; INFRA does not, and neither do many others. So manual allocation is a **routine mode of working**, not an exception to handle.

The prototype must treat it as first-class:

- After pass 1, a requirement routed to an activity with no model sits in a clear state: **activity known, fine allocation to be done manually**.
- This must be visible and filterable — it's a real queue of work, not a failure.
- **The contributors assigned to that activity do it.** Not the project manager by default. Any contributor on that activity can allocate within it.
- If nobody is assigned to that activity at all, it falls to the project management team, who have no scope restriction — consistent with the existing rule.

### 4. Confidence at every level

**Each of PBS, ABS and OBS carries its own confidence**, at both passes. They are independent: the AI can be confident on the PBS and unsure on the ABS derived from it.

- Show doubt **per level**, not collapsed into one row-level signal.
- The existing per-field doubt filter extends to each of them.
- Pass 1's TK OBS carries its own confidence too — being unsure which *activity* a requirement belongs to is a distinct and consequential kind of doubt.

### 5. Reassignment maps onto the two passes

The three reassignment reasons now have a clear structural meaning:

- **Wrong activity** → a pass 1 error. Re-runs the distribution.
- **Right activity, wrong person** → a pass 2 error. Stays within the activity.
- **This activity doesn't apply** → a pass 1 rejection.

Unchanged: reallocation is always a replacement, never a removal. A requirement can never end up with no activity.

### 6. Both passes can be multiple

**Pass 1 can assign several activities** to one requirement, and **pass 2 can assign several teams** within an activity. Allocation is therefore a **two-level branching tree**, not a chain.

One requirement → N activities → each with M teams. A requirement touching three activities, one of which involves two teams, has four leaves.

**This breaks the current expand pattern.** The Expandable Parent Row / Branch Sub-row molecules handle exactly one level of nesting. Two are now needed — activity level, then team level within it. Collapsing both into one flat list of leaves would lose the activity grouping, which is what people actually reason about.

**Compliance consolidation — decided: the same rule, applied twice.**

Most restrictive wins, at each level:

1. **Teams → activity.** Where several teams answer within one activity, the most negative verdict becomes the activity's verdict.
2. **Activities → requirement.** The most negative activity verdict becomes the requirement's overall verdict.

So an **activity carries its own verdict**. It is never entered by anyone — it is derived from its teams, exactly as the requirement's verdict is derived from its activities.

Two things follow mechanically:

- **Pending propagates upward.** An activity stays pending until every one of its teams has answered; the requirement stays pending until every activity is resolved. One silent team blocks its activity, and therefore the final verdict.
- **A locked final verdict is excluded from recalculation** — otherwise the lock would mean nothing. Since locking only happens at the top, this applies there and nowhere else.

**The lock applies only at the top level** — the requirement's final verdict. Never a leaf, never an activity.

This fits what the lock is for: the final verdict is what goes into the compliance matrix sent to the client, and locking it says "this is our answer, whatever the tree computes underneath."

Consequences:
- The tree below keeps computing normally. Contributors can still work and change their verdicts; the derived activity verdicts still update. The final verdict simply stops following them.
- **The lock is visible to everyone allocated on that requirement**, not just the last person who answered — several contributors may be working underneath a verdict that no longer reflects their input, and they need to know.
- The original computed verdict is preserved and shown in the detail panel only, as already specified.

## Prototype impact

**The table needs to show two allocation levels on a Turnkey tender, one on the others.** Today there is a single OBS column, which no longer carries one meaning: at pass 1 it's an activity, at pass 2 it's a team.

Options — pick one and be consistent:
- Two distinct columns (activity, then team/person), the first empty on non-Turnkey tenders;
- Or one column whose meaning follows the tender type, clearly labelled.

**Do not reuse "OBS" as a single label for both.** Two different things under one name in the same table is how users lose trust in what they're reading.

Also affected:
- **The detail panel** — sequential presentation, per-level confidence, both passes visible on Turnkey, and two levels of nesting where allocation branches.
- **Row expansion** — two levels instead of one.
- **Filters** — by allocation level, by pass, and by "awaiting manual allocation".
- **The activity list** must distinguish activities that have a model from those that don't.

## Definition of done

1. Turnkey tenders run pass 1 then route to the activity's model; other tender types skip pass 1.
2. Pass 1 uses one dimension only, chosen by technical / non-technical.
3. PBS, ABS and OBS are presented and derived in sequence, not as a crossing.
4. Each level carries and displays its own confidence.
5. Activities with no model produce a clear, filterable "manual allocation" state, actionable by that activity's contributors.
6. The table never labels two different things "OBS".
7. `build_merge.py` runs clean, `node --check` passes, zero dead hrefs.

## Open

- **Which activities have a model**, beyond SIG and RSC. Needed to seed the prototype accurately rather than guessing.
- **Activity-level views.** With allocation now branching at two levels, the activity becomes the unit people are assigned to, reason about, and now hold a verdict at. That makes activity-oriented views considerably more important than they were — for a contributor working their own scope, and for a project manager following a Turnkey tender across many activities. Specified separately; this ticket only establishes that the activity carries a verdict.
