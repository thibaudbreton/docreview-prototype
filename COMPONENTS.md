# Components

_Maintained alongside the code. Updated in the same commit as any component change._

This inventory was seeded on 2026-09-01 by reading every screen's source HTML/CSS/JS in full (`accueil.html`, `creation-projet.html`, `documents.html`, `qa.html`, `compliance.html`, `dashboard-et-config.html`, `revue-documentaire.html`) — the merged files (`index.html`, `docreview-app.html`) were not read; per `README.md`, sources are always edited, never the merged output. See `CLAUDE.md` for the rules that keep this file current from here on.

**Design tokens actually defined** (both theme blocks, same names, different values): `--bg`, `--panel`, `--line`, `--text`, `--text-2`, `--text-3`, `--accent`, `--accent-soft`, `--ia`, `--ok`, `--human`, `--warn`, `--paper`, `--paper-ink`, `--text-xs/sm/base/lg/xl`, `--space-1` through `--space-8` (4/8/12/16/20/24/32px), `--radius-xs/sm/md/lg/pill`, `--font-ui/doc/mono`, and since 2026-09-22 `--font-heading` and `--brand-red` (decorative only, exact value to confirm). Since 2026-10-06 (DEC-115) the font tokens resolve to the brand's Alstom face, declared once per screen as the `"Alstom UI"` family and metric-matched to Noto Sans, its fallback: `--font-ui` Alstom → Noto Sans; `--font-heading` Antarctica → Alstom → Noto Sans; `--font-mono` Alstom (identifiers and codes — its figures are all one width) → the monospace stack; `--font-doc` stays Georgia, the source document's face. Alstom is embedded only in the local build; the published one shows the fallbacks.

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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): unused copies of the rule removed — risks.html's (the Risks page has no primary button) and compliance.html's `.upload-zone .btn-primary` (no upload zone on that screen). `.btn-primary`, near-identical across all seven screens. Hover uses `--accent-hover` (untracked). Text color hardcoded `#fff`, never a token. Several screens duplicate this exact recipe under their own class instead of reusing it — see Danger Button, Cast Add Confirm (noted under Add-Person Flow).

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

### Icon
- **level**: atom
- **file**: revue-documentaire.html, compliance.html, dashboard-et-config.html, creation-projet.html, accueil.html, documents.html, qa.html
- **variants**: file, lock, bell, camera, trash, copy, eye, clock, hourglass, chat, globe, clip, ask (arrow up-right), keyboard, search, flag, flagfill, fork, merge, upload, download, corner, chevron, filter, columns, and for the settings menu sliders, users, flow, refresh, contrast, sparkle, undo, lang
- **tokens**: currentColor (inherits the text colour); size 1.05em
- **built-from**: none
- **added**: 2026-09-24
- **changed**: 2026-09-24
- **notes**: `<i class=ic-NAME></i>` — an inline SVG (24px grid, 2px stroke, round caps) used as a CSS mask over `currentColor`, so it follows the text colour and size. The markup has no quotes on purpose: it sits inside JS strings of every quoting style. Replaced glyph icons that rendered badly: emoji (📄 🔒 🔔 📷 🗑 🎭 🕐 💬 🌐 📎 ⏳ — coloured Apple emoji) and symbols Noto Sans lacks (⇗ ⌨ ⎘ ⌕ ⚐ ⑂ ◷ ⇲ ⏷ ▤ ▸ ▶ ⤵, and the heavy ⬆ ⬇), plus the whole settings-menu set (◈ ◉ ⇄ ↻ ◐ ✦ ↺ ⇗ ◷ Aa) so it reads as one family. Plain arrows, ✓ ✕ ⚠ ✎ ⚑ (outside Compliance) ↻ ↺ ▾ stay text — they render correctly. CSS (the `i[class^="ic-"]` rule and one `--i` data URI per icon) is duplicated in each of the seven files, before the first `</style>`. Vertical alignment `-.16em` hardcoded.

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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): compliance.html and dashboard-et-config.html had two dots in the bell's markup and only hid the first when nothing is waiting, so the second never went away — one dot now. risks.html's copy of the CSS removed (no bell there). `.badge-dot`, nested inside Icon Button. Hardcoded `8px` circle with hardcoded `2px` border/offset, not on the space scale.

### Nav Button
- **level**: atom
- **file**: documents.html, qa.html, dashboard-et-config.html, risks.html
- **variants**: none
- **tokens**: --space-3, --radius-md, --panel, --text-2, --text-sm, --accent, --accent-soft
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): risks.html's `.nav-btn svg` rule removed — its button carries an icon-font glyph (`<i class=ic-…>`), not an SVG. `.nav-btn` (icon+label "destination" link, e.g. "Documents", "Dashboard"). Each instance carries a code comment explicitly framing it as the deliberate replacement for a plain back-arrow link — an intentional, designed-for-reuse atom despite low instance count per file. Border relies on untracked `--line-2`.

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
- **variants**: sizes 22px/24px/26px/28px/30px/32px/34px depending on context (inline style overrides, not a size scale); empty (dashed circle with "?", nobody cast)
- **tokens**: --text-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (DEC-117): Statistics adds `.st-av` (24px, white initials hardcoded `#fff`) and its `.is-empty` variant (dashed untracked `--line-2` ring, "?") for a system with no manager; the background is the person's own colour from `PM_TEAM`/`MANAGERS`/the casting directory, `--brand-slate` (untracked) for anyone not in them. `.exp-avatar` / `.exp-av` / creation-projet's unnamed person-initials style — same idea (circle, per-person hex background passed inline from JS data, initials text), independently sized per screen with no shared scale. Background color always a literal hex from JS data (`MANAGERS[]`, `EXPERTS`, `PM_COLORS`), never a token.

### Toggle Switch
- **level**: atom
- **file**: creation-projet.html, dashboard-et-config.html, revue-documentaire.html, compliance.html
- **variants**: on, off
- **tokens**: --radius-pill, --accent, --accent-soft
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-24
- **notes**: 2026-09-24: compliance.html gets the same "Wrap text" `.wrap-switch` as Allocation, CSS copied (no shared stylesheet) — full requirement text, comments and risk notes wrap; rows grow. Three independent implementations (`.tog` in dashboard-et-config.html at 40×22px, creation-projet.html's at 38×21px, revue-documentaire.html's bespoke `.wrap-switch` at 30×17px) — same concept, three different hardcoded geometries, none on any scale.

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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): compliance.html's `.progress-track/.progress-fill` (no markup used them) and `.exp-bar` (the removed Expert Card's) are gone; dashboard-et-config.html's support Phase Cards lose their hidden `.ph-bar`. 2026-10-06 (DEC-117): Statistics drops `.ai-rel-bar`, `.pf-bar`, `.load-bar`, `.late-bar` and `.cons-bar` and adds five pill-ended ones of its own — `.lb-bar` (segmented: allocation / answers / comments), `.sys-bar` (two segments: allocated / to validate), `.ppl-bar`, `.ta-bar` and `.ra-why .bar`, 6–8px — again each its own class. 2026-10-06: accueil.html's `.pc-bar` and `.mini-bar` left with the Tender Card's old gauge. The single most-duplicated primitive in the app — at least a dozen independent class implementations across the seven screens (`.pbar`, `.doc-wbar`, `.doc-prog`, `.ph-bar`, `.exp-lbar`, `.fbar`, `.progress-track/.progress-fill`, `.exp-bar`, `.arb-progress .bar`), all sharing "colored track + fill" but each with its own hardcoded height and no shared height scale. Track background is consistently the untracked `--panel-3`. A strong candidate for the first real consolidation pass.

### Status Dot
- **level**: atom
- **file**: accueil.html, documents.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: pulsing (processing badge), health dot (on_track/at_risk/behind), state dot, notification dot, legend dot (dashboard-et-config.html, compliance-color-coded)
- **tokens**: --ok, --ia, --warn, --accent, --text-3
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): compliance.html's verdict dot (`.vdot`) follows the two verdicts — compliant, not_compliant (`--warn`), none (pending). It only had colours for the retired scale (`partial`, `non`, `needs-clar`) and `.vdot` has no background of its own, so a Not compliant requirement's dot didn't show; the Document view's legend reads Compliant / Not compliant / Pending. Independently hardcoded diameter per instance (5px–9px seen), no shared size token. "None/pending" states rely on untracked `--line-2`.

### Count Badge
- **level**: atom
- **file**: qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: `.qa-views .n`, `.view-badge`, `.tab-count`, `.nh-c`, `.rex-count`, `.count` (dashboard "5" pill)
- **tokens**: --text-xs, --radius-lg, --radius-md, --accent, --accent-soft, --warn, --warn-soft (untracked)
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): `.mcount` is gone — it was never drawn: the `.mode-switch` copies of qa.html, documents.html and risks.html were unused, and compliance.html's switch has no count. 2026-10-06 (DEC-116): qa.html's `.tcount` (on the Answers tab) is now the count inside each view of the Q&A View Switch. Hardcoded vertical padding (1–3px) across every variant instead of a space token.

### Block Badge
- **level**: atom
- **file**: revue-documentaire.html
- **variants**: default (comment count), branch count, blocking, container count ("N requirements captured", on an image block)
- **tokens**: --font-ui, --text-xs, --text-2, --space-1, --space-2, --radius-lg, --accent, --accent-soft, --warn, --human
- **built-from**: Icon
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: `.cbadge` — missed by the 2026-09-01 inventory, entered when next changed. The small pills beside a requirement in the review table and on document blocks. 2026-10-06: sets `--font-ui` itself — on an image block it sits on the document's paper and was inheriting Georgia, the source document's face, unlike the type chip beside it. Vertical padding hardcoded at 2px; default background is the untracked `--panel-3`, and the variants use the untracked `--warn-soft` / `--human-soft`.

### Activity / Requirement Tag
- **level**: atom
- **file**: qa.html, compliance.html, revue-documentaire.html
- **variants**: default, `.tky` (turnkey, filled), `.partner` (a system added for the tender, not from the model — teal, revue-documentaire.html and compliance.html), `.proposed` (pending PM review), `.ptag-more` ("+N" overflow count, dashed — takes `.proposed` when a hidden system is a pending change)
- **tokens**: --font-mono, --text-xs, --ia, --human, --radius-xs, --space-1, --text-2
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the `.ai` variant (dashed, AI-unconfirmed) and the `.perim` wrapper are removed with `perimHTML()`, which nothing called. 2026-09-24 (DEC-082): `.partner` uses `--partner` / `--partner-soft` (`#1b9aaa`), a custom property added for it and **not on the tracked token scale** — `--human` (violet) was taken by `.proposed`. Set through `ptagCls(id)` in both screens (returns " tky", " partner" or ""), with a hover tooltip saying it was added for this tender and isn't part of the model. `.ptag` / `.qa-req` / `.c-id`. Turnkey variant uses a fully hardcoded gray (`#7b8794`), not a token. Letter-spacing (0.6px) hardcoded. Border relies on untracked `--line-2`. In Allocation's System cell (2026-09-23, `typoTagsHTML()`): one line only — as many tags as fit, then "+N" naming the rest on hover; every tag shows in "Wrap text" mode. The fit is estimated from code length (10 + 7.2px per letter, measured on the monospace tags) against the column's actual width minus 34px of padding (`typoCellBudget()` — the 136px default or whatever the user dragged it to), and the System cells re-render when that column is resized. On Turnkey (DEC-077, 2026-09-23) the System cell also carries the routing confidence beside the tag (`.sys-conf`, `--text-xs`/`--text-3`, `--ia` bold below threshold): on a single-system row and on each system's branch row, never on a multi-system parent (the "+N" budget is unchanged). It replaces the "TK OBS" column, which repeated the system; `margin-left:5px` hardcoded.

### Status Badge / Chip
- **level**: atom
- **file**: documents.html, creation-projet.html
- **variants**: `.pstate` (ready/running/queued), `.gap-chip` (a/m/r), `.tagrec` (recommended)
- **tokens**: --text-xs, --space-1, --space-2, --radius-pill, --radius-lg, --accent, --accent-soft, --ia, --ok, --warn, --human
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06: accueil.html's `.pc-badge` stage pill left the Tender Card (the tender's line carries the stage). 2026-09-24: documents.html's `.pstate` lost its leading 5px dot, like the other status pills. Same "soft background + bold colored text" grammar reimplemented under four unrelated class names with inconsistent radius (`--radius-pill` vs `--radius-lg` for what reads as the same pill). Backgrounds rely on untracked `--ia-soft`/`--ok-soft`/`--warn-soft`/`--human-soft`. Sibling family: Status Pill (below), which reimplements the same idea again in three more screens.

### Status Pill (Requirement Workflow State)
- **level**: atom
- **file**: revue-documentaire.html, dashboard-et-config.html
- **variants**: s-incomplete, s-reassign, s-doubt, s-tovalidate, s-allocated, s-changed (revue-documentaire.html); current/done/wait, staffed/unstaffed/partial/noperm (dashboard-et-config.html's `.ph-badge`/`.cast-group-badge`)
- **tokens**: --space-1, --space-2, --radius-xs, --radius-pill, --text-xs, --warn, --ia, --human, --ok, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-29
- **notes**: 2026-09-29 (DEC-103/104): `s-reassign` "Reassignment requested" (untracked --human-soft/--human — the Turnkey level while a reassignment waits). On a Turnkey tender the row pill is the Turnkey-level status for the PM and the contributor's own system status for a contributor; the PM's system sub-rows show no status. 2026-09-24: revue-documentaire.html's `.status-pill` lost its leading 6px dot, like Compliance's `.spill` and Documents' `.pstate`. Backgrounds use the untracked `--warn-soft`/`--ia-soft`/`--human-soft`/`--ok-soft`/`--accent-soft` family (only `--accent-soft` is an actual tracked token). Sibling of Status Badge / Chip (above) and Verdict/Progress Status Chip (below) — three independent codings of "small colored status label" across the app, none sharing a base class. Requirements only since 2026-09-23 (DEC-073): a heading or an information block never shows one — not in its table row, its panel header, the document view or the navigation dot.

### Verdict Pill
- **level**: atom
- **file**: compliance.html
- **variants**: compliant, not_compliant, none, pending (dashed/italic — deliberate, so an unresolved verdict can never read as decided), external pending (`.vpill.pending`, filled grey), corrected (`.vpill.corrected`, outlined + ✎)
- **tokens**: --space-1, --space-2, --radius-sm, --text-xs, --ok, --warn, --text-2, --text-3
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the unused inherited look (`.vpill.inherited`, dashed) is removed from the CSS. 2026-09-30 (DEC-106): external compliance has three values — Compliant / Not compliant / Pending (a gap strategy's result, or no strategy yet) — rendered by `extPillHTML()`; a value the PM corrected carries ✎ and an outline. The old inherited/dashed external look is unused now that nothing is declared. Pending uses the untracked `--panel-3`. `.vpill`. Sibling of Status Pill / Status Badge — same visual grammar, own class.

### Risk Chip
- **level**: atom
- **file**: compliance.html
- **variants**: none
- **tokens**: --font-mono, --text-xs, --radius-xs, --human, --human-soft
- **built-from**: none
- **added**: 2026-09-30
- **changed**: 2026-09-30
- **notes**: `.risk-chip` — a risk's `RSK-` ID, in the table's Risk column and the Gap Editor; a button that opens the risk in risks.html. `--human-soft` is untracked. The closed variant went with DEC-113 (no status). Sibling: `.gap-miss` ("Strategy missing" / "Risk missing"), a dashed `--warn` flag used in the same cells.

### Progress Status Chip
- **level**: atom
- **file**: compliance.html
- **variants**: proposed/assigned, awaiting_answer, awaiting_qa, reassignment_needed, answered
- **tokens**: --space-1, --space-2, --radius-pill, --text-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-24
- **notes**: `.spill`. No leading dot since 2026-09-24 (it was a hardcoded 6px `currentColor` circle) — the colour carries the state. Backgrounds rely on untracked `--panel-3`/`--ok-soft`/`--warn-soft`.

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
- **file**: documents.html, dashboard-et-config.html, revue-documentaire.html, compliance.html
- **variants**: collapsed, expanded (rotated)
- **tokens**: --text-3, --text-xs, --radius-sm
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-24
- **notes**: 2026-09-24: Allocation's `.branch-caret` now sits in the Requirement cell before the text, as on Compliance (it was beside the ID); `margin-right` dropped, the cell's gap spaces it. Row/group-level expand affordance — `▶` glyph in documents.html (9px, no tokens at all), `.cast-caret` (▾) in dashboard-et-config.html, `.branch-caret` in revue-documentaire.html (has real button chrome, hardcoded 20×20px). Distinct from Panel Toggle Chevron (below), which collapses whole side panels rather than a row.

### Panel Toggle Chevron
- **level**: atom
- **file**: compliance.html, revue-documentaire.html
- **variants**: nav collapse, detail-panel collapse
- **tokens**: --radius-sm, --text-3, --text-xs, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-23
- **notes**: `.panel-toggle`. A code comment in compliance.html states this is deliberately "the same pattern as revue-documentaire.html." Hardcoded 20px size. The detail-panel variant is absolutely positioned at left:6px and sat on top of the requirement id; since 2026-09-23 `.set-id-row` carries `padding-left:18px` on both screens to clear it — a hardcoded offset tied to this button's size, not a space token.

### Kbd Key
- **level**: atom
- **file**: compliance.html, revue-documentaire.html
- **variants**: real `<kbd>` element (compliance.html, revue-documentaire.html)
- **tokens**: --font-mono, --text-xs, --radius-xs, --space-1
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (DEC-116): qa.html's `.kb` squares left with the arbitration queue. 2026-09-24 (later): the shortcuts are listed again, on demand — see Shortcut Help. 2026-09-24: compliance.html no longer displays any shortcut hint (the triage bar's J/K · R · Q strip and the `<kbd>` in the Escalate and Reminder buttons are gone); the shortcuts themselves still work. Same "keyboard shortcut hint" concept, two different markup strategies. qa.html's version is a fixed 20×20px square. Borders/backgrounds rely on untracked `--line-2`/`--panel-2`/`--panel-3`.

### Spinner
- **level**: atom
- **file**: qa.html
- **variants**: none
- **tokens**: --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (DEC-116): now inside the "Import the client's answers" button while the simulated import runs. `.qa-spin`, shown during the simulated dossier-extraction wait. Hardcoded 13px size, 0.7s duration; border relies on untracked `--line-2`.

### Match Ring
- **level**: atom
- **file**: compliance.html, revue-documentaire.html
- **variants**: none
- **tokens**: --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.rex-ring`, a `conic-gradient` donut for REX match-percentage, driven by an inline `--p` variable. Entirely hardcoded geometry (22–26px, mask radius, gradient stops) — no tokens beyond the fill color.

### Brand Logo
- **level**: atom
- **file**: accueil.html, creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html, risks.html
- **variants**: light theme (the company's colour logo), dark theme (its white logo) — two `<img>` toggled by `html[data-theme]`
- **tokens**: --space-4, --line
- **built-from**: none
- **added**: 2026-10-09
- **changed**: 2026-10-09
- **notes**: `.brand-logo`, first thing in every header: the Alstom logo, a 1px `--line` rule, then the product's name "SRM" in text (the App Header's `.logo`) — the company's logo is required; the SRM mark beside it was one symbol too many. The files supplied, cropped to the ink and reduced (PNG, 72px high, ~3 KB each), inlined as data URIs in each screen — colours are the logo's own, not tokens. Height 15px (cap line of "SRM") and box 20px hardcoded. Also in the published build (user's choice, 2026-10-09).

### Page Title
- **level**: atom
- **file**: every screen (`h1`, `h2`), plus `.cfg-h`, `.set-title`, `.view-panel-head`, `.fb-bh` as section titles
- **variants**: page (h1/h2, carries the red mark), section (h3 and the class-based titles, no mark), in the status bar (`.tri-title`, Allocation and Compliance)
- **tokens**: --font-heading, --brand-red (h1/h2 mark only), --text-lg / --text-xl where sized
- **built-from**: none
- **added**: 2026-09-22
- **changed**: 2026-10-06
- **notes**: 2026-10-06: on Allocation and Compliance the title no longer owns a row (`.review-head` / `.view-head` removed, 38px of table height at 1280×600 — 7 rows visible instead of 6): it opens the Triage Bar, followed by a 1px `.tri-sep` (hardcoded 20px high). Their subtitles went with it — Allocation's guidance is the title's tooltip; the shown count is `.shown-count` in the toolbar, only while a filter narrows the list; Compliance's "pending consolidation" repeated the bar's "consolidated", its assignment total is now in the bar. The other screens keep their title row. The red mark is a `::before` inline-block so it survives flex and block title containers alike; its height is `.85em`, deliberately relative rather than on the space scale. Red is never applied to interactive or stateful elements — see `--warn`.

### Custom Column Tag
- **level**: atom
- **file**: revue-documentaire.html, compliance.html
- **variants**: none
- **tokens**: --text-3, --line-2, --radius-pill
- **built-from**: none
- **added**: 2026-09-23
- **changed**: 2026-09-24
- **notes**: 2026-09-24: also marks custom columns as "internal" in compliance.html's export column list. `.cf-tag`, the small "custom" pill beside a custom column's name in the View menu's column list. Font size hardcoded 10px, off the type scale. Depends on untracked `--line-2`.

### Paragraph Reference
- **level**: atom
- **file**: revue-documentaire.html
- **variants**: section only (no sub-heading above the requirement), sub-heading (deepest heading wins, full path in the tooltip)
- **tokens**: --text-xs, --text-3, --text-2, --font-mono, --accent
- **built-from**: none
- **added**: 2026-09-23
- **changed**: 2026-09-23
- **notes**: `.set-para`, "§ 2.2.1 Brief Description" under the id in the detail panel header; resolved by `paragraphOf()`. Clicking opens the Document view on the block, same as "View in document". Allocation only: Compliance's requirements carry their top-level section and nothing deeper, so there is no paragraph to show there yet.

### Column Resize Handle
- **level**: atom
- **file**: table-engine.js (behaviour, `TE.bindColumnResize`), revue-documentaire.html and compliance.html (CSS `.col-resize`, host wiring)
- **variants**: idle (invisible), header hover (1px line), hover/focus/dragging (2px accent line)
- **tokens**: --line-2, --accent
- **built-from**: none
- **added**: 2026-09-23
- **changed**: 2026-09-23
- **notes**: A 7px zone straddling the right edge of every header cell except the selection gutter. Drag, double-click to reset, or focus and ←/→ in 16px steps (role="separator"). Widths are px overrides per tender and per table, held in the shell (`getTableLayout`), cleared by Reset demo and by "Reset column widths" in View. Minimums: 56px, ID 64px, Requirement 200px (180 on Compliance) — hardcoded. Depends on untracked `--line-2`. Handle geometry (7px, right:-3px, 8px inset) hardcoded.

### Word Diff
- **level**: atom
- **file**: revue-documentaire.html
- **variants**: deleted (`.diff-del`, struck through), inserted (`.diff-ins`)
- **tokens**: --radius-xs
- **built-from**: none
- **added**: 2026-09-23
- **changed**: 2026-10-07
- **notes**: 2026-10-07 (DEC-119): split in two — `wordDiffOps(prev, cur)` returns the kept / removed / added runs and `wordDiffHTML` renders them as before; the Changes Cell renders the same runs its own way (token colours, compact excerpt). `wordDiffHTML(prev, cur)`, a word-level LCS diff computed at render time — the current text no longer carries diff markup inside it. Used in the Document view's Changes (document blocks — Compare until 2026-10-07) and in the Versions tab. Colours hardcoded (`#f6d5d2`/`#8c2f28`, `#cfe9db`/`#155c3c`), not tokens — same values as the older Compare-mode rules.


### Version Picker Button
- **level**: atom
- **file**: revue-documentaire.html
- **variants**: one requirement (`.chg-ver`, "vs v2.0 ▾" in a Changes Cell), chosen for this requirement (`.own`, accent), quiet (a row with no change, half opacity until hovered or active), all requirements (`.chg-all` in the Changes column header, "vs previous ▾" / "vs first ▾")
- **tokens**: --space-2, --radius-pill, --panel, --text-xs, --text-2, --accent, --accent-soft
- **built-from**: none
- **added**: 2026-10-07
- **changed**: 2026-10-07
- **notes**: DEC-119. Opens the Version Picker Popover. Depends on untracked `--line-2` (border); vertical padding 1px and the quiet opacity (.5) hardcoded. Its title says what the row is compared with (version, date, note).

### Change Type Tag
- **level**: atom
- **file**: revue-documentaire.html
- **variants**: modified (`.chg-tag`, the version(s) the requirement changed in, e.g. "v2.0 · v2.1"), added ("New", "New in v2.0"), same (`.chg-tag.same` — hidden on one line when the column compares with the previous version, the change being in the version in force by definition; shown in Wrap text); in the Changes Navigator `.nc-t` added / modified / removed
- **tokens**: --ia, --ok, --warn, --radius-pill, --text-xs
- **built-from**: none
- **added**: 2026-10-07
- **changed**: 2026-10-07
- **notes**: DEC-119. Depends on untracked `--ia-soft`, `--ok-soft`, `--warn-soft`; padding hardcoded (`0 6px`, `1px 6px`). Known duplication: the same "what kind of change" label exists four times — `.chg-tag` (Changes Cell), `.nc-t` (Change List Card), the paper's `data-chlabel` chip ("Modified in v2.1") and the Versions Tab's `.ver-type` — with the same colour logic written each time.
### Nature Picker
- **level**: atom
- **file**: revue-documentaire.html
- **variants**: default, AI-typed (`.is-ai`, dashed `--ia` border — type detected by the AI, not confirmed), read-only (contributor)
- **tokens**: --text-xs, --radius-sm, --ia, --paper-ink-2
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-08
- **notes**: 2026-10-08 (DEC-120): the AI-typed title gives the characterisation model's level ("…with low confidence") instead of "detected by the AI". 2026-09-28 (DEC-086): disabled for a contributor, in the Document view too (`attachReclassify` leaves it inert with a "Set by the project manager" title). Document view only since 2026-09-23 — the table row's compact "▾" variant (`.row-natpick`, on requirement and information rows) was removed; in the table, nature is corrected in the detail panel's Nature field. `.nat-pick` / `natureTag()`, "Information ▾" beside a block, opens the reclassify menu. Since 2026-09-23 it is where an AI-detected Type shows on headings and information blocks, which no longer carry a status (DEC-073); picking the type the block already has confirms it (it used to do nothing). Background `rgba(0,0,0,.05)` hardcoded.

## Molecules


### Confidence Level Badge
- **level**: atom
- **file**: revue-documentaire.html
- **variants**: high, medium, low (`.weak` — the unconfirmed call that sends a requirement to To review)
- **tokens**: --text-xs, --text-3, --ia, --radius-pill
- **built-from**: none
- **added**: 2026-10-08
- **changed**: 2026-10-08
- **notes**: DEC-120. `.deriv-conf.char-conf`, `charConfBadgeHTML()`: the characterisation model (Nature, Class) gives Low / Medium / High, not a percentage, so its badge is the percentage badge (`.deriv-conf`, `confBadgeHTML()` takes `{level}` as well as `{c}`) with a word in it. Shown only while the value is still the AI's — a person's pick (`dropCharConf()`) carries none. Beside a field label it drops the label's uppercase (`.field>label .char-conf`). Depends on untracked `--panel-3`, `--ia-soft`; padding `1px 6px` hardcoded.
### Shortcut Help
- **level**: molecule
- **file**: revue-documentaire.html, compliance.html
- **variants**: Allocation list (move, select, edit, validate, next, Changes column, undo), Compliance list (move, select, remind, ask the client, set aside, next, undo, custom columns)
- **tokens**: --line-2, --radius-md, --radius-xs, --panel, --panel-2, --text, --text-2, --text-3, --text-sm, --text-xs, --font-mono, --accent, --space-2, --space-3
- **built-from**: Kbd Key
- **added**: 2026-09-24
- **changed**: 2026-10-07
- **notes**: 2026-10-07 (DEC-119): Allocation's list adds C — show / hide the Changes column. 2026-09-24 (DEC-085): lists the new selection keys (X, Shift+↑/↓, ⌘/Ctrl+A, Esc), N and ⌘/Ctrl+Z. `.kbd-help`, a 30px "⌨" at the right end of the filter toolbar; the list (`.kbd-help-pop`, 320px, right-aligned under the icon) opens on hover and on keyboard focus (`:focus-within`, tabindex 0), pure CSS. The rows are written by hand from each screen's keydown handlers — a new shortcut has to be added here too. CSS duplicated in both files. Hardcoded: 30px square, 320px width, 96px key column, shadow `rgba(0,0,0,.25)`. Depends on untracked `--line-2`, `--panel-2`.

### Search Box
- **level**: molecule
- **file**: dashboard-et-config.html, revue-documentaire.html, compliance.html
- **variants**: nav search (full width), toolbar search (fixed 220px), Team-screen search (`.cast-search-wrap`, with leading icon)
- **tokens**: --space-2, --space-3, --radius-md, --accent, --text-base
- **built-from**: Text Input
- **added**: 2026-09-01
- **changed**: 2026-09-24
- **notes**: 2026-09-24: compliance.html's toolbar search is now the same `.search-box` (icon + 220px, CSS copied) — it was a bare input stretching across the toolbar (`flex:1`). There it doesn't shrink (`flex-shrink:0`); Allocation's does, down to ~193px when the toolbar is full. revue-documentaire.html's two instances (`#nav-search`, `#table-search`) are kept in sync via JS. dashboard-et-config.html's icon-offset padding (34px/11px) is hardcoded and relies on untracked `--panel-2`/`--line-2`.

### Filter Toolbar
- **level**: molecule
- **file**: documents.html, qa.html, compliance.html
- **variants**: search + one select (documents.html), qa.html `.qa-bar` (view switch, search, system select on our questions, Export to Excel, Import the client's answers), compliance.html `.f10-tools` (search box, sort reset, Wrap text, Filter, ＋ Column, View, shortcut help)
- **tokens**: --space-2, --space-3
- **built-from**: Text Input, Select Dropdown, Search Box, Toggle Switch, Ghost Button, Shortcut Help
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (DEC-116): qa.html's toolbar carries the view switch and the screen's two actions; the system filter shows on our questions only. 2026-09-24: compliance.html's toolbar now has the same right-hand group as Allocation's — Wrap text, Filter, ＋ Column, View, ⌨ side by side; ＋ Column and View used to sit in the title row. The two sort selects and the Needs my action toggle are gone (DEC-078, DEC-083). Same "filter row" pattern re-implemented per screen. documents.html's input hardcodes `8px` padding instead of `var(--space-2)`; qa.html's hardcodes `7px`.

### Toast
- **level**: molecule
- **file**: accueil.html, creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: ok, warn
- **tokens**: --space-2, --space-3, --space-4, --radius-lg, --text-base, --ok, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): qa.html and documents.html called `toast()` into a `#toast-zone` that had no CSS, so their messages never appeared as toasts; both now carry the same `#toast-zone` / `.toast` rules as the other screens. 2026-09-24 (DEC-085): a toast that offers Undo also pushes onto `UNDO_STACK` (30 max), so ⌘/Ctrl+Z undoes the last one after the toast has gone; the button and the shortcut undo the same entry once. compliance.html's toast gained the Undo button (it had none). `.toast` + shared `toast(msg, kind)` JS helper — verbatim-identical CSS/JS in most screens, but accueil.html colors its "warn" toast with `--ia` (amber) via `.t-warn` while creation-projet.html/documents.html/qa.html/compliance.html/dashboard-et-config.html color the same warn-kind toast with `--warn` (red) via inline style — the same component signals "warning" in two different colors depending on screen. Box-shadow (`rgba(0,0,0,.5)`) and easing are hardcoded everywhere (no shadow/motion token exists in the codebase). Auto-dismiss duration also drifts per file (2600/3200/3400/3600ms).

### Tab Bar
- **level**: molecule
- **file**: accueil.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: underline-active (accueil.html tabs, compliance `.set-tabs`), pill/background-active (`.mode-switch`, dashboard-et-config.html `.stats-tabs`, revue-documentaire.html `.nav-tabs`)
- **tokens**: --space-1, --space-2, --space-4, --space-5, --line, --text-3, --text-2, --text, --accent, --text-base, --text-xs
- **built-from**: none (buttons are plain, not reusing any button atom)
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the unused `.mode-switch` copies in qa.html (the dead code noted below), documents.html and risks.html are removed, and compliance.html's `.nav-toggle` pill — the By section / By contributor switch, gone since 2026-09-24. 2026-10-07 (DEC-119): revue-documentaire.html's `.mode-switch` is Review / Document only — Compare became the navigator's Changes tab, and the switch stays on Document while it is open; the navigator's Outline / Changes tabs (`.nav-tabs`, count pill on Changes) are one more pill implementation, active shadow hardcoded `rgba(0,0,0,.12)`, right margin 34px hardcoded to clear the panel toggle. 2026-10-06 (DEC-116): qa.html's Questions / Answers `.hub-tabs` replaced by the Q&A View Switch. 2026-09-24: the detail panel's `.set-tabs` (revue-documentaire.html and compliance.html) scroll horizontally instead of wrapping or squeezing (`overflow-x:auto`, tabs `flex-shrink:0`/`nowrap`); the per-system tab is labelled "Activity" (was "System") on both screens; compliance.html's "Document" tab is removed. At least four independent implementations of "group of switchable tabs" across the app with two different visual languages and inconsistent hardcoded padding (5–10px). `.mode-switch` CSS exists in qa.html but is never instantiated there — dead code. Active-tab box-shadow hardcoded (`rgba(0,0,0,.15–.4)`) in several variants.

### Segmented Control
- **level**: molecule
- **file**: creation-projet.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: 2-option, 3-option, pill-track (`.gseg`, `.tbl-gran`, revue-documentaire.html)
- **tokens**: --space-1, --radius-md, --radius-sm, --radius-pill, --text-sm, --text-base, --text-2, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): `.screen-nav .sn` (dashboard-et-config.html, revue-documentaire.html) and revue-documentaire.html's copy of `.segc` are removed — no markup used them. `.segc` (dashboard-et-config.html, 8 instances), creation-projet.html's Segmented Choice Group, and revue-documentaire.html's `.gseg`/`.tbl-gran`/`.mode-switch`/`.screen-nav .sn` are five separately-named classes implementing the same "pill-track, active segment gets elevated" pattern with independently hardcoded padding/radius/shadow — the single clearest consolidation candidate in the codebase alongside Progress Bar. Relies on untracked `--panel-2`/`--panel-3`/`--line-2`.

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
- **file**: creation-projet.html, documents.html, qa.html, dashboard-et-config.html
- **variants**: static current segment, clickable project-link segment (documents.html)
- **tokens**: --space-2, --text-2, --text-3, --text, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): qa.html and documents.html name the open tender in the `.project` segment (reference · name, from the shell's current project, as Risks already did) instead of always showing STB-2026; the text in the markup is the fallback when the screen is opened on its own. Same `.crumb` shell reused across files, but the "current segment" styling drifts between `.cur` (static) and `.project` (hover-to-accent link) rather than one consistent modifier.

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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the Discipline chip is removed (no such criterion in the model) and ABS reads "ABS (activity)". `.chips`, wraps the Assignment-criteria Chip Toggles.

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
- **variants**: standalone (`.warnbox`), embedded-in-modal (`.loss`), inline-with-CTA (`.stale-note`), borderless inline (`.hintbox`)
- **tokens**: --space-3, --space-4, --radius-lg, --radius-md, --ia, --warn, --text-sm, --text-2, --text-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): `.locked-hint` removed (no markup used it); documents.html's `.stale-note` reads "N answers reopened by this version" instead of "verdicts made stale". Same "colored notice box" idea under five unrelated class names across three screens, with inconsistent radius (`--radius-lg` vs `--radius-md`). `.warnbox`'s border is a hand-picked raw `rgba(224,164,60,.5)` rather than the `color-mix(in srgb, var(--warn) 35%, transparent)` technique `.loss`/`.stale-note` use — the raw value approximates the dark-theme `--ia` and won't repaint correctly in the light theme the way the color-mix versions do. Relies on untracked `--ia-soft`.

### Requirement Row (Review Table Row)
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: default, selected/bulk-selected, with-branches (Expand Chevron + "Multiple (N)" placeholders), image-sourced (revue-documentaire.html only), information row (static placeholders, revue-documentaire.html only)
- **tokens**: --space-3, --text-xs, --text-sm, --line, --accent, --accent-soft
- **built-from**: Checkbox, Status/Compliance/Verdict Pill, Activity / Requirement Tag, Disclosure Chevron, Select Dropdown, Text Input, Count Badge
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-123): Assigned to is read from the OBS entries (`allocSlots()`/`unassignedLabel()`): a select only when the row has exactly one entry, otherwise first names, "N/M assigned" or "Unassigned" with a per-system tooltip (was "Multiple (n)"), "PM · for partner" when only partners are left. 2026-10-07 (DEC-119, revue-documentaire.html): a Changes Cell after the Requirement cell, empty on information, system and team rows; the requirement's "Δ vX" badge (`.cbadge.chg-delta`, an inline-styled `.cbadge` before) only shows while the Changes column is hidden. 2026-10-01: free-text cells (`.cell-text`, e.g. ABS) end with an ellipsis instead of being cut mid-letter. `.rrow`. Explicitly documented in both screens' source comments as the same review-table engine, shared via `table-engine.js`. Row height (`--rrow-h:44px`) and column-width grid (`--rgrid-cols`/`--frgrid-cols`) are locally-scoped custom properties with fully hardcoded pixel values, none aligned to the space scale — column config differs per screen, everything else is shared.

### Branch / Allocated-Activity Sub-row
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: editable (Select Dropdowns for expert/manager/compliance), locked (🔒, read-only), team sub-row (one per organisation of a system), weak OBS (confidence below threshold)
- **tokens**: --space-6, --text-xs, --text-3, --ia
- **built-from**: Activity / Requirement Tag, Select Dropdown, Status/Verdict Pill
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-123): the person select reads the system's first OBS entry; a contributor can edit the system and team rows of their own system (membership, DEC-102), not only those they hold. 2026-10-09 (legacy cleanup): a system without an allocation model carries a "no model" tag (was "manual" — the Derivation Chain uses "manual" for a system a person added). 2026-10-01 (revue-documentaire.html): the system row now shows its own ABS and PBS values; an OBS below `OBS_THRESHOLD` carries its confidence as `.sys-conf.weak` (`weakObsHTML`), on system and team rows; a team without a named team reads "Organisation N" instead of "Team not set"; a team's status cell stays empty for the project manager on a Turnkey tender (pass 1), where the system row carries it. `.rrow.branch-row`, indented under a parent Requirement Row when it has 2+ activities. Tinted with untracked `--panel-2` to read as a child row.

### Grid Section / Group Header
- **level**: molecule
- **file**: revue-documentaire.html, compliance.html
- **variants**: doctitle, sec (H1), sub (H2/H3), group (Activity group-by header)
- **tokens**: --space-2, --space-3, --space-4, --font-mono, --text-xs, --text-base, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the group without a system is titled NO SYSTEM (was NO ACTIVITY), and a system group's description is its label alone (was "… perimeter"). 2026-09-24: compliance.html's table shows `doctitle` and `sec` rows too, in its new default "Sort: document order" (document, then section, then reference); any other sort is flat. CSS copied, not shared; its data has no H2/H3 level, so no `sub`. Keyboard navigation skips them. Sticky structural divider rows inside the Requirement Row grid. Group header's left accent color comes from a per-typology hardcoded hex palette (`GROUP_PALETTE`) set via inline `style`.

### Nav Tree Item
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: active, dimmed (filtered out, hardcoded `opacity:.28`)
- **tokens**: --space-2, --radius-sm, --accent-soft, --text-2, --text-xs
- **built-from**: Status Dot, Count Badge
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-123): the unassigned badge shows while any OBS entry has nobody; tooltip "Unassigned" or "N/M assigned". `.nav-item`. Hardcoded vertical padding and active border-left width.

### Nav Tree Section Header
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: nav-doc (document, collapsible), nav-h1 (section, with its requirement count `.nh-c`), nav-h2/nav-h3
- **tokens**: --space-2, --text-xs, --text-sm, --text-base, --text-3, --ok, --ia, --warn
- **built-from**: Disclosure Chevron
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the +/~/− change counts (`.sec-changes`) and the `b-change` badge are removed — they could only show in Compare mode, where the outline isn't drawn; changes are in the navigator's Changes tab (DEC-119). `.nav-doc`, `.nav-h1`, `.nav-h2/.nav-h3`. 2026-10-01: `.nh-num` takes `min-width:14px` (was a fixed 14px) so "31.1"-style numbers no longer run into the title.

### Document Block
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: requirement (compliance-colored in compliance.html, workflow-status-colored in revue-documentaire.html), heading, information (dimmed), image (figure+caption, revue-documentaire.html only), change-annotated (Compare mode, revue-documentaire.html only)
- **tokens**: --space-1, --space-2, --space-3, --space-4, --radius-xs, --paper, --paper-ink, --font-doc, --text-base, --accent
- **built-from**: Type Chip / Verdict Pill, Status Dot
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-012) revue-documentaire.html: the redacted variant is gone (`.blk.redacted`, `.redact-fill`, `.redact-note` and their hardcoded colours) — a contributor reads every block. 2026-10-09 (DEC-123) revue-documentaire.html: the unassigned tag takes its text from `data-unassigned`, so it can read "N/M assigned". 2026-10-09 (legacy cleanup): compliance.html's verdict colours follow the two verdicts — the red was keyed on `.dblk.non`, a value the data never holds, so a Not compliant block had no colour; it is `.dblk.not_compliant` now, and the `partial` / `needs-clar` styles are removed. 2026-10-01 (revue-documentaire.html): the image placeholder draws up to three labelled boxes from the figure's `figLabel` ("a → b → c") instead of empty boxes with a caption line; the captured tender gets a demo figure and a four-row interface table in § 31.3 (`addCaptureFigureAndTable`); the image lock icon moved clear of the block ID. `.blk` / `.dblk`. compliance.html is the most hardcoded-color spot in the app: verdict borders/backgrounds and `.vtag` badge colors are fixed hex pairs disconnected from `--ok`/`--warn`/`--ia`/`--accent`. revue-documentaire.html's redacted variant uses a hardcoded repeating-gradient "bar-code" fill, fully outside the token system.

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
- **variants**: ok, send/ia, comment, human, warn (colored connector dot per actor/event type); milestone (a station: 16px ring in `--accent` + the moment's name in the heading face, `.tl-ms`); with before → after (`.before-after`, struck old value, green new value)
- **tokens**: --space-1, --space-2, --radius-pill, --text-sm, --text-xs, --ia, --ok, --accent, --accent-soft, --human, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06: the tender's line, vertical — the connector is a 4px `--accent` rail, the key moments are stations (Captured, Allocated, Answered, Declared to the client — no ◆ pill any more), every other event a 10px stop that keeps its colour by kind. Same CSS in both screens. 2026-10-01: rendered by `activityItemHTML()` in both screens from the shared requirement log — who, what, before → after, time and category. `.tl-item`. Connector line/dot geometry (offsets, 6–9px dot) hardcoded and coupled between the two rules, not tokenized.

### Export Readiness Summary
- **level**: molecule
- **file**: compliance.html
- **variants**: inline banner (`.xr-ready`, compliance.html — renders empty unless complete)
- **tokens**: --accent, --accent-soft, --radius-lg, --radius-md, --space-3, --space-4, --space-5, --text-base, --text-xs
- **built-from**: Primary Button (qa.html only; compliance.html's CTA is bespoke)
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (DEC-116): qa.html's export card is gone: "Export to Excel" is a plain button in the toolbar and sends nothing — the questions are marked as sent by hand. Two screens independently implement "you're ready to export, N items" — same purpose, unrelated markup. compliance.html's relies on untracked `--ok-soft` plus a hardcoded rgba border.

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
- **variants**: uncertain-segmentation (warn-colored)
- **tokens**: --space-3, --space-4, --radius-md, --ia, --ok, --text-sm, --text-xs
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the default variant — a person proposed by the AI, with Accept assignment / Reject (`TYPE_SUGGEST`, `setManagerAssignment()`) — is removed: the AI derives an organisation, never a person (DEC-054). Only the uncertain-segmentation card is left. `.ia-suggestion`. Border/background colors are hardcoded rgba rather than `--ia`/`--warn`-derived, even though those tokens exist.

### Manager Assignment Card
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: assigned (read view), unassigned (dashed CTA), editing (inline select + Done)
- **tokens**: --space-2, --space-3, --radius-lg, --line, --ia, --ok
- **built-from**: Person Avatar, Select Dropdown
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the old read view's CSS (`.mgr-row`, `.mgr-none-row`, `.mgr-chip`, `.mgr-none`) is removed — the field is the person search (`personSearchHTML()`: `.mgr-block`, `.mgr-view`, `.mgr-edit`). `.mgr-row`/`.mgr-none-row`/`.mgr-edit`, documented in-code as "read view, click Change to edit inline (option B)."

### Role Recap Row
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: filled, missing ("To assign" placeholder)
- **tokens**: --text-xs, --text-sm, --text-3
- **built-from**: Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-123): one "Assigned to" row per person and a "To assign — k of m" row. `.role-row`, three compose the Role Recap Card. Label column width hardcoded 62px.

### Allocated-Activity Detail Card
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: default, with pending add-activity proposal, with pending reassignment request, no OBS yet (`.branch-sec-org.is-empty`, --text-3)
- **tokens**: --space-2, --space-3, --radius-md, --human, --text-xs, --text-3
- **built-from**: Activity / Requirement Tag, Status Pill, Select Dropdown
- **added**: 2026-09-01
- **changed**: 2026-09-29
- **notes**: `.branch-sec`, Detail Panel's "Allocations (N)" block. 2026-09-29: one system's version is now `systemAllocationsHTML(branch, bidx)`, shared by the Turnkey system detail and the contributor's own view — which replaces its bare "Assigned to" person search with this block, as on the SIG tender. The person select only offers that system's members (DEC-102). The PM's multi-system version (with proposals and reassignment requests) is still inline in `renderSettings` — known duplication. Borders use the untracked `--line-2`, the head the untracked `--panel-2`.

### Column Filter Section
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-1, --space-2, --text-xs, --text-sm, --accent, --line
- **built-from**: Checkbox
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-123): Assigned to lists one value per OBS entry, plus "PM · for partner" when the tender has partners. `.view-sec` + `.colf-opt`, repeated per data column in the Filter Panel.

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
- **variants**: add, mod, rem; in the Changes Navigator, a filter button (active: outlined in its own colour)
- **tokens**: --space-1, --space-3, --radius-pill, --text-sm, --ok, --ia, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-07
- **notes**: 2026-10-07 (DEC-119): lives in the Changes Navigator now (`.nc-sum .csum`), the Compare Bar is gone; there it is a button that keeps only that kind of change in the list (scale check: hundreds of changes per re-issue). Padding `1px 6px` hardcoded, no wrap inside a pill, the pills wrap between them. `.csum` ("+1 added / ~2 modified / −1 removed"). Counts are computed for the compared document and range since 2026-09-23 — they were hardcoded.

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
- **tokens**: --accent, --accent-soft, --space-1, --space-2, --space-3, --radius-md, --text-sm
- **built-from**: Propose Button (`.propose-btn`), Select Dropdown, Text Input
- **added**: 2026-09-01
- **changed**: 2026-09-23
- **notes**: 2026-09-23 — one propose block everywhere: `proposeBlockHTML()` ("Propose a change", pending requests, "↩ Request reassignment" + "+ Missing system" as filled `.propose-btn`, the 2026-09-10 version) now also renders in a Turnkey system's detail, replacing an older "Raise a problem" copy with `.mini-btn` buttons and its own ids (`#act-reassign`/`#act-missing`, gone). There the reassignment targets the system opened (`renderReassignForm(b,body,branch)`), not the viewer's or the first. Request reassignment is disabled once a request is pending on that system. compliance.html's contributor "↩ Request reassignment" uses the same `.propose-btn` (CSS duplicated there — no shared stylesheet for it); its PM-side "↪ Reassign and send back out" is a different action and keeps `.cta ok`. `.propose-btn:hover` text `#fff` hardcoded; disabled state depends on untracked `--panel-2`/`--line-2`. `.propose-form`/`.reassign-reasons`, Detail Panel for non-admin managers. Sibling of Inline Form Shell (below), which serves the same purpose in compliance.html — two independently-built form containers for the same "propose a change" idea.

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
- **notes**: 2026-09-30: risks.html briefly had a `.rk-kpi` copy too, removed with DEC-113. documents.html's `.stat` (min-width 150px, used 4× in the Document Summary Strip) and dashboard-et-config.html's `.hstat`/`.fb-card` all express "big number + label" with independent hardcoded padding/letter-spacing — a missed-reuse opportunity flagged directly in the dashboard scan.

### Version History Entry
- **level**: molecule
- **file**: documents.html
- **variants**: current, historical, with reopened answers
- **tokens**: --space-3, --font-mono, --text-xs, --text-2, --text-3, --ok
- **built-from**: Status Badge / Chip, Warning / Notice Box (nested)
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-122): the reopened count is what the shell recorded and Compliance applies (`recordVersionChange()`), and uploaded versions survive navigation (`replayVersionChanges()`). 2026-10-09 (legacy cleanup): "stale verdicts" reads "answers reopened" across the screen (version entry, summary strip, filter, toast); the data field keeps its name, `stale`. Row padding, column width, several margins hardcoded.

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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the dead `.filecard` CSS noted below is removed. `.filecard` is fully defined in CSS but never rendered — dead code superseded by `.doccard`. Icon-square dimensions (34/38px) hardcoded.

### Search-to-Add Combobox
- **level**: molecule
- **file**: creation-projet.html, dashboard-et-config.html
- **variants**: empty query (hidden), results, no-match
- **tokens**: --space-3, --radius-lg, --radius-sm, --text-base, --text-2, --text, --text-sm, --text-3
- **built-from**: Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): creation-projet.html's result list (`.pm-add-list`) had no CSS, so it sat in the page flow and never hid — it now floats under the field (absolute, `--panel-2`, hidden until `.open`). Named "Person Search Typeahead" in dashboard-et-config.html's Team-casting flow — a code comment in creation-projet.html explicitly frames this as reusing "the same shape as the casting screen's own SSO-search add flow," confirming intentional cross-screen reuse despite the independent implementation. Dropdown box-shadow hardcoded in both.

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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-124): the remove button shows only where the viewer can edit that system. `castPersonRowHTML`, reused identically for activity/perimeter rosters and the PM-team roster. See Team Member Row note above.

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
- **variants**: one line, both dates; passed / overdue in `--warn`
- **tokens**: --space-3, --space-4, --radius-lg, --text-sm, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (DEC-116): the two banners (one per tab) became one quiet line above the list, `.qa-dates`, both dates side by side; nothing renders for an unset date, as before. Was: `.qa-deadline`, uses `color-mix()` for borders instead of a fixed token. Deliberately renders nothing when the underlying date is unset (explicit "degrade cleanly" code comment).

### Q&A Card
- **level**: molecule
- **file**: qa.html
- **variants**: to send (checkbox + "Mark as sent"), sent ("Not sent" to undo), answer to confirm (`.qa-suggest`, dashed `--human`, "✓ It's the answer" / "Not this one"), answered, selected (`.is-sel`), other bidder (`.is-other`: question, the client's answer, the requirement or "No requirement linked")
- **tokens**: --panel, --line, --accent, --human, --ok, --radius-lg, --space-2, --space-3, --space-4, --text-base
- **built-from**: Activity / Requirement Tag
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (DEC-116): one card for every row of the register — our questions with a status pill (`.qa-st`) and its action, and the other bidders' Q&A; the answer sits under the question it answers. Excluded is gone with Exclude. Depends on untracked `--accent-soft`/`--human-soft`/`--ok-soft`; the pinned 25px indent lines the answer up with the question text. `.qa-card`. Answer sub-block relies on untracked `--ok-soft`. `.is-excluded` uses hardcoded `opacity:.6`.

### Q&A View Switch
- **level**: molecule
- **file**: qa.html
- **variants**: our questions / other bidders (on), other bidders before any import ("—")
- **tokens**: --panel, --panel-3, --radius-md, --radius-sm, --radius-pill, --space-2, --space-3, --text-base, --text-xs, --text, --text-2, --accent
- **built-from**: Count Badge
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: DEC-116. `.qa-views` — replaces the Questions / Answers tabs, whose second tab nobody noticed: each view carries its count, so where the answers are is visible before clicking. Depends on untracked `--panel-3`, `--panel-2`, `--accent-soft`; hardcoded shadow on the active view.

### Q&A Status Filter
- **level**: molecule
- **file**: qa.html
- **variants**: All / To send / Sent / Answer to confirm (only while one exists, outlined `--human`) / Answered, each with its count; selection bar ("N selected · Mark as sent · Clear") or "Select the N to send"
- **tokens**: --line-2, --panel, --accent, --human, --radius-pill, --space-2, --space-3, --text-sm, --text-2, --text-3
- **built-from**: Primary Button
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: DEC-116. `.qa-st-filter` + `.qa-bulk`: what has gone to the client is read at a glance and flagged in one gesture — the tool sends nothing itself. Depends on untracked `--accent-soft`.

### Timeline Item
- **level**: molecule
- **file**: compliance.html
- **variants**: ok, send, warn
- **tokens**: --text, --text-2, --text-3, --text-sm, --ok, --accent, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06: same rail-line restyle as the Activity Timeline Entry. See Activity Timeline Entry (revue-documentaire.html) — near-identical connector-dot pattern, independently coded per screen.

### Filter Pill
- **level**: molecule
- **file**: compliance.html
- **variants**: p-wait, p-clar, p-done, p-reassign, p-aside (contributor only, `--human`); active (p-over "overdue" and p-out "outdated version" removed 2026-09-24)
- **tokens**: --space-1, --space-3, --radius-pill, --line, --text-sm, --text-2, --accent, --accent-soft, --warn, --ia, --ok
- **built-from**: Count Badge-like `.n` span
- **added**: 2026-09-01
- **changed**: 2026-09-24
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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): 2 instances left — the other three went with the Config rows they sat in (see Config Section). `.tog-row`, used 5× across Config sections. Gap hardcoded 12px.

### Theme Picker
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: dark option, light option
- **tokens**: --radius-lg, --text-2, --text-base, --space-2, --space-4, --accent, --accent-soft, --text
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the swatches use the current theme values — dark #071A30 / #4C82FF, light #ffffff / #0B294A (they still showed #171b24 and #0050E3). `.theme-pick`/`.theme-opt`. Swatch previews are deliberately hardcoded hex gradients per a code comment — they must show both themes' literal accents regardless of which theme is currently active, so they intentionally cannot read from `var(--accent)`.

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
- **variants**: normal, over-capacity (late, `--ia` bar and red count)
- **tokens**: --text-sm, --text-xs, --text-2, --text-3, --radius-xs, --radius-sm, --space-2, --ok, --ia, --warn
- **built-from**: Progress Bar
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): `.exp-ln` removed — the Expert Editor Row doesn't use it (`.exp-av` stays). 2026-10-07 (DEC-118): a system code chip (`.exp-code`, mono, on the untracked `--panel-2`) where the person's avatar and name were — the card lists the three systems (sub-systems on a SIG tender) carrying the most answers, from `ANSWERS_BY_SYSTEM`, by `renderAnswersCard()`. `.exp-av`/`.exp-ln` stay in the CSS for the Expert Editor Row. 2026-10-06 (DEC-117): rendered from Statistics' figures instead of three hardcoded rows that contradicted them. `.exp-line`, dashboard sidebar card (3 instances).
### Expert Editor Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3, --line, --radius-lg, --text-base, --text-xs, --text-3, --radius-sm, --warn
- **built-from**: Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the dead `.team-mgr-group` / `.team-mgr-head` / `.team-roster` CSS noted below is removed; adding someone toasts "Contributor added" (was "Expert added"). `.exp-edit-row`, Config → Team & experts. Delete is blocked with a Toast if the expert still has assigned requirements. Dead CSS nearby (`.team-mgr-group`/`.team-mgr-head`/`.team-roster`) has no matching markup — leftover from before the Team-screen redesign replaced it with Cast Person Row.

### Add Expert Form
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-2
- **built-from**: Text Input, Primary Button
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.add-exp`, single instance.

### Stat Block
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: default, full-width (`.stat-wide`), shown only when non-zero (Work invalidated); head with a period (`.stat-when`) or a link (`.stat-link`)
- **tokens**: --radius-lg, --space-1, --space-2, --space-3, --space-4, --text-sm, --text-xs, --text, --text-2, --text-3, --ok, --warn, --ia
- **built-from**: none (hosts whichever content it wraps)
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-124): "By system" is "By system, with who is on it" — a row shows the manager or "N contributors · no manager", only a system with nobody is flagged ("Nobody staffed yet" → Team casting), "Cast one →" is gone; "The team" shows a missing manager neutrally and flags "no contributor on X yet" with a link to Team casting. `.sys-cast` removed. 2026-10-06 (DEC-117): the grey subtitle is gone. Each block opens on `.stat-top` (title, then a period or a link) and `.stat-take` — one computed sentence, what a manager would say out loud, its figures in bold, coloured `.is-late` (--warn) / `.is-tight` (--ia) / `.is-good` (--ok) — then the figure behind it. `.stat-h2` is a small-caps sub-heading inside a block, `.stat-foot` a footnote, `.st-go` a row that opens its screen (hover on the untracked `--panel-3`). `.stat-link` and the period use the untracked `--brand-blue`. Background the untracked `--panel-2`. 12 instances across the three tabs. `.stat-empty` is its "nothing to count yet" line.

### AI Pattern Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3, --line, --radius-lg, --radius-md, --text-sm, --font-mono, --text-base, --text-xs, --text-3, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): 3 instances — the "TKY · Turnkey added" pattern went (Turnkey is a kind of tender, not a system), and the others name a current system code and organisations instead of retired ones. `.pat`, AI Feedback "Recurring patterns" row (4 instances). Relies on untracked `--ia-soft`.

### Live Feedback Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3, --space-2, --line, --text-sm, --radius-sm, --text-xs, --text-2, --ia
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): a correction to a requirement's systems is tagged SYS (was TYPO). `.fb-live-row`, populated dynamically from `window.parent.getAIFeedback()`.

### Phase Card
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: step (primary rail), support (secondary rail); active-phase, done-phase, is-current states
- **tokens**: --space-3, --panel, --line, --radius-lg, --space-4, --accent, --accent-soft, --radius-md, --text-3, --text-base, --text-lg, --text-sm, --text-2, --text-xl, --radius-xs, --ok, --text-xs, --radius-pill
- **built-from**: Status Pill, Progress Bar
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-124): the Team casting card counts systems with someone on them (a missing manager doesn't count against it); its tooltip says "with or without a manager"; it refreshes on return from Team casting. 2026-10-09 (legacy cleanup): the support variant's description and bar, hidden by CSS (`.is-support .ph-desc/.ph-bar{display:none}`), are gone from the markup too; the Risks card opens through `goRoute()` like the other three. 2026-10-07: the support variant stacks name over figure (`.ph-info` in a column), each still able to ellipsis. 2026-10-06: the step variant was replaced by the Tender Line on the dashboard, then restored the same day on review — this area is for getting to the two working screens, minimal, with Allocation and Compliance standing out. `.phase`. A source comment explicitly calls this "the same molecule" reused for both rails — confirmed intentional componentization, one of the few in the codebase. `.is-current` uses `color-mix()` rather than a plain token. Absolute badge/button offsets and min-height (96px) hardcoded.

### Cast Coverage Card
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: complete, unstaffed, partial
- **tokens**: --line, --radius-md, --space-3, --panel, --font-mono, --text-xs, --text-2, --text-sm, --warn, --ok
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-124): the "No manager cast yet" variant is gone — a system is unstaffed only when nobody is on it. `.cast-cov-card`, one per activity (7 instances). Complete/unstaffed border colors hardcoded rgba rather than derived from `--ok`/`--warn`.

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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-124, DEC-102): search options carry the person's system on the right (`.cast-add-opt-where`); someone who belongs to another system stays listed, greyed (`.cast-add-opt.is-blocked`, "In SEN — one system per person"), and picking them is refused with a toast naming that system; someone already in this system can take another perimeter ("Already in RST"). `.cast-add-flow`, driven by `bindCastAddFlow`/`bindPMAddFlow`. Its confirm button (`.cast-add-confirm`) duplicates Primary Button's exact styling under a separate class instead of reusing it.

### Re-run Control
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: available (button + menu), blocked (disabled button, reason in title)
- **tokens**: --panel, --line-2, --radius-md, --text-xs
- **built-from**: Ghost Button (`.mini-btn`), menu options
- **added**: 2026-09-17
- **changed**: 2026-09-23
- **notes**: `rerunControlHTML()`. Menu groups the system's own products first, then borrowable models under a distinct header. Placed in: the model header of the qualification block (manager, single system), the header of a Turnkey system's detail ("Open system detail"), and the head of the contributor view (added 2026-09-23 — ALLOC-014 gives contributors the right). It sat on each system card of the Turnkey PM view from 2026-09-23 until removed the same day at the user's request; the system's detail keeps it. `.rerun-wrap` has `margin-left:auto` for title rows. Menu `min-width:210px` hardcoded. Depends on untracked `--line-2`.

### OBS List
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: empty ("No role yet" / "No organisation yet"), one or several entries (remove on every row), keyed ("role", select-based add) vs free ("organisation", text add)
- **tokens**: --text-sm, --text-xs, --text-3
- **built-from**: UI List (`.ui-list`), Confidence Badge, Icon Button (remove ✕), Text Input (search field of the add picker)
- **added**: 2026-09-08
- **changed**: 2026-09-23
- **notes**: DEC-076 (2026-09-23): every row has its ✕, the last one included — removing the last empties the system's single slot (`obsSlotEmpty()`; organisation, team and person go together) and shows the empty state; the next add fills that slot rather than adding a second. `obsListHTML()` / `bindObsList()`. The noun comes from `OBS_NOUN` — "role" on a keyed Mainline tender (DEC-062), "organisation" elsewhere — for the remove tooltip, add button, toasts and confirm. Removing down to one entry re-syncs the system's and (single-system) the requirement's person and OBS, so the table's "Assigned to" never shows the removed entry's person. Adding (2026-09-23) is a search, not a dropdown: `+ Add role` opens a full-width field over an inline list (`.obs-pick`), filtered as you type on title and the workbook's skill/SoA/job codes; click or Enter adds, ↑/↓ move, Escape or ✕ cancels. On a keyed tender the roles filed under the requirement's ABS are grouped first (sticky group headers); elsewhere it suggests organisations already used on the tender and offers "Add “…”" for what was typed. It replaced a native select of ~45 titles, truncated in the panel width, plus a separate Add button. List max-height 240px and code line 10px hardcoded.

### Custom Column Cell
- **level**: molecule
- **file**: revue-documentaire.html, compliance.html
- **variants**: free text (inline input), single-value list (select), multi-value list (button + checkbox popover `#cf-pop`), empty (system/team sub-rows, information rows)
- **tokens**: --text, --text-3, --line-2, --radius-sm, --text-sm; popover --panel, --line-2, --radius-md
- **built-from**: Text Input (`.cell-text`), Select Dropdown (`.cell-select`), Checkbox
- **added**: 2026-09-23
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-012/100) compliance.html: read-only variant `.cf-ro` on a requirement with no assignment of the contributor's system (`--text-2`, `--text-sm`; padding 3px 6px hardcoded). 2026-09-24: compliance.html has its own (DEC-081, phase "compliance"): `.cf-cell` input/select and `.cf-multi`, appended in `renderTable2()`; empty on system/team sub-rows; Enter commits, Escape restores. No per-column header filter there (Compliance's column filters work on assignments, custom values live on the requirement) — the advanced filter covers them. `cfCellsHTML()`, appended to every grid row centrally in `rowHTML()` rather than inside each row renderer, so a new row type cannot forget it. Keyboard: reachable with the arrows like any column; Enter/F2 edits; text and single-list cells get the engine's Enter (confirm + move down) / Escape (restore) through `.cell-text`/`.cell-select`; the multi-value picker takes the same contract (↑/↓ between options, Space ticks, Enter confirms and moves down, Escape restores the previous values). Column width hardcoded 150px. Popover min-width 190px / max-height 280px hardcoded. Depends on untracked `--line-2`, `--panel-2`.

### Custom Column Header Cell
- **level**: molecule
- **file**: revue-documentaire.html, compliance.html
- **variants**: text (sort + edit), list (sort + column filter + edit), contributor view (edit hidden)
- **tokens**: --text-3, --accent, --accent-soft, --radius-sm, --text-xs
- **built-from**: Column Filter Button (`.colf-btn`), edit button (`.cf-edit`)
- **added**: 2026-09-23
- **changed**: 2026-09-29
- **notes**: 2026-09-29 (DEC-097): the same columns on both screens; a column created on the other screen starts hidden here (`cfShownHere`), and turning it on in View is remembered on the definition (`d.shownIn`, `cfRememberVisibility`). 2026-09-24: compliance.html injects them into `#frgrid-head` from `syncCustomColumns()` — name + ✎ (project manager only), sortable from its header like every column there, resizable. Injected into `#rgrid-head` by `cfRenderHead()`; its grid order and hidden state come from a generated `<style id="cf-style">`, since the static per-column CSS rules cannot know these keys in advance. The ✎ is hidden by `body.restricted`.

### Custom Fields Panel Section
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: text, single list, multi list (toggle chips `.advv-chip`)
- **tokens**: --text-xs, --text-3
- **built-from**: Text Input (`.ui-input`), Select Dropdown (`.ui-select`), Chip Toggle
- **added**: 2026-09-23
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-012/100) compliance.html: read-only (plain `.fval`) for a contributor with no assignment on the requirement. `cfPanelHTML()`, in both the manager panel and the contributor view. One quiet hint line under the fields — the label stays a label (see Page Title / Nature field convention). Reuses the advanced filter's chip style for multi values.

### Versions Tab
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: modified (diff + full previous text), added (no earlier text), with earlier versions listed; pending review vs checked since
- **tokens**: --ia, --ia-soft, --ok, --ok-soft, --paper, --paper-ink, --font-doc, --text-sm, --text-xs, --radius-pill, --radius-sm
- **built-from**: Word Diff, Next-Step line (`.next-step`), Ghost Button (`.mini-btn`)
- **added**: 2026-09-23
- **changed**: 2026-10-07
- **notes**: `versionsTabHTML()`. Only shown when the requirement changed in the version of its document in force (DEC-071) — no tab otherwise. No "reviewed / action" state of its own: the change sets the requirement back to To review and validating it is the treatment (DEC-072); the tab says when a more restrictive status (e.g. Incomplete) is what the pill shows. "Show in the document →" ("Open in Compare" until 2026-10-07, DEC-119) opens the Document view on its Changes, at the document and range of the change; not shown when already there. Replaces the Change Card. Depends on untracked `--ia-soft`, `--ok-soft`, `--panel-2`.

### Removed Requirement Panel
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --paper, --paper-ink, --font-doc, --text-xs, --text-3
- **built-from**: Status Pill (Requirement Workflow State), detail field
- **added**: 2026-09-23
- **changed**: 2026-10-07
- **notes**: `renderRemovedPanel()`, what a removed requirement (a ghost block, shown only under Changes in the Document view — LIFE-006; "Compare only" until 2026-10-07, DEC-119) was and when it went. Read-only. Replaces the Change Card for removals.


### Changes Cell
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: changed (on one line, an excerpt that starts a few words before the first change; in Wrap text, the whole requirement under a line with the Change Type Tag and the Version Picker Button), new (the whole text highlighted as added), no change (quiet picker), single version (no picker — the document has one version), compared with a version of its own (picker in accent)
- **tokens**: --space-1, --space-2, --text-sm, --text-base, --text-xs, --text, --text-3, --warn, --ok, --radius-xs
- **built-from**: Change Type Tag, Word Diff (its runs, `wordDiffOps()`), Version Picker Button
- **added**: 2026-10-07
- **changed**: 2026-10-07
- **notes**: DEC-119. `.rcell.c-chg`, `chgCellHTML()` / `chgDiffHTML()`: the requirement in force with what changed since an earlier version of its own document — removed words struck (`.cd-del`), added ones highlighted (`.cd-ins`), as DOORS shows it. The version compared with is the row's own choice (`state.chgBase[id]`) or the column's (`state.chgAll`: the document's previous version, or its first). Excerpt rule hardcoded in `chgDiffHTML()`: 3 words before the first change, runs of more than 8 unchanged words between changes cut to 4 … 4, the tail left to the cell's ellipsis. Depends on untracked `--warn-soft`, `--ok-soft` for the highlights — the Word Diff atom colours the same runs with hardcoded hex on the paper, so one diff has two colourings. Column width `minmax(280px,1.5fr)` hardcoded in `RCOLS`. A removed requirement has no row, so it never shows here (LIFE-006).

### Version Picker Popover
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: one requirement (the earlier versions of its document with date · note, "— no change since" under a version after which the requirement did not change, "Same as the column" once it has its own), all requirements (the previous version / the first version, and a line saying that choosing resets the requirements set one by one)
- **tokens**: --space-1, --space-2, --radius-md, --radius-sm, --line, --text-xs, --text-sm, --text, --text-2, --text-3, --accent
- **built-from**: Version Picker Button (its anchor)
- **added**: 2026-10-07
- **changed**: 2026-10-07
- **notes**: DEC-119. One `#chg-pop` element appended to the body, fixed-positioned under its button (`openChgRowPop()`, `openChgAllPop()`); closes on an outside click and on Esc. Depends on untracked `--panel-2`, `--panel-3`, `--line-2`. Hardcoded: min/max width 250/340px, z-index 80, shadow `rgba(0,0,0,.35)`, item padding 6px. One more popover implementation next to the column filter's (`#colf-pop`) and the custom column picker's (`#cf-pop`).

### Change List Card
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: added, modified, removed; current (`.on`, accent ring); reopens an answer (warn impact line)
- **tokens**: --space-2, --radius-md, --line, --panel, --accent, --text, --text-2, --text-3, --text-xs, --font-mono, --warn
- **built-from**: Change Type Tag
- **added**: 2026-10-07
- **changed**: 2026-10-07
- **notes**: DEC-119. `.nc-card` in the Changes Navigator: type, ID, § of the paragraph, what changed (clamped to two lines), and what the change does to the work already done (`changeImpact()`: removed → its work stays archived with the earlier version; added → needs allocation / allocated since; was answered → back to To review, in warn; awaiting its answer → the contributor answers the new text; otherwise back to To review). Click selects the requirement and scrolls the paper to it. Hardcoded: horizontal padding 10px, gaps 3px/6px, ring `color-mix(var(--accent) 16%)`. Depends on untracked `--line-2` (hover).
### Nature and Class Fields
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: nature only (heading, information), nature + class (requirement); with the characterisation model's level beside the label (Confidence Level Badge; Low highlighted), read-only (contributor)
- **tokens**: --ia, --text-xs
- **built-from**: Select Dropdown (`.ui-select`), Ghost Button (`.mini-btn`), Confidence Level Badge
- **added**: 2026-09-23
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the unused `.char-ro-ai` CSS and the handlers of the old Confirm buttons (`#f-tech-confirm`, `#f-nature-confirm`) are removed — no element has carried those ids since DEC-099. 2026-10-08 (DEC-120): the label carries the model's level (High / Medium / Low) while the value is the AI's; the read-only "· AI, unconfirmed" (`.char-ro-ai`) is replaced by it. 2026-09-29 (DEC-099): the "Detected by the AI, not confirmed yet" line and its Confirm button are gone for everyone — validating the requirement confirms them. 2026-09-28 (DEC-086): read-only for a contributor — the value as text, "· AI, unconfirmed" when it applies, and "Set by the project manager" (`.char-ro`) underneath; no select, no Confirm. `natureFieldHTML()` / `classFieldHTML()`, at the top of every block's details (SIG and other single-pass tenders, the contributor view; the Turnkey PM view has the same two fields in its own layout, now labelled "Class" too, not "Type"). Nature offers only Information / Heading / Requirement (DEC-074) — it briefly held Functional / Performance / Security / Interface / Regulatory, which are gone from Allocation. Confirm buttons exist because re-picking the current value in a select fires no change event.

### Re-run Prompt
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: action (accent-filled button — "↻ Re-run the model" + reason), blocked (muted strip, no button), no model (muted strip, "check ABS / PBS / OBS by hand")
- **tokens**: --accent, --ia, --radius-md, --text-xs, --space-2, --space-3
- **built-from**: none
- **added**: 2026-09-23
- **changed**: 2026-09-23
- **notes**: `rerunPromptHTML()`, `.rerun-prompt`. DEC-075: shown above ABS when the nature or class differs from what the derivation was made with (`b.derivedWith`, snapshotted at load, reset by `applyRerunTo`). One row, 25px, `nowrap` — the reason (`.rp-why`) truncates first so the action stays readable in a narrow panel. Hardcoded: text `#fff`, `padding:5px`, a `rgba(0,0,0,.12)` shadow, hover `brightness(1.12)`. Muted variant depends on untracked `--ia-soft`. Distinct from Re-run Control, which is the always-available menu in the model header.

### Derivation Chain
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: single-system model block ("SIG's model" — ABS, PBS, OBS), Turnkey pass 1 (Nature, Class, PBS/ABS, System), contributor view
- **tokens**: --panel-2, --line, --radius-md, --space-3, --text-xs, --text-3
- **built-from**: Derivation Step (`derivStepHTML()` — label, confidence badge, control, hint), Confidence Level Badge, OBS List, Re-run Control, Re-run Prompt
- **added**: 2026-09-23
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the project manager's "Distribution across systems" block (`distributionBlockHTML()`) and the "routes into" arrow under it are removed — the block only drew on a Turnkey tender, whose requirements never reach the panel that called it (the PM gets the Turnkey layout, a contributor the system view), so it never showed. `derivationChainHTML(b, myBranch, derivSrc)` loses `rmView` and `opts` (its only option was `noDistrib`). 2026-10-08 (DEC-120): in the Turnkey pass 1, Nature and Class show the characterisation model's level (Low / Medium / High) where PBS / ABS and System keep the allocation model's percentage; Class lost its "· AI, unconfirmed" suffix to the badge. 2026-10-07: in the Turnkey pass 1, the PBS / ABS step shows its confidence badge only beside a value — "87%" over an empty field read as the AI being sure of nothing. 2026-10-06: the contributor's view no longer shows "Distribution across systems" (the compact chip row, `.distrib-compact` / `.distrib-chip`, deleted) — the information was scattered and not theirs to act on; the project manager's distribution block is unchanged. 2026-09-29: optional `opts.noDistrib` drops the distribution block; the Turnkey system detail (DEC-101) renders the chain for the system opened, edits going to that branch. Turnkey pass 1's System list has a ✕ per system since 2026-09-23 (DEC-076, `removeSystem()`), down to none — empty state "No system yet". Each system row carries its provenance, one or the other (2026-09-23): the AI's confidence badge when the Turnkey model proposed it, a "manual" note when a person added it — "manual" used to mean "no allocation model" and sat beside the percentage; "has a model" (accent) stays as a separate note. Its "+ Add system" (`openAddSystem()`, 2026-09-23) adds directly through the OBS List's search picker (`.obs-pick`, reused as-is); it used to open the contributor's proposal form, absent from the PM view, and did nothing. Since 2026-09-23 the model block can carry a Re-run Prompt between its header and ABS (DEC-075). `.deriv-pass` / `.deriv-step`. Not recorded before; entered when the small "↓" between PBS and OBS was removed (2026-09-23) — the steps already read top to bottom and the arrow only took height, so the three steps now sit 16px apart. The only arrow left is Turnkey's "routes into" between the distribution and the system's model, which carries information. Depends on untracked `--panel-2`.

### Turnkey System Card
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: model system, system with no organisation / person yet (grey italic), partner (outside-the-tool note), low-confidence OBS (warn badge)
- **tokens**: --space-1, --space-2, --space-3, --line, --text, --text-2, --text-3, --text-sm, --text-xs
- **built-from**: Activity / Requirement Tag, Status Pill, Compliance Pill, Ghost Button (`.mini-btn`)
- **added**: 2026-09-29
- **changed**: 2026-09-29
- **notes**: `activityBlocksHTML()` + `obsBreakdownHTML()`, the "Systems (N)" list of the Turnkey project manager's detail panel. Head: system tag, then that system's allocation status (`.status-pill.is-static`, not clickable) in the right corner — replaces the three-state `.act-alloc-pill` (Not started / In progress / Allocated), removed with `activityAllocStatus()`. Body: one line per OBS, organisation left and person right (`.act-obs-row`), replacing the "Allocation · Team not set · Unassigned" key/value line. Then a Compliance line laid out like the OBS lines (label left, pill right), and "Open system detail →" alone on the last line, full width — a button beside the data was too cramped at the panel's width. Card frame reuses `.branch-sec` (untracked `--line-2`, `--panel-2`). First recorded on this change; the card existed before without an entry.

### Gap Strategy Editor
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: empty (no strategy yet), unused row (deletable), used row (delete disabled, "used N×"), pending result change (inline confirmation with the count)
- **tokens**: --space-1, --space-2, --space-3, --radius-sm, --radius-md, --text-xs, --text-sm, --text-2, --text-3, --line-2, --warn-soft
- **built-from**: Text Input (`.inp`), Select (`.sel`), Ghost Button, Primary Button
- **added**: 2026-09-30
- **changed**: 2026-09-30
- **notes**: Settings → Compliance → Gap strategies (SPEC-risks.md §2.1, DEC-110/111). `renderStrategiesSetting()`; one row per strategy — name (renamed on change/Enter), external result select, usage, delete. State lives in the shell (`getStrategies`, `addStrategy`, `renameStrategy`, `setStrategyResult`, `removeStrategy`, `reportStrategyUsage`/`getStrategyUsage`) like the partner list, so it survives the iframe reload. Changing the result of a strategy in use asks first, inline under the row (no modal exists on this screen): "N requirements will change external compliance…", PM corrections excepted. Usage is reported by Compliance (step 2 of the Risks build) — until then every strategy reads "unused". Depends on untracked `--line-2` (empty state border) and `--warn-soft` (confirmation); `.gs-rm` is 28px square, hardcoded.

### Gap Editor (Strategy + Risk)
- **level**: molecule
- **file**: compliance.html
- **variants**: editable (responsible, or the PM on a partner verdict), read-only (anyone else — missing values shown as flags), no strategy on the tender, risk search with suggestions, no match, new-risk form open (three questions), several risks linked
- **tokens**: --space-1, --space-2, --space-3, --radius-sm, --radius-md, --text-xs, --text-sm, --text-2, --text-3, --font-ui, --font-mono, --warn, --warn-soft, --ok, --ok-soft, --ia, --ia-soft
- **built-from**: Verdict Pill, Risk Chip, Ghost Button (`.risk-new-btn`), Form Actions
- **added**: 2026-09-30
- **changed**: 2026-10-01
- **notes**: 2026-10-01: a linked risk also shows "N req." (how many requirements share it), like the suggestions. SPEC-risks.md §3-§4. `gapEditorHTML(r,br,editable)` / `bindGapEditor()`; used in the Decision Panel (Not compliant chosen), on an answered Not compliant assignment, and in the PM's partner-verdict form. Strategy select from the tender's list, with "Declared to the client: <pill>" once picked. Risk: linked risks (ID, "There is a risk that…", unlink), then a search over the tender's risks ordered same heading → rest (DEC-114: no system ordering), each with "N req." already linked, max six shown; "＋ New risk" — only if none fits — opens an inline form with the template's three questions as three required fields, "Save and link" (DEC-113: no weight). Writes go straight to the shell (`setGapDoc`, `addRisk`) — no draft. Depends on untracked `--panel-2`, `--panel-3`, `--line-2`.

### External Compliance Field (with PM correction)
- **level**: molecule
- **file**: compliance.html
- **variants**: derived, corrected (note with author, date and reason; "Change the correction", "Revert to derived"), correction form open (three choices + required reason)
- **tokens**: --space-1, --space-2, --space-3, --text-xs, --text-2, --text-3, --radius-md
- **built-from**: Verdict Pill, Verdict Toggle (`.verdict-toggle`, three-way variant), Form Actions
- **added**: 2026-09-30
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the empty `clientDecisionHTML()` stub is removed. DEC-106. `externalFieldHTML()` / `bindExternalField()` on an answered assignment's panel: what the client is told for that system. Only the project manager sees Correct. Replaces the requirement-level declaration form (`clientDecisionHTML()` now returns nothing).

### Progress Sequence
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: step default, step warn (Not compliant not all logged), no data yet
- **tokens**: --space-3, --radius-md, --radius-xs, --text-xl, --text-xs, --text-3, --line, --accent, --warn, --panel
- **built-from**: none
- **added**: 2026-09-30
- **changed**: 2026-09-30
- **notes**: SPEC-risks.md §9 "% NC logged" in a progress sequence — the dashboard had no such sequence, so it was created: Assigned → Internal compliance → Not compliant logged → External compliance, each step a percentage of what it depends on, clickable to its screen. `.prog-seq` / `.prog-step`. Bar track uses the untracked `--panel-3`.

### Key Dates List
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: done (filled `--accent` dot), today (`--brand-blue` dot with a soft halo, name in blue), upcoming (hollow dot, "in N days"), end (ringed dot — submission)
- **tokens**: --space-3, --text-sm, --text-xs, --text, --text-2, --text-3, --accent, --warn
- **built-from**: none
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: `.kd` / `.kd-i`, Statistics › Project › Timeline (DEC-117): received, Q&A cut-off, today, client answers expected, submission. The two Q&A dates are kept identical by hand to qa.html's `TENDER_QA_DATES`; today is submission minus the project's days left (the hero's figure, now read from the project too). Rail and dots hardcoded (2px, 10px); rail and hollow dot on the untracked `--line-2`/`--panel-2`, today on the untracked `--brand-blue`/`--brand-blue-soft`.

### Progress Trend Chart
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: on pace (the dashed projection reaches 100% before submission), late (it meets submission below 100%), complete or stalled (no projection)
- **tokens**: --accent, --ok, --line, --text-2, --text-3
- **built-from**: none
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: Inline SVG, Statistics › Project › Timeline (DEC-117): % of requirements allocated (`--accent`) and answered (`--ok`) from the tender's reception to its submission, a dashed line at this week's pace (the last seven days carried forward, `finishAt()`), today on the untracked `--brand-blue`, the sentence above saying where each lands. Drawn at the width it gets so its 10px labels stay 10px (re-drawn when its tab or the dashboard is shown), 170px tall; margins hardcoded. Replaces the old trajectory-to-deadline chart, also a hand-rolled one-off.

### Leaderboard Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: system row (code in the mono face, its sub-systems and their counts underneath, or "not split into sub-systems"), sub-system row (a single-system tender: name, then validated · answers · comments), top (#1, `.is-top` on the untracked `--brand-blue-soft`)
- **tokens**: --space-2, --radius-md, --radius-pill, --font-mono, --text-sm, --text-xs, --text, --text-3, --accent, --ok
- **built-from**: Progress Bar
- **added**: 2026-10-06
- **changed**: 2026-10-07
- **notes**: 2026-10-07 (DEC-118): ranks systems and their sub-systems, never people — the avatar, the name and role and the "you" pill (`.st-you`) are gone; a single-system (SIG) tender ranks its sub-systems. Each action counts for the system it was done on, whoever did it; live events from the session count for the system they name and show as "not split N". `.lb-row`, Statistics › Project › Most active this week: rank, label, a bar split allocation (`--accent`) / answers (`--ok`) / comments and questions (untracked `--brand-slate`), the total, then a footnote saying nobody's own activity is shown. Never field edits. Grid columns hardcoded (14px/1fr/34%/24px); bar track the untracked `--panel-3`.

### Avatar Stack
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: up to six avatars, then "+N"
- **tokens**: --space-1, --text-xs, --text-3, --panel
- **built-from**: Person Avatar
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: `.st-stack`, Statistics › Project › The team. Overlap (−3px) and the 2px `--panel` ring that separates each avatar are hardcoded.

### Team Role Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: default, gap (a system with no manager: red "has none yet", the row opens Team casting)
- **tokens**: --space-2, --space-3, --radius-md, --panel, --text-sm, --text-xs, --text, --text-3, --warn
- **built-from**: Avatar Stack
- **added**: 2026-10-06
- **changed**: 2026-10-07
- **notes**: 2026-10-07 (DEC-118): the bar counts the systems work moved on this week (a single-system tender: its sub-systems), no longer the people active — it was the last per-person activity figure. `.team-row`, Statistics › Project › The team (DEC-117): project management, system managers, contributors — then the activity bar (`.ta-bar`, untracked `--brand-blue` on `--panel-3`).

### Stacked Bar
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: with figures and legend (26px), clickable to its screen (`data-go`), thin (10px, no legend, when rows below carry the figures)
- **tokens**: --radius-md, --radius-pill, --radius-xs, --space-2, --space-4, --text-xs, --text-sm, --text, --text-2, --text-3, --accent, --ok, --ia, --warn, --human
- **built-from**: Status Dot (legend)
- **added**: 2026-09-30
- **changed**: 2026-10-06
- **notes**: `.sbar` + `.sbar-legend`, `stackedBarHTML(total, segs, route, thin)`. In use since 2026-09-30 without an entry (recorded 2026-10-06). 2026-10-06 (DEC-117): the thin variant, and `s-blue`/`s-slate` segments on the untracked `--brand-blue`/`--brand-slate`; `s-neutral` is the untracked `--line-2`; segment text hardcoded `#fff`. Used by Where the requirements are, What the open requirements are waiting on (thin) and Not compliant by gap strategy.

### System Manager Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: managed (avatar, name, bar allocated `--ok` + to validate `--accent`, done/total), gap (dashed empty avatar, "No manager yet" in `--warn`, "Cast one →" opens Team casting)
- **tokens**: --space-2, --font-mono, --text-sm, --text-xs, --text, --text-2, --text-3, --ok, --accent, --warn, --radius-pill
- **built-from**: Person Avatar, Progress Bar
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: `.sys-row`, Statistics › Allocation › By system, with its manager (DEC-117) — Load by system and Casting gaps in one, with the person in it. The block steps aside on a single-system (SIG) tender. Grid columns hardcoded; "Cast one →" on the untracked `--brand-blue`.

### Reallocation Breakdown
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: three figures (reallocated, kept as allocated, to decide — outlined and clickable while non-zero), reason rows, latest rows with a status pill (Reallocated / Kept / To decide)
- **tokens**: --space-1, --space-2, --space-3, --radius-md, --radius-pill, --panel, --text-lg, --text-sm, --text-xs, --text, --text-2, --text-3, --accent, --accent-soft, --ia
- **built-from**: Person Avatar, Progress Bar
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: `.ra-figs` / `.ra-why` / `.ra-row`, Statistics › Allocation › Sent back for reallocation (DEC-117). Reasons are `REASON_LABEL`, the same three as revue-documentaire.html and compliance.html. The status pill is yet another "small coloured status label" (see Status Pill); To decide on the untracked `--ia-soft`, Kept on `--panel-3`, reason bars on `--brand-blue`.

### System Answers Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: late (red "N late · Nd"), all in (green "✓ all in"), open (grey "N open"); system (code in the mono face) or sub-system (a single-system tender)
- **tokens**: --space-2, --font-mono, --radius-pill, --text-sm, --text-xs, --text, --text-2, --text-3, --ok, --warn
- **built-from**: Progress Bar
- **added**: 2026-10-06
- **changed**: 2026-10-07
- **notes**: Renamed 2026-10-07 from Person Answers Row (DEC-118): one row per system, or per sub-system on a single-system tender — never per person; no avatar. `.ans-row`, Statistics › Compliance › Answers by system: late first, then by share answered. Late is `OVERDUE_BRANCHES` counted under its `unit` — the same entries the "contributor response overdue" card names, because there someone has to be reminded. Grid columns hardcoded (64px/1fr/44px/70px). The list wrapper is now `.st-list`, shared with the Risk Summary Rows.

### Waiting Queue Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: on a contributor (`--brand-blue`), on the client (`--brand-slate`), on your decision (`--ia`), not assigned yet (`--line-2`)
- **tokens**: --space-2, --space-3, --text-lg, --text-sm, --text-xs, --text, --text-3, --warn, --ia
- **built-from**: Status Dot
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: `.wo-row`, Statistics › Compliance › What the open requirements are waiting on, under a thin Stacked Bar (DEC-117) — replaces Consolidation, Bottleneck Row and Q&A Blocked Row. One requirement, one queue (a branch sent back first, then the client, then a contributor). Queue colours on the untracked `--brand-blue`/`--brand-slate`/`--line-2`; dot 10px hardcoded.

### Risk Summary Row
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-2, --font-mono, --text-sm, --text-xs, --text, --text-2
- **built-from**: Person Avatar
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: `.rk-row` in a `.st-list`, Statistics › Compliance › Risks (DEC-117): the four most-linked risks — ID, "There is a risk that…", who raised it, ×links; opens the Risks page.

## Organisms

### App Header
- **level**: organism
- **file**: accueil.html, creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html, risks.html
- **variants**: home (logo + reset + primary CTA + avatar), wizard (logo + static crumb + cancel), workspace (logo-link + crumb + nav/icon buttons + avatar), review (adds mode-switch, version pill), compliance (adds Demo Role Switcher, Icon Cluster, Export)
- **tokens**: --space-4, --space-5, --panel, --line
- **built-from**: Brand Logo, Primary Button, Ghost Button, Icon Button, Nav Button, Demo / Prototype-Only Control, Header Avatar, Breadcrumb, Tab Bar / Segmented Control, Notification Dot
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09: opens on the Brand Logo, a rule, then "SRM" in text — the Logo Mark is gone from the header (it stays the favicon), so the note below about re-embedding the SVG logo now applies to the Brand Logo's two PNGs. Fixed 52px height, consistently hardcoded across every screen (the app's one real cross-screen consistency win). Horizontal padding still drifts (`--space-5` in accueil.html vs `--space-4` elsewhere). Every screen re-embeds the same base64 SVG logo (light+dark variants) inline rather than sharing one asset.

### Triage Bar
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: with/without "pending reassignment" pill, % allocated (revue-documentaire.html), assignment total (compliance.html); opens with the screen's title (Page Title, `.tri-title`)
- **tokens**: --space-1, --space-3, --space-4, --radius-pill, --warn, --ia, --human, --ok, --accent, --font-mono, --text-sm, --text-2, --text
- **built-from**: Progress Bar, Filter Pill / status-count pills, Tab Bar, Ghost Button, Kbd Key
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-012) compliance.html: a contributor-only "My system" pill (`#tp-mine`, `.tpill.p-mine`, `--accent`), off by default, narrows to their system and combines with the status pills; counts cover the whole project. 2026-10-09 (legacy cleanup): unused `.triage` CSS removed from qa.html and documents.html (they have no triage bar), and compliance.html's `.triage-right`. 2026-10-06: starts with the screen's title and a separator (Allocation, Compliance) — they had their own row above the toolbar; compliance.html adds "N assignments" (`.tri-assign`) after "consolidated". 2026-10-01 (revue-documentaire.html): "N requirements" is followed by `.alloc-pct` — a 64px mini bar (`--ok` on the untracked `--panel-3`, 6px height and 6px gap hardcoded) and "<b>N%</b> allocated", allocated over the requirements the viewer can see, computed in `renderTriage`. 2026-09-24 (compliance.html): the 120px bar + "N/M consolidated · % · assignments answered" became a 16px ring (`.p2-ring`, conic-gradient, mask radial hardcoded 4/5px) + "N/M consolidated", the rest in its tooltip; the "By section / By contributor" switch and the shortcut hints are removed; a "⚑ set aside" pill (`.p-aside`, contributor only) filters to the viewer's set-aside assignments. `.triage`, fixed 42–44px height. Both screens independently implement their own `.tpill` rather than sharing one, despite driving the same five/six-state status vocabulary as Status Pill.

### Left Navigator Panel
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: "By section" (Nav Tree Item groups), expanded/collapsed (hardcoded 22px rail), Outline / Changes tabs (revue-documentaire.html, Document view, when a document has an earlier version), collapsed rail with a Changes marker
- **tokens**: --space-1, --space-2, --space-3, --line, --panel
- **built-from**: Search Box, Nav Tree Section Header, Nav Tree Item, Panel Toggle Chevron, Tab Bar, Changes Navigator
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): compliance.html's "By expert" mode is removed with the Expert Card — nothing could open it since the By section / By contributor switch went (2026-09-24). 2026-10-07 (DEC-119): in the Document view the navigator has two tabs — Outline (the tree, its search, Add document, the count) and Changes (the Changes Navigator). Folded to its rail (it folds for the table), it still shows the number of changes and a vertical "Changes" (`.nav-rail-chg`), which opens it on that tab. The outline tree is not rebuilt while the Changes tab is open (scale check). Marker padding and the count's 16px min-width hardcoded. `.nav`. Fixed width (264px) hardcoded. revue-documentaire.html starts fully collapsed by design — a code comment notes real capture data "runs to dozens of sections" and a wide-open tree was unusable at that scale.


### Changes Navigator
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: changes listed, filtered (one kind — added, modified, removed — or the changes that reopen an answer, with "show all N"), no change in the range, document with one version only (says so)
- **tokens**: --space-2, --space-3, --space-4, --radius-sm, --text-xs, --text-sm, --text, --text-3, --warn, --accent
- **built-from**: Compare Summary Chip, Change List Card, native selects (`.nc-select`)
- **added**: 2026-10-07
- **changed**: 2026-10-07
- **notes**: DEC-119, replaces the Compare Bar. `#nav-changes`, `renderNavChanges()`: the Document view's Changes tab in the Left Navigator Panel — the document (versions belong to documents, DEC-069; one at a time, DEC-070), the earlier version compared with "→ vX · in force", the counts, how many changes reopen an answer already given, "Change k of n" with ‹ › (and ] / [ on the keyboard), then a Change List Card per change. The paper shows each change in place and removed requirements where they were; the details panel stays the selected requirement's and opens on its Versions tab. Internally the lens is still `state.mode === "compare"`, so the paper's rendering did not change. The list keeps its scroll when re-rendered and brings the current card into view. Scale check (2026-10-07; one document of 1,000 then 4,000 requirements, 431 then 1,681 changes): the type pills and the "reopens an answer" line filter the list and what ] / [ walk through (`state.ncFilter`, `ncItems()`); a change picked on the paper becomes the current one; ~150–170 ms per click at 4,000 requirements, once the hidden table and outline stopped being redrawn and block lookups were cached (they were 1.1 s). `.nc-select` is its own select styling, not the Select Dropdown atom's. Depends on untracked `--panel-2`, `--line-2`, `--warn-soft`.
### Requirement Table (Review Grid)
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: document-order, sorted, grouped-by-activity, filtered-to-selection, wrap-text, scale-test (revue-documentaire.html — 12,000-row virtualized mode)
- **tokens**: --space-3, --space-5, --radius-lg, --line, --panel, --accent-soft
- **built-from**: Requirement Row, Branch / Allocated-Activity Sub-row, Grid Section / Group Header, Filter Toolbar, Bulk Selection Action Bar, Checkbox, Custom Column Cell, Custom Column Header Cell, Changes Cell, Version Picker Button, Version Picker Popover
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-012, DEC-025) revue-documentaire.html: a contributor sees every row (counts, advanced filter and export cover the whole tender); rows not on their system stay locked (`is-ro`); `visibleTo()` became `isMine()` ("can I change this"); N goes only to their own items. An entry with no person no longer makes a row Incomplete. compliance.html: the contributor's table also covers the whole project, other systems read-only. 2026-10-09 (legacy cleanup): compliance.html gets the `.no-select` rule that `table-engine.js` puts on the body while rows are drag-selected (the text was selected along with them). revue-documentaire.html: "Show only selected" builds its empty column filters from the live keys (`emptyColFilters()`), so the Changes and custom list columns keep their funnel — a fixed list without them made those funnels throw; sorting on a column resets the group-by control in the Filter Panel (`#pf-gseg` — it pointed at a `#gseg` that no longer exists). revue-documentaire.html (2026-10-07, DEC-119): a Changes column (key `chg`, right after Requirement) — see Changes Cell. Its header carries the all-rows Version Picker Button and a column filter (Modified / Added / No change, against each row's own compared version); shown by default when a document has an earlier version, hidden otherwise; C shows or hides it, as does the View menu. Scale check (2026-10-07): the table is not rebuilt while it is hidden — `renderReview()` returns early outside Review (the selection bar still hides), and Review redraws it on the way in; that was ~0.4 s of every click in the Document view at 1,000 requirements. Known cost, untouched: every refresh rebuilds every row with complete ABS / PBS / assignee selects — ~650 ms per click on a 1,000-requirement SIG tender (67,689 `<option>`s), ~135 ms on STB-2026's 825. compliance.html (2026-09-24): the "Sort: …" dropdown is gone — every column header sorts, custom columns included (`F_SORT_KEYS`, `setSortCol()`, `bindSortHeaders()`): ▲ then ▼ then back to document order, with "↺ Document order" in the toolbar while a sort is on, same behaviour and CSS as Allocation; with no sort the document titles and section headings show. The "action needed first" order has no header equivalent and went with the dropdown. `.rgrid`. Explicitly documented in both screens as the same interaction engine (`table-engine.js`) — per-column sort/filter, drag-select across the selection gutter, keyboard active-cell navigation — with only column config differing per screen. Keyboard (revue-documentaire.html, 2026-09-23): ←/→ follow the DRAWN column order (pinned three + `state.colOrder`, so View-menu reordering and custom columns are honoured — it used to be a fixed list); Enter or F2 on the active cell starts editing it; focusing a control inside a cell makes that cell the active one. compliance.html (2026-09-23): a click on a header cell no longer toggles its column hidden — a leftover from when a collapsed column stayed as a clickable sliver; since columns are fully removed (`display:none`), one click made a column vanish with nothing to click it back. Hiding goes through the View menu only, as on Allocation. Both screens (2026-09-23): columns are resizable from a handle on each header's right edge (Column Resize Handle); a dragged width is a fixed px value, so the Requirement column stops being the flexible one until its handle is double-clicked. `--rgrid-cols`/`--frgrid-cols` widths are hardcoded px/fr values. Allocation's table has no Nature column (DEC-074): a block's nature (Information / Heading / Requirement) is read and changed in its details.

### Document Reading View
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: single document, filtered by document, change-annotated (the navigator's Changes tab — Compare mode until 2026-10-07 — revue-documentaire.html only)
- **tokens**: --space-6, --space-8, --paper, --paper-ink, --font-doc, --text-base, --text-xl
- **built-from**: Document Block, Status Dot
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-012): the whole tender for every viewer — no hide or redact mode (the shell's `getRedactMode` is gone). 2026-10-09 (legacy cleanup): revue-documentaire.html's page header names the open tender (`docTitleHTML()`, name and reference from the shell) — it said STB-2026 on every tender. compliance.html draws one sheet per source document under its own name (was one sheet titled "Technical Requirements Specification"), subtitled "Compliance synthesis — consolidated verdicts over the source text · read-only", with a Compliant / Not compliant / Pending legend. 2026-10-07 (DEC-119): no Compare mode any more — the change-annotated paper is the Document view with the navigator on Changes (Changes Navigator). `.doc-scroll`/`.paper`. Deliberately a fixed light "page" regardless of app theme (`--paper`/`--paper-ink` are identical in both theme blocks). Width, padding, and box-shadow all hardcoded.

### Partner Verdict Entry
- **level**: molecule
- **file**: compliance.html
- **variants**: verdict not chosen (green / red), Compliant (their answer as received + confirm), Not compliant (Category + Topic + their answer + confirm)
- **tokens**: --ok, --warn, --partner, --partner-soft, --radius-md, --text-sm, --space-3
- **built-from**: Inline Form Shell, the Decision Panel's choice / confirm buttons (`.dp-c`, `.dp-confirm`, `.dp-picked`), Textarea, Select Dropdown
- **added**: 2026-09-24
- **changed**: 2026-09-24
- **notes**: SPEC-external-partners.md §3, DEC-082. In the project manager's Assignment tab of a branch on a partner system: a `.partner-box` explains who answers, then the PM records the partner's verdict at system level; it consolidates like any other. The answered view labels the response "entered by the project manager from <partner>'s reply" — the provenance is read from the system, no marker field (§6.1 option b). `--partner` is not on the tracked scale.

### Turnkey OBS List Setting
- **level**: molecule
- **file**: dashboard-et-config.html
- **variants**: Turnkey tender (shown), any other line (hidden)
- **tokens**: --font-mono, --text-xs, --line-2, --radius-xs, --text-3, --space-2, --space-3, --partner, --partner-soft
- **built-from**: Text Input (`.inp`), Ghost Button, Activity / Requirement Tag (as `.pt-tag`)
- **added**: 2026-09-24
- **changed**: 2026-09-24
- **notes**: `renderPartnersSetting()`, in Settings › Allocation model. Lists the model's 16 systems (neutral, not editable) then the added ones (`.pt-tag.partner`), with a name field and "＋ Add"; the code is derived from the first word of the name. Stored in the shell (`window.getPartners` / `window.addPartner`, reset with the demo). A ✕ on each added partner removes it while no requirement is assigned to it (DEC-093); otherwise it says how many to reassign. Usage is reported to the shell by Allocation and Compliance (`reportPartnerUsage`), seeded for the demo partner. The added tags use `--partner` / `--partner-soft`, declared in this file too — not on the tracked token scale.

### Decision Panel
- **level**: organism
- **file**: compliance.html
- **variants**: verdict not chosen (green / red choices), Compliant chosen (comment + confirm), Not compliant chosen (Gap Editor, then Category + Topic on a Turnkey tender only, comment, confirm), ask form open, return form open, question pending (banner), original language shown, a resource open (Q&A, Similar, REX, Chat), set aside, wide
- **tokens**: --paper, --paper-ink, --font-doc, --text-lg, --text-sm, --text-xs, --ok, --warn, --accent, --accent-soft, --line, --radius-md, --radius-sm, --radius-pill, --space-2, --space-3, --space-4, --space-5
- **built-from**: Reassignment Request Form, REX Match Item, Compliance Pill, Tab Bar (`.dp-res-tabs`)
- **added**: 2026-09-24
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-121, DEC-122): a reopened assignment says "Reopened by <doc> vX"; Q&A states come from the shared register (To send / Sent / Answer to confirm / Answered, `qaStLabel()`), with the client's answer. 2026-10-09 (legacy cleanup): a question's state uses the Q&A screen's words — To send / Sent / Answered (it said Draft / Internal review / Sent to the client). 2026-10-07: a contributor arriving on Compliance — or switching to another contributor — lands on the first assignment of their queue with this panel open, instead of an empty "No assignment selected"; never when something is already open. 2026-10-06: the Confirm button (`.dp-confirm`, also the partner-verdict form's) is pinned to the bottom of the panel while its place is below the fold — a Not compliant's strategy and risk pushed it ~750px down at 1280×600; a ring in `--panel` (hardcoded 8px) masks what scrolls behind it. 2026-09-30 (SPEC-risks.md, DEC-105 to DEC-108): Not compliant opens the Gap Editor first; Category + Topic only on a Turnkey tender (DEC-107), Topic required there only; confirming never waits on a strategy or a risk (DEC-108); confirming Compliant clears any strategy/risk picked. The reassurance line now says the strategy decides what the client is told. 2026-09-29 (DEC-092): several questions can be open on one assignment; the banner lists them all and says they don't hold the verdict up. 2026-09-24, second review: Set aside / Widen buttons moved above the ID and § line; the requirement text sits on a tinted `--accent-soft` block with an `--accent` left edge (`--ia` when the original is shown); beside "View in the document" an on/off switch "Original · French" (Toggle Switch) shows the tender's own wording when its language isn't English (`r.textOriginal` — demo French originals written for the seeded STB-2026 requirements, composed for generated ones); the verdict choices are filled green and red again; Ask the client / Not mine use `.propose-btn`, Allocation's reassignment button; Q&A items are one column — id + status pill, question, answer, then "Asked by … · date"; set aside uses `--human` (violet) for the pill, the row's tinted ID cell and the button. `renderDecisionPanel()` / `.dp`, SPEC-compliance-decision-panel.md, DEC-079. Replaces the Detail / Assignment Panel when a contributor opens an assignment of their own that waits on their verdict (`isDeciding()`); the project manager's panel and every other state keep the old one. Revised 2026-09-24 (user review): the verdict is a choice first — "✓ Compliant" / "✕ Not compliant" — then only that choice's fields and one "Confirm — …" button, with "Change" to go back (no longer a Compliant button beside an open Not compliant); set aside and widen are labelled pill buttons ("⚐ Set aside", "⇤ Widen panel"); the "Yours · system · person" line is gone; a "Requirement" label heads the text and "📄 View in the document" under it switches to the Document view at that block without leaving the panel (the § link does the same); "⇗ Ask the client" opens a question form (required text) that files the question in the Q&A register, and the contributor keeps the panel and can still decide while it waits (awaiting_qa counts as deciding, with a banner); the Document resource tab became Q&A — our questions on the requirement with their status and answer, then the client's published answers to other bidders' questions (`PUBLISHED_QA`, demo data). Q opens the ask form. Earlier layout, top to bottom: queue progress ("N left · this is k of N · n set aside", Next ›), id + clickable § section + set-aside ⚐/⚑ (S) + widen ⇤, one "Yours · system · person" line, the requirement text in full on paper (`pre-wrap`, dominant), the decision zone (reassurance line on internal vs client verdict, comment, "✓ Compliant" one gesture / "✕ Not compliant…" then Category + Topic then "✕ Not compliant"), two quieter secondary actions ("⇗ Ask the client", "↩ Not mine — return it"), and resources as collapsed tabs. Drafts (pick, comment, category, topic) save on input into `window.parent.__cmpPersonal`, per viewer, so they survive leaving the panel or the screen (not a reload of the whole app); set aside is kept there too, personal, shown as ⚑/✎ on the row's ID cell. Similar = word-overlap stand-in (three best ≥ 25 %) for the platform's similarity capability. Wide = `min(720px,62vw)`. Hardcoded: button text `#fff`, Next hover, the 52px progress bar, `padding:10px` on the verdict buttons. Depends on untracked `--panel-2`, `--panel-3`, `--line-2`.

### Validate Zone
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: single system (one validation), several systems (one per system), Turnkey routing ("Validate & send to the systems"), contributor's own system, disabled with its reason, allocated; pinned (its place below the fold) / in flow
- **tokens**: --ok, --line, --panel, --radius-md, --text-xs, --text-3, --space-2, --space-3
- **built-from**: Primary Button (`.validate-cta`), Ghost Button (`.mini-btn`), Activity / Requirement Tag
- **added**: 2026-09-24
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-025): a missing person never disables validation — an informative note under the open button (`unassignedNoteHTML()`, reusing `.validate-why`; inline on per-system rows): "No one assigned yet — you can still validate; the system's contributors can answer." or "k of m … with no one assigned". The disabled reason reads "Allocation incomplete — complete ABS / PBS / OBS first." Correction 2026-10-09: "Distribution across systems", named below as following the zone in the contributor's panel, was already gone (see Derivation Chain) — the zone precedes custom fields. 2026-10-06 (audit, short screens — at 1280×600 the panel shows ~350px under its header and the button was 224–870px of scroll down): `.validate-zone` wraps the button (and its reason) in every view. It sits right after the data it confirms — Turnkey PM: under the System field, before the Systems follow-up cards; contributor: after their allocations, before custom fields and "Distribution across systems"; other PM panels: after the allocations / Assigned to, before custom fields — and `position:sticky; bottom` keeps it pinned to the bottom of the panel while that place is below the fold, one button, no copy. A done step (`.is-done`) is a status line, not pinned. Hardcoded: `bottom:-16px` and the -16px side margins mirror `.set-body`'s 16px padding; padding 10px/14px. "Source section" left the detail panel at the same time — kept only when the header has no § link (`sourceFieldHTML`). 2026-09-29 (DEC-104): on a Turnkey tender the PM's button validates the routing only ("✓ Validate & send to the systems"), disabled while a reassignment is pending; each system is validated from its own detail — by its contributor (who now has the button on their own system, replacing "never in the contributor's view" below) or the PM. A system with missing data (a no-model system starts empty) is Incomplete and shows the button disabled with its reason. 2026-09-29 (DEC-099): one button per requirement — "✓ Validate & send to Compliance" validates characterisation and allocation together; with several systems, one "Validate & send" per system, each also validating the characterisation. Not shown in the read-only view (DEC-100). `validateCtaHTML()`, at the bottom of the detail panel — now also in the Turnkey project manager's view, which never had it; never in the contributor's view (validating sends to Contributor Review, a PM act). Not recorded before; reworked when the user found the button missing (DEC-084): it treated every requirement with a branch as multi-system, so after the characterisation a single-system requirement showed only a hint. A step that can't run shows its button disabled with the reason underneath instead of a live button that fails on click. Reads the allocation status through `allocHolder(b)` — the single branch when it carries one. Same action as the row's status pill and the V key.

### Detail / Assignment Panel
- **level**: organism
- **file**: compliance.html, revue-documentaire.html
- **variants**: empty state, requirement (multi-tab), text-block/heading (reduced fields), multi-allocation admin view, multi-allocation manager view (own branch only)
- **tokens**: --space-3, --space-4, --line, --accent, --panel
- **built-from**: Detail Field / Frozen Field, Status/Verdict Pill, Manager Assignment Card, AI Suggestion Card, Allocated-Activity Detail Card, Propose/Reassign Form / Inline Form Shell, Activity Timeline Entry / Timeline Item, REX Match Item, Role Recap Row, Comment Composer
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-012/100) compliance.html: a contributor can open other systems' assignments, read-only — next-step text "Read only — <SYS>'s assignment…", no reminder, reallocate, ask or set aside; they land on their own assignment first (`select()`). 2026-10-09 (DEC-121, DEC-122, DEC-125) compliance.html: "Ask the client" is disabled once the verdict is given (`.cta:disabled`, opacity .45 hardcoded; tooltip `ASK_DONE_TIP`), and the Q key answers with the same reason; "Send a reminder" shows only on an assignment still owed by its contributor (awaiting answer or Q&A), never to that contributor; the Awaiting-Q&A block is "Question to the client" and lists each question's register status and answer; the Requirement tab says "Pending — X not answered yet" and opens on the awaiting-answer assignment first (`BLOCK_PRIORITY`). 2026-10-09 (legacy cleanup): compliance.html's leftover render branch for the Document tab (gone 2026-09-24) is removed; in revue-documentaire.html the person-proposal card and the Why Box are gone (see AI Suggestion Card and the Removed section), and selecting a requirement that isn't in the tender (a stale link) shows a toast instead of throwing. 2026-09-29: revue-documentaire.html gains a read-only mode for a contributor on a requirement that isn't theirs (`readOnlyReqHTML`, `.ro-note`, DEC-100; table rows locked by `lockForeignRows`), and the Turnkey system detail is now the SIG panel plus reassignment (DEC-101). compliance.html (2026-09-24): a contributor's own open assignment renders the Decision Panel instead. `.settings`. Fixed width (326px in revue-documentaire.html), narrows under a hardcoded breakpoint. The single largest, most role-branching render path in the app — output differs substantially by viewer role, block type, and branch count. compliance.html's version has an unbuilt Chat tab, present only as an empty-state stub per its own code comment.

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
- **built-from**: Advanced Filter Condition Row, Mini/Ghost Button, Cancel Button
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): Cancel and Apply are styled (Cancel Button, `.btn-submit.ok`), and so is the empty-state hint (`.field-hint`) — they rendered unstyled. `.adv-panel`, wider than Filter Panel (460px, documented in a CSS comment as needed for "field + operator + value in one row"). Draft/apply pattern edits a scratch object that only commits on Apply. Saved-filter persistence via `table-engine.js` (`TE.loadSavedFilters`/`saveSavedFilters`).

### Columns Panel
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-3
- **built-from**: Reorderable Column Row
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.view-panel#cols-panel`, reuses the Filter Panel's `.view-panel` shell with a single section.

### Export Options Modal
- **level**: organism
- **file**: compliance.html
- **variants**: format (Excel, CSV, PDF), rows (all, current view, selection — disabled when nothing is selected), columns (all, as in the table, one by one; custom columns tagged internal and unticked), requirement text language (original / English — non-English tenders only)
- **tokens**: --panel, --panel-2, --line, --line-2, --radius-lg, --radius-pill, --text-sm, --text-xs, --text-3, --accent, --space-2, --space-3, --space-4, --space-5
- **built-from**: Modal (`.overlay` + `.modal`), Segmented Control (`.gseg`), Checkbox, Radio, Custom Column Tag, Primary Button, Ghost Button
- **added**: 2026-09-24
- **changed**: 2026-09-24
- **notes**: `openExport()` / `renderExport()`, opened by Compliance's Export button (and the export-ready banner). It used to generate one fixed register straight away. Generation is still a toast in the prototype (file name, rows, columns, risk summary, a warning when internal custom columns are included, the text language). Columns ticked by default follow what's visible in the table. Modal backdrop `rgba(6,8,12,.7)` and shadow hardcoded. Depends on untracked `--panel-2`, `--line-2`.

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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-012): revue-documentaire.html drops rows not on the contributor's system from bulk validate, mark to review, add system and re-run (`keepOwnSelection()`), with "k selected requirements are not on your system — left as is". 2026-10-09 (DEC-123, DEC-125): revue-documentaire.html's Assign writes the person to the OBS entries of their own system in each selected requirement (`setAllocManager`) and says how many were skipped; compliance.html's Send reminder reminds only eligible assignments, reports the skipped ones, and is hidden for a contributor. 2026-10-09 (legacy cleanup): adding a system to the selection creates each requirement's row for it (`syncBranchesFromPerim()`) — the tag appeared without the system's allocation row. `.sel-bar`, explicitly documented as shared between these two screens' tables. revue-documentaire.html's bar carries a Re-run menu (`#sel-rerun-menu`); since 2026-09-23 it skips information blocks and headings and counts them apart ("N not requirements") instead of deriving onto them. Fixed to viewport bottom (24px) — a code comment explains centering via `margin-inline:auto` was chosen deliberately over `left:50%;translateX(-50%)` to avoid capping width at half the viewport. Its Assign menu lost the "PBS" field that set Functional / Performance / Security / Interface / Regulatory on the selection (DEC-074) — it now holds Assigned to and System.

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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-122) compliance.html (its own drop, not this entry's revue-documentaire.html one): a new item, "N answers reopened by a new document version", filters to those requirements. `.notif-drop`, positioned with hardcoded absolute offsets tied to the current header layout rather than anchored to its trigger button.

### View-As Switcher
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: admin, as-contributor (orange tint), open
- **tokens**: --space-2, --radius-md, --ia
- **built-from**: Icon Button, Person Avatar
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-012): previewing a contributor no longer narrows anything — they read the whole tender and change only their system. Active class renamed `as-contributor` (was `restricted`), and the page-wide banner is now `.viewas-banner` (`#viewas-banner-text`, `#viewas-exit`, eye icon): "Viewing as <name> — contributor on <SYS>: everything is readable, only <SYS> can be changed." (`--ia-soft`, rgba border, off-scale). The toast is "Viewing as <name>". `body.as-contributor` still hides custom-column editing and Classify. 2026-10-09 (legacy cleanup): the preview survives a switch between Table and Document (`setMode()` re-applies `restricted` — the banner went, and custom-field editing and bulk Classify came back for the contributor), and its wording says contributor, not manager. 2026-09-29 (DEC-102): lists only the admin and the MANAGERS entries flagged `viewAs` — one SIG contributor (Louis Renaud) and one SEN contributor (Paolo Ferri); compliance.html's `#f-viewer` select applies the same filter. `.viewas`/`.viewas-menu` + the page-wide `.restrict-banner` it toggles. Demo-only "preview a manager's restricted view" — drives redaction in the Document Reading View and filtering elsewhere.

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
- **changed**: 2026-10-06
- **notes**: 2026-10-06: headed by a Home Section Head ("My tenders · N tenders") under the Onboarding Line; a card opens through `openTender()`, shared with the Continue Card. Grid `minmax(330px,1fr)` hardcoded.

### Tender Card
- **level**: molecule
- **file**: accueil.html
- **variants**: default, processing (pulsing "Processing — opens when it completes" in the footer), submitted (dimmed, last station ticked), demo-only
- **tokens**: --panel, --line, --radius-lg, --space-3, --space-4, --accent
- **built-from**: Product Line Badge, Role Chip, Tender Line (mini)
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (colour pass): "Processing" in the second blue. 2026-10-06 (later): rebuilt around what a tender asks of you — top row: the Product Line Badge, the reference, your Role Chip on the right; then the name in the heading face, the line, the footer. The stage pill (Allocation / Compliance / Processing / Submitted) and the two plain rows (product line with a bar, role with a dot) are gone: the line carries the stage, the badge and the chip carry the rest. 2026-10-06: its gauge is the Tender Line in miniature (`gaugeHTML()`), replacing the Allocation / Compliance progress bar and the submitted card's text line; the processing label and "Response submitted" moved to its tooltip. `min-height:172px` and hover `translateY(-2px)` hardcoded. Listed at molecule level (assembles several atoms into one repeatable card) even though it sits inside the Tender Dashboard Grid organism above.

### Product Line Badge
- **level**: atom
- **file**: accueil.html
- **variants**: Turnkey (navy), SIG (the second brand blue), every other line (slate)
- **tokens**: --accent, --radius-xs, --text-xs
- **built-from**: none
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: `.pc-lineb` — the tender's product line as a metro-line badge, filled in the brand navy; blues only, one per main product line, so they never read as a status colour. Lighter after review (2026-10-06): Medium weight, 0.9px tracking, 20px high, 7px side padding — bold uppercase read as coarse. Hardcoded height, padding, tracking and white text.

### Role Chip
- **level**: atom
- **file**: accueil.html
- **variants**: project manager (flag icon, `--accent` on `--accent-soft`, outlined), contributor (people icon, the second brand blue on its pale tint)
- **tokens**: --accent, --accent-soft, --text-2, --radius-pill, --space-3, --text-sm
- **built-from**: Icon
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (colour pass): role colours shared with the Onboarding Line — project manager navy, contributor blue. `.pc-role` — your role on the tender, on the right of the card's top row. Depends on untracked `--panel-3`; hardcoded 26px height and 1.5px outline.

### Home Hero
- **level**: organism
- **file**: accueil.html
- **variants**: with / without a tender to pick up again; no tender yet (roles line says so)
- **tokens**: --panel, --accent-soft, --accent, --brand-red, --line, --radius-lg, --space-2, --space-3, --space-5, --space-8, --text-xs, --text-sm, --text-lg, --text-2, --text-3, --font-heading
- **built-from**: Page Title, Primary Button, Ghost Button, Continue Card
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (colour pass): the kicker and the first name in the second brand blue; the hero fades from `--panel` to the pale blue; the map's three lines in navy, the second blue and the brand red, more present. The page above the hero takes a pale-blue wash (`.scroll` background, `local`). Uses the untracked `--brand-blue`, `--brand-blue-soft`, `--brand-slate` (accueil.html only, both themes, not on the tracked scale). The home page's front door: a kicker, a time-of-day greeting with the user's first name (the Page Title, at a hardcoded 32px — above the type scale), what SRM is for in one sentence, the user's roles counted from their tenders, New tender / How SRM works, and the Continue Card. Background: a hardcoded 115° gradient from `--panel` to `--accent-soft`, and `.hero-map`, an inline SVG metro map in the brand's colours (navy and red lines, 45° bends, an interchange) — decorative only, the red never on anything clickable (DEC-063). Hardcoded line widths, opacities and positions in the SVG; below a 1220px viewport there is no room beside the Continue card: the card moves under the greeting and the map (440px) fills the free corner beside it, clear of the text.

### Continue Card
- **level**: molecule
- **file**: accueil.html
- **variants**: Allocation next (requirements still to allocate), Compliance next (requirements still to answer)
- **tokens**: --panel, --line, --accent, --radius-lg, --space-3, --space-4, --space-5, --text-xs, --text-sm, --text-lg, --font-heading, --font-mono
- **built-from**: Tender Line (mini), Primary Button
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (colour pass): a 4px navy-to-blue bar along its top edge. "Pick up where you left off": the primary open tender (else the first built-out one) with its line and the next thing to do; the whole card opens the tender. Hardcoded shadow `0 10px 30px rgba(14,30,50,.10)`.

### Onboarding Line
- **level**: organism
- **file**: accueil.html
- **variants**: shown / dismissed ("Got it — hide"; "How SRM works" in the hero reopens it)
- **tokens**: --bg, --accent, --accent-soft, --radius-lg, --radius-pill, --space-1 to --space-6, --text-xs, --text-sm, --text-lg, --text-2, --text-3, --font-heading
- **built-from**: Home Section Head
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (colour pass): the line runs from the second brand blue to navy, the station dots step along it (`color-mix`), the way a tender moves on; the who-tags take the role colours — project manager navy, contributors the second blue — the same code as the Role Chip. 2026-10-06 (later): no frame any more — the section sits on the page, the stations ringed in `--bg`; the who-tags take `--radius-md` and balance their wrap, so a two-line tag on a narrow window stays a block, not a pill. "How a tender travels through SRM": the four stations of the Tender Line, numbered, each with one sentence and who does it, then the always-open screens. Dismissal is kept in the shell (`getHomeIntroHidden` / `setHomeIntroHidden`) so it survives navigation and a demo reset brings it back. Hardcoded 30px stations and 5px line.

### Home Section Head
- **level**: atom
- **file**: accueil.html
- **variants**: with a hint; with an action on the right
- **tokens**: --text-lg, --text-sm, --text-3, --space-3, --font-heading, --brand-red
- **built-from**: none
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: 2026-10-06: carries the brand's red mark, smaller than the page titles' (4px), decorative only. `.home-sec` — one heading style for the home page's sections (How a tender travels, My tenders).

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

### Reassignment Request Form
- **level**: organism
- **file**: compliance.html
- **variants**: contributor-initiated (radio reasons + conditional picker), manager-handling (reallocate-to form)
- **tokens**: --warn, --radius-md, --space-2, --space-3, --text-sm
- **built-from**: Inline Form Shell, Detail Field, Select Dropdown, Textarea
- **added**: 2026-09-01
- **changed**: 2026-09-24
- **notes**: Since 2026-09-24 the contributor-initiated variant opens from the Decision Panel's "↩ Not mine — return it" (submit reads "Return it"). Reuses Inline Form Shell for two distinct flows depending on context.

### Activity Timeline
- **level**: organism
- **file**: compliance.html
- **variants**: none
- **tokens**: --text-3
- **built-from**: Timeline Item
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06: drawn as a vertical rail line — see Activity Timeline Entry. 2026-10-01: one log per requirement, shared by Allocation and Compliance through the shell (`logReqEvent` / `getReqLog`) — explicit events where they happen, every field change caught by diffing a snapshot at each refresh, plus what each screen derives (capture, document versions, an answer on record). A category filter on top (All · Status · Allocation · Compliance · Comments, with counts) and a comment field that writes to the log — Compliance gained both, and its Activity tab now shows on SIG tenders too. The four milestones of a requirement's life are marked in the feed rather than as a separate timeline. Replaces the fabricated lines (fixed date, fixed author) and the per-screen `branchLog`. `.log-filter`, `.log-comment`. `.timeline`, shown only in the Detail Panel's Activity tab.

### Global Header Bar
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-4, --panel, --line
- **built-from**: Breadcrumb, Nav Button, Demo / Prototype-Only Control, Ghost Button, Icon Button, Notification Dot, Header Avatar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: Same App Header pattern as every other screen — kept as a separate entry here only because the dashboard scan named it distinctly; see App Header (above) for the merged cross-screen record.

### Tender Line
- **level**: organism
- **file**: accueil.html
- **variants**: mini (tender card and Continue Card: dots and the four station names, the current one with its count); station states done, current, future
- **tokens**: --accent, --accent-soft, --line, --line-2, --panel, --panel-2, --ok, --ok-soft, --warn, --text, --text-2, --text-3, --font-heading, --text-xs, --text-sm, --text-lg, --text-xl, --radius-pill, --space-1, --space-2
- **built-from**: none
- **added**: 2026-10-06
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (final): the dashboard variant is gone (see Removed) — only the mini line on the home page remains. 2026-10-06 (reworked after review): on the dashboard the open line drawing became four station cards on a rail — it was too tall for what it said and not obviously clickable. Each card is a button that says how to open its screen; the rail shows in the gaps, navy as far as the tender has gone. About 105px high instead of ~190. Hardcoded: 18px dots, 4px rail at 25px, 3px bottom progress edge, card shadow. The process as a rail line — the brand's own world, and the step navigation: Capture → Allocation → Compliance → Submission, each station a button that opens its screen (Submission none). Between two stations the line fills with the share of requirements already past the first. `renderTenderLine()` (allocation progress from the shell when Allocation has run, Compliance from the FOLLOWUP_REQS mirror, `TENDER_DEADLINE_LABEL`); `gaugeHTML()` for the mini. Replaces the two-card Phase Rail. Mini: hardcoded 12px dots, 4px segments, 25%-per-segment geometry.

### Phase Rail
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-5, --text-3, --text-lg
- **built-from**: Phase Card (step variant)
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06: removed for the Tender Line (a rail drawing, then four station cards) and restored on review: Capture is automatic and Submission is the project's end, so neither is a screen to open; the days left are already in the hero. `.phase-rail`, 2-column grid with a hardcoded `→` connector glyph.

### Support Rail
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: --space-3
- **built-from**: Phase Card (support variant)
- **added**: 2026-09-01
- **changed**: 2026-10-07
- **notes**: 2026-10-07: each card reads on two short lines — name, then its figure — instead of one shared line that cut both at four cards a row ("Team ca… 5 / …", "Documents & ver… 3 docs · 1 …", even at 1440px). 2026-09-30: a fourth card, Risks (SPEC-risks.md §6) — number of risks in the shell's list; the grid is 4 columns now. `.support-rail`, 2-column below a hardcoded 1000px breakpoint, hosts Team casting / Documents / Risks / Q&A cards.

### Dashboard Attention Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: none beyond its parts
- **built-from**: Count Badge, Attention List Item
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-122): the new-version item is built from what Documents & versions recorded for this tender (`getVersionChanges()`): document, version, gap and the answers Compliance reopened — it said "v2.2 · +2 ~1 −0 · SRM-00009" whatever was uploaded, on every tender. 2026-09-30: the Not compliant item reads Compliance's totals once available — "N Not compliant verdicts", and how many still lack a risk or a strategy — instead of "declared Compliant to the client". `.att-card` ("What needs you now"), 5 items conditionally gated by phase.

### Project Health Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: none beyond its parts
- **built-from**: Stat Tile / Card (Health Stat Tile variant)
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.health-stats` grid, gap hardcoded 14px.

### Experts Summary Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: none beyond its parts
- **built-from**: Compact Expert Line
- **added**: 2026-09-01
- **changed**: 2026-10-07
- **notes**: 2026-10-07 (DEC-118): titled "Answers by system" (by sub-system on a SIG tender) — it listed three people until then. 2026-10-06 (DEC-117): its rows come from the same figures as Statistics (see Compact Expert Line). Dashboard sidebar.

### Activity Feed Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: none
- **tokens**: none beyond its parts
- **built-from**: Activity Feed Item
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-122): the two version items are filled from the tender's last recorded upload (document, version, gap, reopened requirements); the reopened item is dropped when it reopened nothing. 2026-10-09 (legacy cleanup): 4 seeded items (2 still behind the v2.2 flag) — "Allocation milestone reached" went (no milestones, DEC-084) and the others describe what the prototype does (an answer reopened by v2.2, a question asked, a question marked as sent); the dead "View all" link is removed. "Recent activity" card, 5 seeded items, 2 gated behind a phase flag.

### Statistics Panel
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: Project tab (default), Allocation tab, Compliance tab
- **tokens**: --space-4
- **built-from**: Tab Bar, Stat Block, Key Dates List, Progress Trend Chart, Leaderboard Row, Team Role Row, Avatar Stack, Stacked Bar, System Manager Row, Reallocation Breakdown, Progress Sequence, System Answers Row, Waiting Queue Row, Risk Summary Row
- **added**: 2026-09-01
- **changed**: 2026-10-07
- **notes**: 2026-10-07 (DEC-118): no figure measures a person any more — the weekly ranking and the answers are by system and sub-system (sub-systems = the perimeters staffed in Team casting), "active this week" counts systems. People stay named only where the work needs it: who to remind for an overdue answer, who sent a requirement back, who raised a risk, who is staffed. 2026-10-06 (DEC-117): rebuilt — business only, people first; nothing measures the AI any more. **Project**: Timeline (Key Dates List + Progress Trend Chart), Most active this week (Leaderboard Rows), The team (Team Role Rows). **Allocation**: Where the requirements are (Stacked Bar), By system with its manager (System Manager Rows), Sent back for reallocation (Reallocation Breakdown), Work invalidated by a new version (only when non-zero). **Compliance**: Progress to the client (Progress Sequence, now opening on what the client will be told), Answers by person, What the open requirements are waiting on, Not compliant by gap strategy, Risks. Gone: Pass 1 → pass 2, Derivation quality (ring gauges), AI reliability, Load by system and Casting gaps (merged into By system), Consolidation, Assignment funnel, Late by contributor, Blocked on the client and Bottlenecks (merged into Waiting on), Compliance profile (a sentence of Progress to the client now). Sources: Allocation and the timeline read this screen's 14-requirement mirror — not Allocation's own report, which counts the capture's real requirements once Allocation is opened (DEC-098), so the phase card and Statistics can still disagree after that; the Compliance tab reads Compliance's totals (`getGapStats`) and the shell's risk list; history the backend doesn't keep (progress over time, each person's week, decided reallocations, answers per person at Compliance's 100 assigned / 58 answered) is hand-authored; the ranking adds this session's actions live from the shell's activity log (`getActivityLog`). 2026-09-30 (SPEC-risks.md §9): Progress to the client, Risks and Not compliant by gap strategy added to the Compliance tab — kept as they were by DEC-117, each now opening on its sentence. `.stats-panel`.
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
- **variants**: General, Team & contributors, Reminders, Allocation model, Compliance, Appearance, Capture & segmentation, AI feedback, Q&A & submission, Versions, Language (11 total)
- **tokens**: --text-lg, --text-base, --text-3, --space-6
- **built-from**: Warning / Notice Box, Config Field Row
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-012): the "Restricted view (Redacted / Hidden)" row is removed from Team & contributors; the save toast names theme, partners and gap strategies only. 2026-10-09 (legacy cleanup): "Workflow & milestones" is "Reminders" (no milestones, DEC-084), and settings the prototype doesn't have are removed — Outdated-response re-flag (DEC-078), AI duplicate detection (DEC-116), Internal review before sending, Contributor notification on version switch, Default translation target. The variants above are the 11 sections as they stand (the list had fallen behind). `.cfg-sec`, the single most-repeated organism shape in the file. Body max-width capped at a hardcoded 680px.

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
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-124): a system needs no manager — the PM (admin) staffs any system; the manager line reads "No manager — contributors only" (neutral grey) and the no-manager body is the normal perimeter list with its add box, or for a manager of another system a read-only note; the "No manager cast" badge variant is gone (the badge is always coverage); remove buttons follow edit rights. `.cast-noperm` and `.cast-group-badge.noperm` removed. 2026-10-09 (legacy cleanup): the no-manager variant says "No manager yet — this system can't be staffed in the prototype until it has one", and adding a system toasts "<code> added — no manager yet" — both promised staffing the prototype doesn't offer. `.cast-group`. Encodes real permission logic — only the owning manager or an admin viewer sees the add-flow/remove buttons.

### Team Casting Screen
- **level**: organism
- **file**: dashboard-et-config.html
- **variants**: PM overview mode, activity-manager scoped mode
- **tokens**: none beyond its parts
- **built-from**: Search Box, Chip Toggle (unstaffed-filter variant), Demo / Prototype-Only Control, Cast Coverage Card, Cast Activity Group
- **added**: 2026-09-01
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (DEC-124): adding a system toasts "<code> added — staff it below" and opens it with its add box; the "Just added" chip names the system; the 200-row scale demo fills no-manager systems and keeps one system per person. 2026-10-09 (legacy cleanup): "+ Add system" is hidden on a SIG tender (one system; it cannot gain a second). `#team-screen`, the full "Team casting" view. Text and available actions change based on simulated viewer identity.

### Custom Column Editor
- **level**: organism
- **file**: revue-documentaire.html, compliance.html
- **variants**: create, edit, delete confirmation (states the number of values lost)
- **tokens**: --panel, --line, --radius-md, --text-sm, --warn, --warn-soft, --space-2, --space-3
- **built-from**: Modal (`.overlay` + `.modal`), Text Input, Tab Bar / Segmented Control (`.gseg`), Checkbox, Primary Button, Ghost Button
- **added**: 2026-09-23
- **changed**: 2026-09-29
- **notes**: 2026-09-29 (DEC-097): the texts say the column is shared with the other screen and that deleting it removes it from both. 2026-09-24: ported to compliance.html with the same states and locks, for columns of phase "compliance"; the modal CSS (`.overlay`/`.modal`) was added to that file, which had none. `cfOpenEditor()` / `cfRenderEditor()`. Locks are explained in place rather than silently disabled: type change once values exist, going back to single value once a requirement holds several, removing an option in use (refused with a count). The delete button is warn-coloured inline style on `.btn-primary`, not its own class. Depends on untracked `--warn-soft`.

### Risk List
- **level**: organism
- **file**: risks.html
- **variants**: empty (no risk yet — pointer to Compliance), filtered to nothing, row highlighted (arriving from a risk chip in Compliance)
- **tokens**: --panel, --panel-2, --line, --line-2, --radius-lg, --radius-md, --radius-xs, --space-2, --space-3, --text-sm, --text-xs, --text-3, --accent, --accent-soft, --font-mono
- **built-from**: Ghost Button
- **added**: 2026-09-30
- **changed**: 2026-10-09
- **notes**: 2026-10-09 (legacy cleanup): the subtitle says each Not compliant *should* be traced to a risk — a missing risk is flagged, not blocking (DEC-108); the unused `.rk-tools select` style is removed (no select since DEC-114). DEC-113 — the whole Risks page: one row per risk with its three answers in three columns (There is a risk that… / caused by… / impact…), linked requirements (each opens it in Compliance; "all →" opens Compliance filtered on the risk), created by. Search, simulated export. DEC-114: no system column or filter — a risk belongs to the tender. Was "Risk Register" earlier the same day, with weight, status, a selection bar and merge — all removed. Its own table, not the shared table engine. `--line-2`, `--panel-2` untracked.

### Tender Chat
- **level**: organism
- **file**: tender-chat.html (inserted into the shell by build_merge.py)
- **variants**: closed (floating "Ask the tender" button), empty (suggested questions), unavailable (any copy not served by claude.ai), answering (steps from the page tools, then the streamed answer, Stop), answered (Markdown with clickable block citations), error (by code)
- **tokens**: its own `--tc-*` set, copied from the screens' light and dark values (the shell has no token scale of its own); 8/12/999px radii, 11–14px type
- **built-from**: none
- **added**: 2026-10-01
- **changed**: 2026-10-01
- **notes**: **Hidden since 2026-10-01** (`CHAT_ENABLED = False` in build_merge.py) — not built into either output until it is planned; the code stays in tender-chat.html. Asks Claude through the claude.ai artifact runtime's `sample` capability, on the viewer's own Claude account — works only in the published artifact (artifact/srm-prototype.html). Claude reads the captured blocks (`window.CHAT_CAPTURE`, generated from data.js at build time, STB-2026 only) and the shared records (strategies, risks, activity log) through six page tools: search_blocks, get_blocks, list_documents, count_blocks, requirement_record, list_risks. Where the view cannot run tools, the page searches itself and sends the top 25 excerpts. A cited [SRM-…] opens the block in Allocation. Colors are literals duplicated from the screens' tokens, not shared variables — flagged.

## Removed

### Risk Weight Pill — removed 2026-09-30, no longer needed (DEC-113: risks carry no weight)

### Risk Matrix (weight × strategy) — removed 2026-09-30, no longer needed (DEC-113)

### Risk Summary Matrix — removed 2026-09-30, no longer needed (DEC-113)

### Risk Status Pill — removed 2026-09-30, no longer needed (DEC-113: no Open/Closed status)

### Risk Detail Panel — removed 2026-09-30, replaced by the Risk List's rows (DEC-113: no editing, comments or status on this screen)

### Version Pill — removed 2026-09-23, replaced by per-document versions in the Compare Bar (DEC-069)
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-1, --space-2, --radius-pill, --text-sm, --ok
- **built-from**: Status Dot
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.version-pill`, header breadcrumb ("v2.1 active"). Border relies on untracked `--line-2`.

### Change Card — removed 2026-09-23, replaced by the Versions Tab and the Removed Requirement Panel (DEC-071/072)
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: add, mod, rem
- **tokens**: --space-2, --space-3, --radius-md, --radius-lg, --text-xs, --ok, --ia, --warn
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.change-card`, Detail Panel's Change view (Compare mode).


### Row Reclassify Button — removed 2026-09-23, replaced by the detail panel's Nature field (Nature and Class Fields)

### Flag Tag — removed 2026-09-24, no longer needed ("outdated" is not a status on Compliance any more)

### Needs My Action Button — removed 2026-09-24, no longer needed (compliance.html `.f10-needsme`; never had its own entry)

### Client Decision Block — removed 2026-09-24, no longer needed (compliance.html `.decide`, "What the client receives" in the panel header; the table's External compliance and Risk accepted columns carry it, and the declaration form still opens from the next-step action; never had its own entry)

### Verdict Entry Form — removed 2026-09-24, replaced by the Decision Panel's decision zone (DEC-079)

### Finalize / Export Modal — removed 2026-09-24, no longer needed (DEC-084): Allocation gates nothing, validation sends each requirement to its contributor, the register export is in the Export menu

### Export Option Card — removed 2026-09-24 with the Finalize / Export Modal, its only use

### Duplicate Alert — removed 2026-10-06, no longer needed (DEC-116: duplicate detection dropped from the Q&A register)

### Context Row — removed 2026-10-06, replaced by the Q&A Card's other-bidder variant

### Arbitration Guess Button — removed 2026-10-06, no longer needed (DEC-116: no arbitration queue)

### Q&A Dossier Import Box — removed 2026-10-06, replaced by one "Import the client's answers" button in the Q&A toolbar

### Arbitration Queue Card — removed 2026-10-06, replaced by the answer to confirm on the Q&A Card (DEC-116)

### Tender Line, dashboard variant — removed 2026-10-06, replaced by the Phase Rail again (navigation first; Capture and Submission aren't screens to open)

### Glossary Grid — removed 2026-10-06, no longer needed (the home page keeps no vocabulary block)

### Submissions Line — removed 2026-10-06, no longer needed (hard to read, and tenders' deadlines aren't comparable on one line)

### Bottleneck Row — removed 2026-10-06, replaced by the Waiting Queue Row (DEC-117)

### Q&A Blocked Row — removed 2026-10-06, replaced by the Waiting Queue Row's "On the client" queue (DEC-117)

### AI Reliability Row — removed 2026-10-06, no longer needed (DEC-117: Statistics follows the people, not the AI)

### Compliance Bar — removed 2026-10-06, replaced by the sentence opening Progress to the client (what the client will be told); its sidebar variant went on 2026-09-16

### Compliance Summary Panel — removed 2026-09-16 (recorded 2026-10-06), no longer needed: Statistics drew the same bar

### Compare Bar — removed 2026-10-07, replaced by the Changes Navigator (DEC-119: Compare is no longer a mode, the Document view's navigator has a Changes tab)
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-3, --space-4
- **built-from**: Select Dropdown, Compare Summary Chip
- **added**: 2026-09-01
- **changed**: 2026-09-23
- **notes**: `.compare-bar`, Compare mode only. Rendered by `renderCompareBar()` since 2026-09-23 (it was static markup whose version selects did nothing): document select first, then that document's earlier versions, "→ vX (in force)", counts and change navigation computed for the selected document and range (`cmpChangeIds()`). A document with one version says so instead of showing an empty comparison. Versions are per document (DEC-069).

### Dedup Alert Card — removed 2026-10-09, no longer needed (DEC-116: no duplicate detection; compliance.html's `.dedup` CSS was the last copy and nothing drew it)
- **level**: molecule
- **file**: compliance.html
- **variants**: none
- **tokens**: --radius-lg, --space-3, --space-4, --text-sm, --text, --ok
- **built-from**: none (accept/reject are bespoke buttons, not Ghost/Primary Button)
- **added**: 2026-09-01
- **changed**: 2026-10-06
- **notes**: 2026-10-06 (DEC-116): qa.html's unused copy of the CSS deleted. `.dedup`. CSS is byte-for-byte identical between both screens. Border is a hand-picked `rgba(224,164,60,.55)`; background relies on untracked `--ia-soft`.

### Peek Paper Excerpt — removed 2026-10-09, no longer needed (never on screen: `togglePeek()` had no caller in revue-documentaire.html, and compliance.html only had the CSS)
- **level**: molecule
- **file**: compliance.html, revue-documentaire.html
- **variants**: none
- **tokens**: --paper, --paper-ink, --radius-xs, --space-4, --space-5, --font-doc, --text-base, --accent
- **built-from**: none
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.peek-paper`. Styled and functional in revue-documentaire.html (legacy hidden markup kept for compare/segmentation reuse); in compliance.html the CSS exists but no render call was found — likely dead/unwired. Hardcoded max-width and box-shadow.

### Expert Card — removed 2026-10-09, no longer needed (compliance.html's "By expert" navigator mode, its only host, could not be opened since 2026-09-24; `.exp-card`, `remindExpert()` and the mode's code removed)
- **level**: molecule
- **file**: compliance.html
- **variants**: none
- **tokens**: --line, --radius-lg, --space-3, --accent, --accent-soft, --text-xs, --text-base
- **built-from**: Person Avatar, Progress Bar
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: "By expert" nav mode only. Disabled remind button uses hardcoded `opacity:.4`.

### AI Feedback Panel (Why Box) — removed 2026-10-09, no longer needed (its only trigger was the AI Suggestion Card's person-proposal variant, removed the same day; corrections are still logged silently by `logFeedback()` and listed in Configuration › AI feedback)
- **level**: organism
- **file**: revue-documentaire.html
- **variants**: none
- **tokens**: --space-4, --radius-lg, --ia, --accent, --text-sm
- **built-from**: Text Input
- **added**: 2026-09-01
- **changed**: 2026-09-01
- **notes**: `.why-box`, a floating fixed-position card appearing only on high-confidence AI overrides, to solicit a training-feedback reason. Auto-dismisses after a hardcoded 14000ms.

### Logo Mark — removed 2026-10-09, replaced by the Brand Logo and the product's name in text (the SRM mark — the "02 Fan Ribbons" drawing chosen on 2026-10-07, ink / slate with a red AI ribbon — is now only the favicon, in the screens and the shell's HEADER)
- **level**: atom
- **file**: accueil.html, creation-projet.html, documents.html, qa.html, compliance.html, dashboard-et-config.html, revue-documentaire.html
- **variants**: dark, light (two inline SVGs toggled by `html[data-theme]`)
- **tokens**: none
- **built-from**: none
- **added**: 2026-09-22
- **changed**: 2026-09-23
- **notes**: The three lobes and the dot are hardcoded `#fff` / `#1E3246` inside the SVG, not tokens. Height hardcoded 22px. The dot took `--brand-red` on 2026-09-22 and went back to white on 2026-09-23 at the user's request — brand red stays off the logo. The shell's favicon is a base64 copy of the same SVG.
