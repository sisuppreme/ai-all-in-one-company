# Example 3 — Buried failing page vs. per-page deviation log

## Before

The verification summary reports "overall fidelity 97%" and ships. Averaged away inside that number: the checkout page at 89%, and a logged-in account page that was never compared at all because capturing it would have needed the client's login.

## After

The report lists per-page scores: checkout at 89% becomes a defect entry with the diff image attached; the account page is listed as unverified — excluded from scoring under CL-131 because no client-provisioned access existed — and the aggregate is published next to the per-page minimum, so neither fact can hide.

Note: corrects CL-128 / CL-131 — every difference is logged per page, and unverifiable views are excluded and reported, never averaged away or captured by bypass.
