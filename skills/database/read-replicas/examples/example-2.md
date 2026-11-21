# Example 2 — Decorative replica replaced by named, verified routing

## Before

A replica is provisioned during a scaling review. Its connection string is added to configuration, no read is ever routed to it, and the release notes announce read scaling:

```text
Replica status:        running
Replica read queries:  0 (per its query log — never checked)
Primary read load:     unchanged
Release note claim:    "read scaling in place"
```

## After

Two tolerant reads are named, routed, given tolerances, and the replica's own query log is checked to prove traffic arrives:

```text
Routing table:
  product_feed        -> replica   tolerance: 5 min
  public_search       -> replica   tolerance: 15 min
  checkout, balances  -> primary   (pinned, see DB-223)

Verification (G-DB-114): replica query log shows product_feed and
public_search queries executing; primary read QPS drops accordingly.
Only now does the release note say "read scaling in place".
```

**Corrects DB-229** — a replica is not read scaling until routing exists and is verified in query logs.
