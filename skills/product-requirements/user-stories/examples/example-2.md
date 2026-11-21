# Example 2 — Relabeling a disguised task

## Before

Story: "As a user, I want an API endpoint for bulk order import, so that the
system has an endpoint for bulk import."

There is no user, no benefit — the "so that" restates the capability. The item
borrows story legitimacy to skip the prioritization a task would face.

## After

Task T-118: "Add bulk order import endpoint (CSV upload, row-level error
report)." Type: task. Enables: story US-204, "As a dispatch lead, I want to
import the day's orders from the client's spreadsheet, so that I do not
re-type 300 rows each morning."

The engineering work is planned as engineering work, and its value is argued
through the story it enables — where the benefit actually lives.

Note: corrects PR-084 — work with no user-visible benefit is labeled a task and planned as one; it never wears story format.
