# Example 2 — A toy-database run relabeled and reseeded

## Before

The release run executes against the development seed: 12 products, 3 user
accounts, an empty orders table. Search returns instantly because there is
almost nothing to search. The release notes announce:

> "Search holds p(95) under 300 ms at 500 users — release gate passed."

Against the production catalog the same query scans two orders of
magnitude more data. The run proved the test harness works; it proved
nothing about the release, and it was recorded as if it had.

## After

Two corrections, in order:

1. The run is reclassified in the record as a **smoke run** — it verified
   the script executes, and it does not satisfy the release gate.
2. The test environment is seeded to production shape (catalog, accounts,
   and order history at the volumes recorded in TESTING.md), the script
   header declares those volumes, and the data-volume audit (G-QA-063)
   diffs the declared volumes against the seeded row counts before the
   run starts.

The release run then executes against the seeded environment. Search
p(95) comes back higher than the toy run promised — and this time the
number describes the system that is actually shipping.

Note: corrects QA-124 — release runs execute against production-shaped data volumes; a fixture-sized run is a smoke run and cannot satisfy a release gate.
