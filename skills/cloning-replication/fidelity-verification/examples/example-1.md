# Example 1 — Eyeball verdict vs. measured diff run

## Before

The verifier opens the source pricing page and the rebuild side by side, scrolls both once, and writes "pricing page: pixel-perfect clone" in the report. No comparison was run; a 24px spacing shift in the plan cards and a missing focus state go unnoticed because nobody measured anything.

## After

The committed Playwright visual suite runs both captures in the same engine at the three agreed viewports. The pricing page scores 96.8% / 95.9% / 97.4%, and the diff image shows the plan-card spacing shift, which is logged as a defect under CL-128. The report cites run 2026-11-21-04 with the per-page scores — a claim G-CL-065 can trace.

Note: corrects CL-124 / BAN-CL-061 — every page gets a measured comparison result; an eyeball verdict is banned.
