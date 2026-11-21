# Example 2 — Threshold raised instead of masking

## Before

The orders-page screenshot fails intermittently: the "last synced" timestamp changes between the baseline and each run. To stop the noise, the threshold in the Playwright config is raised from a 0.02 to a 0.25 max diff pixel ratio. The test goes quiet — and two months later a 12px padding collapse in the orders header passes the same suite unnoticed, because a quarter of the pixels may now differ for free.

## After

The threshold returns to 0.02, the value recorded in TESTING.md. The orders test masks the timestamp element (`mask: [page.locator('.last-synced')]`) so the dynamic region is excluded from comparison while every other pixel is still held to the tight threshold. The padding collapse, when it is later introduced by accident, fails the job with a readable diff.

Note: demonstrates QA-084 — mask dynamic regions per test; never widen the global tolerance.
