# Claude Design prompt — SRM roadmap slide

> Paste into Claude Design. Goal: one polished pitch-deck slide (16:9) showing the SRM quarterly roadmap. Aim for a high-end, editorial roadmap — not a basic kanban of cards. Editable on the canvas.

---

## Concept

A **horizontal swimlane roadmap** (gantt-style). Time flows left → right across quarterly columns; each **workstream is a lane**; work is shown as **rounded bars that span the quarters they run in** (so continuity is visible — a bar crossing two quarters reads as one ongoing effort). A clear **"now" marker**, a **confirmed vs proposed** distinction, and milestone markers for shipped work.

## Format & tone

- 16:9 slide, generous margins, lots of whitespace.
- Flat and modern: no gradients-as-decoration, no drop shadows, no neon. Clean surfaces, thin hairlines, strong type hierarchy.
- Sentence case everywhere. Two font weights only (regular + medium).
- One accent colour per workstream; everything else neutral. The colour should read at a glance.
- Title: "SRM roadmap" with a light subtitle "3-month batches".

## Columns (time axis, left → right)

1. **Shipped** (narrow, before the timeline starts)
2. **Jul–Sep 2026 — now**  ← mark this column as the present (a subtle vertical "now" line or an accented header)
3. **Oct–Dec 2026**
4. **Jan–Mar 2027**
5. **Apr–Jun 2027**

## Lanes (workstreams) and their bars

Each lane has a coloured label on the left and one or more bars placed under the quarters they cover. `[confirmed]` = solid bar; `[proposed]` = visually lighter / hatched bar (my arbitration, not yet locked).

**Accuracy** (blue)
- Global accuracy — spans Jul–Sep `[confirmed]`, then continues Oct–Dec, Jan–Mar, Apr–Jun `[proposed]` (one continuous bar, solid at the start, lighter afterwards).

**Models** (purple)
- Milestone in Shipped: "RSC model" (a checkmark / diamond marker).
- Model Turnkey — spans Jul–Sep `[confirmed]` → Oct–Dec `[proposed]`.
- Model Mainline — Jul–Sep `[confirmed]`.
- New models: SIG & Urban, Safety — Oct–Dec → Jan–Mar `[proposed]`.
- Remaining product-line models — Jan–Mar `[proposed]`.
- Edge lines & external actors — Apr–Jun `[proposed]`.
- (This lane is the busiest — allow the bars to sit on 2 stacked sub-rows within the lane so they don't collide in time.)

**Platform** (teal)
- Milestone in Shipped: "Capture optimized" (checkmark / diamond).
- Backend rebuild — Jul–Sep `[confirmed]` → Oct–Dec `[proposed]`.
- Backend hardening · rollout-ready — Jan–Mar `[proposed]`.

**Experience** (coral / warm orange)
- UX discovery & design — Jul–Sep `[confirmed]`.
- Design system → build handoff — Oct–Dec `[proposed]`.
- Target-stack UI build & iterate — Jan–Mar `[proposed]`.

**Integration** (amber)
- Capture & charac integration — Jul–Sep `[confirmed]`.
- Additional microservices — Oct–Dec `[confirmed]` (this one IS planned — keep it solid).

**Adoption** (green)
- Adoption & rollout with factories — Apr–Jun `[proposed]`.

## Encoding & markers

- **Now marker:** a thin vertical accent line at the start of the Jul–Sep column, or an accented column header labelled "now".
- **Confirmed vs proposed:** solid, full-colour bars for confirmed; lighter or subtly hatched bars for proposed. Include a one-line legend explaining it.
- **Shipped milestones:** small diamond or check markers in the Shipped column, not bars.
- **Legend:** the six workstream colours + the confirmed/proposed cue, on one compact row at the bottom.
- Rounded bar ends; hairline lane separators; quarter columns subtly delineated (light vertical gridlines, not heavy).

## Elevated touches (pick what looks best)

- A subtle **left-to-right certainty fade** reinforcing that the near term is firm and the far term is directional.
- Bars with a small inline label; if a bar spans two quarters, label it once, centred.
- Keep the shipped column visually "done" (muted/checked) so the eye starts at "now".

Deliver it as an editable slide so I can tweak wording and re-arbitrate the proposed bars.
