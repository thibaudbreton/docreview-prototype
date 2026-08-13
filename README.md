# Smart Requirement Manager (SRM) — interactive prototype

A clickable, single-file prototype of an AI-assisted review experience for rail-industry
tender documents: requirements are captured and characterised automatically, then a human
reviews, assigns and validates them.

**This is a disposable design artifact for moderated user testing — not production code.**
No backend, no database, no persistence: everything runs in memory and resets on reload.

## Run it

Open the hosted version, or open `index.html` directly in a browser — no server, no build step,
no dependencies.

## Try it

The demo opens on **Energy Monitoring System** (`STB-2026`), the one fully navigable project.
The other tenders in the list illustrate statuses and background processing only.

Worth a look:

- **Review** — the core screen. Inline editing on every field, multi-select (click, shift-range,
  drag across the selection gutter), per-column sort and filters, bulk actions, collapsible columns.
- **Multi-allocation requirements** (`EXG-003`, `EXG-007`) — one requirement, several parallel
  allocations. Expand the caret in the table; the detail panel adapts to who is looking
  (use the eye icon in the header to preview a branch manager's view).
- **Image containers** (`Figure 1`) — the AI does not read images, so a human captures the
  requirements an image holds. The folder row expands into real, fully editable requirements.
- **Scale test** — View menu → loads 12,000 synthetic rows to check the table stays usable.
- **Reset demo** — `Ctrl+Shift+R` anywhere, or the button on the Home screen.

## Build

The app is authored as six standalone screens, each self-contained (own `<style>`, own
`<script>`, no shared runtime). A merge step inlines them into one hostable file.

```bash
python3 build_merge.py
```

Reads the six sources, base64-encodes each, and writes `docreview-app.html` and an identical
`index.html`. **Always edit the sources — never the merged files.**

| Source | Screen |
|---|---|
| `accueil.html` | Home — tender list |
| `dashboard-et-config.html` | Project dashboard + configuration + team management |
| `revue-documentaire.html` | Document review (largest screen) |
| `suivi-experts-et-versions.html` | Expert follow-up + Versions & Q&A |
| `creation-projet.html` | New-tender wizard |
| `expert-space.html` | Expert Space — the individual expert's own screen |

Cross-screen navigation goes through `parent.route(...)` / `parent.routeUrl(...)` rather than
`<a href="…">`, so each screen also opens standalone during development.

## Notes

All names, companies and requirement content in the demo data are fictional.

UI copy is in English throughout.
