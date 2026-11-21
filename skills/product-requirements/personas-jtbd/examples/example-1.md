# Example 1 — Rewriting a feature as a job

## Before

JTBD: "When I open the app, I want a dashboard, so I can see my dashboard."

The "job" is a screen. It justifies building the screen and tests nothing
about the progress the user is trying to make.

## After

JTBD: "When the morning shift starts, I want to know which orders are already
late, so I can reassign drivers before customers start calling."

The situation (shift start), the motivation (know which orders are late), and
the outcome (reassign before complaints) are all testable — and several
solutions besides a dashboard could serve them.

Note: corrects PR-042 and PR-043 — the statement follows When / I want / so I can, and the job names progress sought, not a product feature.
