# Ticket — Merge the expert space into a single Compliance step

> Follows directly from user test session 3: within their own activity, experts and bid managers have the same permissions. The role distinction that justified a separate expert screen no longer exists.

## The change

**There is no expert space.** The second step of the workflow becomes **Compliance**, and it serves both audiences from one screen:

- **Contributors** enter their compliance verdicts there.
- **The project manager** does global follow-up there.

Same table, same components, same interactions the users already know from the review step — multi-select, bulk actions, filters, keyboard navigation. Someone moving from review to compliance relearns nothing.

## Vocabulary — only "contributor" survives

**"Expert" and "manager" are replaced by "contributor"**, everywhere: UI copy, code, comments, documentation.

The role model is now:

| Role | Scope |
|---|---|
| **Project Manager** | global follow-up, override and lock, consolidation |
| **Contributor** | enters compliance on what they're allocated, within their activity |
| VIP | read-only KPI dashboard, cross-project |
| Admin | internal platform management |

The boundary that survives is **project manager vs. contributor**. Manager vs. expert is gone.

This supersedes the pending vocabulary work, which had `Branch Manager → Activity Manager`. That rename is void — the target is now `contributor`.

## What to build

### 1. Rename the second step to "Compliance"

Its purpose is now explicit rather than role-based. Update the step navigation and any screen title accordingly.

### 2. Add the missing piece: entering a verdict

The screen is largely usable as it stands. What it lacks is the verdict form itself:

- **Compliant** → a single free comment field.
- **Not compliant** → a **Category** (closed list) plus a **Topic** (free text).
- "R&D needed" is not a value — it's written as plain text inside a Compliant comment.

**Blocked, partially:** the Category list has no defined values yet. Build the field; the list can be populated later. Do not invent values — use an obvious placeholder and mark it as such.

### 3. Move the research panel into the detail column

The expert space had a collapsible right-hand panel with Document / REX / Chat. **That idea stays** — it was never about being an expert, it was about the task: rendering a verdict sometimes means digging.

It becomes **tabs inside the detail column**, alongside the tabs already there. This collapses the three-zone layout to two — table plus detail — which is simpler and consistent with the review step.

- **Document** — the tender, opened at the position relevant to the current row.
- **REX** — REX linked to the current requirement.
- **Chat** — with the existing switch between the tender document and the company's internal documents.

**Keep the naming safeguard:** the Chat tab and the "Ask the client" action must stay visually and verbally distinct. Chat answers instantly with no consequence; asking the client leaves the company for days and blocks consolidation. If both read as "ask a question", someone will send an official question by mistake.

### 4. Default scope differs by role, on the same screen

- **Project manager** lands on global follow-up — everything.
- **Contributor** lands on what's allocated to them.

Same screen, different default scope. This mirrors what was already specified for the follow-up view; it is not a second implementation.

### 5. Show the compliance comment inline

Already on the prototype to-do from session 3, and it belongs here: the comment must be visible alongside the verdict without opening anything. For anyone reviewing or following up, the reasoning matters as much as the value.

## Documentation to update

- **Archive `SPEC-expert-space.md`** — superseded. Add the header `> SUPERSEDED by the Compliance step on <date>. Kept for reference. Do not build from this.` Do not delete it: it holds the reasoning behind the research panel and the Ask-the-client naming risk, both of which survive.
- **The vocabulary alignment ticket** needs correcting: `Activity Manager` is no longer the target, `contributor` is.
- **Personas** — two of the three personas (the activity manager and the expert) now share one in-tool role. They remain distinct *people* with different profiles and motivations, so the personas stay as they are; only the role label changes.

## Not affected

The three profiles observed in the field — the fast verdict, the one needing research, the misrouted allocation — still hold. They were about the **task**, not the role, so they survive the merge intact. The research tabs exist precisely to serve the second one.

## Definition of done

1. The second step is named Compliance and serves both roles.
2. A contributor can enter a verdict, with the conditional Category/Topic form.
3. Document, REX and Chat are tabs in the detail column; the three-zone layout is gone.
4. Default scope differs by role on the same screen.
5. No "expert space" remains in the code or the UI, and no screen refers to "expert" or "manager" as a role.
6. `build_merge.py` runs clean, `node --check` passes, zero dead hrefs.
