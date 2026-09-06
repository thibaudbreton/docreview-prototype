# SPEC — Language & translation

> Tenders arrive in whatever language the client writes in. The tool works in English. This covers how both stay true at once.

## 1. Principles

- **All work happens in English.** Characterisation, allocation, compliance, comments — the whole pipeline and everything people write.
- **The original is never altered.** Source fidelity is a standing rule: the document and the text captured from it stay exactly as they came.
- **Translation is trusted, but always checkable.** It runs automatically and people work from it, yet the original stays one interaction away — because that's the only way a bad translation ever gets caught.
- **What goes back to the client is in the original language.** The tool's working language is internal; it must not leak into the deliverable.

## 2. Language of a tender

**One language per tender.** When one document is in a given language, all the others are too — so this is a tender-level property, not a per-document one.

- The **source language is captured at project creation**.
- If it is English, no translation step runs at all.
- If it isn't, translation runs automatically **after capture**, before characterisation.

**Decided (2026-09-05), during `prototype: language & translation lots 4 & 5`:** a document added mid-project is not assumed to already be in the tender's language. It runs the same capture → translate → characterise chain as initial capture; the translation step is only inserted when there's a source language to translate from (i.e. skipped for an English-source tender, same as §2's rule above). No per-document language detection — the tender's one source language still applies to whatever is added to it.

## 3. What gets stored

Two texts per requirement, with different statuses:

- **The original** — captured text, in the source language. **Immutable.** Never edited, by anyone, ever.
- **The English text** — derived by translation. **Correctable** (see §5), and it is what the tool works from.

Both are kept for the life of the project. The English text is not a display convenience; it's the working text, and correcting it changes what everyone downstream sees.

## 4. Reading

In the detail column:

- The requirement shows in **English** by default — that's the working language.
- The **original is directly available**, not buried. Anyone questioning a wording needs to reach it without hunting.
- A **language selector** allows viewing in another language for anyone more comfortable that way. This is reading only — it never becomes the stored text and never feeds the pipeline.

## 5. Correcting a translation

A short, deliberate process, in its own tab in the detail column.

- Shows the **original and the English side by side**, so the correction is judged against the source rather than from memory.
- The **English text is editable**; the original is not.
- The correction is **recorded** — who, when, what changed. This is exactly the signal that tells whether machine translation is good enough on this tender.

### No stale-work flagging

**Correction (2026-09-05), decided during `prototype: language & translation lot 1`:** there is no translation-review gate. Translation runs automatically and the rest of the pipeline proceeds immediately on the machine translation — work does not wait for a human to review or correct it first. The paragraph below assumed the opposite sequencing; kept for the record, superseded by this note.

Corrections are typically **minor**, and in practice **work on a requirement doesn't begin until the translation has been reviewed**. So the situation where a correction invalidates existing characterisation, allocation or compliance doesn't arise, and there is no need for the staleness mechanism used elsewhere.

**This rested entirely on the sequencing** — correction first, work after — which is not how it was built. No staleness mechanism exists: a correction made after work has already started does not flag or invalidate whatever characterisation, allocation or compliance was already produced from the uncorrected translation. Accepted as a trade-off, not treated as a gap still to close — see §7.

## 6. Exporting to the client

**Final deliverables go out in the original language.** The compliance matrix carries the requirement text as it was written by the client, not a round trip through English.

That's straightforward for requirement text, since the original is stored untouched.

**Contributions stay in English.** Compliance comments, and the Category/Topic on a Not compliant verdict, are exported as written — not translated back.

So a client export is mixed by design: **requirement text in the original language, contributions in English.** That is intended, not an oversight.

## 7. Impact on the AI pipeline

**The pipeline runs on the English text.** That follows from all work happening in English, and it's the only way one set of models serves every tender language.

The consequence, stated plainly: **a translation error becomes a classification error.** The chain is capture → translate → characterise → allocate, so a mistranslation propagates into every decision that follows, and looks exactly like an AI mistake to whoever finds it.

Two things follow:

- The correction process in §5 is not a nicety. It is the mechanism that keeps the pipeline honest on non-English tenders — after the fact, not as a gate.
- **Decided (2026-09-05):** the pipeline does not pause for translation review. Characterisation runs immediately on the automatic translation; correction happens alongside it, whenever a human gets to it, and some AI decisions may rest on since-corrected text with no flag raised when that happens. This is the trade-off §5 now states plainly, rather than assuming the timing away.
- **Translation quality is worth measuring**, at least as a count of corrections per tender. If it's high, the trust placed in automatic translation needs revisiting — and that's better learned from a number than from a growing sense that the AI is unreliable. This matters more now that corrections don't gate anything downstream.

## 8. Open questions

Both of this section's original questions were resolved during the build (see §2 and §7 above, both dated 2026-09-05). None open at time of writing.
