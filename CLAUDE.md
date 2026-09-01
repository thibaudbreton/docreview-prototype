# Component manifest — format & maintenance rules

## Why this file exists

The prototype is a static HTML shell with inline styles and scripts. There are no component boundaries in the code — nothing marks where one ends and the next begins. So a component inventory cannot be reliably derived from a diff after the fact; it has to be recorded by whoever writes the component.

That's the rule: **if you build or change a component, you update `COMPONENTS.md` in the same commit.** Not afterwards, not in a separate pass.

## Maintenance rules

**When you add a component** — a reusable UI element with its own identity, not a one-off arrangement — add an entry.

**When you change one** — new variant, changed structure, renamed, different tokens — update its entry and bump its `changed` date.

**When you remove one** — move it to the Removed section at the bottom with the date. Don't delete the line; a component that disappeared is information.

**When in doubt about whether something is a component** — if it appears in more than one place, or is likely to, it is. If it exists once and always will, it isn't. Record the judgement call in `notes` rather than agonising over it.

**Never rewrite the whole file.** Edit the entries that changed. The file's history is what makes it useful.

## Levels

- **atom** — indivisible: button, input, badge, checkbox, chevron, avatar
- **molecule** — assembles atoms: search box, table row, detail field, toast
- **organism** — assembles molecules into a working section: the full table, the detail panel, the dashboard

If a thing doesn't fit cleanly, put it where it's most useful to find and say why in `notes`. The taxonomy serves the inventory, not the reverse.

## Entry format

```markdown
### <Component name>
- **level**: atom | molecule | organism
- **file**: which source file it lives in
- **variants**: the states or types it has, comma-separated — or `none`
- **tokens**: the design tokens it uses (colour, spacing, radius, type)
- **built-from**: for molecules and organisms, which components it assembles — or `none`
- **added**: YYYY-MM-DD
- **changed**: YYYY-MM-DD (same as added if never changed since)
- **notes**: anything a future reader needs — deviations from the token scale, known duplication, why it exists
```

`tokens` matters more than it looks: it's what makes the eventual Figma pass mechanical rather than interpretive, and it's how token drift gets caught. **If a component uses a hardcoded value instead of a token, say so in `notes`.** That's exactly what the audit is looking for.

The tracked token scale is defined once, identically in both theme blocks, near the top of each screen's `<style>`: `--bg`, `--panel`, `--line`, `--text`, `--text-2`, `--text-3`, `--accent`, `--accent-soft`, `--ia`, `--ok`, `--human`, `--warn`, `--paper`, `--paper-ink`, `--text-xs/sm/base/lg/xl`, `--space-1`–`--space-8`, `--radius-xs/sm/md/lg/pill`, `--font-ui/doc/mono`. A number of other custom properties (`--panel-2`, `--panel-3`, `--line-2`, `--accent-hover`, and the `-soft` variants of `--ok`/`--warn`/`--ia`/`--human`) are used constantly across every screen but are **not** part of this scale — treat any component that depends on one of these as carrying a `notes` flag, the same as a raw hardcoded value would get.

## Example

```markdown
### Requirement Row
- **level**: molecule
- **file**: revue-documentaire.html
- **variants**: default, selected, expanded (multi-activity)
- **tokens**: --panel, --line, --text, --space-4, --space-3, --text-sm
- **built-from**: Checkbox, Chip, Avatar, Badge, Compliance
- **added**: 2026-03-12
- **changed**: 2026-08-19
- **notes**: row height is hardcoded at 38px, not on the spacing scale
```

## File structure

```markdown
# Components

_Maintained alongside the code. Updated in the same commit as any component change._

## Atoms
### ...

## Molecules
### ...

## Organisms
### ...

## Removed
### <name> — removed YYYY-MM-DD, replaced by <what> (or: no longer needed)
```
