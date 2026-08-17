# SPEC — Project creation (New tender wizard)

> Derived from the prototype's actual behaviour, per `docs/prompts/PROMPT-derive-specs-from-prototype.md`. Describes `creation-projet.html` as built. Cross-references `docs/specs/SPEC-domain-model.md` §6 (casting) for the shared casting model; does not restate it.

## 1. Purpose

A four-step wizard that creates a new tender project: identity, source documents, AI-processing mode, and initial team casting. Ends by registering the project so it appears on Home and opens on its Dashboard (or, in manual mode, straight on the review table).

## 2. Actors

The person running the wizard is the project's **project manager** — referred to in the code as `"admin"` with the label "Project lead (admin) — you." They are also one of the four seeded activity managers and can cast themselves on an activity like any other manager. No other role interacts with this screen; activity managers who are cast but not the creator only appear as options in the casting selects, they don't use this wizard themselves.

## 3. Entry points

- "＋ New tender" on Home (`accueil.html`, both instances) and on the Dashboard header (`dashboard-et-config.html`, `#new-proj`).
- "Cancel" (header) routes back to Home without creating anything — no confirmation prompt, no draft is kept.

From step 4's completion, this screen routes either to the Dashboard (AI-assisted or segmentation-only modes, after a brief non-blocking overlay) or directly to the Allocation/Review screen (manual mode).

## 4. Layout

- **Header** — logo, "New project" breadcrumb, "Cancel."
- **Left stepper** (270px) — 4 numbered steps (Project details / Source document / Processing mode / Team & review) with a description line each; the current step is highlighted, completed steps are marked done and clickable to jump back.
- **Right content pane** — one form per step, scrollable, max-width constrained for readability.
- **Footer** — "Step N of 4" progress text, Back (hidden on step 1) and Continue/Create buttons.
- **Processing overlay** (modal, non-blocking mode only) — a brief confirmation box shown while control returns to Home.

## 5. Data displayed

**Step 1 — Project details.** Name*, tender reference*, product line (select, 4 options), system (select, 5 options), region (select, 5 options), tender issuer (free text), submission deadline (date input, defaults to a fixed `2026-08-12`). Fields marked `*` are required; all others are optional with a placeholder or default.

**Step 2 — Source documents.** A reorderable list of documents, each showing a synthetic filename (`{ref}_part{n}.pdf`), page count, size, and language — all generated from a fixed 5-entry sample table, cycled by index (see §6). An empty-state upload zone is shown when the list is empty; an "add another document" zone appears once at least one exists.

**Step 3 — Processing mode.** Two presets (AI-assisted / AI segmentation only) as radio-style cards, plus four individual step toggles — Capture, Characterizer, Compliance matrix (its label reads "Compliance matrix" but its live copy describes proposing an *expert*), Allocation (proposes a *manager*) — each with on/off descriptive copy. A computed estimate line (block count guess, steps-enabled count, rough processing time) and, when both Capture and Characterizer are off, a manual-mode warning box.

**Step 4 — Team & review.** A search-combo to add an activity (searches the full `TYPO` activity vocabulary, 13 entries — no predefined subset), one row per added activity showing its activity code, an activity-manager select, and either an expert select (only if the viewer manages that activity themselves), a "to be filled in later" note (if delegated), or a "assign a manager first" prompt. Below it, a flat list of known experts (name, team, remove) with an inline add row. A closing summary table echoes every field entered across all four steps, flagging anything still missing.

## 6. Interactions

- **Step navigation** — click a stepper item (only to a completed or the current step, or forward via Continue which re-validates first), or Back/Continue. *Implemented.*
- **Step 1 validation** — Continue is blocked with a toast ("Project name and tender reference are required") if either is empty; every other field is optional. *Implemented.*
- **Add / reorder / remove a document** — clicking the upload zone or "add another document" appends one synthetic document (cycling through 5 canned `{pages, size}` pairs); ▲/▼ swap it with its neighbour; ✕ removes it. *Implemented*, but see §10 — this is not a real file picker.
- **Processing-mode presets and toggles** — selecting a preset sets all four toggles at once and marks the card active; toggling an individual step switches to "Custom" and updates the estimate/manual-mode copy live. *Implemented*, all client-side state — no AI estimate is actually computed from the (fake) uploaded document; the numbers are a fixed illustrative string ("~2,400 blocks... estimated processing 2 min" style text), not derived from `P.docs`.
- **Add an activity to casting** — typing in the search combo filters the remaining (not-yet-added) activities live; clicking one adds it with no manager/expert yet. *Implemented.*
- **Assign an activity manager to an activity** — a per-row select; choosing `"admin"` (the viewer) automatically also assigns them as that activity's expert (their first expert-pool entry marked `isAdmin`), since they're both the manager and, until they delegate research, effectively the point of contact; choosing anyone else clears any expert selection for that row, since the PM cannot pick an expert on another manager's behalf. *Implemented*, matches `SPEC-domain-model.md` §6's casting model.
- **Assign an expert** (only when the viewer manages the activity themselves) — a per-row select against the flat "known experts" list. *Implemented.*
- **Remove an activity / expert** — ✕ on either row; removing an expert who's referenced by an existing casting row nulls that row's expert selection (index-based sync) rather than leaving a dangling reference. *Implemented.*
- **Add a known expert** (name + team/domain, free text) — appended to the flat expert pool, immediately selectable in any casting row the viewer manages. *Implemented.*
- **Create project** (step 4's Continue, relabelled "✓ Create project") —
  1. Re-validates step 1.
  2. Notifies every delegated activity manager (anyone cast on an activity who isn't the viewer) via a toast reading "{names} notified by email — asked to complete their team," after an 800ms delay. **Represented / backend-dependent** — no real email is sent; see `SPEC-backend-requirements.md` FR7 (notifications).
  3. Computes the processing mode (`ai` / `segmentation` / `manual`) from the toggle state and pushes it, plus the review-validated flag and a project-meta summary, into the shell's shared state.
  4. Registers the project via the shell's `addProject`, carrying the full casting roster through (only activities the viewer cast on themselves arrive with a real expert — delegated ones intentionally arrive empty, to be filled in later on the Team management screen; see `SPEC-domain-model.md` §6).
  5. **Manual mode** routes straight to the Allocation/Review screen with a toast, skipping the normal "click the card on Home" step. **AI-assisted / segmentation-only modes** show the brief non-blocking processing overlay, then route to Home, where the new project now appears with `status:"processing"` and animates via the same background loop described in `SPEC-home.md` §6.

## 7. States

- **Step validation error** — toast only (see §6); the offending field isn't visually marked invalid beyond that.
- **Empty documents** — upload zone shown in place of a list.
- **Empty casting** — "No activity added yet — search above to add the first one."
- **Empty known-experts list** — "No expert yet. You can add them now or later — requirements can be characterized before anyone is assigned."
- **No search match** (casting combo) — "No match," or "Every activity has been added" once the full 13-entry vocabulary is exhausted.
- **Loading** — the processing overlay is the only loading-style state, and it's fixed-duration (1.4s) rather than tied to any real completion signal.
- **Error** — not present; nothing in this wizard can fail beyond the one client-side required-field check.

## 8. Business rules

- **A project manager can only directly assign an expert to an activity they manage themselves.** Every other activity's expert is deliberately left unassigned at creation and filled in later by that activity's own activity manager (async casting, `SPEC-domain-model.md` §6) — this is a confirmed, intended delay to the start of analysis, not a defect.
- **Delegating a manager auto-clears any expert pick on that row**, and **claiming an activity for yourself auto-fills you as its expert** — both directions of the same rule: the expert field only ever holds a value the current viewer is entitled to set.
- **Casting search offers the full activity vocabulary with no predefined subset** — the project manager builds their own activity list from scratch every time, rather than choosing from a hard-coded handful.
- **Manual mode skips the workspace click.** Because manual-mode projects route straight to Review, the wizard calls the shell's `setCurrentProject` directly instead of relying on the Home-card click that normally performs that step for every other mode.
- **New projects are exempt from Home's demo-only block** (`SPEC-home.md` §8) — no `builtOut` flag is set on wizard-created projects, so they're always fully openable, unlike four of the five hand-seeded projects.
- **The deadline field defaults to a fixed calendar date** (`2026-08-12`) rather than to "N days from today" — worth noting since the countdown/urgency chip elsewhere in the app (`SPEC-home.md` §5) is computed from this value, so a project created long after that date would show as already overdue by default unless the field is changed.

## 9. Non-functional

Nothing scale-related — casting is capped by the 13-entry activity vocabulary, and the document list has no stated limit (the per-file "up to 200 MB" cap in the upload-zone copy is never enforced, since no real file is ever read).

## 10. Placeholders & gaps

- **"Drop tender documents here" implies drag-and-drop, but only a click handler exists** on the upload zone and the "add another document" zone — there is no `dragover`/`drop` listener anywhere in the source. A user who actually tries to drag a file onto the zone gets no response at all; only clicking adds a (synthetic) document. This is a real gap between the copy's implied behaviour and the wired behaviour, distinct from the upload itself being simulated (see §6, which is backend-dependent by nature, not a gap).
- **No native file picker.** Clicking the upload zone doesn't open an OS file dialog — it appends a canned document from a fixed 5-entry table. Unlike parsing/storing a real PDF (which does need a backend), opening a file picker is something a static page can do without one; its absence here is a scope choice for the prototype rather than something inherently backend-dependent, so it's listed here rather than folded into §6's backend-dependent items.

## 11. Open points

- The **Compliance matrix** toggle's static label doesn't match its own live description text (which describes assigning an *expert*, i.e. what the Allocation toggle's own copy would suggest) — worth confirming whether the label or the description is the one that's stale; not resolved here since picking one would be guessing at intent.
- The step-3 estimate ("~2,400 blocks... 2 min") is a fixed string regardless of how many documents were actually added in step 2 — unclear whether this is intentional (a fixed demo number, since the "documents" aren't real anyway) or an oversight that should scale with `P.docs.length`.
- Whether the manual-mode warning box in step 3 ("The review screen opens with the document but no blocks") is accurate when zero documents were added in step 2 (a legal path — step 2 has no required minimum) isn't addressed by any copy on this screen.
