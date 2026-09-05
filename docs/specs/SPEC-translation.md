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

**Open:** what happens if a document added mid-project turns out to be in a different language. Rare, but the current rule assumes it can't happen. Worth deciding rather than discovering.

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

Corrections are typically **minor**, and in practice **work on a requirement doesn't begin until the translation has been reviewed**. So the situation where a correction invalidates existing characterisation, allocation or compliance doesn't arise, and there is no need for the staleness mechanism used elsewhere.

**This rests entirely on the sequencing** — correction first, work after. See §7 for the open question about how that window actually exists.

## 6. Exporting to the client

**Final deliverables go out in the original language.** The compliance matrix carries the requirement text as it was written by the client, not a round trip through English.

That's straightforward for requirement text, since the original is stored untouched.

**Contributions stay in English.** Compliance comments, and the Category/Topic on a Not compliant verdict, are exported as written — not translated back.

So a client export is mixed by design: **requirement text in the original language, contributions in English.** That is intended, not an oversight.

## 7. Impact on the AI pipeline

**The pipeline runs on the English text.** That follows from all work happening in English, and it's the only way one set of models serves every tender language.

The consequence, stated plainly: **a translation error becomes a classification error.** The chain is capture → translate → characterise → allocate, so a mistranslation propagates into every decision that follows, and looks exactly like an AI mistake to whoever finds it.

Two things follow:

- The correction process in §5 is not a nicety. It is the mechanism that keeps the pipeline honest on non-English tenders.
- **The pipeline order creates a timing question.** Translation runs after capture and before characterisation. If characterisation follows automatically, the AI has already worked from an unreviewed translation — which contradicts the assumption in §5 that correction comes first. Either the pipeline pauses for a translation review, or correction happens alongside characterisation and some AI decisions rest on uncorrected text. Needs deciding; it determines whether the no-staleness rule holds.
- **Translation quality is worth measuring**, at least as a count of corrections per tender. If it's high, the trust placed in automatic translation needs revisiting — and that's better learned from a number than from a growing sense that the AI is unreliable.

## 8. Open questions

1. **When translation review happens relative to characterisation** (§7). This is the one that matters — the no-staleness rule in §5 depends on it.
2. A document added mid-project in a different language (§2).
