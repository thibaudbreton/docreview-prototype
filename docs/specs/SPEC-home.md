# SPEC — Home (My tenders)

> Derived from the prototype's actual behaviour, per `docs/prompts/PROMPT-derive-specs-from-prototype.md`. Describes `accueil.html` as built. Cross-references `docs/specs/SPEC-domain-model.md` for shared concepts; does not restate them.

## 1. Purpose

The application's entry point and default route. Lists every tender the current user is involved in, so they can resume work on one or start a new tender. This is where a session begins and where "Reset demo" lives for moderated user testing.

## 2. Actors

A single implied user views this screen — the prototype has no login and no per-user data separation. The screen's own copy describes them as **"Bid Director"** (`home-sub`: "Tenders you lead as Bid Director"), which does not match any role name used elsewhere in the corpus — see §11.

## 3. Entry points

- The application's default route (`home`) — reached on first load with no hash, and via `Ctrl+Shift+R` / the Reset-demo button (both route back here).
- The SRM logo, clickable on every other screen, routes back here (`dashboard-et-config.html`, `suivi-experts-et-versions.html`).
- The "← Dashboard" / breadcrumb links on other screens do not lead here directly — they go to the Dashboard hub, not Home (Home and Dashboard are distinct screens; see `SPEC-dashboard.md`).

From here, a user can go to: a tender's Dashboard (clicking an openable card), or the new-tender wizard (`SPEC-project-creation.md`).

## 4. Layout

- **Header** — SRM logo/wordmark (not clickable here, since this already is Home), "↺ Reset demo", "＋ New tender", user avatar (static initials, no menu).
- **Hero** — "My tenders" title, a dynamic subtitle (tender count + role line), a second "＋ New tender" button.
- **Tabs** — All / Processing / In progress / Submitted, each with a live count.
- **Grid** — one card per tender matching the active tab, or an empty-state message.

## 5. Data displayed

Per project card, from the shell's in-memory `PROJECTS` array (seeded by `seedProjects()` in `build_merge.py`, or appended to by `addProject()` when a tender is created):

- `ref`, `name`, `line` (product line), `role` (the viewer's role on that tender — see §11), `status` badge (Processing / Allocation / Expert review / Q&A & Versioning / Submitted — labels differ slightly from the raw status keys, e.g. `requirement_review` displays as "Allocation").
- Deadline chip (`days` until submission) — styled `urgent` at ≤10 days, `soon` at ≤25, plain otherwise, or "overdue" if negative. Only rendered when the project has a `deadline` flag set (all seeds do).
- Body content depends on status: a live progress bar + percentage while `processing`; a "done/total validated|answered|resolved" stat with a mini-bar otherwise; a plain "Response submitted · N requirements" line once `submitted`.
- Footer: "Opens when processing completes" while processing; "Demo project — list & status only" for a demo-only project (see §8); otherwise "Updated {date}" plus an "Open →" affordance on hover.
- Tab counts are computed client-side from the same `PROJECTS` array on every render, not stored separately.

## 6. Interactions

- **Switch tab** — filters the grid to the tab's status group; purely a client-side filter over the in-memory list, no request involved. *Implemented.*
- **Click a project card**:
  - If `status==="processing"` → toast "Still processing — it will open when the models finish"; no navigation. *Implemented.*
  - Else if `builtOut===false` → toast steering the user to the one fully-built reference project instead of opening; no navigation. *Implemented* (see §8's business rule).
  - Else → calls the shell's `openProject(id)`, which sets the project as current and routes to the Dashboard. *Implemented.*
- **"＋ New tender"** (either instance) → routes to the new-project wizard. *Implemented.*
- **"↺ Reset demo"** → a native `confirm()` dialog, then calls the shell's `resetDemo()`. *Implemented.* This is a **global** reset, not scoped to this screen: it restores the original seed `PROJECTS`, and also clears `reviewValidated`, `projectMode`, `projectMeta`, `aiFeedback`, `redactMode`, `v22Uploaded`, and every pending reassignment request — i.e. every piece of shared cross-screen state the shell holds, not just what Home itself displays.
- **Live background processing** — while any project has `status==="processing"`, this screen polls every 700 ms and re-renders so progress bars animate. The actual progress increment (`+2..6` per tick, transition to `requirement_review` at 100%) happens in the shell's own timer (`startProcLoop`, `build_merge.py`), which keeps running even while the user is on a different screen — this screen only reflects it. **Represented / backend-dependent**: a real AI capture/characterise/allocate pipeline is what this simulates (see `SPEC-backend-requirements.md` FR10); here it's a fixed-formula timer with a random increment, not a real job.

## 7. States

- **Empty** — "No tender in this view." shown when the active tab's filter yields zero cards. Present and implemented.
- **Loading** — not present; nothing on this screen depends on a network round-trip, so there is no loading state to design for.
- **Error** — not present; there is nothing that can fail (no request, no validation).
- **No-permission** — not present; there is no access control in the prototype (see `SPEC-backend-requirements.md` FR24 for the intended real-world role scoping this screen doesn't simulate).
- **Partial / demo-only project** — a distinct, deliberate state: four of the five seed projects have `builtOut:false` and can never be opened into real content, by design (see §8). This is not an error state, it's a permanent property of those seed rows.

## 8. Business rules

- **Only one project is fully navigable.** `stb2026` (Energy Monitoring System) is the sole seed with `builtOut:true`; its Dashboard/Allocation/Follow-up/Expert-Space screens show real, hand-authored content. The other four seeds exist only to populate the list, statuses, and background-processing illustration — clicking them is explicitly blocked with an explanatory toast rather than silently substituting `stb2026`'s content. Projects created via the wizard are **exempt** from this block (no `builtOut` flag is set on them at all, so they fall through to the normal open path) — see `SPEC-project-creation.md`.
- **One role per person per project** — the role badge assumes no multi-role case (stated directly in code comments).
- **A processing project cannot be opened**, regardless of `builtOut`, until its status has moved past `processing`.
- **Reset demo restores the exact original seed set** and every piece of shared state listed in §6 — a full application-state reset, not a per-screen one.

## 9. Non-functional

Nothing scale-related applies to this screen — the seed list is 5 items, and nothing here is exercised by the review table's scale test (see `SPEC-review-table.md`).

## 10. Placeholders & gaps

None found. Every visible control (tabs, both "New tender" buttons, Reset demo, card click) is wired to real prototype behaviour.

## 11. Open points

- **Role vocabulary inconsistency.** This screen's subtitle calls the viewer "Bid Director." No other screen or spec in the corpus uses that title: `creation-projet.html`'s `MANAGERS` list and `dashboard-et-config.html` call the same person "Project lead (admin)" / "Project manager," and `SPEC-backend-requirements.md`'s five-role list (Project Manager, Requirement Manager–contributor, Expert Reviewer, Admin, VIP) has no "Bid Director" role at all. "Bid Director" does appear in `docs/research/AS-IS-workflow-map.md` as a pre-SRM role name, suggesting this is a leftover from earlier terminology that was never reconciled with the in-tool role model — flagged here rather than silently normalized to one or the other, since picking one would be a product decision, not a documentation one.
- **Per-card `role` badge vocabulary is also inconsistent with itself**: the seed data uses "Project manager," "Signalling manager," and "Expert" as `role` values on different cards, while the subtitle above the grid says "Bid Director" for the same viewer on the primary card. Both are describing the same person's relationship to different tenders, but the words don't come from one shared list anywhere in the code.
- Whether a demo-only project (`builtOut:false`) that finishes processing and could technically be opened is *supposed* to stay permanently blocked, or whether the block is only meant to apply to the four hand-picked seeds specifically (as opposed to any future non-`stb2026` project) is not stated outside the code itself — the current implementation blocks by flag, not by id, so this is consistent, but no design document defines the rule independently of the code that enforces it.
