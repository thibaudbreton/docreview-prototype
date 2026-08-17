# Instructions — Apply brand colours to the prototype (Claude Code)

> SUPERSEDED by `docs/prompts/PROMPT-design-tokens.md` on 2026-08-04. Kept for reference. Do not build from this — the design-tokens prompt covers the same colour palette plus typography/spacing/radius; this file is its colour-only subset. Renamed from `SPEC-brand-colors.md` (it is a build prompt, not a living spec — see `docs/INVENTORY.md`).

> Paste into Claude Code. Goal: replace the prototype's colour tokens with the brand palette, in **both** dark and light modes, treating the two modes as equally optimised (neither derived from the other). This is a **token-value change only** — do not restyle components, do not change token names. The prototype is already tokenised; the whole change happens in the token definitions.

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

## Accessibility (verify, don't eyeball)

- Target **WCAG AA**: 4.5:1 for normal text, 3:1 for large text/icons.
- **Tertiary text** (`--text-3`) is the tightest in both modes — verify it against its background and darken/lighten one notch if it fails.
- **Accent-on-fill**: check the text colour used **on** `--accent` buttons (white text on `#0050E3` passes; on the dark `#4C82FF` prefer a dark or near-white label and verify). Adjust the button label colour, not the brand accent.

## Build & verify

- Edit the **source** files only; never the merged file.
- `python3 build_merge.py`.
- Verify: each screen still renders in both themes (toggle in Config → Appearance); `node --check` on each changed screen's last `<script>` (should be untouched, but confirm nothing broke); each base64 blob decodes as UTF-8; **0 dead `href="*.html"` links**.
- Copy changed sources next to `docreview-app.html` in the output.
