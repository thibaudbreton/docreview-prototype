# Instructions — Design foundations (colours, type, spacing, radius)

> Paste into Claude Code. Goal: set the prototype's foundation tokens — the brand **colour** palette (both dark and light modes, equally optimised), plus the **typography**, **spacing** and **radius** scales. Colours are a token-value change only (don't restyle components, don't rename tokens). Type/spacing/radius are partly untokenised today; introduce the scales below and snap existing hardcoded values to the nearest step. These same foundations map 1:1 to Figma variables for the design system.

---

## Scope & method

- Each of the 5 source files (`accueil.html`, `dashboard-et-config.html`, `revue-documentaire.html`, `suivi-experts-et-versions.html`, `creation-projet.html`) has its own `<style>` with its own token block (a `:root`/base block for **dark** and a `[data-theme="light"]` block for **light**). Apply the same value changes in **all five files** so the palette is consistent everywhere.
- **Map to the existing token names.** The names below (`--bg`, `--panel`, `--text`, `--accent`, `--line`, `--ok`, `--warn`, `--danger`, …) are the expected ones — match them to whatever the files actually use and swap values. Do not rename tokens or touch component CSS.
- After editing sources, run `python3 build_merge.py` and verify (see bottom).

## Palette source (brand)

Blues: `#022B6D` (deep navy), `#0050E3` (vivid action blue), `#8A9AEF` (soft blue-violet), `#E6E6F0` (near-white blue), `#1E3246` (slate). Red `#DC3223` is **reserved for semantics only** (never a general UI accent).

## Principle

A UI needs **roles**, not two brand colours. Same role logic in both modes; each mode gets values tuned to be optimal there. The **accent stays "the brand blue" in both modes but is adjusted so it has the same perceived punch** (not the same exact value) — vivid `#0050E3` on light, lightened on dark. **Neutrals are tinted toward the brand blue**, never pure grey.

---

## Dark mode (base / `:root`)

```css
--bg:          #141F2B;  /* deep background (1E3246 darkened) */
--panel:       #1E3246;  /* brand slate as the surface */
--panel-2:     #26374C;  /* raised surface */
--panel-3:     #2F4257;  /* hover surface */
--text:        #EEF1F8;  /* strong text (blue-tinted white) */
--text-2:      #AAB6C6;  /* secondary text */
--text-3:      #7E8EA2;  /* tertiary text */
--line:        #2C3E52;  /* border */
--line-2:      #3A4E66;  /* stronger border */
--accent:      #4C82FF;  /* action blue, lifted for dark bg */
--accent-soft: #1E3A63;  /* accent background fill */
--accent-hover:#6A97FF;  /* accent hover */
--ok:          #3FBE86;  /* Compliant */
--warn:        #E3A64B;  /* R&D needed */
--danger:      #F2604F;  /* Non compliant (brand red, lifted) */
```

## Light mode (`[data-theme="light"]`)

```css
--bg:          #F4F5FA;  /* near-white, blue-tinted (E6E6F0 diluted) */
--panel:       #FFFFFF;  /* surface */
--panel-2:     #F4F5FA;  /* raised surface */
--panel-3:     #E6E6F0;  /* hover surface (brand tint) */
--text:        #1E3246;  /* ink = brand slate (never pure black) */
--text-2:      #4A5A6E;  /* secondary text */
--text-3:      #66748A;  /* tertiary text */
--line:        #E1E3EE;  /* border */
--line-2:      #CDD2E3;  /* stronger border */
--accent:      #0050E3;  /* action blue, vivid on light */
--accent-soft: #E9EFFD;  /* accent background fill */
--accent-hover:#0043C2;  /* accent hover */
--ok:          #1E8E5A;  /* Compliant */
--warn:        #C67A16;  /* R&D needed */
--danger:      #DC3223;  /* Non compliant = brand red */
```

---

## Semantic colours (compliance)

The compliance scale maps to the three semantic colours — the brand red carries the strongest signal:

- **Compliant** → `--ok`
- **Compliant with R&D / R&D needed** → `--warn`
- **Non compliant** → `--danger` (the brand red `#DC3223`, lifted to `#F2604F` on dark)

These are **not** general UI accents. Keep the vivid blue `--accent` for actions/selection/links, and the red strictly for the non-compliant / danger meaning.

## Optional — AI accent

If a separate AI-accent token exists (e.g. `--ia`), set it to the soft blue-violet so AI-related UI stays distinct from the primary action blue:
- Dark: `#8A9AEF`  ·  Light: `#5D6BD6`

---

## Typography

Font families are already tokenised in the prototype — keep them:

```css
--font-ui:   "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;  /* app UI */
--font-mono: ui-monospace, "SF Mono", "Cascadia Code", Menlo, monospace;                  /* IDs, refs, code */
--font-doc:  Georgia, "Times New Roman", serif;                                           /* document view (the tender text) */
```

The **type scale is not tokenised today** — the prototype hardcodes many sizes with drift (11, 11.5, 12, 12.5, 10.5…). The design system normalises them into a clean scale; when applying, **snap existing sizes to the nearest step** (drop the half-pixels).

```css
--text-xs:  11px;   /* dense table text, micro labels, badges */
--text-sm:  12px;   /* default UI text */
--text-base:13px;   /* comfortable body / inputs */
--text-lg:  16px;   /* section titles */
--text-xl:  21px;   /* screen / hero titles */
```

Weights: **400** (regular), **500** (medium), **600** (semibold) — no others. Use weight, not extra sizes, for emphasis. Line-height: **~1.45** for body/wrapping text, **~1.2** for titles.

## Spacing

Not tokenised today (hardcoded, with some 6/10/14 drift). Normalise to a **4px-based scale**; snap existing paddings/margins to the nearest step.

```css
--space-1: 4px;
--space-2: 8px;
--space-3: 12px;
--space-4: 16px;
--space-5: 20px;
--space-6: 24px;
--space-8: 32px;
```

(A tight **2px** and **6px** exist in very dense controls — keep them as exceptions, don't spread them.)

## Radius

The prototype tokenises only `--radius:8px` but uses many one-off values (6, 9, 10, 12, 20…). Normalise to a clean scale; snap existing radii to the nearest step.

```css
--radius-xs:   4px;    /* tiny controls */
--radius-sm:   6px;    /* chips, inputs, small buttons */
--radius-md:   8px;    /* default — buttons, cells, small cards (replaces --radius) */
--radius-lg:   12px;   /* cards, panels, popovers */
--radius-pill: 999px;  /* pills, status badges (was ~20px) */
```

> These three scales are **rationalised from the prototype's real usage** — they capture the intent, not a pixel-for-pixel copy of the drift. Keep the same token names when moving to Figma variables (type → text styles; spacing & radius → number variables).

## Accessibility (verify, don't eyeball)

- Target **WCAG AA**: 4.5:1 for normal text, 3:1 for large text/icons.
- **Tertiary text** (`--text-3`) is the tightest in both modes — verify it against its background and darken/lighten one notch if it fails.
- **Accent-on-fill**: check the text colour used **on** `--accent` buttons (white text on `#0050E3` passes; on the dark `#4C82FF` prefer a dark or near-white label and verify). Adjust the button label colour, not the brand accent.

## Build & verify

- Edit the **source** files only; never the merged file.
- `python3 build_merge.py`.
- Verify: each screen still renders in both themes (toggle in Config → Appearance); `node --check` on each changed screen's last `<script>` (should be untouched, but confirm nothing broke); each base64 blob decodes as UTF-8; **0 dead `href="*.html"` links**.
- Copy changed sources next to `docreview-app.html` in the output.
