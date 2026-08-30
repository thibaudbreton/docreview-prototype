# Ticket — Redesign the casting screen

> The current screen is unclear: choose a thing, add a thing, with no sense of where you are or what's left. It was designed for a handful of entries. The real casting holds **150 to 200 experts**, filled progressively by many people. That difference in scale is the whole ticket.

## What this screen actually is

**Project user management.** Not a step in project creation — a permanent screen that says who can do what, and on which scope. People are added and changed throughout the project's life, not settled once at the start.

Framing it as user management rather than as a creation step is what makes the rest coherent: nobody expects to finish user management in one sitting, and nobody expects it to block everything else while it's incomplete.

**The point is to start work on the tender before the casting is complete.** Capture and characterisation don't need it at all; allocation needs it only for the activities actually present in the document. Anything the casting doesn't yet cover falls to the project management team, who have no scope restriction — so an incomplete casting slows things down, it never stops them.

## Two populations, not one

The screen manages two distinct groups:

### The project management team

**Several people hold project-manager status, not one.** The PM will not be running the whole tender alone, and everything specified so far assumes a single person — that assumption is wrong and needs undoing.

- Any member of the team can do what "the project manager" does today: consolidate, override and lock a verdict, arbitrate Q&A matching, manage the casting itself.
- Their scope is **the whole project** — no activity restriction. That's what distinguishes them from contributors.
- The person who creates the project is automatically the first member.
- A team member can add another.

**Consequence across the specs:** every place that reads "the Project Manager" should read "a member of the project management team". This affects compliance override and lock, Q&A arbitration, the dashboard follow-up view, and casting management itself.

### Contributors

Attached to an activity, and optionally to a perimeter within it. They work on what allocation assigns them, scoped to their activity.

**Confirmed: project-manager status carries no scope restriction at all** — like an admin. So "a PM is also a contributor" is a description of what they do, not a permission to grant. There is nothing to assign: they can already modify and give compliance anywhere on the project.

Two situations where this matters in practice:

- **Their own specialty.** On a SIG tender, the PM is often a SIG specialist themselves, and works requirements alongside everyone else.
- **Requirements belonging to no team.** Where the casting has nobody matching, the PM covers them — which is also a partial answer to the gap raised in user test session 3. Not necessarily the whole answer, but a real fallback rather than a dead end.

**Design consequence:** do not build a mechanism to add a PM as a contributor. Do not show them as one in the roster either — it would suggest a restriction that doesn't exist. What they need is simply not to be blocked anywhere.

## The data chain

**Activity / sub-activity → perimeter → expert.** An expert is attached to a perimeter; the perimeter belongs to an activity. Each expert then carries their own details (identity, contact), which SSO supplies — nothing about a person is typed by hand.

**The perimeter is optional.** Sometimes staffing happens at the activity level alone, with no perimeter involved. So an expert can be attached either to a perimeter, or directly to an activity. Do not force a perimeter choice — a required field here would push people into picking something arbitrary just to get past it.

The real activity and perimeter values should replace the mockup's invented ones. That alone does more for credibility in a user test than any layout change.

## Who uses this screen, and how they arrive

Two very different entries, and the screen must serve both:

**A contributor responsible for an activity**, arriving from their invitation email. They care about one thing: staffing their own scope. They should land **directly on it**, already expanded, ready to add someone — not on a 200-row list they have to navigate. Everything else stays available but out of the way.

**A member of the project management team**, arriving to check where things stand. They care about coverage: which activities still have nobody, and whether allocation can run. They land on an **overview grouped by activity**, with completeness visible at a glance rather than counted by hand. The project management team itself is visible and editable here too — it's part of who can do what on this project.

## Core behaviour: adding someone must be fast and repetitive

This is the interaction that happens 150+ times. Everything else is secondary.

- **Search a person via SSO**, typeahead. Pick from results. No typing names, no looking up emails, no spelling mistakes — this is the single biggest gain over the current shared file.
- **Assign an activity, and optionally a perimeter within it.** The choice is scoped to what the current user may staff: their own scope and anything nested beneath it. The PM sees all. Leaving the perimeter blank is a valid, ordinary outcome — not a skipped step to nag about.
- **After confirming, stay put.** The form resets to an empty person field, in the same perimeter, ready for the next one. Do not close a panel, do not scroll away, do not make the user re-navigate to their section. Adding twelve people should be twelve searches, not twelve journeys.
- **Keyboard-first.** Type, arrow to the right result, Enter, type again. Someone staffing a large perimeter shouldn't need the mouse.
- **The same person can hold several perimeters.** Offer to add them to another perimeter without searching for them again.
- **Warn on duplicates** — same person, same perimeter — rather than silently creating a second row.

## Making progress visible

The casting's whole purpose is to make allocation possible, so the screen must answer "are we there yet?" without anyone tallying rows.

- **What's unstaffed is the important state**, not what's filled. Whatever blocks allocation — an activity with nobody on it, or a perimeter left empty where perimeters are being used — should read as visually unfinished, not as a neutral empty row indistinguishable from a completed one.
- **Show coverage per activity**, so a PM sees which activities are lagging without expanding each. Since perimeters are optional, coverage is judged at the activity level: an activity staffed directly, with no perimeter breakdown, is complete — not partially filled.
- **What the document actually involves comes first.** Once characterisation has run, the system knows which activities and perimeters this tender genuinely touches. Those are what matter; the rest of the reference list is noise and should be secondary or collapsed.
- **Attribution** — who added whom, and when. A useful piece of context for the PM rather than a core feature: worth surfacing where it doesn't compete with the above, not worth building a whole view around.

## Handling 200 rows

- **Grouped and collapsible** by activity, then by perimeter where perimeters are used. Experts attached straight to an activity sit at the activity level, not under a placeholder perimeter. Never a flat 200-row list.
- **A manager's own perimeters are expanded by default**; everything else collapsed.
- **Search across the whole roster** — "is this person already on the project, and where?" — so someone can check before adding rather than after.
- **Filter to what's unstaffed**, since that's the actionable subset.
- Nothing about the layout should degrade as rows accumulate: adding the 180th person should feel like adding the 3rd.

## Removing and changing

- Removing a person from a perimeter is straightforward while nothing depends on them.
- If they already hold work on this tender, **reassignment applies rather than deletion** — the existing rule stands: a requirement can never end up with no one on it. Surface that consequence at the moment of removal instead of letting the user discover it afterwards.

## States to handle

- **Nothing staffed yet** — the first manager to arrive. Should be inviting and obvious, not an empty grid.
- **Partially staffed** — the normal state, most of the time. Must communicate what's missing without alarm.
- **Fully staffed** — say so plainly; this is the signal the PM is waiting for.
- **No permission** — a manager looking at a perimeter that isn't theirs sees it read-only, with a clear reason, not a dead control.

## Definition of done

1. A manager arriving from their email link lands on their own scope, expanded, ready to add.
2. Adding several people in a row requires no re-navigation between them.
3. Anything unstaffed is visually distinct from anything staffed, at a glance.
4. An expert can be added to an activity without choosing a perimeter, with no friction.
5. The screen stays usable and responsive with 200 entries.
6. Real activity and perimeter values replace the mockup's invented list.

## Open

- Does the activity level carry permissions of its own — can someone act across a whole activity — or is it purely a grouping?
- The perimeter reference list exists for one activity in the source material. Is it maintained centrally for the others, or per tender?
- **What remains in the project creation flow.** If casting is ongoing user management, creation only needs enough to start: metadata, documents, and whoever is on the project management team at the outset. To confirm as part of reworking the creation flow.
