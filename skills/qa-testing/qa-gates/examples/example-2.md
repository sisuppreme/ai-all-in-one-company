# Example 2 — The threshold that moved with the code

## Before

A PR adds a heavier hero section and the performance gate fails: LCP measures 2.9s against the 2.5s budget. In the same PR, the author edits the budget file to 3.5s with the commit message "adjust budget to match implementation." The gate goes green, the PR merges, and the standard quietly became whatever the code already did — no reviewer ever decided that 3.5s was acceptable.

## After

The provenance check (G-QA-113) blocks the merge: the threshold file changed in the same PR as the code it failed on, and no waiver exists. The author splits the work — the hero PR is reworked until it meets 2.5s, and the budget question is raised separately as a standards change. When a later, deliberate decision raises the budget, it lands as its own reviewed change with a waiver record naming the owner, the reason (measured user impact), and a review date.

Note: demonstrates QA-223 — threshold and test changes in the same PR as the failing code require a waiver record with owner and expiry.
