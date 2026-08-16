# Nightly Ticket Runner — SRM prototype

> Paste this as the routine's prompt at claude.ai/code/routines (or via `/schedule` in the CLI). Attach a **Scheduled** trigger for overnight hours. Select the SRM-PROTO repository. This prompt is meant to run fully unattended — no one will be there to clarify or course-correct, so follow it literally.

## Context

This repository is the SRM (Smart Requirement Management) prototype. Before doing anything, read:
- `HANDOVER.md` — project context, architecture, conventions
- Any `SPEC-*.md` files relevant to the ticket you pick up
- **The ticket queue file** — the Markdown file whose top-level heading is `# Tickets — Continuity & consistency fixes`. Locate it by that heading rather than by filename, so a rename doesn't break this routine.

## What to do, in order

1. **Read the ticket queue file** (heading: `# Tickets — Continuity & consistency fixes`). Find the first ticket still marked `- [ ]` (unchecked), reading top to bottom.
   - **If the file contains no `- [ ]` checkboxes at all**, do not guess which items are tickets and do not start work. Stop, and leave a single note at the top of the file saying the queue needs checkbox formatting (`- [ ] ticket text`) before this routine can run.
2. **If there are no unchecked tickets**, stop here. Do not invent work. Do not touch any other file. End the run.
3. **Implement the ticket** by editing the relevant **source** HTML file(s) — `accueil.html`, `dashboard-et-config.html`, `revue-documentaire.html`, `suivi-experts-et-versions.html`, or `creation-projet.html`. Never hand-edit the merged `docreview-app.html` directly; it is generated.
4. **Rebuild**: run `build_merge.py` to regenerate the merged file.
5. **Verify**, in this order:
   - `node --check` on any script block you touched.
   - The existing jsdom-based link-check script (not Puppeteer) to confirm **zero dead hrefs**.
6. **If verification fails**: try to fix it. If it still fails after a reasonable attempt, **revert your changes for this ticket**, leave it unchecked, and add a one-line note directly under the ticket explaining what blocked you (e.g. `> blocked: build_merge.py fails on X`). Then move to the next ticket — do not get stuck retrying indefinitely.
7. **If verification passes**: mark the ticket `- [x]`, add a short one-line summary of what changed directly after it, and commit with a clear message referencing the ticket text.
8. **Repeat** for the next unchecked ticket. Keep going until either the queue is empty, or you judge you are running low on context/budget for the session — in that case, finish the ticket you are currently on cleanly, commit, and stop. Do not start a new ticket you won't be able to finish.

## Hard boundaries — do not deviate

- **Never push to `main`** and never push to any branch other than a `claude/`-prefixed one. Never merge anything.
- **Never invent scope.** If a ticket is ambiguous, do the most conservative reasonable reading, note your interpretation in the commit message, and flag it. Do not expand a ticket into a redesign.
- **Confidentiality**: never write the real client company name anywhere — files, commits, comments. Use "the client" or "the company" only.
- **All produced content is in English** — code, comments, UI copy, commit messages — even though this repo belongs to a French-speaking team.
- Do not touch files outside what a ticket requires. Do not "clean up" unrelated code.
- Do not delete or rewrite the ticket queue file's structure — only tick boxes, add summaries, and append blocker notes. Leave headings, groupings and any severity ordering exactly as they are.

## At the end of the run

Update the **Run log** section at the top of the ticket queue file (create the section if it doesn't exist yet):
- Date/time of the run
- Tickets completed (list)
- Tickets blocked, with the reason (list)
- Tickets remaining untouched

Commit this update along with your last ticket's changes (or as its own commit if the queue was already empty).
