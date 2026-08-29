# Ticket — Three support screens: Casting, Documents & versions, Q&A

> Supersedes T6 in `TICKETS-prototype-ux-batch5.md`, which moved "Versions & Q&A" out of the follow-up screen as a single space. It becomes **two** separate screens instead, alongside Casting.

## The structure

Alongside the main workflow steps (review, compliance), there are **three support screens**:

1. **Casting** — who works on what. Already specified in `TICKET-casting-screen-redesign.md`.
2. **Documents & versions** — the tender's source material. Specified below.
3. **Q&A** — questions to the client and the answers coming back.

Each is its own screen, reached by a button. None of them is a panel or tab inside a workflow step.

**Why separate rather than one "support" space:** they serve different moments and different people. Casting happens at the start and involves many contributors. Documents get added and revised throughout. Q&A runs on the client's timeline, not the project's. Bundling them would mean one screen with three unrelated modes.

---

## Screen 2 — Documents & versions

### Purpose

A clear view of every document in the tender, and the two things people need to do with them: **add a new document**, and **upload a new version of an existing one**.

### What it shows

The tender is made of several documents treated as one continuous whole, in a chosen order, with each requirement remembering where it came from. This screen is where that structure is visible and editable.

For each document:

- **Its name and position** in the tender order.
- **Its current version**, and when it arrived.
- **How much of the tender it represents** — a row count, so the weight of each document is obvious at a glance.
- **Its processing state** — captured and characterised, or still running, or not yet processed. A document added mid-project won't be at the same stage as the others, and that has to be visible rather than assumed.

### Adding a new document

Available at any time, not only at project creation. A tender can hold up to around thirty documents on the largest projects.

- Upload, then place it in the tender order.
- **The AI pipeline runs on it after the fact** — capture, then characterisation. It joins the existing material rather than starting a separate project.
- Progress must be visible while it processes; the user can leave and come back.

### Uploading a new version

A new version replaces a document in place — it does not create a second document.

- **Gap analysis runs automatically**: added, modified, removed. Surfaced with the existing Gap Chip / Version Item components.
- **Work made stale is flagged** — a verdict given before the change on a requirement the change affected. This is the consequence that matters most, and it should be stated plainly on this screen, not left to be discovered later in the compliance step.
- **Version history is kept** and readable per document.

### Reordering and removing

- **The order is editable.** It determines how requirements read as one continuous tender.
- **Removing a document** is a heavy action — it takes its requirements with it, including any work already done on them. Say what will be lost before it happens, not after.

### Also here

**Per-document export** — from session 3. This screen is the natural home for it, since it's where the documents are listed and where someone thinks in terms of one document rather than the whole tender.

---

## Screen 3 — Q&A

Not detailed in this session. What is already decided and should carry over:

- Questions are **identified objects**, each linked to the contributor who raised it and to their activity.
- An **internal review step** happens before anything leaves, and **duplicate questions are detected** so they can be merged.
- **Questions are exported, not sent** — structured text or a table (CSV / Excel) — per T5 in batch 5. Nothing goes out of the tool directly.
- Answers return as **one dossier mixed with every competitor's questions**; the matching brick attaches each answer to the requirement it clarifies.
- A branch awaiting an answer is in **Awaiting Q&A** and **blocks consolidation**.

**Open:** the screen's own layout and priorities haven't been worked through. Worth its own pass rather than being derived from the list above.

---

## Definition of done

1. Three separate support screens exist, each reachable by a button, none as a panel inside a workflow step.
2. The Documents screen lists every document with its version, position, weight and processing state.
3. A new document can be uploaded mid-project and processed by the AI afterwards.
4. A new version can be uploaded, triggering gap analysis and flagging stale work.
5. Document order is editable; removal states its consequences before acting.
6. Per-document export is available from this screen.
7. `build_merge.py` runs clean, `node --check` passes, zero dead hrefs.
