# SPEC — Project creation (New tender wizard)

> Derived from the prototype's actual behaviour, per `docs/prompts/PROMPT-derive-specs-from-prototype.md`. Describes `creation-projet.html` as built. Implements `TICKET-tender-creation-rework.md` — see that ticket for the reasoning behind each decision below; this spec states the result. Supersedes every earlier version of this document, which described a five-step wizard with per-activity casting built into it.

## 1. Purpose

**Creation produces the minimum needed to start working, and nothing more.** A four-step wizard collecting identity, documents, processing mode and the project management team, then ends by starting capture and landing the user on the project — not on another form. Everything it collects stays editable afterwards; nothing here is a commitment.

## 2. What left the flow, and why

Casting — assigning who works on which activity — used to be steps 4 and 5 here. It is gone. Casting stopped being a creation-time activity: it's ongoing project user management, on its own permanent screen (`SPEC-team-management.md`), filled in by several people at their own pace, throughout the project's life. A sequential form can't represent that, and trying to was the actual source of the old flow's confusion — it asked for things nobody could answer yet.

Capture and characterisation never needed a roster. Allocation only needs one for the activities characterisation actually finds in the document — which creation can't know in advance either.

## 3. Actors

The person running the wizard is the project's creator, automatically the first member of its project management team (`id:"admin"`, `"Bid Director — you"`). No other role interacts with this screen.

## 4. Entry points

- "＋ New tender" on Home (`accueil.html`) and on the Dashboard header (`dashboard-et-config.html`, `#new-proj`).
- "Cancel" (header) routes back to Home without creating anything — no confirmation prompt, no draft is kept.

From step 4's completion: **AI-assisted or segmentation-only mode** routes to the Dashboard, where capture is already running in the background — not to a review-then-open flow, and not to Casting. **Manual mode** routes straight to the Review/Allocation screen, since there's no processing to show and a human does every step from the start.

## 5. Layout

- **Header** — logo, "New project" breadcrumb, "Cancel."
- **Left stepper** (270px) — 4 numbered steps (Project identity / Documents / Processing mode / Management team), current step highlighted, completed steps marked done and clickable to jump back.
- **Right content pane** — one form per step, scrollable, max-width constrained for readability.
- **Footer** — "Step N of 4" progress text, Back (hidden on step 1) and Continue/Create buttons.
- **Processing overlay** (modal, non-blocking, AI/segmentation modes only) — a brief confirmation shown while control passes to the Dashboard.

## 6. Data collected

**Step 1 — Project identity.** Name*, BO-ID*, product line, system (select, 5 options), region (select, 5 placeholder-acronym options — the real list is still to collect, per the ticket's own open question), tender issuer (free text), submission deadline (date, defaults to a fixed `2026-08-12`).

**Product line gets its own control**, not a plain `<select>` among the other fields: six buttons (Turnkey / RCS / SIG / INFRA / Rolling Stock / Services) with a live note underneath stating the downstream consequence — Turnkey resolves allocation to an **activity** (further split by technical/non-technical classification); every other line resolves it to a **person**. This is deliberately surfaced because it's a setting, not a label — allocation behaves differently depending on it. Whether the choice can still change after allocation has run is explicitly open in the ticket; nothing here locks it.

**Step 2 — Documents.** A reorderable list, each showing a synthetic filename (`{ref}_part{n}.pdf`), page count, size, and language, generated from a fixed 5-entry sample table cycled by index. Unchanged from before this rework — it already matched what the ticket asks for (multiple documents, ordered, more expected later on the Documents screen).

**Step 3 — Processing mode.** Two presets (AI-assisted / AI segmentation only) as radio-style cards, plus three individual step toggles — Capture, Characterisation, Allocation — each with on/off descriptive copy, down from four. The fourth toggle, labelled "Compliance matrix," is removed: the matrix is built continuously from verdicts as contributors answer, not produced by an AI pipeline step, so offering it as one was misleading. "Allocation" now means proposing which **activity** a requirement needs, not a manager or expert — there's no roster to propose against at creation time any more. A computed estimate line and, when both Capture and Characterisation are off, a manual-mode warning box, unchanged.

**Step 4 — Project management team.** A list starting with the creator, pre-seeded and permanently first (no remove control on that row). A search-add row below it (own local directory, SSO-style typeahead — same interaction the Casting screen's own PM-team add flow uses) lets the creator add others now; nothing requires it, and skipping straight to Create is a normal path. A closing summary table echoes every field entered across all four steps.

## 7. Interactions

- **Step navigation** — click a stepper item (only to a completed or the current step, or forward via Continue which re-validates first), or Back/Continue. *Implemented.*
- **Step 1 validation** — Continue is blocked with a toast ("Project name and BO-ID are required") if either is empty; every other field is optional. *Implemented.*
- **Pick a product line** — click sets `P.line` immediately (no hidden `<select>` to keep in sync) and swaps the consequence note. *Implemented.*
- **Add / reorder / remove a document** — clicking the upload zone or "add another document" appends one synthetic document; ▲/▼ swap it with its neighbour; ✕ removes it. *Implemented*, not a real file picker (§10).
- **Processing-mode presets and toggles** — selecting a preset sets all three toggles at once; toggling one individually switches to "Custom" and updates the estimate/manual-mode copy live. *Implemented*, all client-side — the estimate is a fixed illustrative string, not derived from `P.docs`.
- **Search and add a project management team member** — typing filters the local directory live (top 8 matches); clicking one adds them with whole-project scope and no further fields — there's no perimeter step, unlike the Casting screen's per-activity add flow, because a PM team member isn't attached to one. *Implemented.*
- **Remove a project management team member** — ✕ on any row except the creator's, which has none. *Implemented.*
- **Create project** (step 4's Continue, relabelled "✓ Create project") —
  1. Re-validates step 1.
  2. Computes the processing mode (`ai` / `segmentation` / `manual`) from the toggle state and pushes it, plus the review-validated flag and a project-meta summary, into the shell's shared state.
  3. Registers the project via the shell's `addProject`, carrying `pmTeam` through (stored on the project object for completeness; not yet consumed by the Casting screen's own independent `PM_TEAM`, per this project's no-shared-data-layer convention — same treatment the old `experts` field got before it).
  4. **Manual mode** routes straight to Review with a toast. **AI-assisted / segmentation-only** show the brief non-blocking overlay, then route to the **Dashboard** — capture is already running by the time it opens (`accueil.html`'s "still processing, opens when complete" gate only applies to opening a project by clicking its card from the tender list; a direct route right after creating it is unaffected).

## 8. States

- **Step validation error** — toast only; the offending field isn't visually marked invalid beyond that.
- **Empty documents** — upload zone shown in place of a list.
- **No search match** (PM team add) — "No match in the directory."
- **Loading** — the processing overlay is the only loading-style state, fixed-duration (1.4s) rather than tied to a real completion signal.
- **Error** — not present beyond the one client-side required-field check.

## 9. Business rules

- **The creator is always the first project management team member and can never be removed from this form** — mirrors the Casting screen's own "a project always keeps at least one" rule, enforced from the start rather than only once you can trigger it there.
- **Adding to the project management team here is optional, never required** — forcing it would reintroduce exactly the problem this rework removes (asking for things nobody can usefully answer yet).
- **New projects are exempt from Home's demo-only block** (`SPEC-home.md` §8) — no `builtOut` flag is set on wizard-created projects, so they're always fully openable, unlike the hand-seeded demo projects.
- **The deadline field defaults to a fixed calendar date** (`2026-08-12`) rather than to "N days from today" — the countdown/urgency chip elsewhere in the app is computed from this value, so a project created long after that date would show as already overdue by default unless the field is changed.

## 10. Non-functional

Nothing scale-related — the document list has no stated limit (the per-file "up to 200 MB" cap in the upload-zone copy is never enforced, since no real file is ever read), and the PM-team directory is a 12-entry illustrative pool.

## 11. Placeholders & gaps

- **"Drop tender documents here" implies drag-and-drop, but only a click handler exists.** A user who tries to drag a file onto the zone gets no response; only clicking adds a synthetic document.
- **No native file picker.** Clicking the upload zone appends a canned document from a fixed 5-entry table rather than opening an OS file dialog.
- **Region acronyms are still placeholders**, per the ticket's own open question — the real regional code list hasn't been collected.

## 12. Open points

Carried over unresolved from the ticket:

- Do the per-step AI toggles survive alongside the manual/AI-assisted mode as two views of the same setting (current behaviour), or should the mode replace them entirely? Two overlapping controls for the same thing risks being confusing.
- Whether the product-line choice can change after allocation has run — probably worth locking at that point, since it drives allocation rules retroactively, but not decided; nothing here locks it yet.
