# Smart Requirement Manager / SRM (iSenS) — Prototype Handover

> Paste this into the new environment (e.g. as `HANDOVER.md` or the start of a `CLAUDE.md`). It is the single source of truth for picking the project back up.

---

## 1. What this is and why it exists

**Smart Requirement Manager** ("**SRM**" for short — working name for the **iSenS** requirements-review experience) is an interactive, dark-UI web prototype of an AI-assisted platform for processing **rail-industry tender / bid documents** (AOs). A tender is captured, its requirements are segmented and characterised by AI, then a human reviews, assigns, and answers them.

**Purpose of the prototype:**
- Test a **restructured interface** for the requirements workflow with real users (moderated 1-on-1 sessions).
- Put one core **design hypothesis** to the test: **defer the DOORS import to the very end** and keep users inside the tool through review, expert answer, matrix compilation and Q&A — instead of exporting to DOORS early.
- Serve as a **shared visual + behavioural reference** for the future build, not as production code.

**It is a disposable reference artifact.** The credibility that matters for testing comes from realistic *content*, not from technical plumbing (no database, no backend).

---

## 2. Architecture and technical decisions (with rationale)

### 2.1 Six source screens + a Python merge
The app is authored as **six standalone HTML files**, each a self-contained screen (own `<style>` and `<script>`, no shared runtime, no external dependencies):

| Source file | Screen |
|---|---|
| `accueil.html` | **Home / "My tenders"** — entry point, project list |
| `dashboard-et-config.html` | **Project dashboard** (hub) + **Configuration** + **Team management** (B4) |
| `revue-documentaire.html` | **Document review** (largest/most complex screen) |
| `suivi-experts-et-versions.html` | **Expert follow-up** + **Versions & Q&A** |
| `creation-projet.html` | **New-project wizard** |
| `expert-space.html` | **Expert Space** — the individual expert's own qualification screen (committed Aug 12, after this doc's first draft — see §2.1's note below and TG1) |

`build_merge.py` reads the six files, rewrites inter-file `href="X.html"` links into `parent.routeUrl(...)`, base64-encodes each screen (UTF-8), and emits a **single** `docreview-app.html`. A thin shell hosts a full-screen `<iframe>` and swaps its `srcdoc` on hash-routed navigation.

- **Why separate sources + merge:** each screen stays isolated and easy to edit; the single merged file is trivial to host on **GitHub Pages** for testing (rename to `index.html`, public repo). For development, **always work in the six sources** — the merged file is only the deliverable.
- **Why vanilla HTML/CSS/JS, no framework:** fast iteration, zero build tooling, statically hostable, disposable. This is deliberate for a throwaway prototype.

### 2.2 Cross-screen state lives in the shell
Because each screen is an isolated iframe that reloads on navigation, anything that must persist across screens lives in the **shell** (in `build_merge.py`) and is reached via `parent.*`:
- `getTheme/setTheme` (dark/light), `getRedactMode/setRedactMode`
- `getProjects/addProject/openProject/getCurrentProject/resetDemo`
- background **processing loop** (`startProcLoop`, `setInterval` in the shell) — so a project keeps "processing" while you navigate elsewhere
- `isReviewValidated/setReviewValidated` (drives Allocation's own "Done" phase-card state; no longer gates Follow-up — see TE2), `getProjectMode/setProjectMode`, `getProjectMeta/setProjectMeta`
- `pushAIFeedback/getAIFeedback`
- **Why:** non-blocking background processing and shared flags cannot live inside a single iframe that gets torn down on navigation.

### 2.3 Theming
All colours are **design tokens** (`--bg`, `--panel`, `--text`, `--accent`, `--ia`, `--ok`, `--human`, `--warn`, etc.). Light mode is a `html[data-theme="light"]` block that overrides the semantic tokens. A head-loader applies the shell theme before render to avoid a flash. **Why token-based:** flipping the theme is a single override block; ~90% of surfaces switch cleanly (a few hard-coded shadows are slightly heavy in light — acceptable).

### 2.4 The review table (the heart of the tool)
- **Two render paths.** Normal data (hundreds of requirements) → **full render**, all rows, variable height, wrapped/readable text, inline editing. The **scale test** (12,000 synthetic rows) → **windowed/virtualised** render (fixed 44px rows, no inline edit). **Why:** real AOs are hundreds of requirements, where full render enables Excel-like inline editing and full-text reading; windowing is only needed to prove volume handling.
- **Excel-like intent** (driven by repeated stakeholder feedback that users are fastest/most familiar in Excel): inline per-cell editing of every editable field (Class, Activity, Type, Manager, Expert, Status), fast multi-select (click / shift-range / select-all), collapsible columns, and document structure (section + heading rows) shown inline so you follow the document thread.

### 2.5 Data model decisions
- **Block natures:** `heading` / `info` (Information) / `requirement` / `image`. Titles build the collapsible nav hierarchy (H1›H2›H3); Information is context with no detail panel; Requirements get the full panel; Images render in the document and can be **characterised** as Information or Requirement. Reclassification is inline. **The detail panel keys off `blockNature(b)`, not raw `kind`**, so an image classified as a requirement gets the full panel and joins the table.
- **HITL is a pattern, not a role:** the AI proposes, a human validates before an object advances — enforced per-item (a requirement only reaches `allocated` through an explicit validation action, see §8 of `SPEC-domain-model.md`), not by gating access to a whole phase: Allocation and Follow-up run side by side (TE2 — see 3).
- **Manager vs Expert are distinct:** *Manager* = who handles the requirement (delegation, one per requirement, admin sees all); *Expert* = the OBS-derived assignment. Both are separate columns/fields.
- **OBS drives assignment** via a PBS→ABS→OBS chain with confidence; weak OBS (<75%) auto-flags "to review" but never locks (human validation always wins).
- **Activity** is a multi-select of 12 values; **Turnkey (TKY)** is a first-class selectable value (the most complex/variable case).
- **Multi-document:** a tender = several documents the user uploads and **orders**; they are **concatenated** (not interleaved) into one tender. Provenance is preserved (doc banner in the flow + a document filter). No per-document role.
- **AI feedback** is captured implicitly on every correction (future-training signal); an explicit "why" is requested only on high-confidence overrides.

---

## 3. Current state (what is built and working)

- **Home / workspace** with 5 seed projects, statuses (`Processing`, `Requirement review`, `Expert review`, `Q&A & Versioning`, `Submitted`), non-blocking background processing with live progress bars, and **Reset demo** (button + `Ctrl+Shift+R`).
- **New-project wizard**: fields incl. Product line / System / Region; **multi-document upload** with up/down reordering; processing mode (AI-assisted / segmentation-only / fully manual) via 4 toggles now labelled **Capture / Characterizer / Compliance matrix / Activity**. **Casting (B2)**: the project manager assigns one activity manager per activity at creation; casting is **asynchronous** — the PM only fills in experts directly for activities attached to themselves, everyone else's experts are filled in later by that activity manager on the Team screen, at their own pace (see §6 of `SPEC-domain-model.md`).
- **Dashboard**: reworked layout — phase rail (where am I) + "what needs you now" (primary) + "project health" (secondary) + activity feed. **No cross-phase gating (TE2):** Allocation and Follow-up are both always open and run side by side — an earlier version locked Follow-up until Allocation was finalized (TE1), reverted because the real workflow no longer works that way. **Team management (B4)**: a dedicated Team screen (no global nav entry, reachable via the dashboard header) where each activity manager fills in their own experts against the activities cast to them; a project-manager view aggregates casting-completion progress across the whole team.
- **Document review** (3 modes: Document / Review / Compare):
  - Collapsible **heading hierarchy** in the left nav.
  - Three **block natures** with inline reclassification; images displayed and characterisable.
  - **Excel-like table**: full-text readable rows, section+heading rows inline, inline editing of all fields, collapsible columns, multi-select + bulk bar (Manager / Activity / Validate).
  - **Classification** Technical / Non-technical (routes PBS vs ABS).
  - **Characterisation/allocation progression (B6/B7)**: `suggested` → `edited`/`toreview` → `allocated`, replacing an older vocabulary that conflated "AI is confident" with "a human confirmed it" — an item only reaches `allocated` through an explicit human validation action (see §8 of `SPEC-domain-model.md`).
  - **REX tab** in the detail panel (badge count, titles only, opens in source system) — mocked.
  - **Modular Export** panel: pick steps (Capture / Characterization / Allocation) × format (Excel / CSV / ReqIF / DOORS 9 / DOORS Next) — mocked (toast).
  - **Multi-document**: doc banners in the flow + document filter; 2 seed documents.
  - **Scale test** toggle (12,000 rows, virtualised).
- **Expert follow-up** and **Versions & Q&A** — both always open (TE2; no longer gated on Allocation being finalized).
- **Expert Space** (`expert-space.html`, added after this document's first draft): the individual expert's own screen — triage by status, render a compliance verdict (Compliant / R&D Needed / Not compliant), ask a Q&A question, request reassignment. Enforces a **activity-parent hierarchy** for permissions (a manager/expert on a parent activity automatically sees descendant activities too) — implemented in this screen only, see §9 of `SPEC-domain-model.md`.
- **Configuration**: Appearance (dark/light), AI feedback loop, Team & experts (restricted view: redact/hide). Most other Config sections (Workflow, AI & segmentation, Q&A, Versions, Language) are marked demo-only in the UI — not wired to real behavior in this build.
- **Deliverable:** `docreview-app.html` (merged, ~930 KB — grows as content/features are added; don't treat the figure as load-bearing). Language rule enforced: **all UI copy in English**.

---

## 4. What remains to do

**Immediate / prototype phase**
- **Replace the demo dataset with realistic, anonymised AO content** — this is the single biggest lever for credibility in user tests (real requirement wording, real section structure, tables, hundreds of items, their vocabulary and ID conventions). Content is being sourced. Everything else is secondary to this.
- Extend the **bulk bar** to cover Expert / Type / Class (currently Manager / Activity / Validate). Inline per-row editing already covers all fields.
- Optional: **chatbot** (discussed, not built) — read-only "chat with the captured tender", as a floating button + an "Ask about this" action from a requirement's detail that pre-loads context. Keep it read-only (do not let it act — that conflicts with HITL).

**Deferred / conditional**
- Excel-style **keyboard navigation** in the table (arrow/Tab/Enter) — only if testing shows users want it.
- **Real export** file generation (currently mocked).
- Traditional **discovery** on Expert review / Q&A (still upstream, many unknowns — not a prototype test).
- Structured **persona interviews**.

**Post-validation (only after user tests confirm the concept AND the stack is confirmed with the dev lead)**
- Rewrite in the **target stack** as a clean, componentised codebase. Deliverables that belong to the design mandate: **design system** (tokens, components), **reference components**, **interaction spec**, **data schema + business rules**. Building the application itself is the developers' territory.

---

## 5. Pitfalls & constraints (read before touching anything)

- **Reference, not codebase.** Do **not** try to "clean up" the vanilla JS into a product. CSS/HTML recycle well; the JS is throwaway and gets **rewritten** in the target stack. The value to transfer is the design + behaviour + data model, not the code.
- **Order matters.** Do not start the real codebase before (a) user tests validate the concept and (b) the stack is confirmed with the dev lead. A head-start in the wrong direction is a step backward.
- **Scope / mandate.** Design foundation (system, reference components, spec, schema) is in scope. Developing the app is not. Claude Code makes the boundary easy to cross — keep it in mind.
- **Build & verify workflow** (unchanged, follow every time):
  1. Edit the **five source files** — never the merged file directly.
  2. `python3 build_merge.py`
  3. Verify: extract the last `<script>` of each screen and `node --check`; confirm each base64 blob decodes as UTF-8; confirm **0 dead `href="*.html"` links**; use **jsdom** for behavioural checks.
  4. Copy changed sources into the output alongside `docreview-app.html`.
- **jsdom, not puppeteer.** Puppeteer fails here (no Chromium download on the restricted network). Use jsdom; note `clientHeight` is 0 under jsdom, so the windowed scale-test paints 0 rows in tests (works in a real browser).
- **Network allowlist** (for any tooling): npm / pypi / github only.
- **Only one project is fully navigable:** *Energy Monitoring System* (`stb2026`). The other projects illustrate the list, statuses and non-blocking processing; opening them shows the built project's data. Steer test participants to the EMS project for task scenarios.
- **Image-as-requirement is handled by nature**, not `kind` — keep any new panel/table logic keyed on `blockNature(b)`.
- **In-memory only.** No localStorage/DB; state resets on reload. Reset-demo restores the seed (keeps the theme).
- **Language rule (hard):** everything the tool produces is **English** (UI, labels, copy, docs, code). Working discussion happens in French.
- **Client confidentiality (hard):** never store or embed the real client company name, real surnames, or other identifying entities. Use "the client" / generic placeholders. The names in the demo data are fictional.
- **User-testing setup:** moderated 1-on-1, ~1h (30 min observing current DOORS usage + 30 min prototype test with a scenario). Prototype hosted on GitHub Pages; the participant works on **their** machine and shares **their** screen over Teams (record the call, get spoken consent). Iterate the proto only **between** sessions, and only for clear defects — version-tag who saw what; park design-hypothesis changes until several participants confirm them.

---

## 6. File manifest

```
accueil.html                     # Home / My tenders (entry point)
dashboard-et-config.html         # Dashboard hub + Configuration + Team management (B4)
revue-documentaire.html          # Document review (largest)
suivi-experts-et-versions.html   # Expert follow-up + Versions & Q&A
creation-projet.html             # New-project wizard
expert-space.html                # Expert Space — the individual expert's own screen
build_merge.py                   # Merges the 6 sources -> docreview-app.html (shell + state live here)
import_capture.py                # Converts real .xlsx AO captures (kept out of the repo) into data.js
docreview-app.html               # MERGED deliverable (host this; rename to index.html for GitHub Pages)
```

**Routes:** `home` (default), `dashboard`, `config`, `review`, `followup`, `versions`, `new`, `expert`.
**Reset demo:** `Ctrl+Shift+R` (anywhere) or the button on Home.
