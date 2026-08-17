# Documentation cleanup report

Produced 2026-08-16 on the local-only branch `docs-cleanup` (not pushed; see the branch note at the end). Summarizes the one-off reorganization of the SRM functional-docs corpus, run per `docs/prompts/PROMPT-specs-cleanup.md`. Full detail behind every claim below lives in `docs/INVENTORY.md` and `docs/decisions/DECISIONS.md` — this report indexes those, it doesn't duplicate them.

## Scope

The corpus turned out to be materially larger than `SRM-PROTO/SPECS/`: **28 `.md` files** across the repo (6), the author's Desktop (3), and Downloads (19) — nothing outside the repo had ever been backed up or tracked anywhere. Per the user's explicit instruction, the full scattered corpus was included, and the real client company name (found in two byte-identical copies of one file) was scrubbed to "the client" wherever it appeared.

## What moved where

| From | To | Why |
|---|---|---|
| `SPECS/SPEC-domain-model.md` | `docs/specs/SPEC-domain-model.md` | Living spec, current. |
| `SPECS/SPEC-review-table.md` | `docs/specs/SPEC-review-table.md` | Living spec, current. |
| `~/Desktop/SPECS.md` (also `~/Downloads/SPECS.md`, identical) | `docs/specs/SPEC-backend-requirements.md` | Recovered — see "Recovered files" below. Renamed and scrubbed of the client name. |
| `~/Downloads/SPEC-expert-space.md` | `docs/specs/SPEC-expert-space.md` | Living spec, reconciled in place — see below. |
| `SPECS/TICKETS-continuity-fixes.md` | `docs/archive/TICKETS-continuity-fixes.md` | Fully completed (all TA–TG tickets checked). |
| `SPECS/TICKETS-followup-workflow.md` | `docs/archive/TICKETS-followup-workflow.md` | Fully completed (all T1–T12 built). |
| `~/Downloads/TICKETS-manager-features-batch2.md` | `docs/archive/TICKETS-manager-features-batch2.md` | Fully completed (S1, S2, B1–B5 built). |
| `~/Downloads/TICKET-wire-capture-data.md` | `docs/archive/TICKET-wire-capture-data.md` | Fully completed. |
| `~/Downloads/TICKETS-review-expert-batch4.md` | `docs/tickets/TICKETS-review-expert-batch4.md` | **Kept in `tickets/`, not archived** — B11 is still open work. |
| `~/Downloads/PROMPT-multi-allocation-rows_1.md` | `docs/prompts/PROMPT-multi-allocation-rows.md` | Promoted to canonical name — this is the version actually built (UI-only, no derivation engine). |
| `~/Downloads/PROMPT-multi-allocation-rows.md` (original) | `docs/archive/PROMPT-multi-allocation-rows-v1.md` | Superseded by the above — see decision D1. |
| `~/Downloads/PROMPT-nightly-ticket-routine_1.md` | `docs/prompts/PROMPT-nightly-ticket-routine.md` | Promoted to canonical name — locates its queue by heading, not a hardcoded filename. |
| `~/Downloads/PROMPT-nightly-ticket-routine.md` (original) | `docs/archive/PROMPT-nightly-ticket-routine-v1.md` | Superseded by the above. |
| `~/Downloads/SPEC-Design tokens.md` | `docs/prompts/PROMPT-design-tokens.md` | Renamed — it's a build prompt, not a living spec, despite the `SPEC-` prefix; also dropped the space in the filename. |
| `~/Downloads/SPEC-brand-colors.md` | `docs/archive/PROMPT-brand-colors.md` | Renamed + archived as superseded by `PROMPT-design-tokens.md` (colour-only subset of a later, broader prompt). |
| `~/Downloads/PROMPT-filter-selection-keyboard-nav.md` | `docs/prompts/` | Unchanged, moved as-is. |
| `~/Downloads/PROMPT-roadmap-slide-claude-design.md` | `docs/prompts/` | Unchanged, moved as-is. |
| `~/Desktop/PROMPT-specs-cleanup.md`, `PROMPT-specs-maintenance.md` | `docs/prompts/` | Unchanged, moved as-is — this cleanup's own tooling. |
| `~/Downloads/AS-IS-workflow-map.md`, `DEBRIEF-user-interview.md`, `PERSONAS-srm-roles.md` | `docs/research/` | Unchanged, moved as-is — evidence documents. |

`HANDOVER.md` and `README.md` **stayed at the repo root**, deliberately — they're read by name from the root by the nightly-ticket-routine prompts and serve as the onboarding entry point for a new agent picking up the repo cold. Moving them would have broken that convention for no benefit.

**Nothing was deleted.** Every superseded or completed file was archived with a header explaining what superseded it (or that it's simply done), per the source instructions' hard rule.

## Files intentionally left out of `docs/`

- **`~/Downloads/PITCH-SRM.md`** and **`PITCH-SRM-slides.md`** — sales/pitch-deck content, not functional documentation. They don't map to any of the seven target categories (`specs/decisions/tickets/stories/research/prompts/archive`), and forcing them into one would misrepresent what they are. Left at their original location, untouched. **Flag for a human:** decide whether `docs/` needs an eighth category (e.g. `business/`) or whether this content belongs in a different repo entirely.
- **`docs/stories/`** — created but left empty. The only "user stories" content found in the whole corpus is a single, non-duplicated section inside `SPEC-backend-requirements.md` ("## User Stories," 9 stories across 5 roles). Extracting it into a separate file would mean inventing a new document that didn't exist before, which is beyond this cleanup's mandate ("do not resolve a genuine product question," extended here to "do not invent document structure"). **Flag for a human:** decide if that section should be split out.

## Contradictions found

### Resolved (one side was clearly later, with explicit reasoning)

1. **Compliance scale: two values vs. three (R&D Needed).** `SPEC-expert-space.md` originally described a two-value model (Compliant/Not compliant) as "already final," explicitly by choice. `SPEC-domain-model.md` §9.2 (decision **D8**, ticket TF3) later — and explicitly — reversed this, narrating its own prior self-contradiction and resolving it in favor of a three-value, countable scale, matching the code that had already shipped. `SPEC-expert-space.md` was updated in place to reflect this; original wording preserved in `docs/decisions/DECISIONS.md`.

   **⚠ This directly contradicts a "known case" named in the cleanup prompt itself** (`docs/prompts/PROMPT-specs-cleanup.md`), which asserted the two-value model was current. It was current at some earlier point, then reversed — the prompt's brief was stale on this specific point. See D8's flag note in the decisions log for the full reasoning on why the later, code-matching side was treated as current truth rather than left as an unresolved 50/50 dispute.

2. **Image model: container/folder vs. auto-created requirement row.** `TICKETS-review-expert-batch4.md` (B9) explicitly states it supersedes a container/folder model. `SPEC-domain-model.md` and `SPEC-review-table.md` currently contain zero trace of the container model — confirming the newer model is what's actually live. No live document needed editing; recorded as decision **D4**.

### Not resolved — flagged for a human

3. **"One user-stories file supersedes an earlier sample."** Named as a known case in the cleanup prompt, but no matching pair of files (or any duplicate/sample user-stories document) was found anywhere in the 28-file corpus. Could not be verified against anything real — not acted on.
4. **Status-vocabulary label mismatch.** The cleanup prompt describes the four-value status model as "Incomplete/Doubt/To validate/Valid." The actual, current labels (confirmed by reading `SPEC-domain-model.md` §8.2 directly) are **Incomplete / To review / To validate / Allocated** — two of the four names differ. Treated the spec as authoritative (it matches the shipped code) and noted the discrepancy rather than silently using either label set elsewhere.
5. **Two structurally near-identical "nightly ticket runner" prompts**, one hardcoding a queue filename (`NIGHTLY-TICKETS.md`) that doesn't exist anywhere in the corpus, the other locating its queue by heading text instead. The `_1` (heading-based) version was treated as canonical since it matches how the routine actually found its queue this session — but *why* the filename convention was abandoned was never written down anywhere found. Not invented here.
6. **Three files referenced by name elsewhere in the corpus but not found anywhere:** `SPEC-review-table-batch3.md` (ticket B1–B7 predecessor), `NIGHTLY-TICKETS.md` (see #5), `SPEC-image-container-requirements.md` (the file B9 says it supersedes). None of these are cross-reference breaks caused by this cleanup — they were already-dangling references before this cleanup started (confirmed: none of the corpus's other files were renamed *from* these names). Left as open gaps.

## Recovered files

Two files cited by name throughout `SPEC-domain-model.md` and other tickets (`SPEC-expert-space.md`, `SPEC-backend-requirements.md`) as missing — `SPEC-domain-model.md` §9.1's own TG2 note states plainly "neither file exists in this repo, and no record of their content survived." That statement is accurate as written: TG2's search was scoped to this repo's git history, and neither file was ever committed here. This cleanup's search was scoped wider, per the user's explicit "include everything" instruction, and found strong content candidates for both outside the repo (Desktop/Downloads). They are now at `docs/specs/SPEC-expert-space.md` and `docs/specs/SPEC-backend-requirements.md`, each carrying a provenance note stating plainly that the match is very likely, not confirmed byte-identical to whatever the original citations pointed to. TG2's own careful writeup in `SPEC-domain-model.md` was left intact rather than rewritten, with a short pointer note appended directing readers to the recovered copies.

## Specs updated (with driving ticket/decision)

- **`SPEC-expert-space.md`** — compliance section rewritten from two-value to three-value (driven by **D8**/TF3); two-surface table/document access model added (driven by **D11**/B11, explicitly flagged as not-yet-built); both originally-open questions marked resolved; historical Figma-variant-count note kept but annotated as itself since reversed.
- **`SPEC-domain-model.md`** — two short pointer notes appended near §9.1/§9.2 (not rewrites) noting that candidate recovered copies of the previously-missing cited files now exist in `docs/specs/`.
- **`SPEC-backend-requirements.md`** — newly introduced to the repo (previously untracked anywhere); client name scrubbed; provenance note added.

## Cross-references (Step 6)

Checked every `.md`-to-`.md` reference across the corpus, plus every `SPEC-*`/`HANDOVER.md` mention inside the six prototype HTML files' code comments. **Result: nothing broken by this cleanup's moves.** The entire corpus — including every file moved in this cleanup — already referenced other documents by bare filename only, never by directory path, so relocating files into `docs/{specs,archive,prompts,research,tickets}/` didn't invalidate any existing citation. The prototype's own dead-link checker (which validates `href="*.html"` navigation, unrelated to markdown docs) wasn't affected since no HTML file was touched. The three dangling references noted above (item 6) predate this cleanup and are not link breaks it caused.

## Branch note

All of this was committed to a **local-only branch**, `docs-cleanup`, created from `origin/main` with its upstream explicitly unset. Per instruction, it has not been pushed and will not be merged automatically — it needs human review first, given the scale of the reorganization and the confidentiality-sensitive content it touches.
