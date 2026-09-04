# Tickets — Prototype fixes (batch 6)

> From a review pass on the mockup. Formatted for the nightly routine: one `- [ ]` per ticket, detail indented. Ordered quick-and-contained first.

## Run log

_(the routine appends here after each run — do not edit by hand)_

---

## Queue

- [ ] **Add a back arrow on the support screens**
  The three support screens — Casting, Documents & versions, Q&A — have no way back. Add a back control returning to the project.
  - Same placement and behaviour on all three, so it's learned once.

- [ ] **Unify the row IDs**
  IDs are still not unified. One identifier scheme across headings, information and requirements — a row keeps its ID when its type is corrected.
  - Already raised in session 3 and still outstanding; treat as a defect rather than a new request.

- [ ] **Show information rows in the detail panel**
  Opening an information row currently gives nothing useful. It should open the detail panel and show its content, like any other row.
  - Information rows still carry **no** other fields — no class, no activity, no allocation, no compliance. That rule stands.
  - What they do carry: their text, their source document and position, their type, and the review state of that type.
  - **Confirm if this reading is wrong** — the request was brief, and the intent may have been broader.

- [ ] **Add activities from the team screen**
  In the team/casting screen, allow adding an activity — not only people within existing ones.
  - **Open, needs an answer before building:** are activities picked from the reference list, or can a free-form one be created? The reference list is what keeps allocation and casting aligned, so ad-hoc activities would need a deliberate decision. Build the reference-list version first; flag the other.

- [ ] **Export what the filters currently show**
  Export should follow the active filters rather than always exporting everything.
  - Applies to the per-column chips and, once it exists, the advanced filter.
  - State plainly what's being exported — row count and the active filter in plain language — so nobody exports a narrowed set believing it's the whole tender. That mistake is silent and expensive.

- [ ] **Prepare the login for SSO**
  Wire the identification flow so SSO can be plugged in, rather than assuming a hand-entered identity.
  - Prototype-level: no real SSO integration, but the screens and the user model should assume an identity supplied by the directory.
  - Consistent with the casting screen, which already assumes SSO/directory search for finding people.

- [ ] **Language: original at capture, English in the tool, viewable in any language**
  Requirements arrive in whatever language the tender is written in. The tool works in English. Both must be true at once.
  - **At project creation:** capture the tender's **source language**.
  - **Storage:** the requirement is stored in its **original language**, always. Source fidelity is a standing rule — the original document is never altered, and neither is the text taken from it.
  - **In the detail column:** show the requirement in its **original language**, plus a **selector to view it in any other language**. Translation is for reading; it never replaces the stored text.
  - **Larger than it looks** — touches project creation, storage, the detail panel, and whatever performs the translation. If it can't be completed cleanly in one pass, leave it unchecked with a blocker note rather than committing a partial version.

  **Open, and it matters more than the display question:** does the AI pipeline — characterisation, allocation — run on the **original text or a translation**? Running on the original means each language needs handling; running on a translation means every downstream decision rests on a machine translation, and a mistranslation becomes a misclassification nobody can trace. This needs deciding before the language work goes further than the display.

---

<!--
Format reminder:
- [ ] not yet done — the routine picks this up
- [x] Summary of what changed — done
> blocked: reason — routine couldn't finish it safely
-->
