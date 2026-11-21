# Example 3 — Splitting an epic along the workflow

## Before

Story: "As a dispatch lead, I want full reporting, so that I can handle all
reporting tasks."

Estimated at "large," scheduled whole, and still unfinished three iterations
later. Nobody can say which reporting behavior exists and which does not.

## After

Split along the dispatch lead's workflow, each piece usable on its own:

1. "As a dispatch lead, I want late orders flagged on one screen, so that I
   can reassign drivers before customers call."
2. "As a dispatch lead, I want to export the filtered order list as CSV, so
   that I can send month-end totals to finance."
3. "As a dispatch lead, I want a saved month-end report definition, so that
   the same totals regenerate each month without rebuilding the filter."

Each story fits one iteration, carries its own acceptance criteria, and
delivers value even if the next piece is never built.

Note: corrects PR-085 and PR-088 — oversized stories are split along workflow steps before estimation, and each split keeps value whole.
