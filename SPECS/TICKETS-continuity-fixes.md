# Tickets — Continuity & consistency fixes

> **Note (automated queue routine, 2026-08-13):** added `- [ ]`/`- [x]` checkboxes to each ticket below so this queue can drive the automated routine. Checked state mirrors the existing "DONE" markers; nothing about ticket content changed.

> Consolidated from three audit passes (ad-hoc functional audit, `workflow-continuity-audit`, `journey-experience-audit`) run on 2026-08-13. Prototype / UI-only: fixes are about making the demo internally consistent and trustworthy for moderated user testing, not about production hardening. Build in order within each group; groups themselves are roughly ordered by how much they block a credible test session. Aligns with `SPEC-domain-model.md`, `SPEC-review-table.md`, `TICKETS-followup-workflow.md`.

---

## Group A — Cross-project data binding (do first, almost everything else assumes this)

- [x] **TA1 — DONE.** Reframed against `HANDOVER.md`'s own documented scope ("Only one project is fully navigable... steer test participants to the EMS project") rather than building four more full datasets: the four illustration-only seeds (`rfp114`/`ao088`/`stb133`/`stb2025`) are now blocked from opening in `accueil.html`, with an explicit "Demo project — list & status only" card label and a warn-toast on click, instead of silently substituting stb2026's content (`build_merge.py`'s `seedProjects()` gained a `builtOut` flag; `accueil.html`'s `cardHTML()`/click handler read it). Projects created via the wizard stay exempt from the block. A newly created project's Dashboard now also shows its own name/ref/line (previously always "Energy Monitoring System") plus an explicit "Prototype scope" banner explaining that Allocation/Follow-up/Expert Space below still reuse the EMS reference content for this phase. Verified in-browser: opening a demo-only card no longer navigates and shows the toast; a freshly created project's dashboard shows its own identity + banner; `stb2026` renders unchanged (no regression).

~~TA1 — Route every screen through `getCurrentProject()`~~ (superseded by the above)
`dashboard-et-config.html`, `revue-documentaire.html`, `suivi-experts-et-versions.html` and `expert-space.html` render the hardcoded STB-2026 dataset regardless of which project was opened from Home. Only `accueil.html` (and, partially, `dashboard-et-config.html`'s breadcrumb) actually reads live shell state. Opening any project other than STB-2026 is the fastest way a tester breaks the illusion. Minimum credible fix for the test phase: make the other four seed projects (RFP-2026-114, AO-2026-088, STB-2026-133, STB-2025-071) either open a distinct (even smaller) dataset, or show an explicit "not built for this project" state instead of silently substituting STB-2026's content.

- [x] **TA2 — DONE.** `build_merge.py`'s `addProject()` now accepts and stores `casting`/`experts` on the project object. `creation-projet.html`'s `createProject()` passes them through — deduped by expert index, admin-self-cast activities only (delegated ones intentionally arrive expert-less, per SPEC §6). `dashboard-et-config.html`'s Team screen (`EXPERTS`) now sources from `getCurrentProject().experts` when present, falling back to the stb2026 demo roster otherwise. Verified in-browser end-to-end: cast "Power Supply" to self with Sophie Lang as expert in the wizard → created project → Team screen correctly shows 0/3 *other* managers complete (accurate, nobody else was cast) instead of the old hardcoded Sophie/Karim/Claire roster; `stb2026` unaffected.

Original ticket text, for reference:
**Carry creation-wizard casting into the created project**
`creation-projet.html`'s `createProject()` builds `P.casting`/`P.experts` (step 4) but only passes `{name,ref,line,system,region,mode,days}` to `window.parent.addProject()` — the casting work is discarded. This directly contradicts `SPEC-domain-model.md` §6, which describes the wizard's per-activity branch-manager assignment as the synchronous half of casting, meant to seed Team management (§7). Either extend `addProject`/shell state to carry `casting`/`experts` through, or explicitly scope Team management's data as demo-only and decoupled for this phase — but stop implying persistence with the "notified by email" toast if nothing downstream reflects it.
*Depends on:* TA1 (a newly created project needs somewhere real to land its casting).

---

## Group B — Numbers the user is asked to trust

- [x] **TB1 — DONE.** `dashboard-et-config.html` now carries two hand-authored local mirrors — `REVIEW_REQS` (14 requirement statuses, mirroring `revue-documentaire.html`'s `SECTIONS`) and `FOLLOWUP_REQS` (per-requirement compliance verdict + branch answered/total counts, mirroring `suivi-experts-et-versions.html`'s `REQS`/`consolidate()`) — same independently-hand-authored-per-screen convention already used for `MANAGERS`/`EXPERTS`. `renderReviewKPIs()`/`renderComplianceKPIs()` compute the Allocation phase card, the "Requirements validated" and "Response rate" health stats, the Compliance breakdown bar/legend, and the Follow-up phase card's "answered/overdue" stat from these mirrors on load, instead of typed-in markup. Verified with jsdom: computed values now read 5/14 validated (36% bar), compliance 3 compliant / 0 partial / 1 non-compliant / 8 awaiting (matches `consolidate()` over the real `REQS`), and a response rate of **40%** (6 of 15 branches answered) — catching that the old hand-typed "37.5%" was itself wrong (15 branches total, not 16). `node --check` clean on all six screens' scripts post `build_merge.py`; 6/6 base64 blobs still decode as UTF-8; 0 dead `href="*.html"` links in the merged output.

Original ticket text, for reference:
**Compute Dashboard KPIs from real data, not hardcoded markup**
"10/12 requirements validated," the 5/1/1/5 compliance breakdown, and the 75% response rate in `dashboard-et-config.html` don't match what's computable from `revue-documentaire.html`'s `SECTIONS` (real: ~5/14 fully allocated) or `suivi-experts-et-versions.html`'s `REQS`/`consolidate()` (real: 3/1/0/8, ~37.5%). This is the first data screen a user sees after opening a project — it sets the trust level for everything after it.

- [x] **TB2 — DONE.** The card text itself had already drifted to the correct case (Sophie Lang / EXG-004 / 6 days) by the time this ticket was picked up, but it was still hand-typed markup with no link to the real overdue logic. Added an `OVERDUE_BRANCHES` mirror to `dashboard-et-config.html` (subset of the branch-level detail behind `suivi-experts-et-versions.html`'s `isOverB()`: `awaiting_answer` status + `age >= OVERDUE_DAYS`) and `renderOverdueCard()`, which builds the "N expert response(s) overdue" card text from it and hides the card entirely if the list is empty. Verified: only EXG-004/Sophie Lang/age 6 qualifies against the real `REQS` branch data (EXG-003's `mln` branch is age 4, EXG-012's is age 2 — both under the 5-day threshold); `node --check` clean; `build_merge.py` re-run clean.

Original ticket text, for reference:
**Fix the "who's overdue" activity feed**
Dashboard names "Karim Benali — silent 7 days on EXG-007," but Karim's actual branch on EXG-007 is `answered`. A false overdue alert on a follow-up tool undermines every other alert it shows afterward. Derive this list from the same overdue logic `suivi-experts-et-versions.html`'s `isOverB()` already implements correctly.

- [ ] **TB3 — Compute the "Finalize allocation" modal from `SECTIONS`**
The modal's total ("12 requirements") and per-expert breakdown (Sophie 4 / Karim 3 / Claire 3) are static HTML, not derived — real totals are 14 requirements and 3/2/3. This is the confirmation screen right before an action with real downstream effect (§8.5: validating allocation *is* the send to Expert Review) — it's the worst place in the app for stale numbers.

- [ ] **TB4 — Wire "Send to assigned experts" in the Finalize modal**
Its sibling button ("Export .xlsx") has a handler and shows a toast; this one does nothing on click, silently. A user who clicks it believes experts were notified. At minimum, give it the same toast-confirmation treatment as its sibling.

- [ ] **TB5 — Stop narrating v2.2 as already-arrived**
Dashboard states "Version v2.2 uploaded and processed — gap analysis ready (+2 ~1 −0)" as fact; the Versions screen only reaches that state after the user manually clicks "Simulate upload — v2.2." Either gate the dashboard text on the same trigger, or make it clear this is a rehearsed demo beat the moderator triggers on cue.

---

## Group C — Reconnect the reassignment loop (T5) end-to-end

- [ ] **TC1 — Give the branch manager an actual path to resolve their own expert's reassignment request**
`approveReassign()`/`rejectReassign()` in `revue-documentaire.html` only render inside the admin-gated branch panel (`isAdmin()`). A branch manager who isn't the project manager — the role `TICKETS-followup-workflow.md` T5 explicitly assigns this action to ("The manager can reassign... this stays inside the company") — has no UI path to it at all. Walked in character as a branch manager (see journey-experience-audit, Parcours C), this is a silent dead end: no error, no message, nothing to act on. Scope resolution to the branch's own manager for `byRole:"expert"` requests, reserving admin-only handling for `byRole:"manager"` (B1) escalations.

- [ ] **TC2 — Make `suivi-experts-et-versions.html` read the shared reassignment mailbox**
The Follow-up screen — the branch manager's actual pilot seat per the tickets file — never calls `getReassignRequests()`; its "Returned by the expert" view only shows static seed data (`REQS[...].reassignComment`), never a live request an expert just raised in Expert Space. `TICKETS-followup-workflow.md`'s framing that Expert Space actions could be "represented as already-arrived states" is now stale — that separate build exists (`expert-space.html`) and pushes real requests via `pushReassignRequest`, but nothing wires Follow-up to consume them.
*Depends on:* TC1 (decide the resolution owner first, so this doesn't duplicate a fix in two places).

- [ ] **TC3 — Decide and document: does an Expert Space reassignment route to Review, Follow-up, or both?**
This is a genuine architecture choice, not a bug to silently pick a side on. Today it only reaches Review's admin view. Write the answer into `SPEC-domain-model.md` §2 once decided.

---

## Group D — Reconcile status/compliance vocabulary

- [ ] **TD1 — Pick one canonical compliance-verdict key set and label wording**
`SPEC-domain-model.md` §3 ("R&D Needed") and `TICKETS-followup-workflow.md` T2 ("Compliant with R&D") never agreed, and neither marks the other as superseding — `revue-documentaire.html` (`not_compliant`/`rnd_needed`) and `suivi-experts-et-versions.html` (`non_compliant`/`compliant_rnd`) each faithfully implement a different one of the two. Pick one, mark the other document's wording superseded, reconcile both screens.

- [ ] **TD2 — Bring `revue-documentaire.html`'s branch status up to the spec's six-value set, or document why not**
It currently only uses `{answered, awaiting, reassignment_needed}` — a real collapse of `proposed`/`assigned`/`awaiting_answer`/`awaiting_qa` into one bucket, not a shorthand. Concretely this means a Q&A-blocked branch (`awaiting_qa`) has no representation in the review table at all. `suivi-experts-et-versions.html` already implements the full spec set correctly — use it as the reference.

- [ ] **TD3 — Sync `IMG-1-R1`/`IMG-1-R2` into Follow-up's `REQS`**
These image-sourced requirements exist and are validatable in `revue-documentaire.html` but have no entry in `suivi-experts-et-versions.html` — validate and allocate them today, and they vanish before Follow-up. Any demo scenario touching the image-container feature (`Figure 1`, called out in `README.md` as "worth a look") currently can't be walked end-to-end.

---

## Group E — Follow-up gate & Config screen honesty

- [ ] **TE1 — Resolve the `// TEMP (dev/demo)` Follow-up unlock bypass before user testing**
Both `dashboard-et-config.html` and `suivi-experts-et-versions.html` hardcode Follow-up as unlocked regardless of `reviewDone()`, while the UI copy right next to the phase card still reads "Unlocks when allocation is finalized." Either make the gate real again, or replace the misleading copy with something that matches the demo's actual (open) behavior — a participant reaching Follow-up with allocation unfinished and reading "should be locked" copy is a specific, avoidable confusion during a moderated session.

- [ ] **TE2 — Wire or clearly mark inert Config controls**
Outside of theme and redact-mode, essentially nothing in Config has a downstream effect (overdue threshold, reminder cadence, AI/segmentation settings, Q&A/Submission/Versions/Language sections, Save/Discard). For each: either connect it to real behavior, or mark it visually as non-functional in this build so testers don't waste a task step assuming it did something.

- [ ] **TE3 — Make the redact-mode toggle reflect actual state on load**
It only *writes* `setRedactMode()`; it never initializes its selected option from `getRedactMode()`, so it always shows "Redacted" regardless of the real current mode. Harmless while both default to the same value, but it's a one-way control masquerading as a two-way one.

---

## Group F — Expert Space catch-up

- [ ] **TF1 — Surface compliance lock state in Expert Space**
`SPEC-domain-model.md` §5 explicitly deferred this ("when the expert's own view is built, it must surface the same lock state...") — that trigger has now fired (`expert-space.html` exists, committed Aug 12) but the deferred work wasn't picked up: zero occurrences of `locked`/`lockedBy` in the file. Source from the same fields `revue-documentaire.html` already uses for its lock badge.

- [ ] **TF2 — Decide the scope of the typology-parent hierarchy (§9) beyond Expert Space**
Only `expert-space.html`'s `TYPO` carries a `parent` field and cascade logic (`descendantsOf()`); the other three independently-held typology vocabularies (`revue-documentaire.html`, `suivi-experts-et-versions.html`, `creation-projet.html`) are flat. §9 explicitly says this should refine §7's Team management scope ("a manager's own team scope must include their child typologies' requirements") but `dashboard-et-config.html`'s `expertsOf()` does a flat match only. Either extend the hierarchy to the shared vocabulary and Team management, or scope §9 to "Expert Space only, for now" explicitly in the spec so it stops reading as an unmet requirement elsewhere.

- [ ] **TF3 — Resolve the R&D-Needed reporting question, then remove the spec's self-contradiction**
§9.2 says the two-value compliance form is both "already final" and "still open — do not guess an answer into either spec" in the same paragraph. `expert-space.html` already ships the two-value form the spec was cautioning against committing to. Needs one product decision (does "R&D Needed" need to stay a countable value anywhere downstream of the expert's verdict, e.g. in the compliance-matrix export) and a spec rewrite that removes the contradiction.

---

## Group G — Documentation hygiene

- [ ] **TG1 — Update `HANDOVER.md` and `README.md`'s file manifests and route tables**
Both still list only five screens/seven routes; neither mentions `expert-space.html` or the `expert` route, even though `build_merge.py` has correctly wired both (`SOURCES`, `ROUTES`, `URLMAP` all include it). `HANDOVER.md` bills itself as "the single source of truth for picking the project back up" (line 3) and currently predates three shipped features (B2 casting, B4 team management, B6/B7 status workflow) with no mention of any of their ticket codes.

- [ ] **TG2 — Recover or strip dangling references to `SPEC-expert-space.md` / `SPEC-backend-requirements.md`**
`SPEC-domain-model.md` §9/§9.1/§9.2 cite both files by name and section number (e.g. "§12 of `SPEC-backend-requirements.md`") as load-bearing context — neither file exists anywhere in the repo. Either the content was lost, or it was discussed but never written down. Recover it if it still exists somewhere, otherwise inline whatever's still relevant and drop the dangling citations.

---

## Notes

- Groups C, D and F surface the same underlying, already-accepted convention (per `SPEC-domain-model.md`'s closing note): every screen hand-authors its own `MANAGERS`/`EXPERTS`/`TYPO` rather than sharing a data layer. That's a deliberate prototype choice, not itself a ticket — but TA2, TD1–TD3, TF2 are all places where that choice currently produces a *visible* inconsistency rather than just a maintenance cost, which is why they're worth fixing even in a throwaway build.
- TE1 is explicitly self-flagged in the code (`// TEMP (dev/demo)`) — treat it as the one item in this list that's a *known*, not an *oversight*, but it should still close before any moderated session that walks the allocation→follow-up transition.
- Severity read across all three source audits, for prioritization: **TA1, TA2, TC1** block the credibility of the demo outright (a tester hits them within minutes of free exploration). **TB1–TB4, TC2, TE1** are the next tier — they don't stop a scripted task but will surface the moment a participant cross-checks two screens. **TD*, TF*, TG*** are consistency/spec-hygiene items — real, but lower urgency for a moderated 1-on-1 session that follows a scenario rather than free-roaming.
