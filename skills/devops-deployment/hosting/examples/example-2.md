# Example 2 — A single-box deployment recorded, then promoted

## Before

A production app with paying users runs as a single instance on one VPS, with
its PostgreSQL database on the same disk. The arrangement was never written
down; there is no exit path. One disk failure ends the product and its data
at the same time.

## After

1. The hosting record gains an explicit decision entry: single instance plus
   co-located database, risk accepted for cost reasons, dated.
2. The exit path is named in the same entry: database moves to a managed
   PostgreSQL service, app moves behind the platform's load balancer;
   promotion trigger is the first availability commitment to a customer.
3. When that trigger fires, the database is migrated first, the app is scaled
   to two instances, and the decision entry is closed with the date.

Note: corrects DO-143 — a single point of failure in production is either removed or recorded as a decision with an exit path.
