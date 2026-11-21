# Example 3 — A fully traced requirement

## Before

REQ-31: "The system shall allow CSV export of the order list."

Source: unstated. Test: none named. When the export ships without the totals
column, there is no record of what was actually needed or promised.

## After

REQ-31: "The system shall export the currently filtered order list as a CSV
file containing order ID, date, customer, status, and total."
- Source: stakeholder need N-06 ("month-end reporting without manual
  re-typing"), from finding F-11 (study S-03).
- Priority: Must. Rationale: month-end reporting is the dispatch lead's
  recorded job (persona: dispatch lead, v1.0).
- Verification: test — acceptance scenario AC-31-1 (see acceptance-criteria).
- Forward links: design element "Reports module"; acceptance test AC-31-1.

The requirement can be audited in both directions: back to the need that
justifies it, forward to the test that proves it.

Note: corrects PR-066 — every requirement traces back to a stakeholder need and forward to design and acceptance test.
