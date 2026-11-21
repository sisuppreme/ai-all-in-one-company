# Example 3 — The $80,000 promise

## Before

Statement of work, written after two discovery calls:

> "The data-platform migration will cost $80,000 and complete in 3 months."

No decomposition, no assumptions, no range. The number becomes the client's budget, the team's deadline, and the sales team's promise — one point estimate carrying all three jobs, at the stage where McConnell's Cone of Uncertainty is at its widest.

## After

The estimate record for the same work:

```markdown
## Estimate — data-platform migration

- Method: decomposition, then analogy check against the 2024 billing
  migration (actual: 1.6x its concept estimate).
- Cone position: initial concept. Range factor 0.25x–4x applies to the
  undecomposed total; the decomposed range below is narrower and is the
  one we plan against.
- Decomposition (engineer-weeks):
  - Schema redesign: 3–5
  - ETL rewrite: 4–7
  - Dual-write + backfill: 2–4
  - Cutover + validation: 1–3
  - Total: 10–19 engineer-weeks
- Assumptions: source schema frozen at kickoff; no new compliance
  requirements mid-project; one dedicated engineer.
- Estimate (range): $55,000–$105,000, 10–19 weeks.
- Target (business): $80,000, 14 weeks.
- Commitment (external): "complete by end of Q3, fixed-scope items 1–3" —
  the range and assumptions were shown to the client; the fixed price
  covers the decomposed core only, with items 4+ on the stated range.
- Calibration: team's last three estimates landed at 1.2x, 1.6x, 0.9x of
  actual (see estimate-vs-actual log).
```

Estimate, target, and commitment are three separate numbers, and the client saw the range before anyone promised anything.

## Note

Corrected under PR-226 and PR-230: estimates are ranges with named assumptions and a method, positioned on the Cone of Uncertainty — and PR-227 keeps estimate, target, and commitment as separate numbers.
