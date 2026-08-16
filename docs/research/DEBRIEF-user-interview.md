# User Interview — Debrief

## Part 1 — Findings & design implications

### 1. Expert view — two types of comments
Experts want to write two distinct comments per requirement:
- A **client comment**, which feeds the compliance matrix (external-facing output).
- An **internal comment**, which already exists today at the traceability / activity level.

The internal comment must be accessible to everyone, and in particular to bid managers, who use it to reformulate the client-facing version before it is sent to the client.

### 2. Expert freedom on compliance
Some experts are able to answer a very large number of requirements. When motivated, an expert should be allowed to answer even if they are not the 100% best-suited person, for throughput / time reasons. Design implication: the expert view must not lock an expert to only their strictly-assigned requirements. It should let a willing expert opt in to answer more.

### 3. OBS = a named person (confirmation)
Confirmed: on the OBS we must resolve to a specific named individual, not a generic role. (FYI-level, no change to the model.)

### 4. Document intake and tender size
A tender can range from a single document to roughly 500 documents of varying weight. It is the project manager's job to review them, identify which ones actually contain requirements, and therefore which documents make up the RFP set that gets loaded into the platform. This is a triage / selection step upstream of the pipeline.

### 5. Naming: "Document Review" → "Allocation"
The step currently labelled "Document Review" should be renamed "Allocation."

### 6. Status tags to rework
The current "status" tags are confusing, because they mostly express the AI's confidence in its own choice rather than a real workflow status. To revisit: separate AI-confidence from actual status, and relabel accordingly.

### 7. Two Excel-parity behaviours to add
- **Filter from selection:** select requirements that are not contiguous, then choose to display only the selected ones.
- **Enter to advance:** pressing Enter moves to the cell directly below, staying in the same column.

### 8. UX — user status on the project card
Display the user's status on the project card, to show whether they are **owner** or **contributor**. Even though the user already knows their own status, surfacing it on the card makes identification faster.

---

## Part 2 — Interviewee profile & posture

### Who he is
An RFP expert who does *not* use the tool day-to-day. He has moved up to higher-level responsibilities and is now called in specifically as an expert — a **level-2 expert**, brought in when the regular experts cannot answer a requirement themselves.

### Starting posture: skeptical
He is a very heavy Excel user and relies on Excel's sharing features. Initially he was fairly **resistant to the interface redesign**. His preferred setup was simply to process requirements *inside an Excel file* — not even in DOORS — which he finds very practical today and much more "free" / unconstrained.

### After the demo: reassured
Following the demo and the discussion, he was **rather pleased with what he saw and fairly confident**. That said, he's open about the fact that he could keep working via Excel even with the tool in place, using the export function — and that this would be fine, not a problem.

### What he particularly liked
The **document view** — being able to always refer back to the source document.

### On comfort / the table
On the tool and the table specifically: nothing beats Excel for comfort, but the tool gets close — close enough. No major criticism of the table itself, aside from **a few features to add to go as fast as possible**. His core driver is **speed**: they want to move as fast as they can.
