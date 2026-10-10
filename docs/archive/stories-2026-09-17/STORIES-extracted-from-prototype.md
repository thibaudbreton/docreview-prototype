# User story backlog — extracted from the prototype

> An independent reading of the SRM prototype as it stands today (7 source screens plus the shell in `build_merge.py`). Every story below describes an intent the prototype visibly embodies — what the feature should do when built, as evidenced by the screen — not whether the prototype performs it. Vocabulary is the prototype's own, uncorrected; where the same thing is named differently in different places, that is listed at the end rather than smoothed over.
>
>**Note, 17 September 2026 — vocabulary has moved since this extraction.** What these stories call an *activity* is now a **system** (DEC-045); *activity* went back to naming the ABS — Activity Breakdown Structure — which is the level inside a system. The list of 7 casting activities in §3 and the product-line spellings in §1 have both been replaced since. This document is left as written, as a record of the reading that produced it; the live vocabulary is in [docs/current/TENDER-PROFILES.md](../current/TENDER-PROFILES.md).
>
> Areas follow the order a user meets them: the tender list and creation, then the tender dashboard and its support screens, then the two process steps (Allocation, Compliance), then Q&A, then the flows that span several screens.

---

## 1. My tenders

### Browse my tenders and open one

**Description:** As a Bid Director, I want to see every tender I'm involved in with its state at a glance, so that I can pick the one that needs me and open it.

**Design:** My tenders — `accueil.html`

**Acceptance criteria:**
1. Each tender is a card showing its BO-ID, name, a status pill in the top-right corner, and a stack of System (product line), and my role on it (Project Manager or Contributor).
2. The status pill is one of exactly two values for a tender in progress — Allocation or Compliance — plus Processing and Submitted for tenders outside that model.
3. Directly under the name, a gauge shows Allocation (requirements allocated / total) while any requirement is unallocated, and switches automatically to Compliance (internal compliance filled in / total) once allocation reaches 100%. No manual toggle.
4. Tabs filter the list (All / Processing / In progress / Submitted) with a live count on each; the intro says how many tenders I lead.
5. Clicking a card opens the tender's dashboard; a tender still processing cannot be opened and says so.

### Follow a tender while the AI processes it

**Description:** As a Bid Director, I want a tender I just created to show its processing progress in the list, so that I know when it becomes workable.

**Design:** My tenders — `accueil.html`, background loop in `build_merge.py`

**Acceptance criteria:**
1. A Processing card shows a progress bar and the current stage label (Capturing requirements → Characterising requirements → Allocating to experts).
2. On a tender whose source language is not English, a Translating requirements stage appears between capture and characterisation.
3. Progress advances while I stay on the list and continues while I navigate elsewhere.
4. When processing completes, the card becomes an Allocation card with 0/N allocated and can be opened.

---

## 2. Create a tender

### Define the tender's identity

**Description:** As a Bid Director, I want to describe a new tender in one pass, so that every screen carries the same identity and the deadline drives the countdowns.

**Design:** New project, step 1 — `creation-projet.html`

**Acceptance criteria:**
1. Project name and BO-ID are required; the wizard refuses to continue without them and says why.
2. Product line is a deliberate card-style choice (Turnkey, RCS, SIG, INFRA, Rolling Stock, Services); the form explains the consequence — Turnkey resolves allocation to an activity (split by technical/non-technical), any other line resolves it to a person.
3. System, Region, Source language, Tender issuer and Submission deadline are captured; the source language decides whether translation runs after capture.
4. The step-4 summary restates everything entered and marks what is still not set.
5. Steps can be revisited in any order once their required fields are valid.

### Attach and order the source documents

**Description:** As a Bid Director, I want to attach the tender's documents in reading order, so that they are captured as one continuous tender.

**Design:** New project, step 2 — `creation-projet.html`

**Acceptance criteria:**
1. Several PDF documents can be added (drop zone or file picker); each shows its name, page count, size and language.
2. Documents can be moved up/down and removed; the resulting order is the order they are concatenated in.
3. The project can be created with no document, with a warning that the review screen stays empty until one is attached.
4. Later versions are explicitly deferred to the Documents & versions screen, not this step.

### Choose how much the AI does

**Description:** As a Bid Director, I want to set the processing mode before capture starts, so that the AI does only the steps I trust it with.

**Design:** New project, step 3 — `creation-projet.html`

**Acceptance criteria:**
1. Two presets are offered — AI-assisted (recommended) and AI segmentation only — and three individual toggles: Capture, Characterisation, Allocation. Changing a toggle away from a preset shows a "Custom" tag; matching a preset again re-selects it.
2. Each step's description switches to an "Off — you do X yourself" wording when disabled.
3. An estimate line summarises blocks, enabled steps and expected processing time; turning everything off states that the project opens immediately and every requirement is built by hand.
4. Fully manual mode explains that the review screen opens with the document but no blocks, to be segmented by hand.
5. The chosen mode determines the landing screen after creation: manual goes straight to review, anything else lands on the dashboard with capture already running.

### Name the project management team at creation

**Description:** As a Bid Director, I want to say who else can manage this project, so that the management team exists from day one without staffing every activity up front.

**Design:** New project, step 4 — `creation-projet.html`

**Acceptance criteria:**
1. The creator is the first member automatically, with whole-project scope, and cannot be removed from this form.
2. Other project managers are added by searching a person via SSO; each added member can be removed again.
3. Adding members is optional and never blocks creation; the summary counts them.
4. Activity-level staffing is explicitly not done here — it belongs to the Casting screen.

---

## 3. Tender dashboard

### See where the tender stands

**Description:** As a project manager, I want one screen that tells me how far the tender is and where to go next, so that I don't have to open each step to find out.

**Design:** Dashboard — `dashboard-et-config.html` (dash screen)

**Acceptance criteria:**
1. The hero shows BO-ID, name, system, product line, Bid Director and days to submission.
2. A KPI row shows Total requirements, Confirmed by the systems and Compliance filled in (internal); on a Turnkey tender a fourth count, Confirmed by Turnkey, appears (three counts, no placeholder, elsewhere).
3. The process rail shows exactly two steps — Allocation and Compliance — each with a one-line description, a progress figure and bar, a badge (Current / Open / Done) and an Open link; exactly one step carries the "current" emphasis.
4. A separate "Always open" rail lists Team casting (with staffing coverage), Documents & versions and Q&A, each with its own count and link.
5. Once allocation is finalized, the Allocation card reads Done and the Compliance/Experts side cards become visible.

### Act on what needs me now

**Description:** As a project manager, I want the dashboard to list the things blocking the tender, so that each one is one click from the screen that resolves it.

**Design:** Dashboard, "What needs you now" — `dashboard-et-config.html`

**Acceptance criteria:**
1. Attention cards cover: allocation not finalized (with the count still to validate), uncertain segmentations, overdue contributor responses (naming the person, requirement and days), questions awaiting internal review, a non-compliant requirement, and a new document version ready for review.
2. Each card routes to the screen where the action happens (Allocation, Compliance, Documents, Q&A).
3. Cards are phase-aware: allocation cards show before finalization, compliance/Q&A cards after; the new-version card only once a version has actually arrived.
4. The header count reflects the number of cards currently shown.

### Review pending reassignment requests at tender level

**Description:** As a project manager, I want reassignment requests raised anywhere to be rolled up on the dashboard, so that none waits unseen inside a table.

**Design:** Dashboard rollup card — `dashboard-et-config.html`; data from the shared mailbox in `build_merge.py`

**Acceptance criteria:**
1. A "Pending reassignment requests" card appears only when at least one request is pending, with the count.
2. Each entry names the requirement, who asked and their note, and jumps to the Allocation screen to review it.
3. The card disappears once every request has been approved or rejected.

### Follow recent comments and activity

**Description:** As a project manager, I want the latest comments across the tender in one feed, so that I catch a risk note or a returned assignment without hunting for it.

**Design:** Dashboard, "Recent comments" and "Recent activity" — `dashboard-et-config.html`

**Acceptance criteria:**
1. Recent comments merges reassignment comments (live), compliance verdict comments and risk-field comments, most recent first, capped to the last few.
2. Recent activity lists milestones (version uploaded, Q&A batch sent, allocation milestone reached, a contributor's response) with timestamps.
3. Version-related entries appear only once that version has arrived.

### Read tender statistics for myself and for stakeholders

**Description:** As a project manager, I want operational and comparative statistics on the same panel, so that I can both unblock work and report health.

**Design:** Dashboard, "Statistics" — `dashboard-et-config.html`

**Acceptance criteria:**
1. A "For you" tab shows: bottlenecks by perimeter (ranked by age of the oldest awaiting answer), compliance profile, requirements blocked on the client (Q&A, with age), casting gaps (activities with no manager cast), work invalidated by a new version (only when non-zero), and a trajectory-to-deadline chart.
2. A "For stakeholders" tab shows: compliance profile, progress against deadline in plain words, and AI reliability as a correction rate per field.
3. Bottleneck and blocked rows link to the screen that owns them; the casting gap links to Team casting.
4. Statistics stay visible whatever the allocation state — pending is shown, not hidden.

---

## 4. Team casting

### See casting coverage per activity

**Description:** As a project manager, I want to see which activities and perimeters still have nobody staffed, so that I can close the gaps before allocation lands on them.

**Design:** Team casting — `dashboard-et-config.html` (team screen)

**Acceptance criteria:**
1. A coverage strip shows one card per activity with its state: Fully staffed, n/N staffed, Nothing staffed, or No manager cast yet; clicking a card expands and scrolls to that activity.
2. Each activity group shows its code, name, manager, a "model"/"manual" tag (whether it has its own allocation model) and a coverage badge; groups collapse and expand.
3. Within an activity, each perimeter is a group flagged "Unstaffed" when empty; an activity with no perimeters shows a "Staffed directly (no perimeter)" group.
4. A roster search finds a person across every activity; an "Unstaffed only" toggle hides everything already covered.
5. The dashboard's Team casting card reflects the same coverage (activities fully staffed / total, pending count).

### Staff someone on an activity or perimeter

**Description:** As an activity manager or project manager, I want to add a person to my activity, optionally within a perimeter, so that the activity has someone to answer its requirements.

**Design:** Team casting, "+ Add someone" — `dashboard-et-config.html`

**Acceptance criteria:**
1. The person is found first by searching the SSO directory (keyboard navigable), then a perimeter is chosen: pick an existing one, type a new one (created on the fly and reused thereafter), or leave blank to staff the activity directly.
2. The same person cannot be staffed twice on the same activity and perimeter; the attempt says so.
3. Each staffed row shows who added them and when, and how many requirements they already hold.
4. Only the activity's own manager or a project manager can edit an activity; others see it read-only. An activity with no manager cast cannot be staffed at all.
5. Removing someone is refused while they still hold requirements — their work must be reassigned first.

### Manage the project management team

**Description:** As a project manager, I want the management team visible and editable next to the casting, so that who can do what on the project is settled in one place.

**Design:** Team casting, "Project management team" group — `dashboard-et-config.html`

**Acceptance criteria:**
1. The PM team is shown as its own group with whole-project scope, visible to project managers only.
2. Members are added by SSO search without a perimeter step; adding someone already on the team is refused.
3. A member can be removed, except the last one — a project always keeps at least one project manager.
4. Each member shows who added them and when, or that they created the project.

### Add an activity to the project

**Description:** As a project manager, I want to add an activity that characterisation didn't surface, so that it can be cast and receive requirements.

**Design:** Team casting, "+ Add activity" — `dashboard-et-config.html`

**Acceptance criteria:**
1. Activities are picked from the reference list (Rolling Stock, Communications, Safety & RAMS, Architecture & Buildings…), never typed freehand.
2. Activities already on the project are excluded; when none remain the control says so.
3. The added activity arrives with no manager cast and is expanded, ready to be cast.

---

## 5. Project configuration

### Configure how the project runs

**Description:** As a project manager, I want the project's rules in one settings screen, so that thresholds and workflow choices are explicit rather than implicit.

**Design:** Configuration — `dashboard-et-config.html` (cfg screen)

**Acceptance criteria:**
1. General: project name, BO-ID, product line, submission deadline and the active source document version.
2. Team & experts: the expert roster with requirement counts (an expert with assigned requirements cannot be removed), plus the assignment criteria offered during allocation (PBS, ABS, OBS, Discipline).
3. Workflow & milestones: whether full validation is enforced before export, the overdue threshold in days, the reminder cadence, and whether any change or only substantive changes re-flag an existing response after a new version.
4. AI & segmentation: document rendering approach, uncertainty threshold below which a block is flagged, default table granularity, re-segmentation strategy on a new version, and protection of manual corrections on re-run.
5. Q&A & submission and Versions: issuer channel, AI duplicate detection, mandatory internal review; version numbering, addendum-as-version detection, expert notification timing on version switch.

### Choose appearance and how restricted views hide content

**Description:** As a project manager, I want to set the theme and the restricted-view behaviour, so that the tool fits the room and shows out-of-scope passages the way the team expects.

**Design:** Configuration, Appearance and Team & experts → Restricted view — `dashboard-et-config.html`

**Acceptance criteria:**
1. Light or Dark theme applies immediately across the whole application.
2. Restricted view is either Redacted (blacked-out passages, volume and context perceptible) or Hidden (out-of-scope passages disappear); the choice applies immediately to the Allocation screen's restricted view.
3. The current value is reflected when the screen is reopened.

---

## 6. Documents & versions

### See the tender's source material and its weight

**Description:** As a project manager, I want every document of the tender listed in reading order with its processing state and weight, so that I know what the tender is made of.

**Design:** Documents & versions — `documents.html`

**Acceptance criteria:**
1. Summary counts: documents in the tender, requirements across them, documents still processing, verdicts made stale by a new version.
2. Each row shows position, name and filename, processing state (Ready / Processing / Not processed), current version and date, version count, and weight as a requirement count with a proportion bar and percentage.
3. A document being processed shows a progress strip and the current stage.
4. Search by name or filename; filter to Not fully processed, Has several versions, or Has stale verdicts. The position number stays the document's real place in the tender, not its rank in the filtered view.

### Add a document after creation

**Description:** As a project manager, I want to add a document to a live tender, so that an addendum joins the existing material instead of starting a separate project.

**Design:** Documents & versions, "Add a document" — `documents.html`

**Acceptance criteria:**
1. A dropped PDF is added at the end of the tender and processed after the fact: capture, then translation when the tender's source language isn't English, then characterisation.
2. Progress is visible on the row; the user can leave and come back while it processes.
3. When done, the row becomes Ready with its requirement count, and the document is available for per-document export.

### Reorder or remove a document

**Description:** As a project manager, I want to change the order of documents or take one out, so that the tender reads correctly and mistakes can be undone deliberately.

**Design:** Documents & versions, row actions — `documents.html`

**Acceptance criteria:**
1. A document can be moved earlier or later; the tender order updates.
2. Removing asks for confirmation and states what is lost first: the document's requirements and every characterisation, allocation and compliance verdict recorded against them (or, for an unprocessed document, only the file).
3. Remaining documents keep their order.

### Upload a new version and see what it changes

**Description:** As a project manager, I want a new version of a document to replace it in place and tell me which verdicts it made stale, so that invalidated work is found here, not discovered later.

**Design:** Documents & versions, version history — `documents.html`

**Acceptance criteria:**
1. Uploading a new version increments the version, keeps the history readable per document, and marks the newest as Current.
2. Gap analysis runs automatically and each version shows +added, ~modified, −removed.
3. Verdicts given before the change on affected requirements are counted as stale on the version and on the row, with a direct link to Compliance to confirm or redo them.
4. The screen summary and the "Has stale verdicts" filter reflect the new state.

### Export the requirements of one document

**Description:** As a project manager, I want to export a single document's requirements, so that a partial hand-over doesn't require exporting the whole tender.

**Design:** Documents & versions, "Export one document" — `documents.html`

**Acceptance criteria:**
1. Pick the document, the steps to include (Capture, Characterisation, Allocation) and a format (Excel, CSV, ReqIF, DOORS 9).
2. At least one step must be selected.
3. The result names the format, the document and the number of requirements exported.

---

## 7. Allocation — Requirements review

### Read the tender as a document with requirements overlaid

**Description:** As a project manager, I want to read the tender itself with each block's nature and status visible in place, so that I review in context rather than in a spreadsheet.

**Design:** Allocation, Document mode — `revue-documentaire.html`

**Acceptance criteria:**
1. Documents render as pages with headings, information blocks and requirements; each requirement carries its ID, PBS type and status chip, and comment count.
2. Tables are shown with their own granularity switch (one requirement per row, or the whole table as one requirement).
3. Images render as figures with the number of requirements captured from them; a requirement captured from an image links back to it.
4. Blocks removed in the newer version appear as ghost blocks; each section shows a chip with its change counts.
5. Clicking a block opens it in the detail panel; the same block stays selected and in view when switching between Review, Document and Compare.

### Navigate the requirement tree

**Description:** As a reviewer, I want a collapsible tree of documents, sections and requirements, so that I can move through hundreds of requirements without scrolling blind.

**Design:** Allocation, left navigation — `revue-documentaire.html`

**Acceptance criteria:**
1. The tree is documents → sections → headings → requirements, with requirement counts on documents and sections and change counts (+/~/−) on sections.
2. Everything starts collapsed; selecting a requirement reopens the path to it.
3. Each requirement shows a status dot and badges: to review, unassigned, comments, uncertain segmentation, changed in the version.
4. Search is shared with the table search; an active search or filter shows its full results regardless of what is collapsed, and the footer says how many matched.
5. The panel collapses to a rail and reopens in one click.

### Work through requirements in a table

**Description:** As a project manager, I want every requirement as an editable row, so that characterisation and allocation can be done at speed.

**Design:** Allocation, Review mode — `revue-documentaire.html`

**Acceptance criteria:**
1. Columns: ID, Requirement, Class, Activity, ABS, PBS, TK OBS (Turnkey only), OBS · team, Assigned to, Status, Compliance; rows are grouped under their document and section headers.
2. Class flips in place, Activity opens a multi-select popover, ABS is typed, PBS and Assigned to are dropdowns; each edit marks the row as touched by a human.
3. Requirement text is a one-line excerpt with a Wrap text switch; the row carries badges for parallel allocations, blocked branch, comments and version change.
4. Any column header sorts (ascending, descending, back to document order) and a reset link restores document order; rows can alternatively be grouped by Activity.
5. Requirements can be narrowed to one document; information blocks appear as reduced rows with only their nature and a possible Type-review status.

### Triage requirements by status

**Description:** As a project manager, I want status counts I can click, so that I work the queue that matters (incomplete, to review, to validate, allocated).

**Design:** Allocation, triage bar — `revue-documentaire.html`

**Acceptance criteria:**
1. Pills show live counts for Incomplete, To review, To validate, Allocated and changes between versions; clicking one filters every view, clicking again clears it.
2. A "pending reassignment" pill and, on Turnkey tenders, an "awaiting manual allocation" pill appear only when their count is non-zero.
3. A row's status is the least advanced of its characterisation (Class/Activity) and its allocation (ABS/PBS/OBS); an unassigned requirement is always Incomplete whatever the AI proposed.
4. On a project created in manual or segmentation-only mode, a tag states which AI steps did not run.

### Correct the AI's reading of a block

**Description:** As a reviewer, I want to fix what the AI got wrong about a block — its nature, class, activity or boundaries — so that only trusted characterisation reaches allocation.

**Design:** Allocation, Document and Review modes, detail panel — `revue-documentaire.html`

**Acceptance criteria:**
1. Any block can be reclassified between Heading, Information and Requirement from the document, the table row or the panel; an image can only be demoted to Information.
2. Turning a requirement into Information deletes its allocation data irreversibly and asks for confirmation when an expert has already answered; turning Information into a requirement starts it at Incomplete.
3. AI-detected values (Type, Class, Activity) are marked as unconfirmed; the row reads To review with the reason, and confirming or changing the value resolves it.
4. A block the AI flagged for uncertain segmentation is called out in the panel before validation.
5. A requirement captured from an image can be duplicated to attach a second requirement to the same figure; only duplicates can be deleted, never the original.

### Validate characterisation, then allocation

**Description:** As a project manager, I want an explicit human validation per requirement, so that nothing reaches Allocated — and Compliance — without someone having looked at it.

**Design:** Allocation, status pill / panel CTA / keyboard V — `revue-documentaire.html`

**Acceptance criteria:**
1. Clicking the status pill (or pressing V on the selected row) validates the next stage: characterisation first, then allocation; the pill tooltip says which.
2. Reaching Allocated on the allocation stage sends the branch to Expert Review and says so; the action can be undone from the toast.
3. An Incomplete row cannot be validated and the attempt explains why.
4. On a requirement with several activities, the parent validates only its characterisation; each activity then validates its own allocation from its sub-row.
5. Validating a weak derivation as-is is recorded as AI feedback.

### Assign the person responsible

**Description:** As a project manager, I want to assign who handles a requirement, so that it can be sent out for an answer.

**Design:** Allocation, "Assigned to" — `revue-documentaire.html`

**Acceptance criteria:**
1. The person is chosen inline in the row or, in the panel, by searching the directory plus everyone already assigned on the tender; a new pick joins the roster.
2. An AI-proposed assignment is shown with its reason and can be accepted or rejected.
3. On a multi-activity requirement each activity has its own assignee; on a multi-team activity each team has its own.
4. Assigning or unassigning can be undone from the toast.

### Understand and correct the two-pass allocation on a Turnkey tender

**Description:** As a project manager on a Turnkey tender, I want to see how a requirement was distributed to activities and then allocated within each, so that I can correct the step that went wrong.

**Design:** Allocation, detail panel (PM view and activity view) — `revue-documentaire.html`

**Acceptance criteria:**
1. The PM view shows Type, then the single dimension pass 1 read (PBS if technical, ABS if non-technical), then the Activity list with each activity's confidence and whether it has a model; activities can be added from here.
2. Each activity block shows its OBS breakdown (one row per organisation with confidence), who is assigned, its compliance, and opens an activity detail showing that activity's own PBS → ABS → OBS · team chain.
3. Correcting PBS clears ABS and OBS, correcting ABS clears OBS — the consequence is applied and announced.
4. An activity without a model is tagged "manual" and counted in the awaiting-manual-allocation queue; the derivation is flagged weak below the confidence threshold.
5. In the contributor's view, OBS is an editable list of organisations (add/remove); several organisations mean several verdicts to consolidate.

### Manage a requirement allocated to several activities or teams

**Description:** As a project manager, I want a requirement's activities and teams shown as sub-rows, so that multi-allocation is visible and each part is tracked on its own.

**Design:** Allocation, branch and team sub-rows, panel "Allocations" — `revue-documentaire.html`

**Acceptance criteria:**
1. A caret on the requirement expands one sub-row per activity; an activity with several teams has its own caret for one sub-row per team.
2. Each activity/team sub-row shows its typology, TK OBS confidence, OBS · team, assignee, its own status and its own compliance verdict.
3. A compliance verdict is entered on a team; the activity's and the requirement's verdicts are derived — most restrictive wins, pending until all have answered — never typed.
4. Removing an activity deletes its branch (after confirmation if answered); the last activity can never be removed — a replacement must be requested or added first.
5. The project manager can lock the requirement's final verdict so it stops following the tree; a pending verdict cannot be locked, and the lock is visible to everyone allocated on the requirement.

### Compare two versions of the tender

**Description:** As a project manager, I want to walk the changes between two versions, so that each modification is reviewed and, if needed, turned into an action.

**Design:** Allocation, Compare mode — `revue-documentaire.html`

**Acceptance criteria:**
1. Choose the two versions to compare; a summary shows added, modified and removed counts.
2. Previous/next buttons step through changes and open each in the panel with its type (Added / Modified / Removed), description and affected passage.
3. Each change is marked New, Reviewed no impact, or Action required; an action/reminder can be created from it.
4. Modified requirements are marked in the document, the table and the tree; removed ones appear as ghost blocks.

### Edit the segmentation the AI produced

**Description:** As a reviewer, I want to split, merge and regroup blocks, so that requirement boundaries match the document.

**Design:** Allocation, "Edit segmentation" mode — `revue-documentaire.html` (currently hidden behind a feature flag, see Placeholders)

**Acceptance criteria:**
1. Segmentation mode opens the Document view with Split and Merge controls on every block; reading clicks are suspended while it is on.
2. Split cuts a block in two at a sentence boundary; Merge folds the next block into this one.
3. Tables can be regrouped as one requirement or split back into row-level requirements.
4. Every affected block's characterisation and assignment are flagged for review; leaving the mode saves the changes and adds them to the review queue.

### Read the original language and correct the translation

**Description:** As a reviewer on a non-English tender, I want to read a requirement in its original language and fix the English working text, so that the pipeline runs on a trustworthy translation.

**Design:** Allocation, detail panel → Translation tab — `revue-documentaire.html`

**Acceptance criteria:**
1. A "Read in" selector offers the original language first, then English (working text), then extra reading languages; the original is shown by default and the panel title follows the choice.
2. The original and the English working text are shown side by side; the English can be corrected and saved.
3. Every correction is logged with who, when, before and after; a corrected row is marked.
4. The original text is never edited and never fed back into the pipeline; exports carry the original text with comments in English.

### Consult a requirement's history and comment on it

**Description:** As a reviewer, I want each requirement's timeline and a place to comment, so that decisions are traceable and questions reach the right person.

**Design:** Allocation, detail panel → Activity tab; notifications — `revue-documentaire.html`

**Acceptance criteria:**
1. The Activity tab shows the roles on the requirement (Admin, Assigned to) and a timeline of what happened to it.
2. A comment can be posted with @-mentions; the requirement's comment count updates everywhere it is shown.
3. Notifications list mentions, requirements modified in a new version and reminders; opening one jumps to the requirement's activity.

### See the tender as an activity manager sees it

**Description:** As an activity manager, I want to see only the requirements assigned to me, with the rest redacted or hidden, so that I work my scope without reading the whole tender.

**Design:** Allocation, "View as" / restricted view — `revue-documentaire.html`

**Acceptance criteria:**
1. In a restricted view, the table, tree and document show only the requirements (or activities of a requirement) assigned to that manager; information blocks stay visible.
2. Out-of-scope passages are redacted or hidden according to the project's restricted-view setting.
3. A banner names whose view it is and offers a way back to the admin view; bulk selection is cleared on switch.
4. The manager's own status is the status of their activity, not the requirement's overall rollup.

### Finalize the allocation

**Description:** As a project manager, I want to close the allocation step in one gesture, so that the register is produced and every assigned expert is told what to answer.

**Design:** Allocation, "Finalize allocation" — `revue-documentaire.html`; state shared via `build_merge.py`

**Acceptance criteria:**
1. Finalizing is refused while any requirement is not fully allocated, with the count.
2. The confirmation lists what will happen: export the requirements register (.xlsx, with its column set) and send each assigned expert their requirements with a link to the qualification screen, with a per-expert count.
3. Confirming generates the register, notifies the experts and returns to the dashboard, where Allocation reads Done.

### Export requirements from the review

**Description:** As a project manager, I want to export a chosen subset of requirements in the format the downstream tool needs, so that the register lives upstream in DOORS or Excel when required.

**Design:** Allocation, "Export" panel — `revue-documentaire.html`

**Acceptance criteria:**
1. Scope is a document (or all) narrowed by the active column and advanced filters; the panel states how many requirements match and restates the filter in plain language.
2. Steps to include: Capture, Characterization, Allocation — at least one.
3. Formats: Excel, CSV, ReqIF, DOORS 9 (CSV), DOORS Next (ReqIF).
4. On a non-English tender, requirement text exports in the original language; comments and categories in English.
5. An export with zero matching requirements is refused.

---

## 8. Compliance

### Track consolidation across the tender

**Description:** As a project manager, I want to see which requirements are consolidated and what is holding the others up, so that I chase the right people.

**Design:** Compliance, triage bar and table — `compliance.html`

**Acceptance criteria:**
1. The header shows requirements consolidated / total, the percentage, and assignments answered / total; pills count answered, awaiting answer, awaiting Q&A, reassignment needed, overdue and outdated version, and filter the table.
2. Each requirement row shows Status (progress), Compliance (internal verdict, derived most-restrictive), the compliance comment, External compliance, Risk accepted, last follow-up and age; a requirement is pending until every activity has answered.
3. A caret expands one sub-row per activity and, within an activity, one per team; sub-rows are collapsed by default.
4. Sort by action needed first, status, contributor or reference; a "Needs my action" toggle keeps only reassignment requests and just-unblocked assignments.
5. When every requirement is consolidated, a banner announces the compliance matrix is complete and offers the export.

### Navigate by section or by contributor

**Description:** As a project manager, I want to browse compliance either by document section or by contributor, so that I can read the tender or chase a person.

**Design:** Compliance, left navigation and Document view — `compliance.html`

**Acceptance criteria:**
1. By section: documents → sections → requirements, each with a verdict dot and a count of activities when there are several.
2. By expert: one card per contributor with answered / pending / blocked counts, a progress bar, overdue silence in days, and a Remind button; clicking the card opens their first requirement.
3. A Document view overlays each requirement's consolidated verdict on the source text, read-only.
4. The navigation and detail panels collapse and reopen in one click.

### Render a verdict as a contributor

**Description:** As a contributor, I want to answer the assignments allocated to my activity, so that my technical assessment feeds the consolidation.

**Design:** Compliance, contributor view, detail panel → Assignment tab — `compliance.html`

**Acceptance criteria:**
1. A contributor sees the whole activity they belong to, and only that; the assignment panel shows who it is assigned to, how long it has waited and whether it is over the overdue threshold.
2. Rendering a verdict means choosing Compliant (with an optional comment, where R&D needs are written in prose) or Not compliant (with a category and a free-text topic).
3. The verdict is recorded as internal compliance on that activity; the response, its date and any attached evidence are shown afterwards.
4. Instead of answering, the contributor can request a reassignment (right activity wrong person / wrong activity / activity doesn't apply), naming the replacement and a reason.

### Declare external compliance and the risk accepted

**Description:** As a project manager, I want to declare to the client a compliance that may differ from the internal assessment, and justify it, so that the exported answer is a deliberate decision.

**Design:** Compliance, panel header band and table columns — `compliance.html`

**Acceptance criteria:**
1. External compliance is one declaration per requirement, made by the project manager in the panel header beside the consolidated internal verdict.
2. Left undeclared, external inherits the internal verdict and is shown dimmed; declaring it shows a solid value and a "≠ internal" marker when it deviates.
3. Declaring Compliant over an internal Not compliant requires a risk note; the note is shown in the header and in the Risk accepted column.
4. A declaration can be updated or cleared, in which case the internal verdict travels to the client again.
5. Both values are filterable in the advanced filter (External compliance, Risk accepted).

### Chase overdue contributors

**Description:** As a project manager, I want to see which assignments are overdue and remind their contributors, so that consolidation doesn't stall silently.

**Design:** Compliance, overdue pill, reminders, bulk bar — `compliance.html`

**Acceptance criteria:**
1. An assignment is overdue when it is awaiting an answer for at least the configured threshold; the age column and the overdue pill reflect it.
2. Reminders can be sent per assignment (panel button or R key), per contributor (navigation card), to everyone overdue at once, or to a bulk selection of requirements.
3. A reminder updates the assignment's last follow-up date.

### Escalate a requirement to the client Q&A

**Description:** As a project manager or contributor, I want to raise a question to the issuer from an assignment, so that a blocked assignment is tracked as blocked, not as unanswered.

**Design:** Compliance, "Escalate to client Q&A" — `compliance.html`; register in `qa.html`

**Acceptance criteria:**
1. Escalating creates a draft question pre-filled from the requirement and the assignment's note.
2. The assignment moves to Awaiting Q&A, stops counting as answered and blocks the requirement's consolidation; its panel says so and links to the Q&A register.
3. The Q key escalates the selected assignment.

### Handle an assignment returned by the contributor

**Description:** As a manager, I want an assignment a contributor sent back to come to me with their reason, so that I can reallocate it and send it out again.

**Design:** Compliance, "Reassignment needed" panel — `compliance.html`

**Acceptance criteria:**
1. A returned assignment shows the contributor's reason and reads as an internal loop — nothing leaves the company.
2. I choose a new person from the roster; the assignment goes back to Awaiting answer with a reset age.
3. Requests raised elsewhere (Allocation screen, shared mailbox) appear here the same way; resolving one updates the shared request.

### Export the compliance register

**Description:** As a project manager, I want to export the compliance register for the client, with the risks summarised, so that the answer leaves the tool in one file.

**Design:** Compliance, "Export" — `compliance.html`

**Acceptance criteria:**
1. The export generates the qualification register for the tender.
2. It includes a risk summary: how many requirements are non-compliant and how many are still pending consolidation.
3. On a non-English tender, requirement text is exported in the original language; comments and categories in English.

---

## 9. Q&A

### Prepare and export the question batch

**Description:** As a project manager, I want to consolidate the contributors' questions into one batch for the issuer, so that the client gets one clean list.

**Design:** Q&A, Questions tab — `qa.html`

**Acceptance criteria:**
1. Draft questions raised from Compliance land here; the export card counts what is ready and from how many contributors, and exports the batch as Excel (one row per question with its requirement ID) for me to forward.
2. Questions that look like duplicates are flagged before export and can be merged into one, keeping every requirement link.
3. A question can be excluded from the export and included again; it stays on record in its own group.
4. The register groups Drafts, Sent to the issuer, Answered and Excluded, searchable by text or requirement and filterable by activity.
5. The question cut-off date is shown; once passed, late questions can still be raised and it is my call whether they go out.

### Import the issuer's answer dossier

**Description:** As a project manager, I want to import the client's answers in whatever form they came, so that matching starts from the real document rather than a re-typed one.

**Design:** Q&A, Answers tab — `qa.html`

**Acceptance criteria:**
1. The dossier is imported from a file or pasted as raw text; no fixed layout is assumed.
2. Extraction produces question/answer pairs for every bidder, not only ours; nothing is discarded.
3. The result states how many pairs were extracted, how many matched automatically and how many need arbitration; the expected-answer date is shown and flagged overdue with the number of assignments still blocked.

### Arbitrate the answers that could not be matched

**Description:** As a project manager, I want to resolve unmatched answers one at a time, so that every blocked assignment is unblocked or the answer is filed as context.

**Design:** Q&A, arbitration queue — `qa.html`

**Acceptance criteria:**
1. One item at a time with progress; each shows the answer, whether it is our question or a competitor's, and candidate requirements with confidence.
2. Pick a candidate (keys 1–9), declare No matching requirement (N) or Skip to the back of the queue (S).
3. Matching one of our questions marks it answered, unblocks the assignment and notifies the contributor; competitor answers are attached as context.
4. Resolved items and context are listed once the queue is empty.

---

## 10. Cross-screen flows

### Filter a requirement table

**Description:** As a reviewer, I want to narrow a requirement table by column values or by a compound filter, so that I focus on one subset of work.

**Design:** Allocation table — `revue-documentaire.html`; Compliance table — `compliance.html`; engine in `table-engine.js`

**Acceptance criteria:**
1. A filter control on a column header opens that column's values with All/None and a shown count; unchecking values narrows the table and the header shows the filter is active.
2. A Filter button opens an advanced builder: conditions on any field with type-appropriate operators, one level of groups, match all/any, a live count of matching rows, and a per-condition count while editing.
3. Nothing applies until confirmed; a filter can be saved under a name and reapplied later.
4. Active column and advanced filters are read back as one plain-language sentence with a single Clear.
5. Search is separate from filters and combines with them.

### Select rows in bulk

**Description:** As a reviewer, I want to select many rows and act once, so that repetitive changes take one gesture.

**Design:** Allocation bulk bar — `revue-documentaire.html`; Compliance bulk bar — `compliance.html`; engine in `table-engine.js`

**Acceptance criteria:**
1. Rows are selected by checkbox, shift-range, drag along the selection gutter, or select-all-in-view; a bar shows the count and clears in one click.
2. "Show only these" narrows the table to the selection, suspending the other filters until Show all.
3. On Allocation: assign (person, activity, PBS), classify (technical/non-technical, move to Information), mark to review, validate — with a summary of what was skipped.
4. On Compliance: send a reminder to every pending assignment in the selection, or jump to the first selected requirement to reassign its expert.

### Customise the table and move with the keyboard

**Description:** As a reviewer, I want to hide, reorder and collapse columns and move cell by cell without the mouse, so that the table fits my work.

**Design:** View menu and keyboard on both tables — `revue-documentaire.html`, `compliance.html`, `table-engine.js`

**Acceptance criteria:**
1. A View menu lists the optional columns as checkboxes that can be dragged into a new order; clicking a column header collapses or expands it.
2. On a Turnkey tender the Allocation table switches its default columns between the PM view and the activity view.
3. Arrow keys (and J/K) move an active cell across rows and visible columns; Space toggles selection; Enter confirms an edit and moves down, Escape cancels.
4. Screen shortcuts: V validate and A jump to the assignee on Allocation; R remind and Q escalate on Compliance.

### Request, review and apply a reassignment

**Description:** As a contributor or activity manager, I want to ask for a reassignment or a missing activity, and as a project manager I want to approve or reject it, so that wrong allocations are corrected through one traceable loop.

**Design:** Compliance contributor panel — `compliance.html`; Allocation propose block and "Allocations" cards — `revue-documentaire.html`; dashboard rollup — `dashboard-et-config.html`; mailbox in `build_merge.py`

**Acceptance criteria:**
1. A request names one of three reasons (right activity wrong person, wrong activity, activity doesn't apply), the replacement person or activity, and a note; a missing-activity proposal names the activity and why.
2. The branch reads Reassignment needed everywhere until resolved; the requirement shows a blocked badge and counts in the pending-reassignment pill.
3. The project manager approves or rejects from the requirement's allocation card; approval always replaces (person or activity), never leaves a requirement with zero activities; rejection reverts to the prior state.
4. The request and its outcome are logged on the requirement, visible in the dashboard rollup and comments feed, and reflected on every screen.

### A new document version invalidates prior work

**Description:** As a project manager, I want work done on superseded text to be flagged and reset, so that no verdict silently stands on a requirement that changed.

**Design:** Documents & versions — `documents.html`; Compliance "outdated version" — `compliance.html`; dashboard attention and statistics — `dashboard-et-config.html`

**Acceptance criteria:**
1. A new version's gap analysis counts the verdicts it made stale and links to Compliance.
2. On Compliance, an affected requirement is flagged "outdated version", filterable, and its assignment panel says it was answered on an outdated version.
3. Resetting for the new version wipes the internal verdict and response, the requirement's external declaration and risk, and sends the assignment back to Awaiting answer.
4. The dashboard surfaces the new version as an attention item and counts invalidated answers in statistics.

### Capture AI feedback from corrections

**Description:** As a project manager, I want every correction of an AI proposal to be captured as training signal, with a reason when the AI was confidently wrong, so that the next model improves without extra work.

**Design:** Allocation corrections — `revue-documentaire.html`; Configuration → AI feedback — `dashboard-et-config.html`; store in `build_merge.py`

**Acceptance criteria:**
1. Changing an AI-proposed class, activity, nature or assignment is logged silently with before/after and the AI's confidence.
2. When the AI was above the high-confidence threshold and still wrong, a small box asks for a one-line reason with reason chips or free text; it can be dismissed.
3. The AI feedback section shows acceptance rates per step, recurring correction patterns, and the live corrections of the session.
4. Feedback is queued for a future model; nothing in the current project is re-scored.

### Move between the tender's screens

**Description:** As any user, I want a consistent header on every screen, so that the tender's support screens and settings are always one click away.

**Design:** All screens; routing in `build_merge.py`

**Acceptance criteria:**
1. The breadcrumb names the tender and returns to its dashboard; the logo returns to My tenders.
2. An icon cluster reaches Team casting, Documents & versions, Q&A and notifications; a gear opens Configuration.
3. The current user's identity comes from the directory and shows as an avatar with name and title.
4. Routes are addressable (hash), so a screen can be linked to directly, including the contributor's compliance view.

### Consult a requirement's context

**Description:** As a reviewer or contributor, I want the source passage, the frozen requirement facts and similar past experience beside the requirement, so that I decide with context.

**Design:** Detail panel tabs — `revue-documentaire.html` (Details/Activity/REX/Translation), `compliance.html` (Assignment/Activity/Requirement/Document/REX/Chat)

**Acceptance criteria:**
1. The source section is named and can be opened in the document at the right position.
2. On Compliance, the Requirement tab shows the frozen facts (type, assignments, consolidated verdict, source passage) and states they change only through a new version.
3. A REX tab lists similar past experiences ranked by match, with their source; opening one goes to the source system. The tab appears only when there are matches.
4. A Chat tab is reserved for asking about this requirement without leaving the company (see Placeholders).

---

## Placeholders and gaps

Controls with no behaviour and no evident intent, dead ends, and sample content — distinct from what merely needs a backend.

1. **Notification bells are inert on four of five screens.** Only Allocation (`revue-documentaire.html`) has a dropdown (three fixed items). Dashboard, Compliance, Documents and Q&A show a bell with a badge dot and no behaviour.
2. **The "new version v2.2" story can never appear.** The dashboard's "New version v2.2 ready for review" card, two "Recent activity" entries and the "Work invalidated by a new version" statistic are gated on a shell flag (`isV22Uploaded`) that nothing in any source screen sets any more; the Configuration copy still refers to a "Simulate upload — v2.2" button that no longer exists.
3. **Edit segmentation is hidden behind a feature flag** (`FLAGS.captureCorrection=false`), yet the dashboard's "2 uncertain segmentations — Fix in review" card and the panel's "Uncertain segmentation" warning point at it. There is currently no way to act on an uncertain segmentation.
4. **Compare mode is static.** The two version selects have no behaviour, the summary (+1 ~2 −1) is fixed text, the change list is three fixed requirements, and "Create action / reminder" only confirms.
5. **"v2.1 active — Switch version" pill** in the Allocation header has no behaviour.
6. **Configuration is largely unwired by its own admission.** Every section except Appearance (theme) and Restricted view (redacted/hidden) carries a "demo only — not wired in this build" warning; Save and Discard only confirm that. Two rosters coexist: Configuration's "Team & experts" list and Casting's roster are independent.
7. **Dashboard "Recent activity — View all"** is a link to nowhere (`#`).
8. **Dashboard side cards are hand-typed.** The Compliance bar and the Experts card (Sophie 3/4, Karim 2 late, Claire 3/3) are fixed content; the dashboard's requirement mirrors (14 requirements) do not reconcile with the Compliance screen (104) or Allocation (real capture data), so counts differ across screens by construction.
9. **No way to cast a manager to an activity.** Casting says "Assign an activity manager in the project wizard or from here once that flow is wired"; the wizard no longer does it, and activities added from the reference list stay without a manager.
10. **Compliance bulk "Reassign expert"** only selects the first checked requirement and asks the user to "jump to the branch below" — no bulk reassignment exists.
11. **Reminders are inconsistent.** The R key and the bulk reminder update the assignment's last follow-up; the panel button, the contributor card and "Remind all overdue" only confirm.
12. **Chat tab** (Compliance) is an explicit stub ("Chat isn't built yet"); its tender/internal-documents switch is visual only.
13. **Non-compliance Category list** is an explicit placeholder ("the real categories aren't defined yet").
14. **Region codes** (EUR/MEA/APAC/AME/AFR) and the product lines Rolling Stock and Services are marked as placeholders pending real values.
15. **Placeholder copy** is flagged in the My tenders intro and in the dashboard's per-step descriptions.
16. **Excluding a question from the Q&A batch does not notify the contributor** — the screen says so itself.
17. **REX "Open ↗"** only confirms; there is no source system to open.
18. **Demo scaffolding, not product:** Reset demo (button and Ctrl+Shift+R), the DEMO view-as control on Compliance, "View as" on Allocation (labelled demo only), the "DEMO Compliance (contributor)" link on the dashboard, "Viewing as" on Casting, and "Simulate 200 roster". Also the block on opening any tender other than the built-out one.

## Ambiguities

> **Settled on 2026-09-14** — see DEC-028 to DEC-039 in [`docs/current/OPEN-QUESTIONS.md`](../current/OPEN-QUESTIONS.md). The observations below describe the prototype as it stands today, before those decisions are applied; they are kept as the record of what was found, not as open questions.

Things whose purpose could not be determined confidently from the screen.

1. **What "Finalize allocation" gates.** The button enforces full allocation and marks the step Done, and the Compliance/Experts side cards wait for it — but Compliance is reachable and workable from day one, and the Configuration toggle "Enforce full validation before export" claims to control this while stating it doesn't.
2. **Two mechanisms for "the answer that goes to the client".** Allocation lets the project manager lock a requirement's final verdict (`complianceLocked`, lockedBy, "tree now says…"); Compliance replaced its own lock with an external declaration plus risk note. Which one is the authoritative client-facing verdict is unclear.
3. **Who the "Project manager" is on Compliance.** The role select says Project manager, but the viewer defaults to the first contributor in the roster; the "My team only" chip narrows a project manager to one contributor's team.
4. **Dashboard product line.** The reference tender's dashboard hero shows product line SIG, while My tenders and Allocation treat the same tender as Turnkey (pass-1 distribution, "Confirmed by Turnkey" KPI).
5. **"Compliance" column on the Allocation table.** Allocation shows a 4-value compliance (Compliant / R&D Needed / Not Compliant / Pending) editable per branch and team, while verdicts are meant to be rendered on the Compliance screen with a 2-value scale. Whether Allocation should show or edit compliance at all is unclear.
6. **Document-view legend on Compliance** lists Partially and Needs clarification dots that no data on the screen produces.
7. **Q&A register duplicated.** Compliance still holds its own question list and status groups (Draft / Internal review / Exported for issuer / Answered) alongside the Q&A screen's register (Drafts / Sent / Answered / Excluded); which is the register is unclear.
8. **Peek row** (`togglePeek`) exists in code with no way to reach it — intent unknown.
9. **Q&A "Answers" badge** counts items awaiting arbitration, not answers received.

## Naming inconsistencies

> **Settled on 2026-09-14** — the canonical vocabulary is fixed by DEC-029 (Allocation / Compliance), DEC-030 (Contributor), DEC-031 (two verdicts), DEC-032 (activity list), DEC-033 (Activity → Perimeter → Person, "typology" dropped) and DEC-034 (TK OBS / OBS · team kept) in [`docs/current/OPEN-QUESTIONS.md`](../current/OPEN-QUESTIONS.md). The list below is the record of the drift found, and therefore of what has to be renamed.

Same concept, different names — or one name for two things — as observed. No normalisation attempted.

1. **The first step**: "Allocation" (dashboard, My tenders, finalize button) vs "Requirements review" (screen title), route `review`, "Review finalized" (toast), "Expert Review" (what a branch is sent to on validation).
2. **The second step**: "Compliance" (screen, dashboard) vs "Follow-up" (Configuration copy: "Follow-up screen", "Follow-up's lock") vs "qualification screen" (finalize modal, export filename `_qualification.xlsx`).
3. **Roles**: the same people are "SIG manager" (Allocation, Dashboard) and "SIG contributor" (Compliance); "expert" is used for contributors (finalize modal "Send to assigned experts", Config "Team & experts", wire value `byRole:"expert"`), while Compliance's own copy says contributor. The current user is "Bid Director" (header), "Project lead (admin)" (Allocation roster), "Project manager" (Compliance role select).
4. **Activity vocabularies differ per screen**: Allocation uses 16 capture codes whose labels equal their codes (AFC, CJV, … SIG, TRK); Compliance and Q&A use 5 (SIG & Urban, Mainline Wayside, Safety, Telecom, Infrastructure); Casting uses 7 (Signalling & Urban, Mainline, Infrastructure, Power Supply, Telecom, Civil Works, Systems Integration). `sys` means Safety on Compliance and Systems Integration on Casting.
5. **"Typology" vs "Activity"**: reassignment reasons read "Right typology, wrong person / Wrong typology" on Allocation and "Right activity, wrong person / Wrong activity" on Compliance; internal fields are `perim`/`typo`; the missing-activity proposal is a "missing typology" in its toast.
6. **"Perimeter"** means a sub-activity (Interlocking, ATP…) on Casting, the activity list itself on Allocation (`b.perim`), and an activity in the dashboard's "Bottlenecks by perimeter" / "Casting gaps: perimeters unstaffed".
7. **"OBS"** is an activity in pass 1 ("TK OBS") and a team/service in pass 2 ("OBS · team"); the contributor panel calls the same list "organisation" ("+ Add organisation").
8. **Compliance scales**: Allocation 4 values (Compliant / R&D Needed / Not Compliant / Pending); Compliance 2 values plus pending; dashboard segments Compliant / Partial / Non-compliant / Awaiting and, in statistics, Compliant / R&D needed / Not compliant / Pending; Compliance's document legend adds Partially and Needs clarification; a dashboard feed item cites "verdict Needs clarification".
9. **Status vocabularies**: My tenders statuses (Allocation, Compliance, Processing, Submitted, plus seed values `expert_review`, `qa_versioning` labelled "Expert review", "Q&A & Versioning"); Allocation requirement statuses (Incomplete, To review, To validate, Allocated); branch statuses (Proposed, Assigned, Awaiting answer, Awaiting Q&A, Reassignment needed, Answered); the dashboard's mirror uses `toreview`, `suggested`, `allocated`, `edited` — the last two exist nowhere else.
10. **Q&A question statuses**: Compliance groups Draft / Internal review / Exported for issuer / Answered by issuer; the Q&A screen groups Drafts / Sent to the issuer / Answered / Excluded from export.
11. **"Register"** names both the allocation export (`_requirements.xlsx`) and the compliance export (`_qualification.xlsx`), and the Q&A list ("Q&A register").
12. **Documents screen**: "Documents & versions" (screen, header icons) vs "Versions & exchanges" (Compliance frozen note) vs "Versions" (Configuration section, creation wizard copy).
13. **Identifier label**: "BO-ID" on screens vs `ref` in data; "Project name" (creation, config) vs "tender" everywhere else ("New tender" / "New project" both appear as button labels).
14. **"Manager" field**: the table column is "Assigned to", the data field is `manager`, the panel says "Assigned to · handles this requirement", the finalize modal says "experts".
