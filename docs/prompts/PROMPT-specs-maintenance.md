# Prompt — Keep the specs and user stories current

> Recurring routine. Assumes the one-off cleanup (`PROMPT-specs-cleanup.md`) has already run and `docs/` follows the agreed structure.
>
> Runs unattended: nobody is there to clarify. Follow this literally, and prefer doing nothing over guessing.

## What this routine is for

Decisions get made in tickets and conversations. Specs quietly fall behind. This routine closes that gap: it finds where the documentation no longer matches the decisions taken, and updates it — or flags what it can't safely update alone.

**It maintains documentation. It does not touch the prototype code.**

## Step 0 — Is there anything to do?

Check what changed since the last run (git log, or the routine's own log at the bottom of `docs/DOC-HEALTH.md`).

**If nothing relevant changed — no new or edited tickets, specs, or stories — stop and do nothing.** Write no report, open no PR, invent no work. An empty run is a correct outcome, and a routine that always finds something to change is a routine nobody will trust.

## Step 1 — Propagate decisions from tickets into specs

For each ticket added or modified since the last run:

1. Identify what it **decides** (a rule, a status, a role capability), as opposed to what it merely asks to be built.
2. Find the spec that owns that fact.
3. Update the spec to state the current rule, removing what is no longer true.
4. Add an entry to `docs/decisions/DECISIONS.md`: what, when, what it replaced.

**A ticket is a record of a change; the spec is where the truth lives.** If a rule only exists in a ticket, the spec is out of date by definition.

## Step 2 — Check the specs against each other

Look for the failure modes that reappear as a corpus grows:

- **The same fact stated in two places** — status lists, role permissions, category names. Pick the owning document; make the other reference it instead of restating it.
- **A term meaning two different things**, or one thing carrying two names across documents.
- **A rule contradicted elsewhere** without an explicit supersession.
- **References to files, screens or components that no longer exist.**

## Step 3 — Keep the user stories aligned

For each story affected by a spec change since the last run:

- Update acceptance criteria that a decision has made wrong.
- Where a spec change makes a **new** story necessary, draft it in the same format as the existing ones — Description ("As a… I want… so that…"), design link when one genuinely exists, 4–6 acceptance criteria.
- **Never invent a design link.** If no screen exists, say so.
- **Never resolve an open product question to make a story look finished.** Scope it out explicitly, as the existing stories do.

## Step 4 — Report and, if needed, open a PR

Write `docs/DOC-HEALTH.md`, replacing the previous contents:

- **Updated** — which documents, driven by which decision
- **Needs a human** — contradictions that are genuine product choices, listed with the options and what each implies. Do not pick one.
- **Still open** — decisions the corpus already marks as unresolved, restated so they stay visible rather than forgotten
- **Verified consistent** — what was checked and found sound. Without this there is no sense of proportion.

Append a one-line run log entry at the bottom: date, what was examined, what changed, or "no changes needed".

If anything was modified, commit to a `claude/docs-*` branch and open a PR. **Never push to `main`. Never merge.**

## Hard boundaries

- **Documentation only.** Never edit prototype source, `build_merge.py`, or generated files.
- **Never resolve a product question.** Surfacing a decision with its options is the job; making the decision is not.
- **Never delete a document.** Archive with a supersession header, as the cleanup prompt established.
- **An explicit override is not a contradiction.** A document saying "this supersedes X" is working correctly — leave it be.
- **A marked open question is not an error.** Only flag it if something is being built on top of it.
- **Confidentiality**: the client's real company name never appears in any file, commit, or comment.
- **English throughout.**
- If a change would rewrite more than a few paragraphs of a spec, **stop and describe the change in the report instead of making it**. Large rewrites need a human eye.
