# Example 1 — Empty-cart confirmation fixed by pinning to the primary

## Before

The confirmation page reads through the default (replica) connection immediately after checkout writes the order to the primary:

```sql
-- Checkout write (primary): INSERT INTO orders ... -- commits fine.

-- Confirmation read, routed to the replica by the framework default:
SELECT id, total_cents, status
FROM orders
WHERE id = 9917;
-- Replication lag is 800 ms; the row is not there yet.
-- Result: 0 rows — the customer sees "your cart is empty" and checks out again.
```

## After

The order-confirmation flow is on the written pinned-primary list; its reads bypass the replica for the whole read-your-own-write window:

```sql
-- Routing table entry (in the data-access layer's configuration):
--   flow: order_confirmation  -> target: primary   (read-your-own-write)
--   flow: order_history_feed  -> target: replica   (tolerance: 60 s)

-- Confirmation read, pinned to the primary:
SELECT id, total_cents, status
FROM orders
WHERE id = 9917;
-- Result: the just-committed row, every time.
```

**Corrects DB-223** — consistency-critical and read-your-own-write flows are pinned to the primary, by name.
