# SPEC — Tender dashboard statistics panel

> Defines the statistics panel for the tender dashboard: what each metric measures, what data it needs, and how to display it. Two audiences with genuinely different questions — the Project Manager asks *"what's blocking me today"*, the stakeholder asks *"is this on track and how does it compare"*. Almost no single metric serves both well, so the panel is split accordingly.

## Design principles

These apply to every metric below and matter more than any individual chart:

- **Always show the unknown.** Pending, unallocated, no-verdict-yet are real states, not zeros to hide. Early in a tender, "pending" is the honest majority — a chart that omits it manufactures false confidence.
- **Distributions, not averages.** "Average wait: 4 days" hides the requirement stuck for three weeks — which is exactly the one that matters. Show the oldest, or the tail.
- **Every metric must lead somewhere.** If nobody can act on it, it's taking up space. This is the test that kills most dashboard content.
- **No single overall completion percentage.** 90% done with the hard 10% remaining is not 90% done. It misleads by construction.

---

## Part 1 — For the Project Manager

Operational. Answers "what do I do next".

### 1.1 Bottlenecks by perimeter

**Measures:** where work is piling up and how stale it is.

**Data:** for each perimeter, the count of requirements awaiting an expert answer, plus the age of the oldest one.

**Display:** a ranked list — perimeter name, count, age of oldest. Ordered by age, not by count: one requirement stuck three weeks is more urgent than twelve stuck two days. **Not a chart** — this is a to-do list, and its whole purpose is to be acted on directly. Each row should lead to that perimeter's filtered view.

**Why it's first:** it's the only metric that triggers an immediate action — chase someone.

### 1.2 Compliance profile

**Measures:** the commercial risk position.

**Data:** per requirement, the consolidated verdict — Compliant, Not compliant, or still pending because not every allocated activity has answered.

**Display:** a single stacked bar, with pending clearly present as its own segment. Percentages on the segments, absolute counts on hover.

**Explicitly not a pie chart of two values.** Dropping pending would show a comforting Compliant/Not-compliant split that isn't the truth.

### 1.3 Blocked on the client (Awaiting Q&A)

**Measures:** work that cannot move regardless of internal effort.

**Data:** count of allocated activities in Awaiting Q&A, with the date the question was raised.

**Display:** a distinct callout, visually separated from the bottleneck list. **This separation is the point** — these are not people to chase, they're a client to wait for. Merging them into "late" would send the PM chasing colleagues who are correctly blocked.

### 1.4 Casting gaps

**Measures:** whether allocation can actually run.

**Data:** count of perimeters present in the document (known once characterisation has run) that have nobody assigned.

**Display:** a single number with a binary state — either zero, or "N perimeters unstaffed" as a warning, linking to the casting screen. Nothing more elaborate; it's a blocker, not a trend.

### 1.5 Work invalidated by a new version

**Measures:** rework created by a document revision.

**Data:** count of expert answers given before a change that affected their requirement.

**Display:** appears **only when non-zero**. A permanent "0 stale answers" tile is noise 95% of the time. When it fires, it links to the affected rows.

### 1.6 Trajectory to deadline

**Measures:** whether the tender will actually be finished in time.

**Data:** remaining requirements without a final verdict, sampled over time, plus the submission deadline.

**Display:** a line chart of remaining-work over time, with the deadline marked. The only chart here that earns its space — it's the one answer to "will we make it".

**Needs historical snapshots** (see Data gaps).

---

## Part 2 — For stakeholders (VIP, read-only)

Comparative. Answers "is this healthy, and how does it compare to the others". They look across several tenders, so everything must read at a glance and side by side.

### 2.1 Project health, comparable across tenders

**Measures:** one immediate read per project.

**Data:** a composite of progress against deadline, compliance risk, and blocked volume.

**Display:** one compact indicator per project, in a list of projects. **Deliberately simple** — a stakeholder scanning six tenders needs one signal each, not six numbers each. Drilling in gives the detail.

**Open:** the exact composition of this indicator isn't defined. Getting it wrong makes a project look fine when it isn't, so it needs a real decision rather than a formula picked for convenience.

### 2.2 Compliance profile

Same as 1.2 — the commercial risk position is the one metric both audiences genuinely share.

### 2.3 Progress against deadline

Same underlying data as 1.6, without the operational detail. Are we ahead or behind, and by how much.

### 2.4 AI reliability, measured by human correction rate

**Measures:** how much the AI's proposals actually get changed.

**Data:** count of AI proposals subsequently modified by a human, over total proposals, broken down by field (Type, Class, activity, allocation).

**Display:** a correction rate per field, ideally trending over time.

**Why this and not the confidence score:** correction rate is observed behaviour; a confidence score is the AI's opinion of itself. This distinction matters concretely here — the AS-IS finding was that human classifiers reported being 100% certain even when wrong. Self-reported certainty has already proven a poor proxy for correctness in this exact context, whether the source is human or model.

**Needs the AI feedback loop to be exploited** (see Data gaps).

---

## Display conventions

- **Stacked bar for status distributions, never four separate tiles.** The values form a whole; one bar shows the *shape* of the work at a glance, whereas separate figures force the reader to do the addition.
- **Reuse the existing components** — KPI Tile, Progress Bar, Badge, Status Dot — rather than introducing new chart primitives. The compliance bar and the trajectory line are the only genuinely new visual elements needed.
- **Every metric links to its filtered view** in the review table. A number the user can't open is a dead end.
- **The panel is read-only.** Acting happens in the table, not in the statistics.

## What NOT to include

- **Pie charts of status** — four segments, hard to compare, no trend.
- **A single overall completion percentage** — see principles.
- **Vanity counts** ("4,070 requirements captured") — impressive, decides nothing.
- **Averages of wait time** without the distribution behind them.
- **Permanent zero-state tiles** for exceptional conditions.

## Data gaps — three metrics need work the model doesn't do yet

Flagged honestly: these are worth building, but they are tickets, not display work on existing data.

1. **Age and time-in-status** (1.1, 1.3) require a history of status transitions. The audit log exists in the backend spec but isn't exploited for duration analysis.
2. **AI correction rate** (2.4) requires the AI feedback loop's data to be queryable. The loop is specified, but as a background signal with no defined consumer.
3. **Trajectory** (1.6, 2.3) requires periodic snapshots of remaining work, not just current state. Nothing currently stores history in that form.

Metrics 1.2, 1.4, 1.5 and 2.2 can be built on the current model as-is.
