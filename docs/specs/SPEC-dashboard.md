# SPEC — Dashboard (project hub)

> Derived from the prototype's actual behaviour, per `docs/prompts/PROMPT-derive-specs-from-prototype.md`. Describes the dashboard-hub portion of `dashboard-et-config.html` (`#dash-screen`) as built. The same source file also contains the Configuration screen (`docs/specs/SPEC-configuration.md`) and the Team management screen (`docs/specs/SPEC-team-management.md`) — three functionally distinct screens sharing one file and one header, split into three specs here since cramming them into one document would blur three different topics; see `docs/CLEANUP-REPORT.md` for that call. Cross-references `docs/specs/SPEC-domain-model.md` for shared concepts.

## 1. Purpose

The per-project status hub: where a project stands (phase rail), what needs the viewer's attention right now, overall project health, and recent activity. The landing screen after opening a project from Home.

## 2. Actors

The project manager / branch manager working this specific tender. The screen shows the same content to anyone who opens it — there is no role-conditional rendering on the dashboard hub itself (contrast the Team management screen, `SPEC-team-management.md`, which does adapt by viewer).

## 3. Entry points

- Opening a project from Home (`SPEC-home.md` §6) routes here.
- The "← Dashboard" link present in the header of Allocation, Follow-up, and Versions & Q&A screens.
- Any phase card here routes onward to Allocation, Follow-up, or Versions & Q&A; the Team-casting and Expert-Space cards route to Team management and Expert Space respectively.

## 4. Layout

- **Header** (shared with Configuration/Team management on this file) — logo (routes to Home), breadcrumb ("My tenders / {project ref · name}"), "＋ New project," notification bell, Team-management icon, Configuration icon, avatar.
- **Hero** — kicker ("Tender project"), title, meta line (ref, system, product line, "Bid Director: {name}" — see §11 for the same role-label inconsistency noted in `SPEC-home.md`), and a large deadline countdown.
- **Prototype-scope banner** — conditional, see §8.
- **Phase rail** — three cards: Allocation, Expert follow-up (locked until Allocation is finalized), Versions & Q&A (always open).
- **Team casting card** and **Expert Space card** — each styled like a phase-rail item but not part of the sequential phase-rail grid, since both run alongside the phases rather than gating or being gated by them.
- **Main two-column area** — "What needs you now" (primary, left) and a stacked "Project health" / "Compliance" / "Experts" column (secondary, right).
- **Recent activity** — a chronological feed, full width, below the two-column area.

## 5. Data displayed

- **Phase rail — Allocation**: validated-count / total, a progress bar, and a "Current" or "Done" badge — computed live from `REVIEW_REQS` (a hand-authored mirror of the Allocation screen's own requirement statuses; see §8).
- **Phase rail — Expert follow-up**: while locked, a static "Unlocks when allocation is finalized" message; once unlocked, answered-count / total plus an overdue count, computed from `FOLLOWUP_REQS` and `OVERDUE_BRANCHES` (mirrors of the Follow-up screen's own data).
- **Phase rail — Versions & Q&A**: a **hand-typed, static** "5 questions · 1 answered" stat — not computed from any mirrored data, unlike the other two phase cards (see §11).
- **Team casting card**: managers-completed / total, a progress bar, and a pending-count badge — computed from the same `MANAGERS`/`EXPERTS` roster the Team management screen owns (`SPEC-team-management.md`).
- **Expert Space card**: a **hand-typed, static** "4 requirements awaiting a verdict" stat — likewise not computed from any live source (see §11).
- **What needs you now** — up to 6 possible items, each independently gated: Allocation-not-finalized (before Allocation is done), a new-version notice (only once v2.2 has actually been uploaded on the Follow-up screen, per the TB5 gating fix), uncertain segmentations, an overdue-expert-response item, a Q&A-internal-review item, and a non-compliant-requirement item — the last four only appear once Allocation is finalized. Every item's copy (which expert, which requirement ref, how many days) is **hand-typed**, not computed — only the Allocation-not-finalized item's count and the overdue item's presence are backed by real data (`REVIEW_REQS`, `OVERDUE_BRANCHES`); the rest are fixed strings that happen to be consistent with the seed data today but would not update if the seed data changed.
- **Project health** — total requirements and "Managers assigned" (see §11) always shown; "Validated" (pre-finalization) or "Response rate" (post-finalization) computed from the same mirrors as the phase rail.
- **Compliance** — a segmented bar (Compliant / Partial / Non-compliant / Awaiting) plus a legend, computed from `FOLLOWUP_REQS`, shown only once Allocation is finalized.
- **Experts** — a compact per-expert progress list (avatar, name, team, a mini-bar, an "N/M" or "N late" count) — **hand-typed**, not computed from `EXPERTS` or `FOLLOWUP_REQS`, shown only post-finalization.
- **Recent activity** — a fixed, hand-typed feed of 5 entries (2 of them gated on the v2.2 upload having happened).

## 6. Interactions

- **Click a phase card** — Allocation and Versions & Q&A always navigate; Expert follow-up navigates once unlocked, otherwise shows a "Follow-up is locked — finalize allocation first" toast. *Implemented.*
- **Click the Team-casting card** → opens Team management (`SPEC-team-management.md`) on this same screen. *Implemented.*
- **Click the Expert-Space card** → routes to `expert-space.html`. *Implemented* (that screen itself is out of scope for this cleanup — see `docs/specs/SPEC-expert-space.md`, already reconciled separately).
- **Click a "What needs you now" item** → routes to the relevant screen (Allocation, or Follow-up with its Versions anchor for the version item). *Implemented.*
- **"＋ New project"** → routes to the wizard (`SPEC-project-creation.md`). *Implemented.*
- **Configuration / Team-management icon buttons** → switch this file's internal screen (see §8's three-screens-one-file note). *Implemented.*
- **Notification bell, avatar** — no click handler anywhere in the source, despite the bell carrying a permanently-lit `badge-dot` implying an unread notification. **Placeholder/gap** — see §10; the same pattern (unwired bell + avatar) recurs on the Allocation and Follow-up screens' headers too.
- **Logo** → routes to Home. *Implemented.*

## 7. States

- **Locked** (Expert follow-up phase card) — present and implemented: distinct lock iconography, "Locked" badge, click yields an explanatory toast rather than being visually disabled.
- **Pre- vs. post-finalization** — a genuine two-state screen, not just a loading state: `.p1only` elements (the Allocation-not-finalized attention item, the "Validated" health stat, a "Compliance/experts appear once finalized" hint card) show only before finalization; `.p2only` elements (four of the six attention items, response-rate stat, Compliance card, Experts card, overdue attention item) show only after. Both states are fully designed, not a stub.
- **Prototype-scope banner** — a distinct state for any project that isn't the one fully-built reference project (`SPEC-home.md` §8); see §8 below.
- **Empty / loading / error** — not present; nothing on this screen depends on a request that could be empty, loading, or fail.

## 8. Business rules

- **This screen, Configuration, and Team management are three logically separate screens sharing one file and one `showScreen()` toggle** (`dash` / `cfg` / `team`), not three independently routable pages — the merged app's router only ever targets `dashboard-et-config.html` as a whole, and this file's own JS decides which of the three is visible.
- **The Allocation and Follow-up phase-card numbers are computed from data mirrors, not hand-typed** — `REVIEW_REQS`, `FOLLOWUP_REQS`, and `OVERDUE_BRANCHES` are hand-authored *here*, independently of the Allocation/Follow-up screens' own seed data, per this project's no-shared-data-layer convention (every screen owns its own copy of the demo story). This is a deliberate prototype architecture choice, not an oversight — but it does mean the two sets of data can drift out of sync if one screen's seed is edited without updating the other (this already happened once and was fixed — see `docs/decisions/DECISIONS.md` D12).
- **A project that isn't the one fully-built reference project** (`builtOut !== true`, see `SPEC-home.md` §8) gets its hero title/ref/line overwritten from the real project object and a scope banner explaining that everything below the hero (phase rail, attention list, health) is reused `stb2026` reference content — except Team casting, which *is* that project's own, since it comes from the creation wizard. This banner is the dashboard's own acknowledgment of the same demo-scope limitation `SPEC-home.md` describes.
- **Follow-up unlocks exactly when `isReviewValidated()` is true** — a single shared boolean read from the shell, set only by the Allocation screen's own finalize action (out of scope here; see that screen's spec once written).

## 9. Non-functional

Nothing scale-related — every number on this screen is either a small hand-authored mirror array or a fixed string.

## 10. Placeholders & gaps

- **Notification bell and avatar are unwired** on this screen (no click handler for either, despite the bell's badge-dot implying something to see). The identical pattern is present on the Allocation and Follow-up screens' headers and absent on Home, the wizard, and Expert Space — a real, consistent cross-screen gap, not specific to this screen. Recorded once here in detail; referenced rather than repeated on the other affected specs.
- **The Expert Space card's stat ("4 requirements awaiting a verdict") and the Versions & Q&A phase card's stat ("5 questions · 1 answered") are hand-typed, unlike every other rail number on this screen**, which are computed from a mirror array. Whether this is an intentional shortcut (Expert Space and Versions & Q&A don't have an equivalent mirror-array convention elsewhere in the codebase to draw from) or simply not yet done isn't stated anywhere — flagged rather than assumed either way.
- **The "Managers assigned" health stat is a hardcoded "100%"** with no backing computation at all (unlike the adjacent "Requirements," "Validated," and "Response rate" stats, which are all computed). It cannot currently show anything other than 100%, regardless of the real casting-completion state the Team-casting card computes correctly two rows above it.
- **Four of the six "What needs you now" items are entirely hand-typed** (uncertain-segmentations, Q&A-internal-review, non-compliant-requirement, and the overdue item's specific name/day-count) rather than derived from `REVIEW_REQS`/`FOLLOWUP_REQS`/`OVERDUE_BRANCHES` the way the Allocation and overdue *counts* are. They are internally consistent with the current seed data, but nothing enforces that they'd stay consistent if the seed data changed — a narrower version of the same drift risk noted in §8.

## 11. Open points

- **"Bid Director" appears again here** ("Bid Director: Thibaud Breton" in the hero meta line), the same role-vocabulary inconsistency flagged in `SPEC-home.md` §11 — not re-analyzed in full here, just noted as the same open question recurring on a second screen.
- Whether the Expert Space and Versions & Q&A cards are *meant* to eventually get the same mirror-array treatment as Allocation/Follow-up (i.e., their static numbers are a known placeholder awaiting a data source) or are considered acceptable as permanently-illustrative isn't stated anywhere in the corpus.
