# Tickets — Manager features (batch 2)

> **COMPLETED — S1, S2, B1–B5 all built.** Kept for historical reference; decisions that changed a spec (B2 async casting, B3 locked-compliance exemption) are indexed in `docs/decisions/DECISIONS.md`. Do not treat anything below as open work.

> Hand this to Claude Code. Each ticket states what's confirmed and, where relevant, what's still **OPEN** — do not resolve an open point by assumption, implement around it or ask before proceeding on that specific part. Tickets reference existing components/molecules by name; reuse them, don't rebuild.

**Closed, no action needed:** the earlier idea of a quick gap-analysis view from the table (for branch managers) was dropped — the existing Gap Chip / Version Item / Versions tab mechanism is sufficient. Nothing to build.

---

## Small tickets

Self-contained, no open decisions, low risk of scope creep.

### S1 — Role badge on the Project Card (was ticket 6)

On the home screen's **Project Card** molecule, add a badge showing the current user's role on that project (e.g. "Signalling manager", "Expert", "Project manager").

- One role per person per project — no multi-role case to handle.
- Reuse the **Badge** atom (Neutral or Info tone).

### S2 — Hide the capture-correction mode (was ticket 8)

Hide the toggle/mode that lets a user manually correct the Capture step's output.

- **Hide, don't delete.** Implement as a feature flag / condition so it can be switched back on later without rebuilding it.
- No visual replacement needed — the control (and whatever depends on it) simply doesn't render while the flag is off.

---

## Big tickets

Cross-screen, touch existing domain rules, or carry an open decision that affects scope.

### B1 — Allocation change proposal, manager → project manager (was ticket 1)

A branch manager can propose a change to an allocation; the project manager reviews and validates it.

- **No new status.** Reuse the existing `Reassignment needed` status — same state as the expert→manager loop, just triggered by a different actor (a manager) and surfaced to a different reviewer (the project manager instead of a branch manager).
- The proposal is not necessarily a reassignment — it can also be a **request to add another activity/typology** on the requirement (i.e. the manager thinks a typology was missed). Both cases route to the same `Reassignment needed` state and the same project-manager review.
- **OPEN:** if the project manager rejects the proposal, does it simply revert to the prior state (tracked in the existing history log), or does something else need to happen? Confirm before building the reject path — implement the propose/accept path first if needed.

### B2 — Two-step asynchronous casting (was ticket 2)

**This overrides the previous domain-model decision** that casting is filled in one pass at project creation. New flow:

1. At project creation, the project manager assigns **branch managers per activity**, and can **directly assign experts** for those already attached to himself.
2. Each branch manager then receives an **email notification** and fills in their own experts on the platform, at their own pace — this is asynchronous and can happen well after project creation.
3. This is accepted to **delay the start of analysis** — that's a known, intended trade-off, not a bug to design around.
4. Because of that delay, the **project dashboard needs a progress indicator** for this step (e.g. "3 of 5 managers have completed their team"), in the spirit of the existing Phase Rail Item pattern.

- Ties directly to **B4 (Team management screen)** below — that screen is almost certainly where a branch manager lands to fill in their experts after clicking the email link.
- Flag for later: `SPEC-domain-model.md` currently describes casting as filled "in one shot" at creation — this ticket makes casting an ongoing, editable object. Update the spec once this is built (not required to start the build).

### B3 — Compliance override & lock by the project manager (was ticket 4)

The project manager can override an expert's compliance verdict and lock it.

- Sequence: the project manager **replaces** the verdict, then **locks** it. No comment required.
- The lock must be **visible to the expert** — they need to see their branch is locked and understand why they can no longer act on it.
- The expert's **original verdict is preserved**, but only shown in the **detail panel** (not in the table row — keep the row uncluttered).
- **Domain-model impact:** a locked compliance value must be **excluded from the "most restrictive wins" consolidation** — otherwise another branch's answer could still override a verdict the project manager explicitly locked, which would defeat the point. This needs a small addition to the compliance model in `SPEC-domain-model.md`.
- **OPEN:** can the project manager unlock it later? Not specified — don't build an unlock path until confirmed; ship lock-only first.

### B4 — Team management screen, entry point in the top menu (was tickets 7 + part of 2)

A dedicated **team management** view, per project (the roster is different for every project — nothing global).

- **Entry point:** a new button in the project's top menu (not global navigation).
- **A branch manager** sees and manages **their own team only**, and can add people to it **at any time** — not just during the initial casting step. This is the likely landing screen for the email flow in B2.
- **The project manager** sees **everyone**: a first-level view listing every branch manager together with the experts attached to them.
- Reuse existing pieces where possible: **Avatar**, **Role Recap Row**, **Assignment** molecules already cover "person + role + change" — this screen is largely an assembly of those into a roster, not new atoms.

**Fields (adding a person to the roster):**

- **Person** — a search field against SSO/company directory (typeahead), not a manual name entry. Returns the identified person.
- **Expertise** — a search field into a list (hardcoded for now, or from a base later) to pick the typology/activity this person covers. Scoped to what the current user can assign: a branch manager only sees their own typology (+ its children, per the typology hierarchy), the project manager sees all.
- **CTA: "Validate and invite"** — single button, adds one person at a time. No need to fill the whole roster in one sitting — this form is used incrementally, any time, consistent with B2's async casting (confirmed: "pas besoin de rentrer directement tous les experts").
- **OPEN (minor):** can one person carry more than one expertise in a single add, or does covering two typologies mean adding them twice? Default proposed: **one expertise per add** — simpler to build, and re-adding the same person under a second expertise is a two-second action if it's ever needed.

**Deciding when the invite email actually goes out.** Two real moments compete: right when the manager adds the person to the roster, or only once that person is actually allocated a branch (i.e. the existing `assigned` notification from `SPEC-backend-requirements.md` §8).

My recommendation: **don't pick one — they're two different messages, not two options for the same message.**
- **At roster-add time** — a light, no-action-required notice: *"You've been added to [project] as [expertise]. No action needed yet — you'll hear from us when there's work for you."* Its only job is to avoid the person feeling invited into a void; it sets expectations, nothing more.
- **At actual allocation** — the real, actionable notification (already specified in §8: "an expert is assigned to a branch"). This is the one that matters and already exists in the model — B4 doesn't need to invent a second trigger for it, just point to it.

Why not silence at roster-add and only the second one: the CTA is literally labelled **"invite"** — if clicking it does nothing visible to the invitee, the button is lying about what it does. A light touch at add-time keeps the label honest without spamming anyone with a call to action they can't act on yet (there's no work assigned yet, so "come work" would be premature).

**OPEN — needs your confirmation, not assumed:** re-reading your question, "au moment ils ont validé leur assignation" could mean two different things — (a) the moment their allocation is confirmed by the pipeline/manager (matches the §8 trigger above, no new mechanic needed), or (b) a new step where the **expert themselves** actively accepts/validates being assigned before work starts (which doesn't exist in the model today and would be new scope). I've written the recommendation above assuming (a) — flag it if you actually meant (b).

### B5 — Reuse the review table on the manager follow-up view (was ticket 5)

**Not a simplified alternate table — the same table component**, instantiated on the follow-up screen (`suivi-experts-et-versions.html`), with the same behaviours: row checkboxes, multi-select, **Bulk Action Bar**, **Filter to Selection**, keyboard row navigation, **Column Visibility Menu**.

- "Simplified" happens through **configuration**, not a different component:
  - **Default visible columns are fewer** — the manager can still add columns back via the existing Column Visibility Menu. Nothing new to build there.
  - **Default scope is the manager's own team** — applied through the same filtering mechanism already used elsewhere, not a separate hard-coded view.
- **Two genuinely new pieces** for this screen:
  - A **"Last follow-up"** column (date of the last reminder sent).
  - A **"Send reminder"** action in the Bulk Action Bar for this screen (this screen's bar has a different button set — Send Reminder / Reassign expert — same Bulk Action Bar molecule, different instance content). Selecting several rows and sending a reminder updates the "Last follow-up" timestamp on each selected row.
- **Architecture note:** `PROMPT-filter-selection-keyboard-nav.md` was scoped only to `revue-documentaire.html`. Since this ticket puts the same table on a second screen, build **Filter to Selection** and **keyboard navigation** as shared behaviour on the table component itself, instantiated on both screens — not implemented twice. Widen that prompt's scope accordingly rather than forking the logic.
- **OPEN — decides how big this really is:** is "own team" the default scope a **filter the manager can lift** (they can still see other managers' branches by clearing it — a UI default), or a **true access restriction** (they cannot see them at all, enforced beyond the UI)? The first is a small config change; the second is a real permission model and connects to the restricted-view requirement already noted in `SPEC-backend-requirements.md` §12. Confirm before building the scoping — build the column/reminder additions in the meantime, they don't depend on the answer.

---

## Follow-up once these are confirmed/built

- `SPEC-domain-model.md` needs updating for **B2** (casting becomes ongoing/async, not one-shot) and **B3** (locked compliance state, exempt from consolidation).
- Once B5's open question is answered, `SPEC-backend-requirements.md` §12 may need a line on whether restricted view is UI-default or enforced.
