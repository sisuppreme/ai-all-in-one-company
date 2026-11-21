# Example 3 — N+1 loop replaced by one batched load

## Before

The invoice list loads each invoice's line items with a separate query — 1 query for the list, then one per invoice:

```sql
-- Query 1
SELECT id, customer_id, issued_at FROM invoices WHERE tenant_id = 7 LIMIT 50;

-- Queries 2..51, one per invoice (shown for invoice 901):
SELECT id, description, amount_cents FROM line_items WHERE invoice_id = 901;
SELECT id, description, amount_cents FROM line_items WHERE invoice_id = 902;
-- ... 48 more. Query count grows with page size; the endpoint's query-count test fails.
```

## After

Line items for the whole page load in one batched query keyed by the page's invoice IDs, and the application groups them in memory:

```sql
-- Query 1 (unchanged)
SELECT id, customer_id, issued_at FROM invoices WHERE tenant_id = 7 LIMIT 50;

-- Query 2 (the only other query, for all 50 invoices)
SELECT id, invoice_id, description, amount_cents
FROM line_items
WHERE invoice_id = ANY (ARRAY[901, 902, 903 /* ...all 50 ids from query 1... */])
ORDER BY invoice_id, id;
-- Total: 2 queries at any page size. The query-count assertion in CI pins this.
```

**Corrects DB-148** — collection loads are eager or batched, verified by query counts, never row-by-row loops.
