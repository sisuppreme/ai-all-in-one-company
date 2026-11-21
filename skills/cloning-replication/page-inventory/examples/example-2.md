# Example 2 — URL variants merged into one canonical row

## Before

The merged table lists `/pricing`, `/pricing/`, `/Pricing`, and `/pricing?utm_source=newsletter` as four separate rows, plus `/plans` as a fifth — even though `/plans` redirects to `/pricing`. Reconstruction builds the pricing page twice from two rows, the copies drift, and the fidelity check later compares the rebuild against the wrong variant.

## After

Canonicalization (lowercased host, trailing slash resolved, tracking parameters stripped, redirect followed to target) collapses all five entries into one row: canonical URL `/pricing`, with `/plans` and the parameter variants recorded as attributes of that row. The canonical-uniqueness gate confirms zero duplicates across the table before sign-off.

Note: corrects CL-022 — one row per canonical page; redirect sources and URL variants are attributes of the target row, never rows themselves.
