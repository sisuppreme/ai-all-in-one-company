# read-replicas

## Metadata

- **Owner department:** D5 Databases & Data (DB)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** AWS documentation, "Working with DB instance read replicas" — https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html ; PROJECT_ANATOMY.md Part 11, *Read replicas and read scaling*
- **Depends on:** data-access, schema-design, backup-recovery
- **Feeds into:** data-warehousing, query-performance, caching

## When to use / Do NOT use

- **Use when:** read load threatens the primary, reporting or feed traffic needs isolation, or an existing replica setup needs its routing, lag, and failover made honest.
- **Do NOT use when:** the real problem is a few bad queries (fix them under query-performance first), or the workload is write-bound — replicas scale reads only. Never present a replica as a backup; backup-recovery owns recovery.

## Rules

1. **DB-221 — The primary takes writes and read-your-own-write.** Anything that must see its own just-committed write reads from the primary. Replicas serve reads that tolerate staleness.
2. **DB-222 — Routing is named, never global.** Each query or service declares its target (primary or replica) explicitly. A blanket "reads go to replicas" default is forbidden.
3. **DB-223 — Consistency-critical reads are pinned.** Checkout, permissions, and balances always read from the primary, and the pinned list is written down.
4. **DB-224 — Every replica read states its staleness tolerance.** Each replica-routed read documents how old its data may be and still be correct for that feature.
5. **DB-225 — Lag is measured continuously.** Replication lag (in seconds and bytes) is a monitored metric with a stated alert threshold, not a quantity discovered through user complaints.
6. **DB-226 — Excess lag triggers a declared fallback.** When lag passes the threshold, affected reads fall back to the primary or the feature degrades explicitly — it never silently serves unbounded staleness.
7. **DB-227 — Promotion is rehearsed.** Replica promotion and failover are documented runbook steps that have been practiced, not improvised during an outage.
8. **DB-228 — Endpoints are configuration.** Primary and replica connection strings are separate, injected configuration. Code never hardcodes a host.
9. **DB-229 — A replica is not read scaling until reads flow.** Provisioning a replica changes nothing by itself; routing must exist and be verified in query logs before scaling is claimed.
10. **DB-230 — Heavy read traffic leaves the primary.** Dashboards, reports, and feeds read from a replica or the warehouse, never from the primary at peak load.

## BAN list

- **BAN-DB-111 — The decorative replica.** Banned: provisioning a replica, routing nothing to it, and reporting read scaling as delivered. Defeats: DET-CODE-003. Bad: the replica's connection string sits unused in config while the launch notes claim "read scaling in place" and the primary still takes every read. Instead: route the named, staleness-tolerant reads and verify replica traffic in its query log (DB-229). Severity: BLOCK.
- **BAN-DB-112 — Checkout reading its own write from a replica.** Banned: sending a read-your-own-write flow to an asynchronously replicated copy. Defeats: DET-CODE-030. Bad: the order is written to the primary, the confirmation page reads the replica, lag shows an empty cart, and the customer pays twice. Instead: pin read-your-own-write flows to the primary (DB-221, DB-223). Severity: BLOCK.
- **BAN-DB-113 — The hardcoded replica host.** Banned: writing a replica hostname or address as a literal in application code. Defeats: DET-INF-007. Bad: a reporting service embeds the replica's hostname; after failover it silently queries a demoted, stale node for a week. Instead: separate injected configuration per endpoint (DB-228). Severity: BLOCK.
- **BAN-DB-114 — Unmonitored lag.** Banned: running replicas with no lag metric and no threshold. Defeats: DET-INF-011. Bad: during a campaign, lag grows to several minutes; users see stale prices, support fields the complaints, and nobody was alerted. Instead: continuous lag measurement with an alert threshold and a declared fallback (DB-225, DB-226). Severity: BLOCK.

## Gates

- **G-DB-111 — Routing audit.** Verifies: DB-222, DB-223, DB-224. Check: review — the pinned-primary list covers every named consistency-critical flow, and every replica-routed read carries a written staleness tolerance. Pass: both lists complete. Fail: block shipment. Recorded in: progress.md.
- **G-DB-112 — Lag visibility test.** Verifies: DB-225. Check: automated — in staging, write a sentinel record on the primary and measure time-to-visible on the replica. Pass: visibility time is under the stated tolerance and the lag metric reports it. Fail: block shipment. Recorded in: progress.md.
- **G-DB-113 — Fallback drill.** Verifies: DB-226. Check: automated — in staging, force replica lag beyond the threshold (paused replay or load) and assert affected reads fall back to the primary or degrade explicitly. Pass: fallback engages and no read serves staleness past its tolerance. Fail: block shipment. Recorded in: progress.md.
- **G-DB-114 — Replica traffic check.** Verifies: DB-221, DB-229. Check: automated — production query logs show the routed read traffic actually executing on the replica. Pass: replica read volume matches the routing table. Fail: warn; a replica with zero routed reads fails the next release review. Recorded in: progress.md.

## Anti-patterns

- **Replica as backup.** The replica is listed as the disaster-recovery plan, although it replicates deletions and corruption with the same fidelity as data. Catch it: recovery belongs to backup-recovery; a replica is a performance tool.
- **Failover by folklore.** Promotion steps live in a chat thread from the last incident. Catch it: if the runbook cannot be followed by whoever is on call, DB-227 is unmet.
- **Lag by anecdote.** "It feels instant in testing" substitutes for a metric, right up until a traffic spike makes it minutes. Catch it: no threshold on a dashboard means no threshold at all.
- **Split by framework magic.** A library's automatic read/write splitting routes a permissions check to a replica because nobody declared the exception. Catch it: DB-222 — routing is named per flow, never inherited from a default.

## Examples

- [Example 1 — Empty-cart confirmation fixed by pinning to the primary](examples/example-1.md) — corrects DB-223.
- [Example 2 — Decorative replica replaced by named, verified routing](examples/example-2.md) — corrects DB-229.
- [Example 3 — Unbounded staleness replaced by a tolerance and a fallback](examples/example-3.md) — corrects DB-224, DB-226.

## Recall anchors

- Writes and read-your-own-write go to the primary. Always.
- Routing is named per flow; there is no global replica default.
- Every replica read carries a written staleness tolerance.
- Lag is a metric with a threshold and a fallback, not a surprise.
- No routed reads, no read scaling — a replica alone changes nothing.

## Checklist

- [ ] The pinned-primary list covers checkout, permissions, and balances (DB-223, G-DB-111).
- [ ] Every replica-routed read has a documented staleness tolerance (DB-224).
- [ ] Lag is monitored with an alert threshold, and the visibility test passes (DB-225, G-DB-112).
- [ ] The fallback drill passes with lag forced past the threshold (G-DB-113).
- [ ] Replica query logs show the routed traffic actually arriving (G-DB-114).
- [ ] Promotion steps are in the runbook and have been rehearsed (DB-227).
