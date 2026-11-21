# Example 1 — From story-copy criteria to a real scenario

## Before

Story: "As a dispatch lead, I want to export the filtered order list as CSV,
so that I can send month-end totals to finance."

Acceptance criteria: "The export works as described in the story. The file
downloads correctly."

Nothing here can fail. Whatever the build produces will be declared correct.

## After

Scenario: Export reflects the current filter
  Given the order list is filtered to status "delivered" for March
  When the dispatch lead exports the list
  Then a CSV file downloads containing exactly the orders shown on screen,
  with columns order ID, date, customer, status, and total,
  and the file's total row equals the on-screen total.

Context, one action, and an outcome a test can pass or fail.

Note: corrects PR-101 — criteria are written as Gherkin scenarios, not restatements of the story.
