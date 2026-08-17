# Spec derivation report

Produced 2026-08-16 on the local-only branch `docs-derive-specs` (branched from `docs-cleanup`, not pushed — see the branch note at the end), per `docs/prompts/PROMPT-derive-specs-from-prototype.md`. Summarizes the specs written from the prototype's actual behaviour and the things worth a human's attention.

## Specs produced

The prompt expected "roughly" one spec per screen with no existing spec (home, project creation, dashboard & configuration, expert follow-up & versions) — 4 documents. It produced **7**, because two of those four source files each contain multiple functionally distinct screens glued together in one HTML file, and cramming them into one spec would have produced documents where half the template's sections (Layout, Interactions, States) described three unrelated things at once:

| Spec | Source | Notes |
|---|---|---|
| `SPEC-home.md` | `accueil.html` | One screen, one spec. |
| `SPEC-project-creation.md` | `creation-projet.html` | One screen, one spec. |
| `SPEC-dashboard.md` | `dashboard-et-config.html` (`#dash-screen`) | Split 1 of 3 — the status hub. |
| `SPEC-configuration.md` | `dashboard-et-config.html` (`#cfg-screen`) | Split 2 of 3 — project settings. |
| `SPEC-team-management.md` | `dashboard-et-config.html` (`#team-screen`, ticket B4) | Split 3 of 3 — the roster screen. |
| `SPEC-followup.md` | `suivi-experts-et-versions.html` (`#screen2`) | Split 1 of 2 — matches the file's own `screen:2` boundary and the "Follow-up" top-nav tab. |
| `SPEC-versions-qa.md` | `suivi-experts-et-versions.html` (`#screen3`) | Split 2 of 2 — matches `screen:3` and the "Versions & Q&A" tab. |

**Not touched, per the prompt's explicit instructions:**
- `SPEC-backend-requirements.md`, `SPEC-domain-model.md`, `SPEC-review-table.md` — already exist, referenced for vocabulary, not rewritten.
- `SPEC-expert-space.md` — the prompt says to leave it alone since it "describes a screen not yet in the prototype." **That premise no longer holds**: `expert-space.html` exists and is fully built (confirmed while reading `HANDOVER.md` for this task). The instruction to leave the file alone was followed literally regardless, since it's also independently listed under "what already exists — do not rewrite these." No spec was produced for `expert-space.html` and `SPEC-expert-space.md` was not touched — flagged here rather than silently working around a stale premise.

**Deliberately not covered:**
- `revue-documentaire.html` — already has `SPEC-review-table.md`.
- A cross-cutting spec (navigation, notifications, export) — considered and not written. Routing/shared-state architecture is already covered by `HANDOVER.md` §2.2 at the right level of detail; a functional-spec rewrite of it would mostly duplicate that document. There's no real cross-cutting *notification* behaviour to describe (every notification affordance across every screen is either absent or a dead icon — see below) — a spec describing "nothing happens" isn't a useful document; the finding itself is recorded below instead. Export exists on two screens but as two independently-built, non-shared implementations (see below) — a real finding, but not one that needs its own spec once each screen's own spec already describes its own Export button.

## Couldn't confidently classify (implemented / represented / gap)

- **The wizard's document upload** (`SPEC-project-creation.md` §6, §10) — split verdict, not a single classification. Adding a (synthetic) document is *represented* — a real upload needs a backend. But the "Drop tender documents here" copy implies drag-and-drop, and there is no `dragover`/`drop` listener anywhere in the source — that specific gap is real and backend-independent (a static page can support HTML5 drag-and-drop with no server), so it's recorded as a genuine placeholder, not folded into the backend-dependent classification of the upload itself.
- **Configuration's inert controls** (`SPEC-configuration.md` §6) — six of nine sections are non-functional by design and say so in their own UI copy. Classified in bulk as *represented*, since every one maps to a real, described capability elsewhere in the corpus (the domain model's real gate/overdue logic, the backend spec's AI-pipeline and notification requirements) — this was a single bulk judgment call across ~20 individual controls rather than 20 separate close calls, noted here so it doesn't read as more certain than it is.
- **"View historical diff"** (`SPEC-versions-qa.md` §6, §10) — landed on *placeholder*, not *represented*, specifically because it produces nothing at all beyond a toast: no state change, no view, no navigation. Every other simulated action in the whole corpus (upload, answer-recording, bulk-import matching, email notifications) at least mutates real in-memory state or renders a full result. This one is the exception, which is why it's flagged rather than grouped with the rest.

## Couldn't confidently interpret

- **Wizard step 3's "Compliance matrix" toggle** — its static label doesn't match its own live description text, which reads like the *Allocation* toggle's copy instead. Unclear which of the two is stale; not resolved here.
- **Two Dashboard rail stats are hand-typed while their siblings are computed** (`SPEC-dashboard.md` §5, §11) — the Expert Space card and the Versions & Q&A phase card show fixed numbers, while Allocation, Follow-up, and Team casting compute theirs from mirrored data. No document states whether this is a known gap awaiting a data source or an accepted permanent simplification.
- **The one-shot v2.2 upload limit** (`SPEC-versions-qa.md` §11) — could be a deliberate prototype-scope decision (avoiding an ever-growing hand-scripted version list) or a real constraint being previewed. Not stated anywhere in the corpus.
- **Bulk "Reassign expert" on Follow-up** (`SPEC-followup.md` §10) jumps to a single-row reassignment form rather than acting on the whole selection, despite sitting in the Bulk Action Bar next to genuinely bulk actions like "Send reminder." Could be intentional (reassignment is inherently a per-branch judgment call) or an unfinished bulk path.

## Inconsistencies noticed between screens

- **Role vocabulary.** Home and the Dashboard both label the viewer "Bid Director" — a term that appears nowhere else: not in `creation-projet.html`'s or `dashboard-et-config.html`'s own `MANAGERS` list ("Project lead (admin)" / "Project manager"), not in per-card role badges ("Signalling manager," "Expert"), and not in `SPEC-backend-requirements.md`'s five-role list. It does appear in `docs/research/AS-IS-workflow-map.md` as a pre-SRM term, suggesting a holdover that was never reconciled with the in-tool role model. Flagged on both affected specs (`SPEC-home.md` §11, `SPEC-dashboard.md` §11) rather than silently normalized.
- **Notification bell + avatar.** Present but entirely unwired (no click handler anywhere) on Dashboard, Follow-up, Versions & Q&A, and the Allocation screen; absent altogether on Home, the wizard, and Expert Space. Wherever it's present, the bell also carries a permanently-lit "unread" badge-dot that never turns off and never means anything. A single, consistent cross-screen gap, documented in full once (`SPEC-dashboard.md` §10) and referenced from every other affected spec rather than repeated.
- **Export is two unrelated implementations, not one shared feature wearing two skins.** The Allocation screen (`SPEC-review-table.md`, already existing) has a modular step × format picker; Follow-up (`SPEC-followup.md` §6) has a single fixed action with no options. Both are labeled "Export" and sit in the same header position, which could read as one consistent feature — it isn't, and nothing in the corpus explains why the two were built to different depths.
- **Data-mirroring is inconsistent even within one screen.** The Dashboard computes 2 of its 4 phase-adjacent rail stats from mirrored arrays and hand-types the other 2 (see above); its "Managers assigned" health stat is a hardcoded `100%` with no computation behind it at all, sitting directly next to three other stats that are all genuinely computed.

## Branch note

Committed to a **local-only branch**, `docs-derive-specs`, branched from the also-local `docs-cleanup` (which reorganized the docs corpus this session's earlier work depends on — the four "already exists" specs this task reads live there, not on `main`). No upstream was set; nothing was pushed. Per instruction, not merged automatically — this reads the prototype's actual behaviour in detail and makes several split/classification judgment calls that a human should review before either branch lands on `main`.
