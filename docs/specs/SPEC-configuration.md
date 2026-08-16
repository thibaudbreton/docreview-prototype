# SPEC — Configuration

> Derived from the prototype's actual behaviour, per `docs/prompts/PROMPT-derive-specs-from-prototype.md`. Describes the configuration portion of `dashboard-et-config.html` (`#cfg-screen`) as built — one of three screens sharing that file; see `docs/specs/SPEC-dashboard.md` §1 for why they're split into separate specs. Cross-references `docs/specs/SPEC-domain-model.md` and `docs/specs/SPEC-backend-requirements.md` for shared concepts.

## 1. Purpose

Per-project settings, organized into 9 sections. Most sections are explicitly marked in the UI itself as not wired to real behaviour in this build — this screen's honest job in the prototype is to **show the full intended settings surface**, not to actually change how the project behaves, with two clearly-marked exceptions (Appearance, and the restricted-view control in Team & experts).

## 2. Actors

Whoever is managing the project — no role-gated content exists on this screen; every section is visible and editable to anyone who opens it.

## 3. Entry points

- The Configuration icon button in the header, present on the Dashboard, Allocation, and Follow-up screens.
- A direct `#config` hash deep-link, handled on load.

There is no "back" affordance specific to this screen beyond the shared header's Dashboard/Team-management icons and the logo.

## 4. Layout

- **Left nav** (220px) — 9 section items: General, Team & experts, Workflow & milestones, Appearance, AI & segmentation, AI feedback, Q&A & submission, Versions, Language.
- **Right body** — one section visible at a time, each with a heading, a subtitle, and (for 6 of the 9 sections) a dashed warning box stating plainly that the section is demo-only.
- **Sticky footer** — "Discard changes" / "Save configuration."

## 5. Data displayed

- **General** — project name, tender reference, product line, submission deadline, and the active source document filename — all pre-filled with the reference project's values.
- **Team & experts** — the live expert roster (name, team, avatar) shared with the Team management screen (`SPEC-team-management.md` — same in-memory `EXPERTS` array, not a copy: adding or removing an expert here is immediately visible there and vice versa); a 4-chip "assignment criteria" row (PBS/ABS/OBS on, Discipline off); a Redacted/Hidden segmented control for restricted view.
- **Workflow & milestones** — a gate toggle, an overdue-threshold range slider (1–14 days, default 5), a reminder-cadence select, and an outdated-response re-flag control.
- **AI & segmentation** — document-rendering choice (Faithful PDF / Reconstructed HTML), an uncertainty-threshold slider (50–95%, default 80%), table-granularity choice, re-segmentation strategy, and a "never overwrite manual edits" toggle.
- **Q&A & submission** — issuer channel choice, AI duplicate-detection toggle, internal-review-stage toggle.
- **Versions** — numbering scheme, addendum-detection toggle, expert-notification timing.
- **Language** — source-document language, default translation target, interface language selects.
- **Appearance** — a Dark/Light theme picker.
- **AI feedback** — 4 hand-typed acceptance-rate cards (Segmentation/Typology/Characterization/Assignment), a hand-typed "recurring patterns" list, and a **live** "This session" feed populated from real correction events (see §6).

## 6. Interactions

- **Section navigation** — click a nav item, switches the visible section. *Implemented.*
- **Theme picker** — click Dark or Light: applies immediately (`document.documentElement` attribute + the shell's `setTheme`, which also re-applies to the currently-loaded iframe), confirmed with a toast, and is read back correctly on next load via the shell's `getTheme`. *Implemented*, in-memory only — does not survive a page reload (no persistence anywhere in the prototype).
- **Restricted-view control** (Team & experts section) — Redacted/Hidden: applies immediately via the shell's `setRedactMode`/`getRedactMode`, read back correctly on load. *Implemented.* This is what a branch manager's out-of-scope requirements look like elsewhere in the app (redacted text vs. hidden entirely) — the actual behaviour it controls lives on other screens, not here.
- **Expert add / remove** (Team & experts section) — adds to or removes from the shared `EXPERTS` roster; removing an expert with `count>0` assigned requirements is blocked with an explanatory toast. *Implemented*, same mechanism as the Team management screen's own add/remove (`SPEC-team-management.md` §6).
- **Every other toggle, segmented control, chip, and range slider** (General; Workflow & milestones; AI & segmentation; Q&A & submission; Versions; Language) — visually responds to a click (toggles state, updates a percentage/day label) but changes nothing else. Each of these sections carries its own on-screen warning box stating this directly (e.g. "these controls aren't wired to the rest of the app in this build"). **Represented / backend-dependent**: every one of these settings corresponds to real, described backend capability — the review milestone gate and overdue threshold to `SPEC-domain-model.md`'s Follow-up-unlock and overdue-branch logic (both real, but driven by actual validation/branch-age state, not this slider); segmentation/rendering/granularity settings to the AI capture pipeline (`SPEC-backend-requirements.md` FR10); Q&A channel/dedup/review-stage settings to the Q&A workflow (`SPEC-backend-requirements.md` FR19–20, and the Follow-up screen's own real duplicate-detection UI, which this panel doesn't drive); language settings to the (currently hard, English-only) language rule. The intent behind every one of these controls is real and documented elsewhere; only the wiring between this settings screen and that behaviour is what's missing in the prototype.
- **AI feedback — session feed** — genuinely live: every correction made on the Allocation screen (a reassignment, a typology change) is pushed to the shell's `pushAIFeedback` and read back here via `getAIFeedback`, rendered as a real per-item row (surface, before/after value, high-confidence-override flag). *Implemented*, the one section beyond Appearance/restricted-view where this screen reflects real session activity rather than static or inert content. The acceptance-rate cards and "recurring patterns" list above it, by contrast, are fixed hand-typed numbers, not derived from the session feed.
- **"Save configuration"** — does not persist any field; its toast reads "Theme and restricted-view mode apply immediately — other settings on this page aren't wired in this build," matching what actually happened. *Implemented as an honest no-op*, not a silent failure.
- **"Discard changes"** — likewise a no-op with a matching toast ("Nothing to discard — most fields on this page aren't wired in this build").

## 7. States

- No section has a distinct empty, loading, or error state — every field is always pre-filled with fixed or live values, and nothing here depends on a request that could fail.
- The two working controls (theme, restricted view) do have a real applied/not-applied state, reflected immediately and correctly on load.

## 8. Business rules

- **Two controls have real, immediate, cross-screen effect; the rest are deliberately inert and say so on-screen.** This is not a hidden inconsistency — every inert section carries its own explanatory warning box, so a user reading the screen is never told something works when it doesn't.
- **The expert roster is shared, not duplicated**, between this screen's Team & experts section and the standalone Team management screen (`SPEC-team-management.md`) — both read and write the same in-memory array.
- **The language rule is a hard constraint stated in `HANDOVER.md`**, not merely a default: UI copy stays English throughout regardless of what's selected here, by design, for the duration of this prototype phase.

## 9. Non-functional

Nothing scale-related.

## 10. Placeholders & gaps

None beyond the header-level notification bell and avatar already described in `SPEC-dashboard.md` §10 (this screen shares the same header). Every inert control in this screen's body is a disclosed, represented/backend-dependent placeholder (§6), not an undisclosed gap — the distinction matters here specifically because this screen would otherwise look like it's full of dead controls; it isn't, it's explicit about what it simulates versus what it doesn't.

## 11. Open points

None found specific to this screen beyond the role-vocabulary question already raised in `SPEC-home.md` §11 and `SPEC-dashboard.md` §11 (not repeated here, since this screen doesn't display a role label itself).
