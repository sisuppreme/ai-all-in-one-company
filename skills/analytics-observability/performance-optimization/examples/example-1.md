# Example 1 — Memoization without a measurement

## Before

A developer wraps the dashboard's data transforms in memoization helpers across six files and opens the change with: "Dashboard was re-rendering a lot; this should make it much faster." There is no baseline: no field p75 for the dashboard template, no profile showing rendering was the constraint, and no after-measurement planned. The change merges. Two weeks later the dashboard's field p75 is unchanged — the actual constraint was a 900 KB charting bundle — and nobody can say whether the memoization helped, hurt, or did nothing, because nothing was ever measured.

## After

The work starts with a baseline: the dashboard template's field p75 LCP and INP are pulled from RUM for the last 28 days, and a throttled lab profile decomposes the problem — the charting bundle is 62% of the page's JavaScript weight, while rendering time is minor. The memoization change is closed as unmeasured guesswork. Instead, one change code-splits the charting library to the dashboard route only; the same lab harness re-runs and records LCP before/after, and the field check is scheduled to confirm the p75 moved in production.

*Corrects AN-241 and AN-242: a baseline names the problem before any fix, and the after-measurement on the same harness is what proves it.*
