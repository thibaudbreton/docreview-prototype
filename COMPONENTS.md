# Components

_Maintained alongside the code. Updated in the same commit as any component change._

This inventory was seeded on 2026-09-01 by reading every screen's source HTML/CSS/JS in full (`accueil.html`, `creation-projet.html`, `documents.html`, `qa.html`, `compliance.html`, `dashboard-et-config.html`, `revue-documentaire.html`) — the merged files (`index.html`, `docreview-app.html`) were not read; per `README.md`, sources are always edited, never the merged output. See `CLAUDE.md` for the rules that keep this file current from here on.

**Design tokens actually defined** (both theme blocks, same names, different values): `--bg`, `--panel`, `--line`, `--text`, `--text-2`, `--text-3`, `--accent`, `--accent-soft`, `--ia`, `--ok`, `--human`, `--warn`, `--paper`, `--paper-ink`, `--text-xs/sm/base/lg/xl`, `--space-1` through `--space-8` (4/8/12/16/20/24/32px), `--radius-xs/sm/md/lg/pill`, `--font-ui/doc/mono`.

**Untracked custom properties in near-constant use** — not part of the token scale above, so not swappable by theme the way real tokens are, and a likely first fix before any Figma pass: `--panel-2`, `--panel-3`, `--line-2`, `--accent-hover`, `--ok-soft`, `--warn-soft`, `--ia-soft`, `--human-soft`. They're flagged per-entry below wherever a component depends on one.

**Reading this file**: several components below are genuinely one component shared byte-for-byte across screens (file lists more than one screen). Many more are the *same idea* re-implemented independently per screen under a different class name, with independently-drifted hardcoded values — those are kept as separate entries (one per file) with a `notes` cross-reference to their siblings, because collapsing them would hide exactly the duplication this manifest exists to surface.

## Atoms

### Primary Button
- **level**: atom
- **file**: accueil.html, creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: default, hover, disabled (creation-projet.html only)
- **tokens**: --space-2, --space-4, --radius-md, --accent, --text-base
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.btn-primary`, near-identical across all seven screens. Hover uses `--accent-hover` (untracked). Text color hardcoded `#fff`, never a token. Several screens duplicate this exact recipe under their own class instead of reusing it — see Danger Button, Cast Add Confirm (noted under Add-Person Flow).

### Ghost Button
- **level**: atom
- **file**: creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: default, hover, small (`--text-sm` inline override, revue-documentaire.html)
- **tokens**: --space-3, --radius-md, --text-2, --text-sm, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.btn-ghost`. Border uses untracked `--line-2`. Vertical padding hardcoded (6–7px) instead of a space token. CSS also exists in accueil.html but is never instantiated there — dead code.

### Cancel Button
- **level**: atom
- **file**: documents.html
- **variants**: none
- **tokens**: --space-2, --space-3, --radius-md, --text-2, --text-sm
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.btn-cancel` — a near-duplicate of Ghost Button under its own class, missing even the `:hover` state Ghost Button has. Candidate to just become a Ghost Button instance.

### Danger Button
- **level**: atom
- **file**: documents.html
- **variants**: none
- **tokens**: --space-2, --space-4, --radius-md, --warn, --text-sm
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.btn-danger` duplicates Primary Button's box model with `--warn` swapped for `--accent`, as a fully separate ruleset rather than a modifier class. Text hardcoded `#fff`.

### Icon Button
- **level**: atom
- **file**: documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: plain, active (`.on`, dashboard-et-config.html only), with Notification Dot
- **tokens**: --radius-md, --text-2
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.icon-btn`. Hardcoded fixed `32×32px`, not derived from the space scale. Hover background is untracked `--panel-3`.

### Notification Dot
- **level**: atom
- **file**: accueil.html, documents.html, qa.html, compliance.html, dashboard-et-config.html
- **variants**: none
- **tokens**: --warn, --panel
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.badge-dot`, nested inside Icon Button. Hardcoded `8px` circle with hardcoded `2px` border/offset, not on the space scale.

### Nav Button
- **level**: atom
- **file**: documents.html, qa.html, dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3, --radius-md, --panel, --text-2, --text-sm, --accent, --accent-soft
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.nav-btn` (icon+label "destination" link, e.g. "Documents", "Dashboard"). Each instance carries a code comment explicitly framing it as the deliberate replacement for a plain back-arrow link — an intentional, designed-for-reuse atom despite low instance count per file. Border relies on untracked `--line-2`.

### Demo / Prototype-Only Control
- **level**: atom
- **file**: accueil.html, dashboard-et-config.html, compliance.html
- **variants**: reset-style (`.reset-btn`, accueil.html), link-style (`.demo-link`, dashboard-et-config.html and compliance.html)
- **tokens**: --text-xs, --text-3, --space-1, --space-3, --radius-md, --human, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: A code comment in dashboard-et-config.html explicitly states `.demo-link` "mirrors accueil.html's `.reset-btn`." Dashed border and an unusual `--human` hover color are a deliberate convention across the codebase to make moderator/demo-only affordances read as "scaffolding, not the product" (also used by the Demo Role Switcher organism in compliance.html). Border relies on untracked `--line-2`.

### Header Avatar
- **level**: atom
- **file**: accueil.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: none (fixed initials "TB")
- **tokens**: --text-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.avatar`, byte-for-byte identical across every screen that has it (absent from creation-projet.html's header). Background is a hardcoded gradient `linear-gradient(135deg,#e0a43c,#c4763a)`, text hardcoded `#fff`, radius hardcoded `50%` instead of `--radius-pill` — none of this can follow a theme change.

### Person Avatar
- **level**: atom
- **file**: creation-projet.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: sizes 22px/26px/28px/30px/32px/34px depending on context (inline style overrides, not a size scale)
- **tokens**: --text-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.exp-avatar` / `.exp-av` / creation-projet's unnamed person-initials style — same idea (circle, per-person hex background passed inline from JS data, initials text), independently sized per screen with no shared scale. Background color always a literal hex from JS data (`MANAGERS[]`, `EXPERTS`, `PM_COLORS`), never a token.

### Toggle Switch
- **level**: atom
- **file**: creation-projet.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: on, off
- **tokens**: --radius-pill, --accent, --accent-soft
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Three independent implementations (`.tog` in dashboard-et-config.html at 40×22px, creation-projet.html's at 38×21px, revue-documentaire.html's bespoke `.wrap-switch` at 30×17px) — same concept, three different hardcoded geometries, none on any scale.

### Chip Toggle
- **level**: atom
- **file**: dashboard-et-config.html
- **variants**: on, off
- **tokens**: --radius-pill, --text-sm, --text-2, --accent-soft, --accent, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.chip-tog` (Assignment-criteria chips). Border relies on untracked `--line-2`. `.cast-unstaffed-toggle` (same file, Team screen) is the same pill-toggle idea with a warn-colored active state, implemented as an unrelated class instead of a variant of this one.

### Checkbox
- **level**: atom
- **file**: compliance.html, revue-documentaire.html
- **variants**: row-select (with indeterminate "select all" state), multiselect option box
- **tokens**: --accent, --radius-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.rowsel`. Native input, only `accent-color` themed; hardcoded `15×15px`. Shared via `table-engine.js` between these two screens' review grids.

### Radio Selector Dot
- **level**: atom
- **file**: creation-projet.html
- **variants**: on, off
- **tokens**: --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Used only inside Selectable Preset Card. 17px diameter and 3px inset hardcoded; border relies on untracked `--line-2`.

### Text Input
- **level**: atom
- **file**: creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: bordered (`.inp`, `.field input`), quiet/in-grid (`.cell-text`, revue-documentaire.html only — invisible border until hover/focus), search (no border)
- **tokens**: --radius-md, --space-2, --space-3, --text, --text-base, --text-sm, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: The most-reused atom in the codebase. Several instances hardcode `8px` padding instead of referencing `var(--space-2)` (same value, dropped token reference) — e.g. documents.html's `.doc-tools input`. Background/border on some instances rely on untracked `--panel-2`/`--line-2`.

### Select Dropdown
- **level**: atom
- **file**: creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: bordered (`.sel`, `.field select`), quiet/in-grid (`.cell-select`, revue-documentaire.html — AI-suggested dashed state, empty/warn-colored state)
- **tokens**: --radius-md, --space-2, --space-3, --text-sm, --text-base, --accent, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.cell-select`'s dropdown chevron is a hand-drawn SVG with a **hardcoded hex fill (`#66708a`)** baked into the CSS background-image data URI — defined once on `:root`, so it cannot repaint for the light theme at all.

### Textarea
- **level**: atom
- **file**: qa.html, compliance.html
- **variants**: dashed/paste box (qa.html, 90px min-height), solid/response box (compliance.html, 110px min-height)
- **tokens**: --radius-md, --space-2, --space-3, --text, --text-sm, --text-base, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Same functional atom, independently sized per screen.

### Range Slider
- **level**: atom
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --accent, --font-mono, --text-base
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Native `input[type=range]` + `.range-val` readout ("Overdue threshold", "Uncertainty threshold"). Gap to readout hardcoded 14px.

### Progress Bar
- **level**: atom
- **file**: accueil.html, creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: gradient fill, solid fill, thin inline strip — track heights independently hardcoded per instance (3px, 4px, 5px, 6px, 8px seen)
- **tokens**: --radius-xs, --accent, --ok, --ia
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: The single most-duplicated primitive in the app — at least a dozen independent class implementations across the seven screens (`.pc-bar`, `.pbar`, `.mini-bar`, `.doc-wbar`, `.doc-prog`, `.ph-bar`, `.exp-lbar`, `.ai-rel-bar`, `.fbar`, `.progress-track/.progress-fill`, `.exp-bar`, `.arb-progress .bar`), all sharing "colored track + fill" but each with its own hardcoded height and no shared height scale. Track background is consistently the untracked `--panel-3`. A strong candidate for the first real consolidation pass.

### Status Dot
- **level**: atom
- **file**: accueil.html, documents.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: pulsing (processing badge), health dot (on_track/at_risk/behind), state dot, notification dot, legend dot (dashboard-et-config.html, compliance-color-coded)
- **tokens**: --ok, --ia, --warn, --accent, --text-3
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Independently hardcoded diameter per instance (5px–9px seen), no shared size token. "None/pending" states rely on untracked `--line-2`.

### Count Badge
- **level**: atom
- **file**: qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: `.mcount`, `.tcount`, `.view-badge`, `.tab-count`, `.nh-c`, `.rex-count`, `.count` (dashboard "5" pill)
- **tokens**: --text-xs, --radius-lg, --radius-md, --accent, --accent-soft, --warn, --warn-soft (untracked)
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Hardcoded vertical padding (1–3px) across every variant instead of a space token.

### Activity / Requirement Tag
- **level**: atom
- **file**: qa.html, compliance.html, revue-documentaire.html
- **variants**: default, `.ai` (dashed, AI-unconfirmed), `.tky` (turnkey, filled), `.proposed` (pending PM review)
- **tokens**: --font-mono, --text-xs, --ia, --human, --radius-xs, --space-1
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.ptag` / `.qa-req` / `.c-id`. Turnkey variant uses a fully hardcoded gray (`#7b8794`), not a token. Letter-spacing (0.6px) hardcoded. Border relies on untracked `--line-2`.

### Status Badge / Chip
- **level**: atom
- **file**: accueil.html, documents.html, creation-projet.html
- **variants**: `.pc-badge` (processing/req/exp/qa/sub/neutral/info), `.pstate` (ready/running/queued), `.gap-chip` (a/m/r), `.tagrec` (recommended)
- **tokens**: --text-xs, --space-1, --space-2, --radius-pill, --radius-lg, --accent, --accent-soft, --ia, --ok, --warn, --human
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Same "soft background + bold colored text" grammar reimplemented under four unrelated class names with inconsistent radius (`--radius-pill` vs `--radius-lg` for what reads as the same pill). Backgrounds rely on untracked `--ia-soft`/`--ok-soft`/`--warn-soft`/`--human-soft`. Sibling family: Status Pill (below), which reimplements the same idea again in three more screens.

### Status Pill (Requirement Workflow State)
- **level**: atom
- **file**: revue-documentaire.html, dashboard-et-config.html
- **variants**: s-incomplete, s-doubt, s-tovalidate, s-allocated, s-changed (revue-documentaire.html); current/done/wait, staffed/unstaffed/partial/noperm (dashboard-et-config.html's `.ph-badge`/`.cast-group-badge`)
- **tokens**: --space-1, --space-2, --radius-xs, --radius-pill, --text-xs, --warn, --ia, --human, --ok, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Backgrounds use the untracked `--warn-soft`/`--ia-soft`/`--human-soft`/`--ok-soft`/`--accent-soft` family (only `--accent-soft` is an actual tracked token). Sibling of Status Badge / Chip (above) and Verdict/Progress Status Chip (below) — three independent codings of "small colored status label" across the app, none sharing a base class.

### Verdict Pill
- **level**: atom
- **file**: compliance.html
- **variants**: compliant, not_compliant, none, pending (dashed/italic — deliberate, so an unresolved verdict can never read as decided)
- **tokens**: --space-1, --space-2, --radius-sm, --text-xs, --ok, --warn, --text-3
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.vpill`. Sibling of Status Pill / Status Badge — same visual grammar, own class.

### Progress Status Chip
- **level**: atom
- **file**: compliance.html
- **variants**: proposed/assigned, awaiting_answer, awaiting_qa, reassignment_needed, answered
- **tokens**: --space-1, --space-2, --radius-pill, --text-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.spill`. Leading dot is a hardcoded 6px `currentColor` circle. Backgrounds rely on untracked `--panel-3`/`--ok-soft`/`--warn-soft`.

### Blocking Chip
- **level**: atom
- **file**: compliance.html
- **variants**: none
- **tokens**: --space-1, --space-2, --radius-sm, --text-xs, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.blocking-chip` ("⛔ Reassignment needed"). Background relies on untracked `--warn-soft`.

### Compliance Pill
- **level**: atom
- **file**: revue-documentaire.html
- **variants**: c-compliant, c-rnd_needed, c-not_compliant, c-pending (dashed/italic), locked (PM override, adds 🔒)
- **tokens**: --space-1, --space-2, --radius-xs, --text-xs, --ok, --ia, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Same "-soft" background pattern as Status Pill (untracked custom properties).

### Type Chip
- **level**: atom
- **file**: revue-documentaire.html
- **variants**: st-incomplete, st-doubt, st-tovalidate, st-allocated
- **tokens**: --radius-lg, --text-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.type-chip`, floats above a Document Block. All four colors are **fully hardcoded hex pairs**, deliberately not `--warn`/`--ia`/`--human`/`--ok` (the paper background is always light regardless of app theme) — but this means the chip's palette silently can't be updated by changing the tokens. Same disconnect as compliance.html's `.vtag` inside Document Block there.

### Flag Tag
- **level**: atom
- **file**: compliance.html
- **variants**: none
- **tokens**: --text-xs, --space-2
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.flag-out` ("Δ outdated"). Background relies on untracked `--ia-soft`.

### Deadline Chip
- **level**: atom
- **file**: accueil.html
- **variants**: default, soon, urgent
- **tokens**: --ia, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Text-only, no background/pill — the simplest of the status-signal atoms, inconsistent in form with Status Badge / Chip despite a similar purpose.

### Required Field Marker
- **level**: atom
- **file**: creation-projet.html
- **variants**: none
- **tokens**: --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: A styled `*`, reused on 3 wizard step-1 field labels.

### Disclosure / Expand Chevron
- **level**: atom
- **file**: documents.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: collapsed, expanded (rotated)
- **tokens**: --text-3, --text-xs, --radius-sm
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Row/group-level expand affordance — `▶` glyph in documents.html (9px, no tokens at all), `.cast-caret` (▾) in dashboard-et-config.html, `.branch-caret` in revue-documentaire.html (has real button chrome, hardcoded 20×20px). Distinct from Panel Toggle Chevron (below), which collapses whole side panels rather than a row.

### Panel Toggle Chevron
- **level**: atom
- **file**: compliance.html, revue-documentaire.html
- **variants**: nav collapse, detail-panel collapse
- **tokens**: --radius-sm, --text-3, --text-xs, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.panel-toggle`. A code comment in compliance.html states this is deliberately "the same pattern as revue-documentaire.html." Hardcoded 20px size.

### Kbd Key
- **level**: atom
- **file**: qa.html, compliance.html, revue-documentaire.html
- **variants**: real `<kbd>` element (compliance.html, revue-documentaire.html), `<span class="kb">` square (qa.html)
- **tokens**: --font-mono, --text-xs, --radius-xs, --space-1
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Same "keyboard shortcut hint" concept, two different markup strategies. qa.html's version is a fixed 20×20px square. Borders/backgrounds rely on untracked `--line-2`/`--panel-2`/`--panel-3`.

### Spinner
- **level**: atom
- **file**: qa.html
- **variants**: none
- **tokens**: --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.qa-spin`, shown during the simulated dossier-extraction wait. Hardcoded 13px size, 0.7s duration; border relies on untracked `--line-2`.

### Match Ring
- **level**: atom
- **file**: compliance.html, revue-documentaire.html
- **variants**: none
- **tokens**: --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.rex-ring`, a `conic-gradient` donut for REX match-percentage, driven by an inline `--p` variable. Entirely hardcoded geometry (22–26px, mask radius, gradient stops) — no tokens beyond the fill color.

## Molecules

### Search Box
- **level**: molecule
- **file**: dashboard-et-config.html, revue-documentaire.html
- **variants**: nav search (full width), toolbar search (fixed 220px), Team-screen search (`.cast-search-wrap`, with leading icon)
- **tokens**: --space-2, --space-3, --radius-md, --accent, --text-base
- **built-from**: Text Input
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: revue-documentaire.html's two instances (`#nav-search`, `#table-search`) are kept in sync via JS. dashboard-et-config.html's icon-offset padding (34px/11px) is hardcoded and relies on untracked `--panel-2`/`--line-2`.

### Filter Toolbar
- **level**: molecule
- **file**: documents.html, qa.html, compliance.html
- **variants**: search + one select (documents.html, qa.html), search + two selects + toggle (compliance.html `.f10-tools`)
- **tokens**: --space-2, --space-3
- **built-from**: Text Input, Select Dropdown
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Same "filter row" pattern re-implemented per screen. documents.html's input hardcodes `8px` padding instead of `var(--space-2)`; qa.html's hardcodes `7px`.

### Toast
- **level**: molecule
- **file**: accueil.html, creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: ok, warn
- **tokens**: --space-2, --space-3, --space-4, --radius-lg, --text-base, --ok, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.toast` + shared `toast(msg, kind)` JS helper — verbatim-identical CSS/JS in most screens, but accueil.html colors its "warn" toast with `--ia` (amber) via `.t-warn` while creation-projet.html/documents.html/qa.html/compliance.html/dashboard-et-config.html color the same warn-kind toast with `--warn` (red) via inline style — the same component signals "warning" in two different colors depending on screen. Box-shadow (`rgba(0,0,0,.5)`) and easing are hardcoded everywhere (no shadow/motion token exists in the codebase). Auto-dismiss duration also drifts per file (2600/3200/3400/3600ms).

### Tab Bar
- **level**: molecule
- **file**: accueil.html, qa.html, compliance.html, dashboard-et-config.html
- **variants**: underline-active (accueil.html tabs, qa/compliance `.hub-tabs`/`.set-tabs`), pill/background-active (`.mode-switch`, `.nav-toggle`, dashboard-et-config.html `.stats-tabs`)
- **tokens**: --space-1, --space-2, --space-4, --space-5, --line, --text-3, --text-2, --text, --accent, --text-base, --text-xs
- **built-from**: none (buttons are plain, not reusing any button atom)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: At least four independent implementations of "group of switchable tabs" across the app with two different visual languages and inconsistent hardcoded padding (5–10px). `.mode-switch` CSS exists in qa.html but is never instantiated there — dead code. Active-tab box-shadow hardcoded (`rgba(0,0,0,.15–.4)`) in several variants.

### Segmented Control
- **level**: molecule
- **file**: creation-projet.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: 2-option, 3-option, pill-track (`.gseg`, `.tbl-gran`, revue-documentaire.html)
- **tokens**: --space-1, --radius-md, --radius-sm, --radius-pill, --text-sm, --text-base, --text-2, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.segc` (dashboard-et-config.html, 8 instances), creation-projet.html's Segmented Choice Group, and revue-documentaire.html's `.gseg`/`.tbl-gran`/`.mode-switch`/`.screen-nav .sn` are five separately-named classes implementing the same "pill-track, active segment gets elevated" pattern with independently hardcoded padding/radius/shadow — the single clearest consolidation candidate in the codebase alongside Progress Bar. Relies on untracked `--panel-2`/`--panel-3`/`--line-2`.

### Version Pill
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-1, --space-2, --radius-pill, --text-sm, --ok
- **built-from**: Status Dot
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.version-pill`, header breadcrumb ("v2.1 active"). Border relies on untracked `--line-2`.

### Multiselect Dropdown
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: open, closed, placeholder text
- **tokens**: --space-1, --space-2, --space-3, --radius-md, --radius-sm, --radius-xs, --accent, --text-base
- **built-from**: Checkbox, Activity / Requirement Tag
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.msel`, Detail Panel's Activity field.

### Breadcrumb
- **level**: molecule
- **file**: creation-projet.html, documents.html, dashboard-et-config.html
- **variants**: static current segment, clickable project-link segment (documents.html)
- **tokens**: --space-2, --text-2, --text-3, --text, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Same `.crumb` shell reused across files, but the "current segment" styling drifts between `.cur` (static) and `.project` (hover-to-accent link) rather than one consistent modifier.

### Detail Field
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: label + select, label + text input, label + read-only value (`.fval`)
- **tokens**: --text-xs, --text-3, --text-base
- **built-from**: Select Dropdown or Text Input
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.field`. Bottom margin is a hardcoded `16px` in both screens rather than `var(--space-4)` (same value, dropped token reference) — one of several places this exact drift recurs. compliance.html additionally has Frozen Field (`.frozen`, bordered box) serving the same read-only purpose with different chrome — near-duplicate worth consolidating.

### Frozen Field
- **level**: molecule
- **file**: compliance.html
- **variants**: none
- **tokens**: --line, --radius-md, --space-3, --text-xs, --text-3, --text-base
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Used in the read-only "Requirement" tab; see Detail Field note above.

### Config Field Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: with/without helper text, with appended Option Description Box
- **tokens**: --space-4, --line, --text-base, --text-sm, --text-3
- **built-from**: Text Input, Toggle Switch, Segmented Control, Chip Group, or Range Slider
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.frow` — the core repeating unit of every Config section (~20 instances). Label column width hardcoded 230px, off any scale.

### Chip Group
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-2
- **built-from**: Chip Toggle
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.chips`, wraps the Assignment-criteria Chip Toggles.

### Option Description Box
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --text-sm, --text-3, --space-2, --space-3, --radius-md, --line, --text-2
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.opt-desc`, explanatory note following most Segmented Controls (5 instances). Relies on untracked `--panel-2`.

### Warning / Notice Box
- **level**: molecule
- **file**: creation-projet.html, documents.html, dashboard-et-config.html
- **variants**: standalone (`.warnbox`), embedded-in-modal (`.loss`), inline-with-CTA (`.stale-note`), neutral/dashed (`.locked-hint`), borderless inline (`.hintbox`)
- **tokens**: --space-3, --space-4, --radius-lg, --radius-md, --ia, --warn, --text-sm, --text-2, --text-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Same "colored notice box" idea under five unrelated class names across three screens, with inconsistent radius (`--radius-lg` vs `--radius-md`). `.warnbox`'s border is a hand-picked raw `rgba(224,164,60,.5)` rather than the `color-mix(in srgb, var(--warn) 35%, transparent)` technique `.loss`/`.stale-note` use — the raw value approximates the dark-theme `--ia` and won't repaint correctly in the light theme the way the color-mix versions do. Relies on untracked `--ia-soft`.

### Dedup Alert Card
- **level**: molecule
- **file**: qa.html, compliance.html
- **variants**: none
- **tokens**: --radius-lg, --space-3, --space-4, --text-sm, --text, --ok
- **built-from**: none (accept/reject are bespoke buttons, not Ghost/Primary Button)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.dedup`. CSS is byte-for-byte identical between both screens. Border is a hand-picked `rgba(224,164,60,.55)`; background relies on untracked `--ia-soft`.

### Requirement Row (Review Table Row)
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: default, selected/bulk-selected, with-branches (Expand Chevron + "Multiple (N)" placeholders), image-sourced (revue-documentaire.html only), information row (static placeholders, revue-documentaire.html only)
- **tokens**: --space-3, --text-xs, --text-sm, --line, --accent, --accent-soft
- **built-from**: Checkbox, Status/Compliance/Verdict Pill, Activity / Requirement Tag, Disclosure Chevron, Select Dropdown, Text Input, Count Badge
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.rrow`. Explicitly documented in both screens' source comments as the same review-table engine, shared via `table-engine.js`. Row height (`--rrow-h:44px`) and column-width grid (`--rgrid-cols`/`--frgrid-cols`) are locally-scoped custom properties with fully hardcoded pixel values, none aligned to the space scale — column config differs per screen, everything else is shared.

### Branch / Allocated-Activity Sub-row
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: editable (Select Dropdowns for expert/manager/compliance), locked (🔒, read-only)
- **tokens**: --space-6
- **built-from**: Activity / Requirement Tag, Select Dropdown, Status/Verdict Pill
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.rrow.branch-row`, indented under a parent Requirement Row when it has 2+ activities. Tinted with untracked `--panel-2` to read as a child row.

### Grid Section / Group Header
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: doctitle, sec (H1), sub (H2/H3), group (Activity group-by header)
- **tokens**: --space-2, --space-3, --space-4, --font-mono, --text-xs, --text-base, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Sticky structural divider rows inside the Requirement Row grid. Group header's left accent color comes from a per-typology hardcoded hex palette (`GROUP_PALETTE`) set via inline `style`.

### Nav Tree Item
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: active, dimmed (filtered out, hardcoded `opacity:.28`)
- **tokens**: --space-2, --radius-sm, --accent-soft, --text-2, --text-xs
- **built-from**: Status Dot, Count Badge
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.nav-item`. Hardcoded vertical padding and active border-left width.

### Nav Tree Section Header
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: nav-doc (document, collapsible), nav-h1 (section, with +/~/− change counts), nav-h2/nav-h3
- **tokens**: --space-2, --text-xs, --text-sm, --text-base, --text-3, --ok, --ia, --warn
- **built-from**: Disclosure Chevron
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.nav-doc`, `.nav-h1`, `.nav-h2/.nav-h3`.

### Document Block
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: requirement (compliance-colored in compliance.html, workflow-status-colored in revue-documentaire.html), heading, information (dimmed), image (figure+caption, revue-documentaire.html only), redacted (restricted view), change-annotated (Compare mode, revue-documentaire.html only)
- **tokens**: --space-1, --space-2, --space-3, --space-4, --radius-xs, --paper, --paper-ink, --font-doc, --text-base, --accent
- **built-from**: Type Chip / Verdict Pill, Status Dot
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.blk` / `.dblk`. compliance.html is the most hardcoded-color spot in the app: verdict borders/backgrounds and `.vtag` badge colors are fixed hex pairs disconnected from `--ok`/`--warn`/`--ia`/`--accent`. revue-documentaire.html's redacted variant uses a hardcoded repeating-gradient "bar-code" fill, fully outside the token system.

### REX Match Item
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: none
- **tokens**: --space-1, --space-2, --space-3, --radius-lg, --text-xs, --text-base, --accent, --accent-soft
- **built-from**: Match Ring, Activity / Requirement Tag
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.rex-item`. Match-score column width hardcoded (26–30px).

### Activity Timeline Entry
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: ok, send/ia, comment, human, warn (colored connector dot per actor/event type)
- **tokens**: --space-1, --text-sm, --text-xs, --ia, --ok, --accent, --human, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.tl-item`. Connector line/dot geometry (offsets, 6–9px dot) hardcoded and coupled between the two rules, not tokenized.

### Peek Paper Excerpt
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: none
- **tokens**: --paper, --paper-ink, --radius-xs, --space-4, --space-5, --font-doc, --text-base, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.peek-paper`. Styled and functional in revue-documentaire.html (legacy hidden markup kept for compare/segmentation reuse); in compliance.html the CSS exists but no render call was found — likely dead/unwired. Hardcoded max-width and box-shadow.

### Change Card
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: add, mod, rem
- **tokens**: --space-2, --space-3, --radius-md, --radius-lg, --text-xs, --ok, --ia, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.change-card`, Detail Panel's Change view (Compare mode).

### Export Option Card
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: xls, send (with nested expert list)
- **tokens**: --space-2, --space-3, --radius-lg, --radius-md, --accent-soft, --ok, --accent, --text-base, --text-sm
- **built-from**: Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.export-opt`, used in the Finalize/Export Modal.

### Export Readiness Summary
- **level**: molecule
- **file**: qa.html, compliance.html
- **variants**: card with big number (`.export-card`, qa.html), inline banner (`.xr-ready`, compliance.html — renders empty unless complete)
- **tokens**: --accent, --accent-soft, --radius-lg, --radius-md, --space-3, --space-4, --space-5, --text-base, --text-xs
- **built-from**: Primary Button (qa.html only; compliance.html's CTA is bespoke)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Two screens independently implement "you're ready to export, N items" — same purpose, unrelated markup. compliance.html's relies on untracked `--ok-soft` plus a hardcoded rgba border.

### Comment Composer
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-2, --space-3, --radius-md, --accent, --text-sm
- **built-from**: Text Input, Primary Button
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.comment-input`, Detail Panel's Activity tab.

### AI Suggestion Card
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: default, uncertain-segmentation (warn-colored)
- **tokens**: --space-3, --space-4, --radius-md, --ia, --ok, --text-sm, --text-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.ia-suggestion`. Border/background colors are hardcoded rgba rather than `--ia`/`--warn`-derived, even though those tokens exist.

### Manager Assignment Card
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: assigned (read view), unassigned (dashed CTA), editing (inline select + Done)
- **tokens**: --space-2, --space-3, --radius-lg, --line, --ia, --ok
- **built-from**: Person Avatar, Select Dropdown
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.mgr-row`/`.mgr-none-row`/`.mgr-edit`, documented in-code as "read view, click Change to edit inline (option B)."

### Role Recap Row
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: filled, missing ("To assign" placeholder)
- **tokens**: --text-xs, --text-sm, --text-3
- **built-from**: Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.role-row`, three compose the Role Recap Card. Label column width hardcoded 62px.

### Allocated-Activity Detail Card
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: default, with pending add-activity proposal, with pending reassignment request
- **tokens**: --space-2, --space-3, --radius-md, --human, --text-xs
- **built-from**: Activity / Requirement Tag, Status Pill, Select Dropdown
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.branch-sec`, Detail Panel's "Allocations (N)" admin/PM view.

### Column Filter Section
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-1, --space-2, --text-xs, --text-sm, --accent, --line
- **built-from**: Checkbox
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.view-sec` + `.colf-opt`, repeated per data column in the Filter Panel.

### Reorderable Column Row
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: default, dragging (opacity .4)
- **tokens**: --text-sm, --radius-sm
- **built-from**: Checkbox
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.colf-row` + drag handle. Implementation delegated to shared `table-engine.js` (`TE.reorderableColumnListHTML`/`bindReorderableColumnList`) — genuinely shared code, not just visual similarity.

### Notification Item
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: mention, status-change, reminder
- **tokens**: --space-3, --space-4, --text-sm, --text-xs, --accent, --ia, --warn
- **built-from**: Status Dot
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.nd-item`, inside the Notifications Dropdown.

### Compare Summary Chip
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: add, mod, rem
- **tokens**: --space-1, --space-3, --radius-pill, --text-sm, --ok, --ia, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.csum`, Compare Bar ("+1 added / ~2 modified / −1 removed").

### Advanced Filter Condition Row
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: text, enum select, is-any-of multiselect, date/between, in_last (numeric)
- **tokens**: --text-xs, --radius-sm
- **built-from**: Select Dropdown, Text Input
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.adv-row`, groupable into nested AND/OR `.adv-group`. Shared logic lives in `table-engine.js` (`TE.OPS_BY_TYPE`, `TE.matchesFilter`, `TE.describeFilter`).

### Propose / Reassign Form
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: add-activity proposal, reassignment request (3 radio reasons)
- **tokens**: --space-2, --space-3, --radius-md
- **built-from**: Select Dropdown, Text Input
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.propose-form`/`.reassign-reasons`, Detail Panel for non-admin managers. Sibling of Inline Form Shell (below), which serves the same purpose in compliance.html — two independently-built form containers for the same "propose a change" idea.

### Inline Form Shell
- **level**: molecule
- **file**: compliance.html
- **variants**: verdict form, reassignment form
- **tokens**: --radius-md, --space-3, --space-4, --text-xs, --text-3
- **built-from**: Detail Field
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.inline-form`/`.if-label`. Code comment notes it was migrated from a now-deleted `expert-space.html`. See Propose / Reassign Form note above.

### Stat Tile / Card
- **level**: molecule
- **file**: documents.html, dashboard-et-config.html
- **variants**: default, warn (documents.html); default (dashboard-et-config.html's Health Stat Tile and Feedback Stat Card are visually near-identical but independently implemented)
- **tokens**: --panel, --line, --radius-lg, --space-3, --space-4, --text-xl, --text-xs, --text-3, --ia
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: documents.html's `.stat` (min-width 150px, used 4× in the Document Summary Strip) and dashboard-et-config.html's `.hstat`/`.fb-card` all express "big number + label" with independent hardcoded padding/letter-spacing — a missed-reuse opportunity flagged directly in the dashboard scan.

### Version History Entry
- **level**: molecule
- **file**: documents.html
- **variants**: current, historical, with stale verdicts
- **tokens**: --space-3, --font-mono, --text-xs, --text-2, --text-3, --ok
- **built-from**: Status Badge / Chip, Warning / Notice Box (nested)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Row padding, column width, several margins hardcoded.

### Modal Field Group
- **level**: molecule
- **file**: documents.html
- **variants**: labeled select, checkbox list item
- **tokens**: --space-3, --text-xs, --text-3, --radius-md, --space-2, --text-base
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Label uppercase letter-spacing/margin hardcoded.

### Empty State Message
- **level**: molecule
- **file**: accueil.html, documents.html
- **variants**: bordered/dashed (`.empty`, accueil.html), plain text (`.doc-none`, documents.html)
- **tokens**: --radius-lg, --text-3, --text-base, --space-6, --text-sm
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Same "no results" purpose, visibly different weight between the two screens.

### Wizard Step Item
- **level**: molecule
- **file**: creation-projet.html
- **variants**: upcoming, active, done
- **tokens**: --space-3, --radius-md, --accent-soft, --text-xs, --text-3, --accent, --ok, --text-base, --text-2, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Step-number circle (22px) and connecting line (1.5px) hardcoded.

### Form Field Row
- **level**: molecule
- **file**: creation-projet.html
- **variants**: none
- **tokens**: --space-4, --line, --text-base, --text-xs, --text-3
- **built-from**: Text Input / Select Dropdown, Required Field Marker
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Label column width (190px) hardcoded. Reused ~7× in Wizard Step 1. Sibling of Config Field Row (dashboard-et-config.html) — same "label + control" idea, independently built.

### Selectable Preset Card
- **level**: molecule
- **file**: creation-projet.html
- **variants**: default, selected
- **tokens**: --space-3, --space-4, --radius-lg, --line, --panel, --accent, --accent-soft, --text-base, --text-sm, --text-3
- **built-from**: Radio Selector Dot, Status Badge / Chip (`tagrec`)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Border weight (1.5px) hardcoded.

### Toggle Setting Row
- **level**: molecule
- **file**: creation-projet.html
- **variants**: none
- **tokens**: --space-3, --space-4, --line, --text-base, --text-sm, --text-3, --ia
- **built-from**: Toggle Switch
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Description swaps between two hand-authored strings by toggle state.

### Upload Dropzone
- **level**: molecule
- **file**: creation-projet.html, documents.html
- **variants**: empty, add-another, inline/horizontal (documents.html)
- **tokens**: --radius-lg, --panel, --accent-soft, --accent, --text-base, --text-sm, --text-3, --text-xl, --space-4, --space-5, --space-6
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: **Concrete CSS bug** in creation-projet.html: `.add-doc:hover` is declared twice with conflicting `background` values — the second silently wins, making the first dead code. Also independently styled per screen (accent icon circle vs. `--panel-3` icon box) despite serving the identical purpose.

### Document / File Card
- **level**: molecule
- **file**: creation-projet.html
- **variants**: with ordering controls (`.doccard`, the one actually rendered)
- **tokens**: --space-3, --radius-lg, --line, --panel, --radius-md, --radius-xs, --warn, --text-xs, --text-sm, --font-mono, --text-3
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.filecard` is fully defined in CSS but never rendered — dead code superseded by `.doccard`. Icon-square dimensions (34/38px) hardcoded.

### Search-to-Add Combobox
- **level**: molecule
- **file**: creation-projet.html, dashboard-et-config.html
- **variants**: empty query (hidden), results, no-match
- **tokens**: --space-3, --radius-lg, --radius-sm, --text-base, --text-2, --text, --text-sm, --text-3
- **built-from**: Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Named "Person Search Typeahead" in dashboard-et-config.html's Team-casting flow — a code comment in creation-projet.html explicitly frames this as reusing "the same shape as the casting screen's own SSO-search add flow," confirming intentional cross-screen reuse despite the independent implementation. Dropdown box-shadow hardcoded in both.

### Team Member Row
- **level**: molecule
- **file**: creation-projet.html
- **variants**: creator (non-removable), added member (removable)
- **tokens**: --space-3, --radius-lg, --line, --text-base, --text-xs, --text-3, --warn, --ok, --radius-pill
- **built-from**: Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Row margin-bottom (8px) hardcoded. Sibling of Cast Person Row (dashboard-et-config.html), which duplicates this same "person row with remove" idea for the Team casting screen.

### Cast Person Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: editable (with remove), read-only
- **tokens**: --space-3, --line, --text-sm, --text-xs, --text-3, --radius-sm, --warn
- **built-from**: Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `castPersonRowHTML`, reused identically for activity/perimeter rosters and the PM-team roster. See Team Member Row note above.

### Key-Value Summary Row
- **level**: molecule
- **file**: creation-projet.html
- **variants**: default value, missing value
- **tokens**: --line, --radius-lg, --text-xs, --text-3, --space-4, --space-3, --text-base, --text, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Header padding (11px) and top margin (22px) hardcoded.

### Deadline Banner
- **level**: molecule
- **file**: qa.html
- **variants**: ok, soon, passed, overdue
- **tokens**: --space-3, --space-4, --radius-lg, --text-sm, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.qa-deadline`, uses `color-mix()` for borders instead of a fixed token. Deliberately renders nothing when the underlying date is unset (explicit "degrade cleanly" code comment).

### Duplicate Alert
- **level**: molecule
- **file**: qa.html
- **variants**: none
- **tokens**: --space-3, --space-4, --radius-lg, --ia, --text-lg
- **built-from**: Ghost Button
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.dup-alert`. Icon is a plain "⚠" glyph, not an SVG.

### Q&A Card
- **level**: molecule
- **file**: qa.html
- **variants**: draft, sent, answered, excluded (dimmed)
- **tokens**: --panel, --line, --radius-lg, --space-2, --space-3, --space-4, --text-base
- **built-from**: Activity / Requirement Tag
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.qa-card`. Answer sub-block relies on untracked `--ok-soft`. `.is-excluded` uses hardcoded `opacity:.6`.

### Context Row
- **level**: molecule
- **file**: qa.html
- **variants**: none
- **tokens**: --panel, --line, --radius-lg, --space-2, --space-3, --space-4, --text-sm
- **built-from**: Activity / Requirement Tag
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.ctx-row`, "Resolved & context" collapsed list only.

### Arbitration Guess Button
- **level**: molecule
- **file**: qa.html
- **variants**: none
- **tokens**: --space-3, --radius-md, --text-sm, --text-xs
- **built-from**: Kbd Key, Activity / Requirement Tag
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.arb-guess`. List is keyboard-addressable via number keys 1–9.

### Expert Card
- **level**: molecule
- **file**: compliance.html
- **variants**: none
- **tokens**: --line, --radius-lg, --space-3, --accent, --accent-soft, --text-xs, --text-base
- **built-from**: Person Avatar, Progress Bar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: "By expert" nav mode only. Disabled remind button uses hardcoded `opacity:.4`.

### Timeline Item
- **level**: molecule
- **file**: compliance.html
- **variants**: ok, send, warn
- **tokens**: --text, --text-2, --text-3, --text-sm, --ok, --accent, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: See Activity Timeline Entry (revue-documentaire.html) — near-identical connector-dot pattern, independently coded per screen.

### Filter Pill
- **level**: molecule
- **file**: compliance.html
- **variants**: p-wait, p-clar, p-over, p-out, p-done, p-reassign; active
- **tokens**: --space-1, --space-3, --radius-pill, --line, --text-sm, --text-2, --accent, --accent-soft, --warn, --ia, --ok
- **built-from**: Count Badge-like `.n` span
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.tpill`, drives the Triage Bar status filters — the compliance.html equivalent of revue-documentaire.html's own `.tpill` (Triage Bar organism), independently implemented.

### Icon Cluster
- **level**: molecule
- **file**: compliance.html
- **variants**: none
- **tokens**: --line
- **built-from**: Icon Button
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.icon-cluster`. A code comment states this exists specifically so adjacent icon buttons "read as attached… one cluster, not three separate controls."

### Column Visibility Menu
- **level**: molecule
- **file**: compliance.html
- **variants**: none
- **tokens**: --radius-lg, --space-3
- **built-from**: Checkbox, Reorderable Column Row
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.view-panel#f-cols-panel`, fixed hardcoded width 260px.

### Demo Role Switcher
- **level**: molecule
- **file**: compliance.html
- **variants**: none
- **tokens**: --text-xs, --radius-md, --space-1, --space-3, --human
- **built-from**: Select Dropdown, Demo / Prototype-Only Control
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.demo-link` + `.view-panel.demo-panel`. Explicitly a moderator-only affordance per its own code comments.

### Toggle Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --text-base
- **built-from**: Toggle Switch
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.tog-row`, used 5× across Config sections. Gap hardcoded 12px.

### Theme Picker
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: dark option, light option
- **tokens**: --radius-lg, --text-2, --text-base, --space-2, --space-4, --accent, --accent-soft, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.theme-pick`/`.theme-opt`. Swatch previews are deliberately hardcoded hex gradients per a code comment — they must show both themes' literal accents regardless of which theme is currently active, so they intentionally cannot read from `var(--accent)`.

### Config Nav Item
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: default, active
- **tokens**: --space-2, --space-3, --radius-md, --text-2, --text-base, --accent-soft, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.cfg-nav-item`, 9 instances form the Config sidebar.

### Attention List Item
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: warn icon, ia icon, accent icon
- **tokens**: --space-3, --radius-md, --line, --text-base, --text-xs, --text-3, --accent, --warn, --ia
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.att`, 5 instances in "What needs you now."

### Activity Feed Item
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: ok, send, ia, warn
- **tokens**: --text-sm, --text-2, --text, --text-xs, --text-3, --ok, --accent, --ia, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.feed-item`. Rule/dot geometry fully hardcoded.

### Compact Expert Line
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: normal, over-capacity
- **tokens**: --text-sm, --text-xs, --text-3, --radius-xs, --ok, --ia, --warn
- **built-from**: Person Avatar, Progress Bar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.exp-line`, dashboard sidebar "Experts" card (3 instances).

### Expert Editor Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3, --line, --radius-lg, --text-base, --text-xs, --text-3, --radius-sm, --warn
- **built-from**: Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.exp-edit-row`, Config → Team & experts. Delete is blocked with a Toast if the expert still has assigned requirements. Dead CSS nearby (`.team-mgr-group`/`.team-mgr-head`/`.team-roster`) has no matching markup — leftover from before the Team-screen redesign replaced it with Cast Person Row.

### Add Expert Form
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-2
- **built-from**: Text Input, Primary Button
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.add-exp`, single instance.

### Bottleneck Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: normal, aged/warn
- **tokens**: --space-3, --radius-sm, --font-mono, --text-xs, --text-3, --text-sm, --text-2, --radius-pill, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.bn-row`, grid columns hardcoded.

### Q&A Blocked Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-2, --radius-sm, --font-mono, --text-xs, --text-3, --text-sm, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.qa-blocked-row`, Statistics panel.

### AI Reliability Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3, --space-2, --text-sm, --text-2, --radius-xs, --accent, --text-xs, --text-3
- **built-from**: Progress Bar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.ai-rel-row`, grid columns hardcoded.

### Stat Block
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: default, full-width
- **tokens**: --radius-lg, --space-4, --text-sm, --text-xs, --text-3
- **built-from**: none (hosts whichever content it wraps)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.stat-block`, generic heading+subtitle+content card, 9 instances in the Statistics panel.

### AI Pattern Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3, --line, --radius-lg, --radius-md, --text-sm, --font-mono, --text-base, --text-xs, --text-3, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.pat`, AI Feedback "Recurring patterns" row (4 instances). Relies on untracked `--ia-soft`.

### Live Feedback Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3, --space-2, --line, --text-sm, --radius-sm, --text-xs, --text-2, --ia
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.fb-live-row`, populated dynamically from `window.parent.getAIFeedback()`.

### Compliance Bar
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: static (dashboard sidebar), dynamic (Statistics panel, ×2)
- **tokens**: --radius-md, --space-2, --text-sm, --text-2, --radius-xs
- **built-from**: Status Dot (legend variant)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.comp-bar`/`.comp-legend`. Bar height hardcoded 24px.

### Phase Card
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: step (primary rail), support (secondary rail); active-phase, done-phase, is-current states
- **tokens**: --space-3, --panel, --line, --radius-lg, --space-4, --accent, --accent-soft, --radius-md, --text-3, --text-base, --text-lg, --text-sm, --text-2, --text-xl, --radius-xs, --ok, --text-xs, --radius-pill
- **built-from**: Status Pill, Progress Bar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.phase`. A source comment explicitly calls this "the same molecule" reused for both rails — confirmed intentional componentization, one of the few in the codebase. `.is-current` uses `color-mix()` rather than a plain token. Absolute badge/button offsets and min-height (96px) hardcoded.

### Cast Coverage Card
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: complete, unstaffed, partial
- **tokens**: --line, --radius-md, --space-3, --panel, --font-mono, --text-xs, --text-2, --text-sm, --warn, --ok
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.cast-cov-card`, one per activity (7 instances). Complete/unstaffed border colors hardcoded rgba rather than derived from `--ok`/`--warn`.

### Cast Perimeter Group
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: staffed, unstaffed, collapsed
- **tokens**: --line, --radius-md, --space-2, --space-3, --text-sm, --text-xs, --warn, --text-3
- **built-from**: Cast Person Row, Disclosure / Expand Chevron
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.cast-perim`. Unstaffed border hardcoded rgba.

### Add-Person Flow
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: activity/perimeter flow (2-step: search then assign), PM-team flow (1-step: search only)
- **tokens**: --accent-soft, --accent, --space-3, --radius-md, --text-sm
- **built-from**: Search-to-Add Combobox, Text Input
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.cast-add-flow`, driven by `bindCastAddFlow`/`bindPMAddFlow`. Its confirm button (`.cast-add-confirm`) duplicates Primary Button's exact styling under a separate class instead of reusing it.

## Organisms

### App Header
- **level**: organism
- **file**: accueil.html, creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: home (logo + reset + primary CTA + avatar), wizard (logo + static crumb + cancel), workspace (logo-link + crumb + nav/icon buttons + avatar), review (adds mode-switch, version pill), compliance (adds Demo Role Switcher, Icon Cluster, Export)
- **tokens**: --space-4, --space-5, --panel, --line
- **built-from**: Primary Button, Ghost Button, Icon Button, Nav Button, Demo / Prototype-Only Control, Header Avatar, Breadcrumb, Tab Bar / Segmented Control, Notification Dot
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Fixed 52px height, consistently hardcoded across every screen (the app's one real cross-screen consistency win). Horizontal padding still drifts (`--space-5` in accueil.html vs `--space-4` elsewhere). Every screen re-embeds the same base64 SVG logo (light+dark variants) inline rather than sharing one asset.

### Triage Bar
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: with/without "pending reassignment" pill
- **tokens**: --space-1, --space-3, --space-4, --radius-pill, --warn, --ia, --human, --ok, --accent, --font-mono
- **built-from**: Progress Bar, Filter Pill / status-count pills, Tab Bar, Ghost Button, Kbd Key
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.triage`, fixed 42–44px height. Both screens independently implement their own `.tpill` rather than sharing one, despite driving the same five/six-state status vocabulary as Status Pill.

### Left Navigator Panel
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: "By section" (Nav Tree Item groups), "By expert" (Expert Card list, compliance.html only), expanded/collapsed (hardcoded 22px rail)
- **tokens**: --space-1, --space-2, --space-3, --line, --panel
- **built-from**: Search Box, Nav Tree Section Header, Nav Tree Item, Expert Card, Panel Toggle Chevron
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.nav`. Fixed width (264px) hardcoded. revue-documentaire.html starts fully collapsed by design — a code comment notes real capture data "runs to dozens of sections" and a wide-open tree was unusable at that scale.

### Requirement Table (Review Grid)
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: document-order, sorted, grouped-by-activity, filtered-to-selection, wrap-text, scale-test (revue-documentaire.html — 12,000-row virtualized mode)
- **tokens**: --space-3, --space-5, --radius-lg, --line, --panel, --accent-soft
- **built-from**: Requirement Row, Branch / Allocated-Activity Sub-row, Grid Section / Group Header, Filter Toolbar, Bulk Selection Action Bar, Checkbox
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.rgrid`. Explicitly documented in both screens as the same interaction engine (`table-engine.js`) — per-column sort/filter, drag-select across the selection gutter, keyboard active-cell navigation — with only column config differing per screen. `--rgrid-cols`/`--frgrid-cols` widths are hardcoded px/fr values.

### Document Reading View
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: single document, filtered by document, redacted (restricted view), change-annotated (Compare mode, revue-documentaire.html only)
- **tokens**: --space-6, --space-8, --paper, --paper-ink, --font-doc, --text-base, --text-xl
- **built-from**: Document Block, Status Dot
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.doc-scroll`/`.paper`. Deliberately a fixed light "page" regardless of app theme (`--paper`/`--paper-ink` are identical in both theme blocks). Width, padding, and box-shadow all hardcoded.

### Detail / Assignment Panel
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: empty state, requirement (multi-tab), text-block/heading (reduced fields), multi-allocation admin view, multi-allocation manager view (own branch only)
- **tokens**: --space-3, --space-4, --line, --accent, --panel
- **built-from**: Detail Field / Frozen Field, Status/Verdict Pill, Manager Assignment Card, AI Suggestion Card, Allocated-Activity Detail Card, Propose/Reassign Form / Inline Form Shell, Activity Timeline Entry / Timeline Item, REX Match Item, Role Recap Row, Comment Composer
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.settings`. Fixed width (326px in revue-documentaire.html), narrows under a hardcoded breakpoint. The single largest, most role-branching render path in the app — output differs substantially by viewer role, block type, and branch count. compliance.html's version has an unbuilt Chat tab, present only as an empty-state stub per its own code comment.

### Role Recap Card
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-2, --space-3, --radius-lg, --line, --panel
- **built-from**: Role Recap Row
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.role-recap`, fixed 3-row (Admin/Manager/Expert) summary atop the Activity tab.

### Filter Panel
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-2, --space-3, --radius-lg
- **built-from**: Column Filter Section, Segmented Control, Select Dropdown
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.view-panel#filter-panel`, fixed width 300px. Also hosts the "load 12,000 synthetic rows" scale-test control and the entry point into Advanced Filter Builder.

### Advanced Filter Builder
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: empty, flat conditions, grouped (nested AND/OR), with saved filters
- **tokens**: --space-2, --space-3, --radius-lg, --radius-md
- **built-from**: Advanced Filter Condition Row, Mini/Ghost Button
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.adv-panel`, wider than Filter Panel (460px, documented in a CSS comment as needed for "field + operator + value in one row"). Draft/apply pattern edits a scratch object that only commits on Apply. Saved-filter persistence via `table-engine.js` (`TE.loadSavedFilters`/`saveSavedFilters`).

### Columns Panel
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-3
- **built-from**: Reorderable Column Row
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.view-panel#cols-panel`, reuses the Filter Panel's `.view-panel` shell with a single section.

### Export Panel (header ad-hoc export)
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-2, --space-3, --space-4, --radius-sm, --radius-lg
- **built-from**: Select Dropdown, Checkbox, Primary Button
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.export-panel`, from the header's "Export ▾" — a lightweight document/steps/format export, distinct from the milestone Finalize/Export Modal below.

### Bulk Selection Action Bar
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: hidden, visible with N selected
- **tokens**: --space-2, --space-3, --radius-lg, --radius-md, --ok
- **built-from**: Select Dropdown, menu options
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.sel-bar`, explicitly documented as shared between these two screens' tables. Fixed to viewport bottom (24px) — a code comment explains centering via `margin-inline:auto` was chosen deliberately over `left:50%;translateX(-50%)` to avoid capping width at half the viewport.

### Finalize / Export Modal
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none (blocked with a Toast if requirements aren't fully allocated)
- **tokens**: --space-4, --space-5, --radius-lg, --ok, --line, --panel
- **built-from**: Export Option Card, Primary Button, Ghost Button
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.overlay`/`.modal`, fixed width 480px — the generic Modal shell, worth tracking as reusable layout even with one instance here. See Modal Dialog (documents.html) for the sibling shell used elsewhere.

### Modal Dialog
- **level**: organism
- **file**: documents.html
- **variants**: remove-confirmation, per-document export
- **tokens**: --panel, --radius-lg, --space-5, --text-lg, --text-sm, --text-2, --space-2, --space-3
- **built-from**: Warning / Notice Box, Modal Field Group, Cancel Button, Danger Button, Primary Button
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.modal-back`/`.modal`. A code comment explicitly documents this shell as shared between its two use cases — the clearest example in the codebase of a component built with reuse as an explicit goal, though it's a separate implementation from revue-documentaire.html's Finalize/Export Modal shell.

### Notifications Dropdown
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-3, --space-4, --radius-lg, --line
- **built-from**: Notification Item
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.notif-drop`, positioned with hardcoded absolute offsets tied to the current header layout rather than anchored to its trigger button.

### Compare Bar
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-3, --space-4
- **built-from**: Select Dropdown, Compare Summary Chip
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.compare-bar`, Compare mode only. Includes change navigation (Change 1/3, ‹ ›) through `changesOrder`.

### AI Feedback Panel (Why Box)
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-4, --radius-lg, --ia, --accent, --text-sm
- **built-from**: Text Input
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.why-box`, a floating fixed-position card appearing only on high-confidence AI overrides, to solicit a training-feedback reason. Auto-dismisses after a hardcoded 14000ms.

### View-As Switcher
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: admin, restricted (orange tint), open
- **tokens**: --space-2, --radius-md, --ia
- **built-from**: Icon Button, Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.viewas`/`.viewas-menu` + the page-wide `.restrict-banner` it toggles. Demo-only "preview a manager's restricted view" — drives redaction in the Document Reading View and filtering elsewhere.

### AI Feedback Panel (Config)
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3, --line, --radius-lg, --space-4, --text-sm, --text-2, --ok
- **built-from**: Stat Tile / Card, AI Pattern Row, Live Feedback Row
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.fb-accept` + `.fb-block`s + `.fb-status` banner. The status dot's glow (`box-shadow` built from `--ok-soft`) is the only shadow in the codebase built from a token rather than a raw rgba value.

### Tender Dashboard Grid
- **level**: organism
- **file**: accueil.html
- **variants**: filtered by tab
- **tokens**: --space-5, --space-6, --space-8
- **built-from**: Tab Bar, Tender Card, Empty State Message
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Grid `minmax(330px,1fr)` hardcoded.

### Tender Card
- **level**: molecule
- **file**: accueil.html
- **variants**: default, processing, submitted
- **tokens**: --panel, --line, --radius-lg, --space-3, --space-4, --accent
- **built-from**: Status Badge / Chip, Progress Bar, Status Dot, Deadline Chip
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `min-height:172px` and hover `translateY(-2px)` hardcoded. Listed at molecule level (assembles several atoms into one repeatable card) even though it sits inside the Tender Dashboard Grid organism above.

### Wizard Stepper Panel
- **level**: organism
- **file**: creation-projet.html
- **variants**: none
- **tokens**: --panel, --line, --space-5, --space-6, --text-base, --text-sm, --text-3
- **built-from**: Wizard Step Item
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Fixed sidebar width (270px) hardcoded.

### Processing Overlay
- **level**: organism
- **file**: creation-projet.html
- **variants**: none
- **tokens**: --radius-lg, --space-6, --text-lg, --text-sm, --text-3, --text-2, --font-mono
- **built-from**: Progress Bar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Backdrop blur and box-shadow both hardcoded — no elevation/overlay token exists anywhere in the codebase, so every overlay/modal/dropdown hand-picks its own shadow value independently.

### Project Management Team Section
- **level**: organism
- **file**: creation-projet.html
- **variants**: none
- **tokens**: none beyond its constituent molecules
- **built-from**: Team Member Row, Search-to-Add Combobox, Key-Value Summary Row
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Wizard Step 4 — a code comment notes it deliberately replaces a larger, removed "casting" step.

### Document Table
- **level**: organism
- **file**: documents.html
- **variants**: filtered, expanded row (Version History Entry list), processing row (inline progress strip)
- **tokens**: --panel, --line, --radius-lg, --space-2, --space-3, --space-4, --text-xs, --text-3, --font-mono
- **built-from**: Status Badge / Chip, Progress Bar, Status Dot, Version History Entry, Filter Toolbar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Column widths hardcoded via a local `--doc-cols` custom property. Action buttons hidden until row hover/focus — a density optimization noted in-code for scaling to ~30 documents.

### Document Summary Strip
- **level**: organism
- **file**: documents.html
- **variants**: none
- **tokens**: --space-3, --space-5
- **built-from**: Stat Tile / Card
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Four Stat Tiles in a wrapping flex row; two conditionally apply the warn variant.

### Q&A Dossier Import Box
- **level**: organism
- **file**: qa.html
- **variants**: file-upload mode, paste mode, extracting state
- **tokens**: --radius-lg, --space-3, --space-4
- **built-from**: Spinner, Textarea, Primary Button, Tab Bar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.qa-upload`. Simulates an LLM extraction step via a 900ms `setTimeout`, per its own code comment.

### Arbitration Queue Card
- **level**: organism
- **file**: qa.html
- **variants**: active item, empty/done state
- **tokens**: --panel, --line, --radius-lg, --space-3, --space-4, --space-5, --accent, --text-lg
- **built-from**: Progress Bar, Arbitration Guess Button, Kbd Key, Activity / Requirement Tag
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.arb-card`. A code comment calls this "the interaction that decides whether this screen works at volume" — one item, full context, decide, auto-advance, fully keyboard-operable.

### Verdict Entry Form
- **level**: organism
- **file**: compliance.html
- **variants**: Compliant (with comment), Not compliant (with placeholder category + topic)
- **tokens**: --ok, --warn, --radius-md, --space-2, --space-4, --text-sm
- **built-from**: Inline Form Shell, Detail Field, Textarea, Select Dropdown
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Two-way toggle — a code comment notes a prior three-way ("R&D Needed") version was demoted to free text on merge from a removed screen. Category list is an explicit placeholder.

### Reassignment Request Form
- **level**: organism
- **file**: compliance.html
- **variants**: contributor-initiated (radio reasons + conditional picker), manager-handling (reallocate-to form)
- **tokens**: --warn, --radius-md, --space-2, --space-3, --text-sm
- **built-from**: Inline Form Shell, Detail Field, Select Dropdown, Textarea
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Reuses Inline Form Shell for two distinct flows depending on context.

### Activity Timeline
- **level**: organism
- **file**: compliance.html
- **variants**: none
- **tokens**: --text-3
- **built-from**: Timeline Item
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.timeline`, shown only in the Detail Panel's Activity tab.

### Global Header Bar
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-4, --panel, --line
- **built-from**: Breadcrumb, Nav Button, Demo / Prototype-Only Control, Ghost Button, Icon Button, Notification Dot, Header Avatar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Same App Header pattern as every other screen — kept as a separate entry here only because the dashboard scan named it distinctly; see App Header (above) for the merged cross-screen record.

### Phase Rail
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-5, --text-3, --text-lg
- **built-from**: Phase Card (step variant)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.phase-rail`, 2-column grid with a hardcoded `→` connector glyph.

### Support Rail
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3
- **built-from**: Phase Card (support variant)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.support-rail`, 3-column grid (2-column below a hardcoded 1000px breakpoint), hosts Team casting / Documents / Q&A cards.

### Dashboard Attention Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: none beyond its parts
- **built-from**: Count Badge, Attention List Item
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.att-card` ("What needs you now"), 5 items conditionally gated by phase.

### Project Health Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: none beyond its parts
- **built-from**: Stat Tile / Card (Health Stat Tile variant)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.health-stats` grid, gap hardcoded 14px.

### Compliance Summary Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: none beyond its parts
- **built-from**: Compliance Bar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Gated to phase 2, dashboard sidebar.

### Experts Summary Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: none beyond its parts
- **built-from**: Compact Expert Line
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Gated to phase 2, dashboard sidebar.

### Activity Feed Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: none beyond its parts
- **built-from**: Activity Feed Item
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: "Recent activity" card, 5 seeded items, 2 gated behind a phase flag.

### Statistics Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: "For you" tab, "For stakeholders" tab
- **tokens**: --space-4
- **built-from**: Tab Bar, Stat Block, Bottleneck Row, Q&A Blocked Row, AI Reliability Row, Compliance Bar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.stats-panel`. Also embeds a hand-rolled inline SVG trajectory-to-deadline line chart, drawn with hardcoded pixel geometry — a one-off visualization, not a reusable chart component.

### Config Sidebar Nav
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-4, --space-3, --panel, --line
- **built-from**: Config Nav Item
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.cfg-nav`, fixed 220px column width hardcoded on the parent grid.

### Config Section
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: General, Team & experts, Workflow & milestones, AI & segmentation, Q&A & submission, Versions, Language, Appearance, AI feedback (9 total)
- **tokens**: --text-lg, --text-base, --text-3, --space-6
- **built-from**: Warning / Notice Box, Config Field Row
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.cfg-sec`, the single most-repeated organism shape in the file. Body max-width capped at a hardcoded 680px.

### Team & Experts Config Editor
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: none beyond its parts
- **built-from**: Expert Editor Row, Add Expert Form, Chip Group, Config Field Row, Segmented Control
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: The "Team & experts" Config Section's body.

### Cast Activity Group
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: staffed, unstaffed, partial, no-manager, read-only, PM-team variant
- **tokens**: --panel, --line, --radius-lg, --space-3, --accent
- **built-from**: Status Pill, Disclosure / Expand Chevron, Cast Perimeter Group, Cast Person Row, Add-Person Flow
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.cast-group`. Encodes real permission logic — only the owning manager or an admin viewer sees the add-flow/remove buttons.

### Team Casting Screen
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: PM overview mode, activity-manager scoped mode
- **tokens**: none beyond its parts
- **built-from**: Search Box, Chip Toggle (unstaffed-filter variant), Demo / Prototype-Only Control, Cast Coverage Card, Cast Activity Group
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `#team-screen`, the full "Team casting" view. Text and available actions change based on simulated viewer identity.

## Removed

_(none yet — this section starts empty as of the 2026-09-01 seed)_
