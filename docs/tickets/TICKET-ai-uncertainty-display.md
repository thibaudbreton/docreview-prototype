# Ticket — Surface AI uncertainty on the imported requirements

> The real captured data is now in the prototype, but every row reads as equally certain. The AI's confidence signal — and the review state it triggers — is missing, which removes the whole reason the human-correction workflow exists.

## The model

**The AI emits a graded confidence per decision it makes.** That gradation stays **in the data only** — the real engine will produce it anyway, it costs nothing to store, and it keeps the door open if sorting by degree of uncertainty is ever wanted.

**Nothing about the gradation reaches the screen.** A threshold turns it into one thing: anything below the confidence bar is **to review**.

**"To review" is the row's global status — not a badge on top of a status column.** One signal, not two saying the same thing.

**Observed distribution: ~87% of decisions come out confident.** So roughly one row in eight needs review — enough to matter, not so much that the tool looks unreliable.

### Which decisions carry a confidence

Every field the AI decides, each independently:

**Characterisation**
- **Type** — requirement / information / heading
- **Class** — technical / non-technical

**Allocation**
- **ABS**, **PBS**, and the **activity (OBS)** derived from them

A row's confidence is not a single value — each field has its own. One row can be confident on Type and unsure on Class.

### Information and heading rows can also be to review

Deciding that a line *is* an information or a heading is itself an AI decision, and it can be uncertain like any other. So **any row can be to review on its Type**, whatever category it ended up in.

This needs a small adjustment to the current rule that information rows carry no fields at all:

- Information and heading rows still carry **no class, no activity, no allocation, no compliance** — they don't enter the allocation or compliance pipeline. That part stands.
- They **do** carry the review state for their Type. It isn't a workflow status so much as "a human should confirm this is really what the AI thinks it is."

**Why this matters practically:** reclassifying a row already exists — turning an information or heading into a requirement unblocks its fields, which the user then fills manually. But without a review signal, a misclassified requirement sitting quietly as an information would never resurface. Nobody would think to look. This is the mechanism that gets it back.

### Status mapping

| AI confidence | Resulting status |
|---|---|
| Confident on every field | **To validate** — no human has acted yet |
| Below the bar on any field | **To review** |

**Confirm:** is "To review" the same state as the previously-defined "Doubt", under a better name? Assumed yes — the ticket uses "to review" throughout. If it's meant to be a distinct fifth status, stop and confirm, because that changes the status machine.

## What to build

### 1. Generate confidence values for the imported data

The real capture files contain **no confidence column** — the data doesn't exist in the source. It must be generated for the prototype.

- Target distribution: **~87% confident**, the rest below the bar.
- Generate **per field**, not per row, so a row can be confident on one thing and unsure on another.
- Include **Type on every row**, whatever its category — information and heading rows included.
- Make it **deterministic** (derive it from the row ID) so re-running the importer produces an identical file and the demo stays stable between sessions.
- **Mark it clearly as generated** in the data file — a banner comment and a flag on each seeded value. This is demo scaffolding calibrated on a real statistic, not captured data, and nobody should mistake it for the latter in three weeks.

### 2. Derive the status from the confidence

Apply the threshold at import time: any field below the bar puts the row in **to review**; all-confident puts it in **to validate**. Rows the AI couldn't decide at all stay **incomplete**.

### 3. Show it in the table

- The row's **status** carries the signal — no separate warning badge duplicating it.
- **Which field is uncertain must be visible**, not just that the row is uncertain. A row to review because of its Class is a different job from one to review because of its activity.
- Information and heading rows show the review state on their Type and nothing else — their other columns stay empty, as today.
- The existing per-field doubt filter should now return meaningful results — verify it against the generated data.

### 4. Show it in the detail panel

When a row is opened, the uncertain field(s) should be identifiable at a glance, so the reviewer knows where to look rather than re-reading everything.

Where the uncertain field is the **Type**, the reclassify action is the resolution — it already exists and unblocks the fields, which the user then fills manually.

## Deliberately not in scope

**Do not surface the graded confidence to the user.** The threshold has already turned it into a decision; showing the gradation as well would ask the user to interpret a nuance the system has acted on. Keep the graded value in the data, expose only the state.

**No separate warning badge.** The status already says it. Two indicators for one fact is noise.

If a real need for the gradation emerges in a user test, that's a separate ticket.

## Definition of done

1. Roughly one row in eight is to review, driven by generated per-field confidence.
2. Information and heading rows can be to review on their Type, while still carrying no other fields.
3. The uncertain field is identifiable in both the table and the detail panel.
4. The per-field doubt filter returns correct results.
5. The graded confidence appears nowhere in the UI.
6. Generated confidence is deterministic and clearly labelled as generated in the data file.
7. `build_merge.py` runs clean, `node --check` passes, zero dead hrefs.
