# Prompt — One-off cleanup & reorganisation of the SRM functional docs

> Run this **once**, in Claude Code, on the repo holding the SRM documentation. It reorganises the corpus and resolves accumulated contradictions. The recurring maintenance routine (`PROMPT-specs-maintenance.md`) assumes this has already been done.
>
> Work on a branch. Do not merge automatically — this moves and rewrites files, and a human should review it.

## Why this exists

The corpus grew organically across many sessions. Three problems accumulated:

1. **Superseded documents still read as current.** Nothing marks them dead, so a reader can act on an abandoned model.
2. **The same fact lives in several files**, so the copies drift apart.
3. **Decisions live in tickets rather than specs**, so the specs describe a state the project has moved past.

The goal is not to rewrite the content. It is to make it possible to find the current truth without reading everything.

## Target structure

```
docs/
  specs/        current state only — no history, no "we first decided X"
  decisions/    append-only log of decisions, with dates and what each supersedes
  tickets/      work to do; archived once done
  stories/      user stories, derived from specs
  research/     AS-IS, personas, journeys — evidence, rarely changes
  prompts/      build prompts for Claude Code
  archive/      superseded documents, kept readable but clearly dead
```

**The organising rule: one fact, one place.** If a status list, a role definition, or a business rule appears in more than one file, exactly one of them is the source of truth and the others must reference it rather than restate it.

## Step 1 — Inventory before moving anything

List every `.md` in the repo. For each: its subject, its apparent age, and whether anything else covers the same subject. Produce this inventory as a file (`docs/INVENTORY.md`) **before** making changes — it's the map for everything that follows, and the record of what was where.

## Step 2 — Find contradictions and supersessions

For every pair of documents covering the same subject, determine which is current. Signals, in order of reliability:

- An explicit statement ("this supersedes X", "overrides the earlier decision") — trust these.
- A later file contradicting an earlier one on the same point.
- Near-duplicate filenames (e.g. one differing by a single character) — a strong sign one is an accidental copy.

**Known cases to resolve** (verify each rather than assuming):
- The image container model was replaced by a simpler one: an image produces one requirement row, duplicable when the image is a table. Any spec or prompt still describing an image as a *container* holding typed-in requirements is dead.
- One user-stories file supersedes an earlier sample of the same stories.
- The review table's status model is now four values (Incomplete / Doubt / To validate / Valid). Any document describing three is stale.
- "R&D needed" is no longer a compliance value — compliance has exactly two: Compliant / Not compliant.

Report every contradiction found. **Do not resolve a genuine product question by picking a side** — if two documents disagree and neither is clearly later, flag it for a human.

## Step 3 — Extract decisions into a log

Create `docs/decisions/DECISIONS.md`. For each significant decision found across the tickets and specs, record: **what was decided**, **when** (as precisely as the documents allow), **what it replaced**, and **why**, when the reason is stated.

This is what lets the specs drop their history. Do not invent rationale that isn't written down — "reason not recorded" is an acceptable and honest entry.

## Step 4 — Move files into the structure

Move each file to its folder. When moving:

- **Superseded documents go to `archive/`**, and get a one-line header at the top: `> SUPERSEDED by <file> on <date>. Kept for reference. Do not build from this.`
- **Never silently delete anything.** Archiving is reversible; deletion isn't.
- Normalise filenames: one language (English), one convention (`SPEC-`, `TICKETS-`, `STORY-`). Note every rename in the inventory so links can be fixed.

## Step 5 — Reconcile specs against the tickets that overrode them

This is the most valuable step. Where a ticket changed a rule, **the spec must be updated to state the new rule** — the ticket is a record of a change, not the permanent home of the truth.

For each spec: read the tickets that touch its subject, apply the current decisions, and remove statements that are no longer true. The spec should read as if it had always said this — the history belongs in the decisions log, not in the spec.

**Do not resolve open questions while doing this.** Corpora legitimately contain unresolved decisions; keep them marked as open. Only close what the documents themselves have already settled.

## Step 6 — Fix cross-references

After the moves and renames, every link between documents will be broken. Fix them all. Any reference to a file that no longer exists under any name is itself a finding — report it.

## Step 7 — Report

Produce `docs/CLEANUP-REPORT.md`:

- What moved where
- What was archived, and what superseded it
- Contradictions resolved, and on what evidence
- **Contradictions NOT resolved**, needing a human decision
- Specs updated, and which ticket drove each change
- Broken references found

## Rules

- **Never delete.** Archive with a header.
- **Never resolve a product question.** Surface it.
- **Preserve the confidentiality rule**: the client's real company name appears nowhere, in any file, including in moved or rewritten content.
- **English throughout** — content, filenames, commit messages.
- Commit in logical steps (inventory, then moves, then spec reconciliation) so the diff is reviewable rather than one giant rewrite.
