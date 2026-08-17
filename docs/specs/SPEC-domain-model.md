# Spec — Domain model (allocated activities, statuses, compliance)

> Referenced by `TICKETS-followup-workflow.md` and the review-table allocated activity work but never written down until now. Scopes the concepts shared across the review table, the follow-up screen and (eventually) the expert's own view. Prototype / UI-only — this describes the model the UI simulates, not a backend implementation.

---

## 1. Allocated activities, not requirements

The unit of assignment is the **allocated activity**: one activity, on one requirement, handled by one manager and one expert. A single-activity requirement has exactly one allocated activity; a multi-activity (multi-allocation) requirement has one allocated activity per activity.

Each allocated activity carries: requirement ref, activity, manager, expert, allocated-activity status, compliance verdict (or null).

## 2. Allocated activity status (progress axis)

`proposed` / `assigned` / `awaiting_answer` / `awaiting_qa` / `reassignment_needed` / `answered`

Status and compliance are **two separate axes** — status is progress, compliance is result. `awaiting_qa` is a progress status, never a verdict, and blocks consolidation (see §4) same as any other not-yet-`answered` state.

`reassignment_needed` is reused for **both** directions of escalation the model currently supports:
- **Expert → manager** (T5, internal reassignment loop): the expert judges the allocation wrong and returns it.
- **Manager → project manager** (B1, allocation-change proposal): an activity manager proposes a reassignment, or proposes an entirely new activity/allocated activity the requirement may be missing. No new status was introduced for this — the same `reassignment_needed` state carries both, distinguished in the UI by who raised it and who is expected to act on it next.

### 2.1 Where an Expert Space reassignment lands (TC1–TC3)

An expert-raised request (`byRole:"expert"`) routes to **both** the review table (`revue-documentaire.html`) and the follow-up screen (`suivi-experts-et-versions.html`) — not one or the other. Each screen independently pulls the pending request off the shared shell mailbox (`pushReassignRequest`/`getReassignRequests`/`updateReassignRequest`) and resolves it against its own hand-authored allocated activity data, consistent with the no-shared-data-layer convention (Notes, below). The **resolution owner** is the allocated activity's own manager, in whichever of the two screens they're working from — not the admin; a `byRole:"manager"` request is the separate B1 escalation and stays admin-only, resolved only in the review table's admin allocated activity panel.

Resolving in one screen calls `updateReassignRequest` so the mailbox entry stops being `pending`, which stops the *other* screen from applying it fresh on its next sync — but it does **not** retract an already-rendered "action needed" card if the other screen had synced it in before the resolution happened. That staleness window is accepted for this prototype: the two screens hold independent copies of the data by design (Notes, below), a live re-push isn't part of the mailbox contract, and closing it would mean building the shared data layer this project has deliberately avoided elsewhere. A demo walkthrough should resolve a given request from one screen only, not both.

## 3. Compliance verdict (result axis)

Only meaningful once the allocated activity is `answered`. Scale: **Compliant** / **R&D Needed** / **Not Compliant**. Null/`pending` = not yet answered.

### 3.1 Canonical keys and wording (TD1)

The code-level keys are `compliant` / `rnd_needed` / `not_compliant` (optionally `pending`), with exactly the labels above. This is the canonical set — `revue-documentaire.html`'s `COMPLIANCE_DEFS` and `expert-space.html`'s `COMPLIANCE_LABELS` already used it; `suivi-experts-et-versions.html` used to diverge (`compliant_rnd`/`non_compliant`, "Compliant with R&D"/"Non compliant") and has been reconciled to match. `TICKETS-followup-workflow.md`'s T2 wording ("Compliant with R&D" / "Non compliant") is **superseded** by this section — treat this spec as the source of truth for compliance vocabulary going forward.

## 4. Consolidation — "most restrictive wins"

The requirement-level verdict is **derived**, not stored: most restrictive across its allocated activities, and **pending until every allocated activity is `answered`**. For a single-activity requirement, the sole allocated activity's verdict is the requirement's verdict. Order of restrictiveness (most → least): Not Compliant > R&D Needed > Compliant.

### 4.1 Locked verdicts are excluded from consolidation input, not from its output (B3)

The project manager can **override and lock** an allocated activity's compliance verdict (see §5). A locked verdict is a **decision**, not a pending data point — it must never be re-derived or re-ranked against sibling allocated activities as if it were still an open answer. Concretely:

- A locked allocated activity's verdict **counts toward the consolidated result** at its locked value (it is not dropped from the rollup).
- What it is excluded from is **being overridden by "most restrictive wins" logic reacting to a sibling allocated activity's later or worse answer**. Once locked, no other allocated activity's verdict — however restrictive — can change what the locked allocated activity itself reports. The consolidation still takes the most restrictive value among allocated activities, but a locked allocated activity supplies a fixed input to that comparison, not a live one.
- In short: **locking freezes that one allocated activity's contribution to the derivation; it does not freeze or bypass the derivation itself.** Without this rule, a locked "Compliant" could be silently dragged to "Not Compliant" by an unrelated allocated activity's answer arriving later — exactly the loophole the project manager's lock is meant to close.

This prototype does not compute the rollup live (`rollupCompliance` is hand-authored per requirement, as elsewhere in this codebase) — this section documents the rule the eventual derivation must follow, and the seed data assumes it.

## 5. Compliance override, lock & unlock (project manager only)

- The project manager may **replace** an allocated activity's verdict and then **lock** it. No comment/reason is required for either the override or the lock.
- **Only the project manager can lock or unlock a verdict** — no other role (activity manager, expert) ever has access to these controls. Unlocking is confirmed and in scope: the project manager can unlock an allocated activity they previously locked, which returns it to a normal, freely-editable verdict (the compliance value itself is unchanged by unlocking — only its editability).
- The allocated activity retains its **original (expert-submitted) verdict** separately from the current (possibly overridden) one — surfaced only in the **detail panel**, never in the table row, so the row stays uncluttered. This original value is preserved across lock/unlock/re-lock cycles — only the *first* override after the expert's answer is recorded as "original."
- The lock must be **visible to whoever owns the allocated activity** — currently the activity manager (no dedicated expert view exists yet). **When the expert's own view is built, it must surface the same lock state and the reason the allocated activity is no longer actionable** — this was explicitly deferred, not forgotten.

## 6. Casting is asynchronous and ongoing, not a one-shot creation-time step (B2)

**This overrides an earlier, undocumented assumption** that casting — assigning an activity manager and an expert to each activity — was filled in a single pass at project creation. It is not. Casting is a genuinely **asynchronous, ongoing, editable object**, not a snapshot taken once and left alone:

- At project creation, the project manager assigns one **activity manager per activity**. This part is synchronous — it happens in the creation wizard, before the project exists.
- The project manager may also assign the **expert directly**, but only for activities where they cast *themselves* as the activity manager. For every other activity, expert assignment is **delegated**: the activity manager fills it in later, at their own pace, from the Team management screen (§7) — not during creation, and not necessarily soon after.
- Each delegated activity manager receives a **notification** (simulated as an email trigger in this prototype) prompting them to complete their team.
- **This delays the start of analysis for those activities, and that delay is intentional** — not a gap to design around or a bug to fix. An activity manager can add or change experts on their team **at any time**, not just once during an initial casting window.

Practical consequence for anything built on top of this model: never assume every activity has a fully-cast team by the time a project exists. "Casting complete" is a state a project moves *into* over time, tracked per activity manager (see §7), not a precondition of project creation.

## 7. Team management (B4)

A per-project roster, scoped by role — never global, and never showing another project's people:

- **An activity manager** sees and manages **only their own team** (the experts they've attached), and can add to it at any time, independent of where the project is in the casting timeline.
- **The project manager** sees **everyone** — a first-level, read-only view listing every activity manager together with the experts currently attached to them. This is where "N of M managers have completed their team" (§6) is observable in detail, not just as a dashboard count.
- "Completed their team" means the activity manager has attached **at least one expert** — it is not a statement about whether that team is *sufficient* for the activity's actual workload, only that casting has moved past "nobody assigned yet."

## 8. Characterisation/allocation progression (B6/B7)

### 8.1 Requirements and allocated activities progress independently, asynchronously (B6)

Requirements are independent entities, and — within a multi-activity requirement — so are allocated activities once allocation starts. Nothing in the UI gates one requirement's or allocated activity's progress on another reaching the same point; there is no "move to next phase" action waiting on 100% completion. An expert (or manager) can validate an already-processed row while a sibling row is still `Incomplete`.

This is a UI discipline, not a new rule about §4's consolidation: within one requirement, the compliance rollup ("most restrictive wins, pending until every allocated activity has answered") is unchanged. B6 is about requirements/allocated activities relative to *each other*; §4 is about allocated activities *within* one requirement's compliance verdict. The two must not be conflated.

### 8.2 The status vocabulary: Incomplete → To review → To validate → Allocated

This lives directly in `status` (characterisation) / `allocStatus` (allocation) — not as a separate "needs review" axis alongside them. Compliance (§3) stays a separate axis because it's an independent, once-computed verdict; this progression is a step in the same workflow the requirement/allocated activity already moves through, so it belongs in the status itself.

- **Incomplete** (red) — nothing usable yet: the AI produced no value, or there's a true gap a human must fill from scratch.
- **To review** (amber) — the AI produced a value, but at least one field carries doubt. On the characterisation axis that's Class or Activity (`techAI`/`perimAI`); on the allocation axis it's ABS, PBS or OBS (whichever is the `weakestLink()`, below the confidence threshold) — all five fields are treated identically, this state is reached regardless of which one.
- **To validate** (purple) — the AI produced a complete value with no doubt at all, but no human has acted on it yet. This is where freshly-processed requirements sit, including on first arrival.
- **Allocated** (green) — reached only through an explicit human validate action (individual or bulk), never automatically from AI confidence alone — whether it arrived via To review (corrected) or straight from To validate (a trusting click).

Internally the field/status value keeps the shorter name `doubt` (`status:"doubt"`, `doubtField`, `allocDoubtField`) — only the label shown to users is "To review"; this was a deliberate rename (the original "Doubt" label read as visually and conceptually too close to the unrelated "unassigned"/OBS-assignment concept, which is why that concept was dropped from this screen's quick-filter bar entirely — see §8.6).

`Allocated` is a deliberately distinct name from the pipeline's later, unrelated "Validated" milestone (§4's compliance-consolidation rollup, reached only after every allocated activity is `answered` in Expert Review). The two must never be confused: this section's `Allocated` is what gets an allocated activity *into* Expert Review; the later `Validated` rollup is what comes *out* of it.

#### 8.2.1 An unassigned OBS is an absolute floor — "most restrictive wins" across both axes

A row's pill (and every filter/count that reads it) never shows the characterisation axis's status in isolation once allocation has something worse to report. For a single-activity row (or a real allocated activity), the two axes are combined by rank — `Incomplete < To review < To validate < Allocated` — and the **lower** rank always wins, exactly the same principle as §4's compliance consolidation. Concretely: `computeAllocStatus` treats an unassigned OBS (`alloc`/`expert` empty) as `Incomplete` regardless of how confident the AI's PBS/ABS/OBS *suggestions* were — a suggestion nobody accepted isn't a completed field. So a row can never display "To review" or "To validate" while its OBS assignment reads "— Unassigned —", even if Class and Activity are both fine. The reverse holds too: if characterisation itself is the weaker axis, that's what shows. Only when *both* axes are at least as far along as `Allocated` does the row's pill actually read `Allocated`. This combining only applies to a single allocated activity's own two axes — it is unrelated to, and must not be confused with, §4's cross-allocated activity compliance rollup or §8.1's cross-row independence.

### 8.3 Derivation is sticky — recomputed once, then frozen

`status`/`allocStatus` are derived from the AI's own confidence signals (`techAI`, `perimAI`, `weakestLink()`) rather than hand-authored per item. This derivation runs once, at data load, and never re-runs once a human has explicitly reached `Allocated` — a later edit to an already-allocated field does not silently reopen it. A manual correction on a field that hasn't yet reached `Allocated` moves its axis back to `To validate` (not straight to `Allocated` — the human still has to hit validate), matching the habit this model supports: batch-validate the confident "To validate" items first, then work `To review` (inspect, correct), then `Incomplete` (fill in) — each ending in the same action, validate.

### 8.6 Triage bar shows exactly these four states, nothing else

The table's top quick-filter bar was originally seeded with two unrelated pills carried over from before this vocabulary existed — "unassigned" (OBS/expert not assigned) and "uncertain segmentation" (a document-parsing confidence flag). Both were dropped from this bar: keeping them alongside the four status pills read as if they were more status values, when they're really a different axis each (OBS assignment; document segmentation), and "unassigned" in particular was easy to mistake for "To review" once both existed as quick filters. The bar now shows exactly the four states above plus "Changes v2.0 → v2.1" (blue, a version-diff flag, not a workflow state) — nothing else. The underlying "unassigned" and "uncertain segmentation" concepts still exist and are still surfaced elsewhere (the OBS column filter's "Unassigned" option; the per-row uncertain-segmentation warning banner) — only their top-bar quick-filter shortcut was removed.

### 8.4 Granularity: characterisation is per-requirement, allocation is per-activity

Confirmed rather than assumed, because it changes how allocated activities are tracked: characterisation (Class, Activity) progresses once per requirement, on `status`. Allocation (ABS, PBS, OBS) progresses independently **per allocated activity** on `allocStatus` — a single-activity requirement's sole (implicit) allocated activity reaches its own `Allocated`; a multi-activity requirement's allocated activities each reach `Allocated` on their own schedule, consistent with §8.1. A multi-activity requirement's row only ever shows its characterisation status at the requirement level — once that's `Allocated`, the row's pill shows each allocated activity's own progress, tracked on the allocated-activity sub-row instead.

### 8.5 Validating allocation is also the send to Expert Review

Reaching `Allocated` on the allocation axis is not a status change followed by a separate manual "send" step — the same action does both at once, because this is what actually makes §8.1's asynchronous per-activity progression meaningful (an allocated activity's own validation is what lets it move on independent of its siblings). Since control genuinely leaves this screen, the UI states this plainly rather than treating it as a silent side effect: the validate button reads "Validate & send to Expert Review" once that's the action it's about to take, and the resulting toast repeats it. Validating characterisation alone (before allocation is reached) does not trigger this — only the allocation-axis validate does.

## 9. Activity hierarchy — a permissions-only concept (Expert Space)

Surfaced while designing the expert's own screen, and applicable wherever activity-scoped access is checked:

- Activities can **nest**, to **arbitrary depth** — an activity's `parent` field points to another activity, or is `null` at the root.
- The nesting affects **permissions only**. It has **no effect** on characterisation, allocation, or compliance consolidation (§4) — a requirement's activity tag doesn't inherit or cascade anything from the hierarchy for those purposes. A child activity's requirements are characterised/allocated/consolidated exactly as if the hierarchy didn't exist; only *who can see and act on them* changes.
- A manager **or** expert assigned to a **parent** activity automatically gets **view + modify** rights on every **descendant** activity's requirements, recursively (a grandchild inherits from its parent's parent too).
- This is **additive**, not a replacement: a child activity can still carry its own directly-assigned manager/expert. The inherited parent access stacks on top of that — it doesn't override or hide the child's own assignment.
- This refines §7 (team management): a manager's "own team" scope must include their child activities' requirements, not just requirements tagged with their exact activity.

### 9.0 Implementation scope (TF2): Expert Space only, for this build

Only `expert-space.html`'s `TYPO` carries a `parent` field and cascade logic (`descendantsOf()`). `revue-documentaire.html`, `suivi-experts-et-versions.html` and `creation-projet.html` each hold their own independently-authored, **flat** activity vocabulary (per this project's no-shared-data-layer convention — Notes, below) — extending the hierarchy to all three, plus `dashboard-et-config.html`'s `expertsOf()` (currently a flat match) to do recursive cascade, is a real feature addition across four files' data models, not a display-only fix. That's out of scope for this prototype phase: **§9's parent/cascade hierarchy is implemented in Expert Space only.** Elsewhere in the app, activity stays flat and §7's "own team" scope means exact-activity match, not descendant-inclusive. Revisit if/when team management itself needs the hierarchy for a user-testing scenario — until then, this line is not an unmet requirement, it's a scoping decision.

### 9.1 The expert's restriction is enforced, not a UI default

For the expert's own screen specifically: access is a **strict restriction**, confirmed directly ("ne peut pas voir les autres"). An expert's visible-requirement set is *their own activities' union with every descendant activity*, computed once and applied at every read path (row list, counts, search) — there is no "show all" toggle, admin override, or filter that widens it back out. The manager follow-up view's own restricted-view behavior (`suivi-experts-et-versions.html`, redact vs. hide, configured in §7's Team & experts screen) is a **separate, already-implemented mechanism** — it predates this section and isn't unified with it; whether the two should eventually share one restriction model is open, but nothing here is blocked on deciding that.

_(TG2 — this subsection used to cite `SPEC-expert-space.md` and `SPEC-backend-requirements.md` §12 for the "filter-vs-restriction... still open" framing and the restricted-view precedent; neither file exists in this repo, and no record of their content survived. Rather than leave a dangling citation, the paragraph above states plainly what's actually known/decided and flags what's genuinely still open, without attributing it to a source that can't be checked.)_

_(Docs cleanup, 2026-08-16 — TG2's search was scoped to this repo's own git history, which is accurate: neither file was ever committed here. A wider search of files outside the repo (Desktop/Downloads) later turned up strong content candidates for both — now at `docs/specs/SPEC-expert-space.md` and `docs/specs/SPEC-backend-requirements.md`. This isn't confirmed as the exact original source TG2's citations pointed to, so TG2's substantive rewrite above is left as-is rather than re-attributed; the recovered files are noted here for anyone who goes looking.)_

### 9.2 R&D Needed stays a countable verdict (TF3 — resolved, was self-contradictory)

This section previously asserted the expert verdict form was "already final at two values: Compliant / Not compliant" while in the same breath calling R&D Needed's status "still open — do not guess an answer into either spec." Both couldn't be true at once, and `expert-space.html` had already shipped the two-value form the caution was warning against committing to.

**Decision:** R&D Needed stays a first-class, countable compliance value all the way through, including at the point of expert entry — not text folded into a Compliant comment. This is the option consistent with §3/§3.1's canonical 3-value scale (`compliant`/`rnd_needed`/`not_compliant`), which `revue-documentaire.html` and `suivi-experts-et-versions.html` already implement structurally (rollup, `CMP_ORDER`, consolidation). Letting the expert's own entry point silently drop it to free text would have made those two screens' structured handling pointless downstream — a rail-tender compliance matrix commercially needs to distinguish "compliant as-is" from "compliant pending R&D investment," which is exactly the kind of figure a countable value serves and free text doesn't.

`expert-space.html`'s verdict form now has a third **R&D Needed** button alongside Compliant/Not compliant, with its own comment field ("what R&D work is needed for compliance?"); `COMPLIANCE_LABELS` carries the `rnd_needed` key. (This subsection used to also cite `SPEC-backend-requirements.md` §11 for the compliance-matrix export's needs — that file doesn't exist in this repo; see TG2's note in §9.1 for how the missing-file citations across this spec were handled, and the docs-cleanup follow-up note immediately below it about a recovered candidate copy.)

---

## Notes
- Two escalation loops must never be confused: expert→manager (internal, T5) and manager→project-manager (B1) both reuse `reassignment_needed` but have different actors and different reviewers.
- All data in the current build is hand-authored; nothing here describes live backend derivation.
- Casting (§6) and team management (§7) are prototype-local per screen: the project-creation wizard, the dashboard progress indicator and the Team management screen each hold their own hand-authored `MANAGERS`/`EXPERTS`, consistent with how the rest of this codebase avoids a shared data layer — they tell the same demo story, but are not wired to a single source of truth. Expert Space (§9) adds its own `EXPERTS`/`TYPO` too, for the same reason.
