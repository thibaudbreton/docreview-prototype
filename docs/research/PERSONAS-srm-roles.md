# Personas — SRM roles

> **Key — every fact below is tagged:**
> - **[A] Confirmed** — drawn directly from what's established in `AS-IS-workflow-map.md` or our TO-BE specs.
> - **[I] Interpreted** — a reasonable extrapolation from confirmed facts, not itself directly stated anywhere.
> - **[N] Invented** — pure fictional detail added for realism (name, age, personal habits, voice, quote phrasing). No evidentiary basis — illustrative only.
>
> All three work at the same company, unnamed by design (per the standing confidentiality rule).
>
> **Correction (2026-08-28), per `TICKET-merge-expert-space-into-compliance.md`:** Persona 2 (the activity manager) and Persona 3 (the expert) now share one in-tool role, **contributor** — "no action boundary between experts and bid managers... within their own activity, experts and bid managers can do the same things." They remain two distinct *people* below, with different backgrounds and motivations — only the role label changed, not the profiles.

---

## Persona 1 — The Bid / Project Manager

**Sophie Vasseur** [N], 47 [N] — Bid Manager / Project Manager [A, role confirmed to exist]

> *"Je n'ai pas besoin d'un outil qui me dit ce qui a mal tourné après coup — j'ai besoin de savoir avant que ça en devienne un."* [N]

**Note on the role itself [I]:** the AS-IS interviews used "Project Manager" and "Bid Manager" somewhat interchangeably when describing who chairs casting and who overrides verdicts. This persona treats them as one role; split it into two if that turns out to be wrong.

### Background
- Reports to the Head of Tendering [A].
- Chairs the **TLW**, the kick-off meeting at the very launch of a bid response, where casting is decided in one sitting with every Activity Manager present [A].
- Holds the authority to **override an expert's compliance verdict** when she judges it necessary [A].
- Nearly twenty years in tendering [N], has seen enough bids go sideways from a missed Q&A or a late-surfacing compliance gap to trust her own radar more than a spreadsheet [I].

### Goals / Motivations
- Hit her QCDP commitment without last-minute compliance surprises [I — derived from her override authority and role scope].
- Keep every activity aligned, despite each one potentially running different tooling — different DOORS versions, or shared Excel instead of DOORS entirely [A, tooling fragmentation confirmed].
- Cut down the sheer volume of Q&A questions that come back impossible to match to the right requirement [A].
- Be confident that a "validated" requirement was actually looked at by someone, not just waved through [I — this is exactly the tension behind the To-validate/Valid distinction from today's session].

### Pain points
- Casting has to land correctly in **one sitting** at the TLW — if an Activity Manager hasn't thought it through yet, the gap only surfaces later, once it's expensive to fix [A + I].
- Consolidating compliance verdicts today is **entirely manual**, using the same "most restrictive wins" logic she'd gladly see automated [A].
- Oversight is harder than it should be because activities don't share one workflow — some are on DOORS 9, some on DOORS Next, some skip DOORS for expert review in favour of shared Excel [A].
- A **1–2 week turnaround** from external RFP-to-Excel providers eats into her timeline before analysis can even start [A].

### Tools today
DOORS (version varies by activity) [A], Excel [A], Salesforce as CRM [B, unvalidated internally].

---

## Persona 2 — The Contributor (manager-flavoured)

**Karim Boujaidi** [N], 44 [N] — Contributor, signalling subsystem [N for subsystem, A for role — was "Activity Manager", see the correction note above]

> *"Je sais ce qui est technique et ce qui ne l'est pas — je n'ai pas besoin qu'un outil me le confirme."* [I/N — phrasing invented, but the underlying attitude reflects a confirmed AS-IS fact: classifiers reported being 100% certain of their calls, right or wrong]

### Background
- One of several contributors who attend the TLW to align casting with the Bid/Project Manager, in the same room, at bid launch [A].
- Personally does the **Technical vs. Non-technical classification** for his activity [A].
- Deep technical background in his subsystem [N] — has been doing this classification call directly, by feel, for years, with no second opinion built into the process [A/I].

### Goals / Motivations
- Get his activity staffed with the right experts as early as possible in the bid [I].
- Trusts his own judgment on classification calls — wants a tool to be genuinely better before he defers to it, not just present [I, playful extrapolation of the "100% certain" finding].
- Wants less time lost to manual clean-up — a confirmed AS-IS finding is that roughly two-thirds of rows in a DOORS export are non-requirement titles needing a manually retyped fix [A, though this specific data point comes from the V&V track — attributing it to this contributor specifically is **[I]**, not confirmed to be his task precisely].

### Pain points
- Classification and activity tagging is entirely manual, and entirely on him — there's no equivalent of a doubt signal today, even to flag a tricky case to himself for later [A].
- No visibility into where each of his own experts stands on their assignments until he actively chases them [I — no AS-IS confirmation either way on this specific point].

### Tools today
DOORS or shared Excel, depending on the activity's own preference [A].

---

## Persona 3 — The Contributor (field-expert-flavoured)

**Julien Ferrand** [N], 39 [N] — Contributor, field / subsystem [A — was "Expert", see the correction note above]

> *"Donne-moi le bon bout du document et je te dis en trente secondes si c'est bon ou pas. Le problème, c'est jamais le jugement — c'est de retrouver l'info."* [N/I — phrasing invented, but the underlying split between "fast, obvious calls" and "slow, research-heavy calls" is a confirmed AS-IS observation, not our invention]

### Background
- Operational field engineer profile: experienced, not management, though carrying real supervisory weight on his subsystem and expected to stay well-informed [A].
- Pulled into a tender via an email that also grants him **DOORS access scoped strictly to his own assigned activity** [A].
- Gives his verdict directly in an **Excel cell**, sometimes with a comment, sometimes without [A].
- Some of his colleagues on other activities work entirely in a **shared Excel sheet instead of DOORS**, because DOORS doesn't flex the way they need [A] — Julien has opinions about this [N].

### Goals / Motivations
- Wants to move fast on the obvious calls and save real time for the ones that genuinely need research — a real split he already experiences, not a hypothetical [A].
- Doesn't want to spend cycles on requirements that were never actually his to review — misrouted allocation, straight to reassignment [A].
- Wants a question he raises to the client to come back as an answer he can actually find again — not buried in a dossier mixed with every competitor's questions [A].

### Pain points
- Q&A today comes back so mixed with competitor questions that matching his own question to its answer is close to manual detective work [A].
- A real share of what lands on his desk was never his to review in the first place [A].
- No REX or similarity tooling exists today — if a case needs research, he does that legwork entirely himself, with whatever he can dig up on his own [I — absence of tooling isn't directly confirmed, but nothing in the AS-IS suggests otherwise].

### Tools today
DOORS (scoped access) or shared Excel, whichever his activity uses [A].

---

## One role deliberately left out

**RME (Requirement Management Engineer)** — confirmed to exist as guardian of the DOORS baselines (As Required / As Specified / As Sold) [A], but never named as a direct actor in any of the B1–B7 tickets, the Compliance step, or the workflow map. **[I]** It may overlap with the contributor role above, or be a distinct, adjacent one — not enough evidence yet to build a fourth persona without guessing. Worth a direct question next time you're with a real user.
