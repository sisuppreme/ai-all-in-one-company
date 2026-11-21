# Example 2 — Disaggregating a performance figure

## Before

Fact sheet, performance section: "Average export time: 1.8 seconds."

One aggregate number. It hides the fact that the average is computed over
small workspaces, while the largest customers wait far longer — the exact
customers most likely to test the claim.

## After

Fact sheet, performance section (measured March, production logs, dataset
linked):

- Export, up to 500 orders: median 0.9 s, p95 1.8 s.
- Export, 500–5,000 orders: median 3.1 s, p95 6.4 s.
- Export, over 5,000 orders: median 11.2 s, p95 19.7 s — flagged: above the
  10 s threshold the product promises in its help docs; limitation recorded.

The breakdown changes a marketing number into an engineering fact, and it
surfaces a limitation the aggregate was concealing.

Note: corrects PR-125 — performance is reported broken down by the conditions that change it; aggregate-only figures are flagged incomplete.
