# SPEC — Team management (Casting)

> Derived from the prototype's actual behaviour, per `docs/prompts/PROMPT-derive-specs-from-prototype.md`. Describes the casting portion of `dashboard-et-config.html` (`#team-screen`) as built. Implements `TICKET-casting-screen-redesign.md` — see that ticket for the reasoning behind each decision below; this spec states the result. Supersedes every earlier version of this document, which described a single-tier, single-admin screen that no longer exists.

## 1. Purpose

Permanent project user management, not a step in project creation. Says who can do what, and on which scope, at any point in the project's life — not settled once and then forgotten. The point is to let work start before casting is complete: an incomplete casting slows allocation down for the activities it hasn't reached yet, it never blocks the rest of the project.

## 2. The data chain

Activity → perimeter (optional) → expert, plus a project management team that sits outside this chain entirely.

- **`CAST_ACTIVITIES`** — the tender's activities. Each may or may not yet have an activity manager (`managerId`) cast to it; `cvl` (Civil Works) ships with none, a real "not yet cast" state, not a gap.
- **`PERIMETERS`** — per activity, optional. `inf` and `tlc` ship with none at all (direct-activity staffing only) — a real, intended case per the ticket, not missing data. Not a closed vocabulary: typing a new one at add-time creates it (`resolvePerimeter`), available for reuse on that activity from then on. Values are illustrative, not sourced from a real reference list — the ticket's own "Open" section flags that no such list was available for this build.
- **`ROSTER`** — who is actually staffed: `{personId, activityId, perimeterId, addedBy, addedAt, count}`. `perimeterId:null` means staffed directly on the activity, an ordinary end state.
- **`DIRECTORY`** — the simulated SSO-searchable company pool a person is picked from. Nothing about a person is typed by hand once chosen; identity/contact is represented as SSO-supplied.
- **`PM_TEAM`** — separate from all of the above. See §3.

## 3. Two populations

- **Activity managers** (`MANAGERS`) — one per activity, own that activity's casting and staff their own experts (`ROSTER`) onto it. Scoped to their activity only.
- **The project management team** (`PM_TEAM`) — several people, each with **whole-project scope and no activity restriction**. The project creator is the first member (seeded as `admin`); any member can add another via the same SSO search pattern used for casting, no perimeter step. Never shown in `MANAGERS`/the contributor roster — that would suggest a scope restriction on them that doesn't exist. A project always keeps at least one member: removing the last one is blocked with a toast, mirroring the domain model's "never zero" rule elsewhere (a requirement can't end up with no one on it; a project can't end up with no PM).

`viewerInfo(id)` resolves a viewer id against both populations (`isPM: true/false`) — the "Viewing as" selector offers both, grouped by optgroup, and everything below reads that flag rather than the old single `.admin` boolean.

## 4. Entry points

- The Team-management icon button in the shared header (present on Dashboard and Configuration).
- The Dashboard's "Team casting" phase-adjacent card (`SPEC-dashboard.md` §6), which reads the same `ROSTER`/coverage model, so the two surfaces never disagree.
- A Dashboard button ("Back to the project dashboard") on this screen, since Casting and Configuration are internal screen-switches within this same file, not routes — the button is hidden while the dashboard itself is the visible screen.

## 5. Layout

Two different landings on the same screen and data, chosen by whether the current viewer is a PM-team member or an activity manager:

- **A PM-team member lands on the overview**: a coverage strip (one card per activity — code, label, and a staffed/unstaffed/partial/no-manager stat, click to jump to and expand that activity); the project management team section (accent-bordered, its own add/remove); then every activity, collapsed by default, each showing a completion badge.
- **An activity manager lands directly on their own activity, already expanded** — everything else stays present, collapsed, and read-only with a stated reason ("🔒 Read-only — {name} manages this activity, not you"), never a dead control with no explanation. A PM-team member can additionally edit any activity that already has a manager cast to it (full staffing authority); one with no manager yet stays blocked for everyone — a data-integrity gate, not a permission one.

A search bar above both ("is this person already staffed, and where?") queries across the whole roster regardless of collapse state. An "⚠ Unstaffed only" toggle filters to the actionable subset. A dashed 🎭 DEMO control ("Simulate 200 roster") generates synthetic rows at the ticket's real scale on demand — see §8.

## 6. Adding someone

The core, repeated interaction (150+ times on a real casting):

1. Type into an SSO-style typeahead (`DIRECTORY`, case-insensitive substring match, top 8 shown). Arrow keys move the active result, Enter or a click picks it — no mouse required.
2. **Activity add only** — a second step then asks for a perimeter: pick an existing one (datalist), type a new one freely, or leave it blank to staff the activity directly. Blank is a valid, ordinary outcome, not a skipped step. **PM-team add has no second step** — a PM-team member isn't attached to a perimeter at all.
3. On confirm: pushed to `ROSTER` (or `PM_TEAM`), a toast confirms it, and **the same input resets and refocuses** — ready for the next search immediately, no panel close, no scroll, no re-navigation. A "Just added {name} — staffing them on another perimeter too?" chip appears after an activity add, since the same person can legitimately hold several perimeters.
4. **Duplicate blocked**: the same person on the same activity+perimeter (or already on `PM_TEAM`) is refused with a toast rather than silently added twice.

## 7. Removing and changing

- An activity roster row removes cleanly while `count===0` (holds no assigned work yet).
- If `count>0`, removal is refused with a toast naming the reassignment requirement — the domain model's "never zero" rule: a requirement can never end up with no one on it.
- A PM-team member removes cleanly unless they are the last one (§3). If the current viewer removes themselves, the viewer falls back to whichever member remains rather than simulating someone who no longer exists.

## 8. Non-functional — scale

The real casting holds 150–200 people; the shipped seed data (~13 rows) is enough to exercise every state but not a scale test. Rather than bloat the shipped demo data — which every other narrative on this screen (coverage counts, the "just added" chip) is tuned around — the "🎭 DEMO Simulate 200 roster" control generates the scale on demand: synthetic people spread at random across every *castable* activity/perimeter (never the uncast `cvl` — a real block, not something scale should paper over), through the same duplicate check a manual add goes through, new names folded into `DIRECTORY` so search and add keep working normally afterwards. Idempotent — a second click above the target does nothing but toast. Verified live at 200 rows: generation ~8ms, a full search re-render ~4ms, an unstaffed-filter toggle ~1ms — the layout does not degrade as rows accumulate.

## 9. States

- **Nothing staffed** — an activity/perimeter with zero rows reads visually unstaffed (warm border/background), not a neutral empty row indistinguishable from a completed one.
- **Partially staffed** — `{staffed}/{total} perimeters` on the badge and coverage card.
- **Fully staffed** — a plain green "✓ Fully staffed" state.
- **No manager cast yet** — an activity with no manager at all is blocked for everyone, stated plainly, not a dead control.
- **Read-only** — a manager viewing a scope that isn't theirs sees the roster with a stated reason, no edit controls.

## 10. Left independent

Configuration's own "Team & experts" section (`SPEC-configuration.md` §5) keeps its separate, simpler `EXPERTS` list and add form, unchanged — per this project's no-shared-data-layer convention, each screen owns its own copy of the demo story.

## 11. Not built, flagged rather than silently skipped

- **"What the document actually involves comes first"** (surfacing only the activities/perimeters the tender's characterised requirements actually touch, with the rest secondary/collapsed) is not implemented — it would need reading into `revue-documentaire.html`'s independently-seeded requirement data, which this project's per-screen convention keeps separate.
- **Real perimeter reference values.** The ticket's own "Open" section confirms no real list was available for this build; `PERIMETERS` stays illustrative.
- **What remains in the project creation flow** once casting is ongoing user management (metadata, documents, and the initial PM-team member only?) — the ticket explicitly defers this to a future pass on `creation-projet.html`; not touched here.

## 12. Open points

Carried over unresolved from the ticket:

- Does the activity level carry permissions of its own, or is it purely a grouping?
- Is the perimeter reference list maintained centrally across activities, or per tender?
