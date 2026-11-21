# Example 2 — Deleted record lingering in results, fixed by same-flow index delete

## Before

Product deletes touch only the database. The search index is refreshed by a nightly job, so a deleted product stays purchasable-looking in search results for up to a day:

```text
DELETE FROM products WHERE id = 42;        -- database: gone immediately
-- search index: still holds product 42 until tonight's job
-- result: users find it, click through, and hit a 404 — or worse, a cached buy flow
```

## After

The write path emits a change event in the same transaction (transactional outbox), and the indexer applies inserts, updates, and deletes from that stream — a delete leaves the index in the same flow as the database:

```sql
-- Inside the same transaction as the product change:
INSERT INTO outbox (aggregate, aggregate_id, event, payload)
VALUES ('product', 42, 'product.deleted', '{"id": 42}');

-- Indexer (consumes the outbox in order, idempotently):
--   product.created / product.updated -> reindex the record's tsvector row
--   product.deleted                   -> remove the record from the index
-- Freshness contract: searchable within 60 s of commit (monitored, G-DB-133).
-- The correctness gate (G-DB-131) deletes a record and asserts it disappears.
```

**Corrects DB-264** — deletes and updates leave the index in the same flow that changes the database; deleted records never linger in results.
