# SPEC — Team management

> Derived from the prototype's actual behaviour, per `docs/prompts/PROMPT-derive-specs-from-prototype.md`. Describes the team-management portion of `dashboard-et-config.html` (`#team-screen`, ticket B4) as built — one of three screens sharing that file; see `docs/specs/SPEC-dashboard.md` §1. Cross-references `docs/specs/SPEC-domain-model.md` §6–§7 (casting, team management) for the shared model; does not restate it.

## 1. Purpose

The per-project roster screen: where each activity manager fills in their own experts (asynchronously, at their own pace, per the casting model), and where the project manager can see completion across every activity manager at a glance. Reachable only from within a project — there is no cross-project roster view.

## 2. Actors

Two distinct views of the same screen, switched via a "Viewing as" selector that simulates whichever person is currently using it:

- **An activity manager** sees and edits **their own team only** — the actual roster-management surface.
- **The project manager** (`"admin"`) sees a **read-only aggregate**: every activity manager, with the experts each has attached so far.

Both roles are drawn from `SPEC-domain-model.md` §7's per-project, role-scoped roster model.

## 3. Entry points

- The Team-management icon button in the shared header (present on Dashboard and Configuration).
- The Dashboard's "Team casting" phase-adjacent card (`SPEC-dashboard.md` §6).

No other screen links here.

## 4. Layout

- **Header** — shared with Dashboard/Configuration.
- **Title** — "Team management."
- **Viewing-as selector** — one dropdown, every manager (including the project manager) as an option.
- **Body** — either the admin's read-only list of manager groups, or the selected activity manager's own editable roster, one "manager group" card per manager: avatar, name, role, a completion badge, and their expert rows.

## 5. Data displayed

- Per manager group: avatar/initials/color, name, role label, a status badge (green "{N} expert(s)" once they have at least one, amber "Team not complete yet" otherwise).
- Per expert row: avatar, name, team/domain, and an assigned-requirement count (`{N} requirement(s) assigned`) — the same count field the Configuration screen's expert editor and the Dashboard's Experts card would read, though only this screen and Configuration actually render it live from the shared array.
- All of this reads from the same in-memory `EXPERTS`/`MANAGERS` arrays as Configuration's Team & experts section (`SPEC-configuration.md` §5) — not a separate copy.

## 6. Interactions

- **Switch "Viewing as"** — re-renders the body scoped to the newly selected manager (or the admin aggregate, if the project manager is selected). *Implemented.* **Represented / backend-dependent**: this simulates identity/permission switching for demo purposes; a real build would derive the viewer from an authenticated session (`SPEC-backend-requirements.md` FR24–26), not a dropdown anyone can set to anyone.
- **Add an expert** (activity-manager view only) — name + team/domain, appended to the shared roster tagged with the current viewer as `manager`. *Implemented*, immediately reflected in the admin aggregate view, the Dashboard's Team-casting progress, and Configuration's expert editor.
- **Remove an expert** (activity-manager view only) — blocked with a toast if that expert has any assigned requirements (`count>0`); otherwise removed immediately. *Implemented*, same rule as Configuration's expert editor.
- **Admin view has no add/remove controls at all** — it is read-only by design, not merely read-only because nothing is wired.

## 7. States

- **Empty roster** (a manager with zero experts) — "No expert added yet — add the first one below." (editable/own view) or "No expert added yet." (read-only admin view of someone else's team).
- **Team not complete yet** vs. **"{N} experts"** — the two states of the completion badge, driven purely by whether the manager has ≥1 expert attached; there is no partial/in-progress distinction beyond "zero" vs. "at least one."
- No loading or error state — nothing here depends on a request.

## 8. Business rules

- **"Completed their team" means "has at least one expert attached,"** with no further threshold — this is the exact rule the Dashboard's Team-casting progress card also uses (`renderCastingProgress`, shared computation logic, though a separately-written function).
- **Casting is asynchronous** — an activity manager can add or remove experts at any time after project creation, not only during a fixed casting step (`SPEC-domain-model.md` §6, decision D5 in `docs/decisions/DECISIONS.md`).
- **The project manager's own aggregate view excludes themselves** from the list of manager groups shown (`MANAGERS.filter(m=>!m.admin)`) — the PM sees every *other* manager's progress, not a group for their own casting (their own directly-managed activities were already fully cast at project creation, per `SPEC-project-creation.md` §6).

## 9. Non-functional

Nothing scale-related — 4 managers, a handful of experts each in the current seed data.

## 10. Placeholders & gaps

None beyond the shared header's unwired notification bell and avatar, already described in `SPEC-dashboard.md` §10.

## 11. Open points

None found specific to this screen.
