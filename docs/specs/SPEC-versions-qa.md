# SPEC — Versions & Q&A

> Derived from the prototype's actual behaviour, per `docs/prompts/PROMPT-derive-specs-from-prototype.md`. Describes "Screen 3" (`#screen3`, `state.screen===3`) of `suivi-experts-et-versions.html` as built — the counterpart to `docs/specs/SPEC-followup.md` ("Screen 2"); see that spec's header note for why the file is split this way. Cross-references `docs/specs/SPEC-domain-model.md`.

## 1. Purpose

Two related but distinct jobs in one screen: tracking incoming AO document versions and their gap analysis, and recording the tender issuer's official answers to questions the team has sent them. This is the screen's **always-open** half — unlike Follow-up, it is never gated on Allocation being finalized, since a new version or an issuer answer can arrive at any point in the tender lifecycle.

## 2. Actors

The same manager persona as Follow-up; no role-specific content on this screen.

## 3. Entry points

- The "Versions & Q&A" tab in the shared header nav.
- The Dashboard's "Versions & Q&A" phase card, always shown as "Open" (never locked, unlike the Follow-up card).
- **Default landing screen**: on a plain page load, if Allocation isn't yet finalized, the app opens directly here instead of Follow-up (silently — no "locked" toast on a first load, only if the user explicitly tries to click into Follow-up; see `SPEC-followup.md` §7).
- A `#versions` hash deep-link also lands here.

From here: version-review actions route to the Allocation screen's Compare mode (out of scope for this spec). Nothing here routes into `SPEC-followup.md`'s own Q&A register view directly — see §8 for how the two screens' Q&A data actually relate.

## 4. Layout

- **Header** — shared with Follow-up (logo, breadcrumb, screen-nav, notification bell, Export button — hidden on this screen, Configuration icon, avatar). The Follow-up-only mode switch (Table/Document/Q&A) is hidden here.
- **Hub tabs** — "Document versions" / "Issuer responses {count}".
- **Document versions tab** — an upload zone ("Simulate upload — v2.2") above a vertical timeline of version cards, newest first.
- **Issuer responses tab** — a two-column layout: a list of every question already sent to or answered by the issuer (left), and a detail panel for the selected one (right).

## 5. Data displayed

- **Version cards**, from `VERSIONS` (newest-first): version number, a state badge (processing / gap analysis ready / review in progress / integrated), upload date, a one-line note, and state-dependent extras — a progress bar while processing, added/modified/removed gap chips once analysis is ready, a downstream-impact note when one exists, a review-progress bar while a review is in progress, and a "review changes" / "resume change review" / "view historical diff" action depending on state.
- **Issuer-responses list**, from the same `QA` array `SPEC-followup.md` describes, filtered to `sent` or `answered` — question id, text, linked requirement ref(s), sent date, an "Answered · propagated" or "Awaiting issuer" pill, and (if flagged by the simulated bulk-import match) an "Uncertain match — confirm manually" flag.
- **Detail panel** — for an unanswered question: a textarea pre-filled with plausible sample answer text, an attachment placeholder, and what the answer will propagate to; for an already-answered one: the recorded answer, its date, and a 3-step "propagation chain" confirmation (recorded / propagated / expert notified).

## 6. Interactions

- **Switch hub tab** (Document versions / Issuer responses) — swaps the visible pane. *Implemented.*
- **"Simulate upload — v2.2"** — adds a new version card in `processing` state, then after a fixed 2.4s delay flips it to `ready` with gap stats (+2 ~1 −0) and a downstream-impact note, flags `EXG-005` as `outdated` (the same flag `SPEC-followup.md`'s table/document views read to show a "Δ outdated" marker), and calls the shell's `setV22Uploaded(true)` — which is what actually gates the Dashboard's and Follow-up's v2.2-related attention items and activity-feed entries (`SPEC-dashboard.md` §5, decision recorded as TB5 in `docs/decisions/DECISIONS.md`'s ticket history). A second toast confirms the outdated-response flag a second later. Can only be triggered once per session — a second click toasts "v2.2 already uploaded" and does nothing further. **Represented/backend-dependent**: a real upload would parse an actual document and compute a real diff (`SPEC-backend-requirements.md` FR16–17); here the gap numbers and the specific affected requirement are hand-scripted.
- **"Review changes in Compare mode" / "Resume change review"** (on a `ready`/`reviewing` version) — routes to the Allocation screen. *Implemented as a route*, the Compare-mode experience itself is out of scope for this spec.
- **"View historical diff"** (on an `integrated` version with gap data) — a toast only ("Historical diff opened (read-only)"); no diff view, modal, or navigation actually occurs. **Placeholder/gap** — see §10; this is the thinnest interaction on either half of this file, unlike the version-upload flow above, which at least produces a full, if simulated, result.
- **Select an issuer-response row** — opens it in the detail panel. *Implemented.*
- **Record an issuer answer** — the manager types (or uses the pre-filled sample) answer text and clicks "Record & propagate": the question is marked `answered`, and — this is the real mechanism, not simulated — every allocated activity anywhere in `REQS` that was `awaiting_qa` and either referenced this question by `qaRef` or belonged to one of the question's linked requirements is moved back to `awaiting_answer` at age 0. *Implemented.* Two sequenced toasts confirm the record, then (700ms later) the propagation and expert notification. **The unblock itself is real state mutation; the "expert notified" half of that second toast is represented** — no real notification is sent (`SPEC-backend-requirements.md` FR7).
- **"Import response document"** — a single bulk action: a toast claims one answer was matched automatically, then (900ms later) flags one already-`sent` question as an uncertain match needing manual confirmation. **Represented/backend-dependent** — entirely scripted (a fixed toast sequence, not real document parsing), but it does produce one real, visible state change (the flag), unlike "View historical diff" above.

## 7. States

- **Version card states** — processing / ready / reviewing / integrated are each fully designed with distinct visuals and available actions, not stubs.
- **Empty / no selection** (Issuer responses detail panel) — a prompt to select a question or import the response dossier.
- **Answered vs. unanswered** (Issuer responses detail panel) — two distinct, fully designed layouts.
- **Already-uploaded guard** — v2.2 can only be simulated once; a second attempt is a no-op with an explanatory toast, not a silent failure or a duplicate card.
- **Loading** — the processing state on a version card is the closest thing to a loading state, and it's fixed-duration (2.4s) rather than tied to a real completion signal.
- **Error** — not present.

## 8. Business rules

- **This screen is never gated** — unlike Follow-up, there is no finalized-allocation requirement to view or use anything here, matching the stated rationale that a new AO version or an issuer answer can arrive "at any stage, even mid-allocation."
- **Screen 2's Q&A register and this screen's Issuer-responses list are two views onto the same underlying question lifecycle, not two independent datasets.** Both read and write the same in-memory `QA` array: a question drafted and sent from Follow-up's register genuinely appears here once sent, and recording its answer here genuinely unblocks the allocated activity back on Follow-up's table. The two screens differ in audience and stage (internal drafting/batching vs. official issuer-answer recording), not in data ownership.
- **An issuer answer unblocks an allocated activity via two different match paths** — either the allocated activity's own `qaRef` points at the answered question, or the allocated activity's parent requirement id appears in the question's `reqs` list. Both paths are checked; an allocated activity matching either is unblocked.
- **A matched/unblocked allocated activity is not itself "answered."** The issuer's reply closes the *question*, not the *requirement* — the allocated activity returns to `awaiting_answer`, still needing the expert's actual verdict, consistent with the domain model's rule that a Q&A answer removes a blocker rather than substituting for the expert's judgment.

## 9. Non-functional

Nothing scale-related — 3 seeded versions, 5 seeded questions.

## 10. Placeholders & gaps

- **"View historical diff" is a toast-only no-op** with no real destination — the single clearest placeholder on either half of this file. Everything else that's simulated (version upload, answer recording, bulk import) at least produces a full, visible, stateful result; this produces only a confirmation message.
- **Notification bell and avatar are unwired**, same cross-screen pattern noted in `SPEC-dashboard.md` §10.

## 11. Open points

- Whether a second AO version upload (beyond the single v2.2 this build allows) would follow the same script, or whether the one-shot limit is a deliberate demo-scope decision (avoid an ever-growing, increasingly hand-scripted version list) rather than a genuine product constraint, isn't stated anywhere.
- The bulk-import "uncertain match" flag always lands on the same, single already-sent question, deterministically — there's no way to tell from the code alone whether a real matcher's uncertainty would be genuinely content-dependent or whether this fixed behaviour is itself the intended demo script.
