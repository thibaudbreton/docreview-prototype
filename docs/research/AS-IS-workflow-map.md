# AS-IS — Current requirement-review workflow (pre-SRM)

> **Confidence key:** **[A]** confirmed via internal sources. **[B]** public/internet sources, not yet validated internally. **[?]** genuine gap — needs a real answer, not an assumption. This doc is meant to double as an interview guide: the **[?]** lines are the questions to actually ask.
>
> **Scope note:** this is about the requirement-review workflow itself (how a tender's requirements get processed today) — not iSenS's own product-development governance (discovery/delivery phases, roadmap prioritisation). Those are two different AS-IS subjects; the Orga/Adoption pain points already gathered before (alignment between discovery & delivery, roadmap not quantified) belong to the *second* one, not this doc. Flag if you actually wanted them merged.

## Roles today

- **RME (Requirement Management Engineer)** [A] — guardian of the baselines (As Required / As Specified / As Sold), managed via DOORS.
- **Bid Manager** [A] — reports to the Head of Tendering; owns the QCDP commitment from nomination to TTM [B].
- **Requirement Manager** [A].
- **Bid Director / Tender Leader** [A/B].
- **[?] Who plays the "per-activity owner" role today** — the closest equivalent to what we've been calling Activity Manager? Does that granularity (one owner per activity) even exist today, or is allocation coarser?
- **[?] Who plays "Expert" today**, and how do they get pulled into a given tender's review — the same subsystem-expert population as elsewhere in the bid process, or a distinct pool?

## Team & casting, today

- **[?] How are experts assigned to specific requirements/sections today?** Email, a spreadsheet, a kickoff meeting, something else?
- **[?] Is casting decided all at once, or does it evolve over the tender's life today?** This one matters a lot — it tells us whether the async casting model we designed (B2) is solving a real, observed pain, or introducing a complexity that isn't there today.

## Capture, today

- Tooling [A]: **DOORS 9** (legacy, approaching end of support), Excel exports.
- Rail tender documents typically run **600–1,800 text segments** [B].
- **[?] How does a requirement actually get from the raw tender document into DOORS/Excel today?** Manual copy-paste? A first pass by a junior team member? Something semi-automated already?
- **[?] Roughly how long does this take**, for a typical tender?

## Characterisation & Allocation, today

- **[?] Is there a current equivalent of "Activity" tagging?** If so, manual, and by whom?
- **[?] Is there a current equivalent of confidence/doubt flagging** — or does everything get the same level of scrutiny regardless of how clear-cut it is?
- One concrete data point from the V&V track [A]: the **Basic/Derived attribute already exists** in DOORS exports, and roughly **two-thirds of rows in an export are non-requirement titles**, handled today via a manually retyped phrase — suggesting there's already a real manual clean-up step happening. Worth understanding in more depth.

## Expert review, today

- **[?] How does an expert receive their assignment today?** An emailed Excel extract, direct DOORS access, something else?
- **[?] What does "giving a verdict" look like mechanically today?** A column in Excel, a DOORS attribute, a separate document entirely?
- **[?] Is there a current equivalent to the Q&A-to-client cycle**, and how is it actually run — email thread, a formal RFI log, something else?
- From the V&V track [A]: the report is structured as a **multi-round dialogue between verifier and system engineer**, and **TBD is a human negotiation state** — not something a tool resolves on its own. Useful signal that today's process already tolerates back-and-forth rather than a single clean pass.

## Consolidation, today

- **[?] Is there a current equivalent of "most restrictive wins" consolidation across sub-parts of a requirement**, or is compliance assessed at a coarser grain than we've designed for?
- **[?] Who has authority to override a verdict today**, and how visible is that override to whoever gave the original one?

## Versioning, today

- **[?] When the client issues an amended tender document, what happens today?** Any tooling support at all, or entirely manual re-comparison?

## Export / handoff to DOORS & the project, today

- The core friction point already named in our own design thesis [A]: the **Excel/DOORS export–reimport loop** causes errors and rework — but I don't have the granular mechanics behind that claim.
- **[?] Concretely, how many times does data actually get exported and reimported** between Excel and DOORS during a typical tender, and **where do the real errors creep in** — retyping, version mismatches, lost formatting, something else?
- Governance milestones [B, to validate]: Business Opportunity Review → Win/No-Go → Launch Meeting → Tender Gate Review → QCD Review → TRM → submission/negotiation → **TTM** (the tender→project hinge) → FPR0/CPR0 → CPR1 → WLA.
- **[?] At which of these milestones does the Excel/DOORS reimport actually happen?** One big handoff at TTM, or does it recur several times along the way?

## Priority gaps — the three I'd ask about first

If time in the interview is short, these three change the most downstream, so they're worth asking before anything else:

1. **Casting: fixed upfront, or does it evolve today?** Directly tests whether B2's async model answers a real pain.
2. **How a verdict is physically recorded today** — this is the crux of the whole tool's value proposition (getting away from Excel/DOORS), so it's worth being very concrete here.
3. **Where exactly the Excel/DOORS reimport loop breaks today** — our design thesis (defer DOORS import to the end) rests on this friction being real and specific; worth confirming it's not just a general impression.
