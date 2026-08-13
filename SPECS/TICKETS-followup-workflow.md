# Tickets — Expert follow-up workflow (manager side)

> Sequenced tickets for Claude Code to fit the agreed expert workflow into the existing follow-up screen (`suivi-experts-et-versions.html`), which has not changed since we moved to Claude Code. This is the MANAGER's view — receiving and tracking expert responses. The expert's own answering space is a separate, later build. Prototype / UI-only: statuses and data are hand-authored, the Q&A matching is simulated, no backend. Aligns with `SPEC-domain-model.md` (branches, statuses, compliance). Build in order — later tickets depend on earlier ones.

---

## Group A — Data model alignment (do first)

**T1 — Assignments are branches, not requirements**
Seed the follow-up data at the **branch** level: one assignment per typology per requirement. A single-typology requirement = 1 branch; a multi-typology requirement = N branches (one expert each). Each branch carries: requirement ref, typology, manager, expert, branch status, compliance verdict (or null). Reuse the branches seeded for the table multi-allocation work if present.

**T2 — Status set and compliance scale**
- Branch status: `proposed` / `assigned` / `awaiting_answer` / `awaiting_qa` / `reassignment_needed` / `answered`.
- Compliance verdict (only meaningful once `answered`): **Compliant** / **Compliant with R&D** / **Non compliant**. Null = pending.
- Keep status and compliance as **two separate axes** (status = progress, compliance = result). `awaiting_qa` is a progress status, never a verdict.

---

## Group B — Core follow-up view

**T3 — Branch-level tracking list**
The follow-up screen lists all branches with their status + verdict. For each requirement, show the **consolidated** view: overall compliance = most restrictive across its branches, and **pending until every branch is `answered`**. Surface the **blocking branch** (the one holding consolidation up). Group by requirement, with branches beneath.

**T4 — Progress overview**
A header/summary with counts by status (answered / awaiting answer / awaiting Q&A / reassignment needed) and a % complete toward full consolidation. This is the manager's "where does the tender stand" glance.

---

## Group C — The two loops (distinct, different destinations)

**T5 — Reassignment loop (internal → back to manager)**
A branch in `reassignment_needed` (the expert judged the allocation wrong) shows the **expert's comment**. The manager can **reassign** (change expert / OBS); the branch returns to `assigned` → `awaiting_answer`. This stays inside the company. Make it clearly an action item for the manager.

**T6 — Q&A loop (external → to the client)**
A branch in `awaiting_qa` means the expert needs a precision from the tender issuer and **cannot answer yet**. The assignment does **not** change. `awaiting_qa` **blocks consolidation** (counts as "not yet answered"). Surface these distinctly from reassignment — different meaning, different destination.

---

## Group D — Q&A cycle management

**T7 — Questions as identified objects**
Each question raised by an expert is a **first-class object**, linked to that expert and their branch. The manager sees all raised questions in a **"questions to send"** batch view (collect them, ready to go to the client). One question ↔ one branch in `awaiting_qa`.

**T8 — Answer dossier upload + targeted unblock**
The manager uploads **one file** containing the answers to all questions (all companies' questions, in reality — a single upload). Simulate the **matching** (question → answer → branch); matched branches move from `awaiting_qa` back to `awaiting_answer` (the expert can now respond). Assume **one round** of Q&A; keep the model open to a second. (The matching brick — simple algo vs LLM — is a later technical decision; here just simulate it.)

---

## Group E — Manager quality-of-life (filters, sort, tracking)

**T9 — Filters**
Filter the follow-up list by: status, expert, typology, and a **"needs my action"** filter that surfaces the three manager to-dos at once (reassignment requests + questions to send + branches unblocked-but-not-yet-answered).

**T10 — Sort, search, and "what needs you now"**
Sort by status / expert / requirement; search by requirement ref or text. A prominent **"what needs you now"** area collecting: reassignment requests, questions ready to send, and answers just uploaded that unblocked branches.

**T11 — Per-expert tracking**
A per-expert view: each expert's progress (answered / pending / blocked counts), so the manager can see who is holding things up and (mocked) send a reminder.

**T12 — Consolidation & export readiness**
When all branches of the tender are `answered`, indicate the **compliance matrix is complete** and ready for the client export (link to the existing modular export). Until then, show what remains. This closes the loop: the follow-up screen's end state is a client-ready matrix.

---

## Notes
- **Two loops must never be confused** (reassignment = internal; Q&A = external). Different visuals, different actions.
- **`awaiting_qa` is a status, not a verdict**, and blocks consolidation.
- **Compliance is per branch**; the requirement-level verdict is derived (most restrictive, pending until all answered). For a single-branch requirement, the sole expert's verdict is the requirement's verdict.
- Prototype: all data hand-authored, Q&A matching simulated, no backend.
- Dependency: the expert's own answering space is separate — on this screen, expert actions (raising a question, returning an assignment, answering) can be represented as already-arrived states in the seed data, plus the manager-side handling of them.
