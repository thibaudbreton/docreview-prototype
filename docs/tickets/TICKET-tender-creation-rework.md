# Ticket — Rework the tender creation flow

> The early steps are sound; the casting step is not. But the real fix isn't rearranging that step — it's removing it, because casting stopped being a creation-time activity.

## The principle

**Creation should produce the minimum needed to start working, and nothing more.**

Everything the flow currently tries to settle up front — who works on what, in particular — is now ongoing work with its own screen. A creation flow that asks for things nobody can answer yet is what makes it feel unclear: users can't complete it, so they either guess or stall.

The same logic already applies elsewhere: an incomplete casting slows work down, it never blocks it. Creation should follow suit — get to capture fast, refine afterwards.

## What leaves the flow

**Casting.** It is now project user management, on its own permanent screen — people are added throughout the project's life, by several managers, at their own pace. It cannot be a step in a sequential form, and pretending otherwise is the source of the current confusion.

Capture and characterisation don't need it at all. Allocation needs it only for the activities actually present in the document — which characterisation reveals. So there is nothing to fill in at creation time that couldn't be filled in better later.

## What creation must collect

### 1. Project identity

- **BO-ID** — the real name of what the form currently calls "tender reference".
- **Project name**
- **Product line / system** — a real list, currently missing entirely: Turnkey, RCS, SIG, INFRA and the others.
- **Region** — using the real acronyms. They aren't collected yet; use clearly-marked placeholders.
- **Deadline**

**The system choice is more consequential than it looks.** Allocation rules vary by system — Turnkey resolves to an activity, the others resolve to a person, and Turnkey selects a single dimension based on technical/non-technical classification. This is not a label, it's a setting that changes downstream behaviour. Worth treating as a deliberate choice in the interface rather than one field among five.

### 2. Documents

- Upload one or several. A large tender can hold around thirty.
- **Set their order** — it determines how requirements read as one continuous tender.
- Adding more later is expected, not exceptional, and happens on the Documents screen.

### 3. Processing mode

- **Manual or AI-assisted.** In manual mode the AI pipeline doesn't run and a human does every step. In AI-assisted mode it proposes, and humans validate.
- **Remove the compliance-matrix option** from the AI-assisted model choices. The matrix is built continuously from the verdicts as contributors answer — it isn't something an AI produces as a pipeline step, so offering it as one is misleading.
- Where the remaining per-step AI toggles fit into this needs deciding — see open questions.

### 4. Project management team

The creator is automatically the first member. Adding others is possible here but not required — it belongs to the casting screen, and forcing it at creation reintroduces the problem this rework is removing.

## What happens on submit

Creation ends and **capture starts**. The user lands on the project with processing under way, rather than on another form.

This is the point of the whole rework: the gap between "I have the documents" and "the tool is working on them" should be as short as possible.

## What stays editable afterwards

Everything. Metadata, documents and their order, the management team, the casting. Nothing about creation should feel final — it's a starting point, not a commitment.

## Definition of done

1. No casting step in the creation flow.
2. BO-ID, a populated system list, and region acronyms are in place.
3. Several documents can be uploaded and ordered.
4. Manual and AI-assisted modes are selectable.
5. Submitting starts capture and lands the user on the project.
6. Everything collected at creation is editable later.
7. `build_merge.py` runs clean, `node --check` passes, zero dead hrefs.

## Open questions

1. **The per-step AI toggles** (capture, characterisation, allocation) — do they survive alongside the manual/AI-assisted mode, or does the mode replace them? Two overlapping controls for the same thing would be confusing; one of them should go.
2. **Region acronyms** — the real list is still to collect.
3. **Whether the system choice can change later.** It drives allocation rules, so changing it mid-project would affect work already done. Probably worth locking after allocation has run, but not decided.
