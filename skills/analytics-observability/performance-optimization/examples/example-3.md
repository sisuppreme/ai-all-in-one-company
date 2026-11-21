# Example 3 — The orders endpoint that loaded everything

## Before

The orders endpoint loads every row in the orders table, filters by customer and slices the first page in application code. The dashboard reports "average response 210 ms," which looks acceptable — while the p99 sits at 3.8 s and grows with every month of orders. A first fix attempt adds a response cache under a shared key; it is caught in review when a test account is served another account's order list from the warm cache.

## After

The baseline is restated at the tail: p95 and p99 for the endpoint, from production telemetry. `EXPLAIN ANALYZE` names the cause — a sequential scan feeding an in-memory filter. One change bounds the query: the customer filter and pagination move into SQL with a limit, and an index is added exactly where the plan shows the scan; the after-plan and the new p99 are recorded in the change. The k6 suite for the orders journey re-runs green on its `p(95)<200` threshold in the same environment class as the baseline. The shared cache is removed; if caching returns, it comes with a written per-user key and invalidation spec and must pass the two-user test.

*Corrects AN-243 and AN-249: the tail is the target, and queries are bounded and plan-verified instead of fetching everything and filtering in memory.*
