# Example 1 — LIKE '%term%' replaced by full-text search with ranking

## Before

Catalog search is a substring scan over the primary table — unindexed, with results in insertion order:

```sql
SELECT id, name, price_cents
FROM products
WHERE name ILIKE '%' || $1 || '%'
ORDER BY id
LIMIT 20;
-- Full scan on every keystroke; "running shoes" also matches "shoe rack",
-- and the best match appears wherever insertion order puts it.
```

## After

A weighted `tsvector` column with a GIN index does the matching, and `ts_rank` orders by relevance (name weighted above description):

```sql
-- Schema (migration):
ALTER TABLE products ADD COLUMN search_tsv tsvector
    GENERATED ALWAYS AS (
        setweight(to_tsvector('english', coalesce(name, '')), 'A') ||
        setweight(to_tsvector('english', coalesce(description, '')), 'B')
    ) STORED;
CREATE INDEX idx_products_search_tsv ON products USING GIN (search_tsv);

-- Query:
SELECT id, name, price_cents,
       ts_rank(search_tsv, query) AS rank
FROM products, to_tsquery('english', $1) AS query
WHERE search_tsv @@ query
ORDER BY rank DESC
LIMIT 20;
-- Bind $1 as a tsquery string built from structured terms, e.g. 'run & shoe'.
-- EXPLAIN confirms: Bitmap Index Scan using idx_products_search_tsv.
```

**Corrects DB-261** — search starts with PostgreSQL full-text search: `tsvector`/`tsquery`, weighted fields, `ts_rank`, and a GIN index.
