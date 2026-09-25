# SPEC — Compliance decision panel

> The detail panel on the Compliance screen, where a contributor decides a requirement they can't judge at a glance.
>
> **Not a redesign of the screen.** Fast validation already works through the table — select, batch-validate, move on. This covers the other case: the requirement that needs actual attention, where the current panel gets in the way.

## 1. Why the current panel fails

It treats everything at the same level of importance — the requirement text, the allocation, the fields, the verdict form, all flat. But there is **one thing to read** and **one thing to decide**. Everything else is called on when needed and otherwise in the way.

## 2. The contributor's questions, in the order they arrive

The panel exists to answer these. Its layout should follow them.

### "What exactly are they asking for?"

The requirement text, **in full and legible**. Not truncated, not squeezed into a narrow column. Where it contains figures, formulas or a table, those must be readable as written rather than reconstructed from a wrapped paragraph.

Immediately after comes: **"what does that mean in their context?"** — so the clause in the source document, where it sits, with what surrounds it. One gesture away.

### "Is this actually mine?"

A glance to confirm they're in the right place. **Not a detailed allocation block** — just enough not to have to wonder. One line.

And if the answer is no, **the return action is right there**, not buried in a menu. The three reassignment reasons apply as specified.

### "Have we already answered this?"

**The single biggest time-saver on slow cases.** A near-identical requirement a few pages later, or in a past tender. Today this is done from memory, or re-decided from scratch.

This is where similarity grouping — shelved earlier when it was imagined as a sweeping aid — actually earns its place: not to clear easy items faster, but to stop experts re-solving the same problem.

### "What do we know?"

What the product actually does, REX, what colleagues have already decided on the same subject.

### "And if I don't know?"

**Two exits, not one:**
- **Ask the client** — the Q&A cycle.
- **Set aside** — a personal "come back to this", not a shared status.

If the only visible way out is rendering a verdict, a verdict will be rendered. That's how a hard case gets rubber-stamped.

### "What am I risking by saying compliant?"

Since compliance split into internal and external, this question has a clean answer, and **the panel should make it visible**.

The contributor gives the **technical truth**. The commercial bet — declaring compliant when internally it isn't — belongs to the project manager, with a documented risk.

**This should relieve them.** They no longer arbitrate alone between honesty and commercial pressure. But that only works if the interface says so plainly — otherwise they'll keep self-censoring the way they do today, and the internal verdict becomes as unreliable as the old single one.

## 3. One primary action, and nothing competing with it

The section above lists a lot of needs — readable text, document, REX, similar requirements, chat, set aside, ask the client, return the allocation, draft, internal, external. **If each of those becomes a visible button, the panel fails the same way it fails today**: everything at the same level, nothing obvious.

So the hierarchy is fixed:

**One primary action: render the verdict.** It's what the contributor came to do in the overwhelming majority of cases. Always in the same place, unmistakable, never competing with anything else.

**Two secondary actions, visible but quieter: ask the client, and return the allocation.** Neither is rare — misrouted allocation is a confirmed, real share of the flow — so neither hides in a menu. But they don't fight the primary action for attention.

**Everything else is consultation, not action.** Document, REX, similar requirements, chat: tabs in a resources area, not buttons. Treating them as actions is exactly what clutters the panel.

**Two things that aren't buttons at all:**
- **The draft saves itself.** It isn't clicked.
- **Set aside is a light gesture** — an icon, a shortcut — not a button carrying the same weight as rendering a verdict.

### Labels

Say what the action does, not what it is. **"Not compliant"**, not "Save verdict".

And the standing rule: **"Ask the client"**, never "Ask a question" — otherwise someone sends an official question believing they're querying the chat.

### Where simplicity gives way, deliberately

**Not compliant opens Category + Topic. Compliant takes one gesture; Not compliant takes two.**

That friction is wanted. It's where a refusal gets documented, and the difference in cost matches the difference in consequence. Do not smooth it out in the name of speed.

## 4. What that implies for the layout

- **The requirement text dominates.** By a wide margin. It's what the whole panel is for.
- **The decision is immediately reachable** — no scrolling to find it, no mode to enter.
- **Allocation context shrinks to one line.**
- **Resources are one gesture away, not permanently expanded** — document, REX, similar requirements, chat.
- **The panel can widen.** A long requirement with figures or a formula doesn't fit a narrow column — a physical constraint, not a preference. Same panel, more width when the case calls for it, and back afterwards. Not another screen.

## 5. Missing everywhere today: where am I?

The contributor has no sense of progress — how many are left, where they are in their queue.

Without it, they can't judge whether they can afford ten minutes on this one. That judgement happens constantly and is currently made blind.

## 6. Draft state

A hard verdict can span two sessions. If the only options are "render a verdict" or "nothing", partial work is lost — and the contributor is pushed to conclude early.

A verdict in progress must survive leaving the panel.

## 7. Out of scope

- **Difficulty detection.** No automatic flagging of "probably hard" requirements. The contributor sorts their own work; the tool doesn't guess.
- **Redesigning the screen.** Table-based batch validation stays exactly as it is. This spec touches the panel only.

## 8. Open

- **Similar-requirement matching** (§2) reuses the similarity capability already available on the platform, but nothing specifies how matches are surfaced, ranked, or how many are shown. Needs its own pass.
- **Set aside** (§2) — whether the set-aside list is a filter on the table, a separate view, or just a marker.
