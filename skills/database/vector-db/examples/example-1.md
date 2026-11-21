# Example 1 — An index the query never used

## Before

The embeddings table is indexed for cosine distance, because the model was
trained for cosine similarity:

```sql
CREATE INDEX ON documents
  USING hnsw (embedding vector_cosine_ops);
```

But the search query was copied from a tutorial that used L2 distance:

```sql
SELECT id, content
FROM documents
ORDER BY embedding <-> $1
LIMIT 10;
```

The operator does not match the index's operator class, so PostgreSQL cannot
use the index. `EXPLAIN` confirms it:

```text
Limit
  ->  Sort
        ->  Seq Scan on documents        -- 2,000,000 rows, ~800 ms
```

Every search scans the whole table. The ANN index exists, is maintained on
every write, and serves no query.

## After

The query uses the operator the model and the index agree on:

```sql
SELECT id, content
FROM documents
ORDER BY embedding <=> $1   -- cosine distance, matches vector_cosine_ops
LIMIT 10;
```

`EXPLAIN` now shows the index doing the work:

```text
Limit
  ->  Index Scan using documents_embedding_idx on documents
        Order By: (embedding <=> $1)
```

The gate (G-DB-141) runs this `EXPLAIN` in CI against a production-shaped
fixture, so an operator change that breaks index use fails the build instead
of reaching users.

Note: corrects DB-281 — the query operator, the model's distance, and the index operator class are one decision.
