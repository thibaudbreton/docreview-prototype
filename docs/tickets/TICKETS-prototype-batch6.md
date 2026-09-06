# Tickets — Prototype fixes (batch 6)

> From a review pass on the mockup. Formatted for the nightly routine: one `- [ ]` per ticket, detail indented. Ordered quick-and-contained first.

## Run log

_(the routine appends here after each run — do not edit by hand)_

- Back arrow: already in place on all three screens (Casting's "Dashboard" button, Documents & versions' and Q&A's breadcrumb) — verified live, nothing to build.
- Row IDs: the unified SRM-NNNNN scheme was already correct in both importer scripts (`ID_PREFIX = "SRM"`); `data.js` on disk just predated that fix. Renumbered in place, same document order, no other file references the old per-type ids. `data.js` is gitignored (real client content), so this fix lives only in the local file, not in a commit.
- Information rows: fixed — real id in the panel header, a Type field (Nature select/reclassify) added for non-requirement rows. Exposed and fixed a latent bug in the process: the Nature select compared `b.kind` to a nature key, but a captured info row's kind is `"text"`, never `"info"` — every info row's Type dropdown silently showed "Heading". Commit 66c6af5.
- Add activities from casting: built the reference-list version per the ticket's own instruction. PM-only "+ Add activity" in the casting header, picks from a small REFERENCE_ACTIVITIES list not yet cast on the project; added with no manager, same empty state "cvl" already has. Free-form activities stay unbuilt/flagged — the open question. Commit 0c6eb53.
- Export: now composes document scope with the per-column chips and advanced filter (passesColFilters/passesAdvFilter), matching the same combined filter state the toolbar readback chip already speaks for. Panel shows a live row count + filter sentence before Generate; 0 matches blocks Generate with a toast instead of producing an empty file; the confirmation toast repeats the count and flags "· filtered". Search box and quick triage pills deliberately excluded — the ticket names chips + advanced filter specifically. Commit 8c8cc1a.
- SSO prep: no login screen exists in this prototype to redesign — the app opens straight on My tenders. What existed instead: "Thibaud Breton"/"TB" hand-typed into all six screens' own header markup independently. Added a shared `getCurrentUser()` in the shell (same pattern as the existing `getCurrentProject()`), directory-shaped (id/name/title/email/initials); every screen's avatar reads it now, with the same static fallback when opened standalone. Commit 0a44a0c.
- Language: left unchecked per the ticket's own instruction ("if it can't be completed cleanly in one pass, leave it unchecked with a blocker note"). Blocked on its own open question, not on effort: whether the AI pipeline runs on the original text or a translation has to be decided before the display work is built on top of it, and that's a product decision, not one this routine can make. See the blocker note below.
- Language, unblocked and built: the pipeline-timing decision this ticket was waiting on got made during the build itself (`SPEC-translation.md`, decided: no translation-review gate — the pipeline runs on the automatic translation immediately, correction is after-the-fact, not a prerequisite). All four surfaces landed across six commits: data model + demo French original (`2b4b594`), reading (original + selector) (`ea2049f`), correction tab (`900381f`), project creation + documents + export (`7e4ae81`), plus two follow-on polish commits moving the selector into the Translation tab and reworking its styling (`4022171`, `b607deb`) and a correction-tab layout fix (`3ef09ba`). Marked done below; `SPEC-translation.md` updated in the same window to close out both of its open questions.

---

## Queue

- [x] **Add a back arrow on the support screens** — done (already implemented, see run log)

- [x] **Unify the row IDs** — done (data regeneration, see run log)

- [x] **Show information rows in the detail panel** — done, commit 66c6af5
  - Reading confirmed as scoped: no class/activity/allocation/compliance added, only id, type (Nature) and source section — matches the ticket's own list.

- [x] **Add activities from the team screen** — done (reference-list version), commit 0c6eb53
  - Still open, not built: free-form/ad-hoc activity creation — needs the deliberate decision the ticket describes before it's built.

- [x] **Export what the filters currently show** — done, commit 8c8cc1a

- [x] **Prepare the login for SSO** — done, commit 0a44a0c

- [x] **Language: original at capture, English in the tool, viewable in any language** — done, commits `2b4b594`, `ea2049f`, `900381f`, `7e4ae81`, `4022171`, `b607deb`, `3ef09ba`; see `SPEC-translation.md`
  Requirements arrive in whatever language the tender is written in. The tool works in English. Both must be true at once.
  - **At project creation:** capture the tender's **source language**.
  - **Storage:** the requirement is stored in its **original language**, always. Source fidelity is a standing rule — the original document is never altered, and neither is the text taken from it.
  - **In the detail column:** show the requirement in its **original language**, plus a **selector to view it in any other language**. Translation is for reading; it never replaces the stored text.
  - **Larger than it looks** — touches project creation, storage, the detail panel, and whatever performs the translation. If it can't be completed cleanly in one pass, leave it unchecked with a blocker note rather than committing a partial version.

  The blocking question was resolved during the build, not before it: no translation-review gate — the pipeline runs on the automatic translation immediately, and correction (§5 of the spec) is after-the-fact rather than a prerequisite. See `SPEC-translation.md` §5/§7 for the decision as recorded.

---

<!--
Format reminder:
- [ ] not yet done — the routine picks this up
- [x] Summary of what changed — done
> blocked: reason — routine couldn't finish it safely
-->
