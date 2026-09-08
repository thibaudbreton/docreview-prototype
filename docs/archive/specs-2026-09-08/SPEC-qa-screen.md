# SPEC — Q&A screen

> Support screen 3 of 3, alongside Casting and Documents & versions. Covers the full cycle: questions raised by contributors, reviewed and exported by the project manager, and the client's answers coming back and being attached to requirements.

## 1. Purpose

Contributors sometimes cannot answer a requirement without a clarification from the client. This screen carries that round trip.

**The hard part is the return, not the send.** Sending is a handful of actions on a list. Coming back are **hundreds of answers, in whatever format the client chose**, mixed with every competitor's questions — and matching them correctly is manual and broken today. That is the problem worth designing for.

## 2. Two distinct flows

The screen holds two tasks that share a subject but nothing else — different moments, different work, different people:

- **Outbound** — questions accumulate, the PM reviews and exports them. One batch, once.
- **Inbound** — the answer dossier arrives, gets matched, and the PM arbitrates whatever the matching couldn't resolve. Hundreds of items.

**Recommended:** one screen, two clear modes (Questions / Answers) rather than a fourth support screen. They belong to one subject, and contributors need to move between "what did I ask" and "what came back" without navigating elsewhere. Splitting them into separate screens would break that.

## 3. Outbound — questions

### Composing

A contributor raises a question from a requirement, during compliance work. It is an **identified object**, linked to the contributor who raised it and to their activity — not free-floating text.

### Review, by the project manager

The PM reviews the batch before it goes out.

- **Duplicate detection** surfaces near-identical questions so they can be merged. Several contributors hitting the same ambiguity is common and expected.
- **The PM cannot reject a question.** They simply **remove it from the export**. Deliberately kept simple for now.

  **Consequence worth knowing:** a contributor whose question was dropped won't be told, and will keep waiting on an answer that will never come. Acceptable for now, but it's a real gap — worth a notification later.

### Export

- **Excel**, one row per question, with the **requirement ID beside the question**.
- Nothing is ever sent from the tool. The PM takes the file and handles the send outside.

**One batch.** The cycle runs once per tender, not in waves.

## 3bis. Deadlines

Tenders normally impose a **cut-off for submitting questions**, and announce a **date by which answers will come back**. Not confirmed for this client, but common enough to design for — and if it holds, it's the most structuring information on the outbound side.

Build it so it degrades cleanly when unknown:

- **Two optional dates** on the tender: question cut-off, and expected answer date. Both may be empty.
- **When the cut-off is set**, it becomes the anchor of the Questions mode: time remaining, visible without being alarmist. As it approaches, contributors who were going to raise a question need to know they are running out of time — that's the whole point of showing it.
- **When it passes**, the batch is effectively closed. Do not hard-block raising a question — a late question that gets negotiated through is a real situation, and a tool that refuses it just gets worked around. Show clearly that the cut-off has passed and let the PM decide.
- **When the expected answer date is set**, it frames the Answers mode: what the team is waiting on, and whether it's overdue. An overdue dossier is a real problem — branches sit blocked in `Awaiting Q&A` and nobody can act.
- **When either is empty**, the screen simply doesn't show that framing. No placeholder, no "not set" state cluttering the view — the dates are optional and their absence is normal.

**One batch, one cut-off.** Consistent with the single-round cycle; if a second round ever happens, it gets its own dates rather than reusing these.

## 4. Inbound — answers

This is where the design effort belongs.

### The dossier arrives

**In whatever form the client chose** — Excel, PDF, email, something else. There is no format to standardise on, and no importer can assume one.

So the import step must be tolerant: accept a file or pasted content, and **extract question/answer pairs from an arbitrary layout** rather than expecting fixed columns. This is genuine work for a language model, and it's the same brick that does the matching.

The dossier contains **every bidder's questions and answers**, not only ours.

### Matching

The system attaches each answer to the requirement it clarifies:

- **Our own questions** — matched back to the question object, unblocking the branch that was waiting.
- **Competitor answers** — matched to whichever requirement they clarify. They still refine the client's need, so nothing in the dossier is discarded.

### Arbitration, by the project manager

**Where matching fails or hesitates, the PM decides.** With hundreds of answers, even a modest failure rate produces dozens of arbitrations — so this is the interaction that determines whether the screen works.

Design accordingly:

- **A queue, not a list.** One item at a time, showing the answer, the system's best guesses, and enough requirement context to judge. Deciding then advancing automatically, with no navigation between items.
- **Keyboard-driven.** Someone working through forty arbitrations should not need the mouse.
- **Skip is a valid action** — "come back to this" without forcing a decision.
- **"No matching requirement" is a valid answer**, not a failure to resolve. Some answers genuinely relate to nothing in our scope.

*(This is where the one-at-a-time, auto-advance pattern shelved during the expert space discussion actually earns its place — high volume, one repeated judgement, no research needed. Worth building here rather than there.)*

### What resolution does

- An answer to **our** question moves its branch out of `Awaiting Q&A`, back to actionable, and notifies the contributor waiting on it.
- A **competitor** answer attaches to its requirement as context, changing no status.

## 5. Who sees what

- **The project manager** owns the screen: reviews, exports, arbitrates.
- **Contributors have access** to consult questions and answers.

**Open:** whether a contributor sees the whole tender's Q&A or only their own activity. The general rule is activity scoping — but competitor answers are useful precisely *outside* one's own perimeter, and restricting them would discard the value the matching brick just created. Recommend full read access for contributors here, as an exception to the scoping rule, but this needs confirming.

## 6. Volume

Hundreds of questions and answers per tender. Everything on this screen must hold at that scale:

- The question list needs filtering and grouping — by activity, by status, by requirement.
- The arbitration queue must stay responsive throughout, and show how much is left.
- **Progress must be visible**: how many answers matched automatically, how many await arbitration, how many branches are still blocked.

## 7. Open questions

1. **Whether deadlines actually apply** on these tenders, and where the dates come from — set by hand at project creation, or read from the tender documents. The capability is specified in §3bis either way and works without them.
2. **Contributor read scope** — full tender or own activity (§5).
3. **Notifying a contributor whose question was dropped** from the export (§3).
4. **What the client's dossier typically looks like** — worth obtaining a real one before building the import. Designing tolerant extraction against an imagined format is guesswork; one real example would settle most of it.
