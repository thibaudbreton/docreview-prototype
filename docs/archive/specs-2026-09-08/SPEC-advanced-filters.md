# SPEC — Advanced filters

> Raised in user test session 3: filtering needs to go well beyond the current per-column chips. The stated reference was Excel's advanced filters — a composable **list of rules** rather than a fixed set of presets.

## 1. Purpose

Let a user express a precise question about the requirement set — several conditions, combined — and work on exactly the rows that answer it.

**The real value is repeatability, not query complexity.** Users described organising their work as successive sweeps: clear everything uncertain on Type first, then everything with a questionable activity, then the rest. Those sweeps are the same queries, run again on every tender. A powerful builder that forgets what you built is only half the feature — see §6.

**One caution on the Excel reference.** Excel's advanced filter (criteria ranges in spare cells) is genuinely hard to use, and copying it literally would be a mistake. What users mean is the *power* of Excel filtering — combining conditions freely — not that particular interface. Build the capability, not the mechanism.

## 2. Filterable fields

| Field | Type | Notes |
|---|---|---|
| ID | text | |
| Text | text | the requirement content |
| Type | enum | heading / information / requirement |
| Class | enum | technical / non-technical |
| Status | enum | Incomplete / To review / To validate / Valid |
| Compliance | enum | Compliant / Not compliant, plus *no verdict yet* |
| Compliance comment | text | including "is empty" — a verdict with no reasoning is a real thing to look for |
| Activity | enum | from the real activity list |
| Perimeter | enum | optional on a row, so "is empty" matters |
| Responsible person | enum | one person per requirement since session 3 |
| ABS / PBS / OBS · team | enum | sequential — PBS → ABS → OBS, each derived from the one before |
| TK OBS · activity | enum | pass 1 only (Turnkey tenders) — never the same field as OBS · team, see `TICKET-two-pass-allocation.md` |
| Allocation level | enum | single / branches into activities / branches into teams |
| Doubt — which pass | enum | pass 1 (which activity) / pass 2 (within it) / none |
| Awaiting manual allocation | enum | the activity has no allocation model — a normal state, not an error |
| Document | enum | which source document the row came from |
| Section | text | the heading path |
| Doubt on \<field\> | boolean | per AI-decided field: Type, Class, ABS, PBS, OBS · team, TK OBS |
| Last follow-up | date | on the follow-up screen |
| Changed since version | enum | ties into gap analysis |

**Rule:** a field that isn't in the data model doesn't appear in the builder. No placeholder conditions that silently match nothing.

## 3. Operators

Offer only what the field type supports — never a generic operator list that produces meaningless combinations.

- **Text** — contains · does not contain · is · is not · starts with · is empty · is not empty
- **Enum** — is · is not · is any of · is none of · is empty
- **Date** — before · after · between · in the last N days · is empty
- **Boolean** — is true · is false

**"Is empty" matters more than it looks.** Most of the useful questions here are about absence: no verdict, no comment, no perimeter, nobody assigned. Make it first-class, not an afterthought.

## 4. Combining rules

- A filter is a **list of conditions** joined by **AND** or **OR** — one choice for the whole list, not per row.
- **One level of grouping** is allowed: a group is itself a list of conditions with its own AND/OR, and groups combine with the top-level operator.
- **No deeper nesting.** Two levels covers the real questions; beyond that the builder becomes a query language nobody can read back three weeks later.

**Always show the filter in plain language** above the results — *"Status is To review AND Activity is any of SIG, SEN"*. If a user can't read back what they built, they won't trust the result, and a filter that isn't trusted gets abandoned for scrolling.

## 5. Behaviour

- **Live count while building** — "142 of 1,381 rows" — updated as conditions change, so the user sees immediately whether they're narrowing usefully or down to zero.
- **Nothing applies until confirmed**, so a half-built filter never wipes the view mid-thought.
- **Clear all** in one action, always visible.
- **Empty result is a normal outcome**, not an error: say which condition is the restrictive one where that can be determined, rather than showing a blank table.

## 6. Saved filters

This is what makes the feature worth building rather than a one-off convenience.

- **Save a filter with a name**, reuse it on any tender.
- **Reusable across projects** — the sweeps users described are habits, not project-specific.
- No sharing between users.

**Confirmed: saved filters are personal.** One user, their own filters. Sharing is not in scope — if it turns out teams want to spread a way of working, that's a later addition, not a default.

## 7. Relationship to what already exists

Three filtering mechanisms will coexist, and users must not have to guess which one they're in.

- **Per-column filter chips** — quick, single-column, stays as-is. Most filtering is still one column, and forcing that through a builder would be a regression.
- **Advanced filter** — this spec. For anything a chip can't express.
- **Filter to Selection** — narrows to a hand-picked set of rows. Suspends column filters while active, per its own spec.

**Requirements:**
- Chips and the advanced filter must show as **one combined active-filter state**, not two competing indicators — the user should always be able to see everything currently narrowing the view, in one place.
- **The advanced builder inherits the active column chips** as its starting point. Nobody opens it cold: they get there because a chip wasn't enough. Starting blank would force them to rebuild what they just did — which is exactly when scrolling starts to look faster.
  The usual risk of inherited state (surprising the user) is covered by two things already in this spec: the filter reads back in plain language above the results, so inherited conditions are visible; and nothing applies until confirmed, so any of them can be dropped first.

## 8. Applies to every table

**This is not a review-table feature.** Every table in the product uses the same component and must offer the same advanced filtering: the review table, the follow-up screen, the expert workspace, and any table added later.

- Build it **once, in the shared table component** — not per screen. Two implementations will diverge.
- The **available fields adapt to the table**: "Last follow-up" only appears where that column exists, "Changed since version" only where versions apply. Never offer a condition that can't match anything on the current screen.
- Saved filters record which table they were built for, and are offered on that table. A follow-up filter has no meaning on the expert workspace.

## 9. Scale

At real tender volume (up to ~10k rows), filtering has to run **server-side**. The client cannot filter rows it hasn't loaded, and a builder that silently only searches the visible page would be worse than no builder at all — it would return confidently wrong answers.

Target: filter results within the existing table latency budget. Where a query can't meet it, show progress rather than freezing.

## 10. Out of scope

- **Nesting beyond one group level** — see §4.
- **Regex or formula-based conditions.** Real power for a handful of users, unreadable for everyone else, and a support burden.
- **Filters that modify data.** Filtering selects; bulk actions change. Keeping these separate is what makes bulk operations safe to use on a filtered set.
- **Excel's criteria-range interface**, for the reason in §1.

## 11. Open questions

**Which fields users actually filter on most.** The list in §2 comes from the data model, not from observed use, so the builder's field ordering is currently a guess.

Worth resolving by observation rather than by asking: "which filters do you want?" reliably produces "all of them". Instead, have a user walk through their last few tenders and note **what they actually searched on**. Until then, ordering by what's already known about how they sweep — status, per-field doubt, activity — is a reasonable placeholder to correct later.
