# Example 3 — One-off index build replaced by a documented rebuild with parity test

## Before

The search index was populated once, at launch, by a script on a developer's laptop. The script was never committed, and after an index corruption there is no way to recreate what production had:

```text
Index origin:   ~/scripts/reindex_once.py (laptop, deleted)
Rebuild path:   none documented
Recovery plan:  "rebuild it by hand and hope"
```

## After

One documented command rebuilds the full index from the source of truth, and the staging parity test proves the rebuilt index answers the fixed query set identically:

```bash
#!/usr/bin/env bash
# reindex.sh — drop and rebuild the search index from the database. Idempotent.
set -euo pipefail

psql "$DATABASE_URL" <<'SQL'
DROP INDEX CONCURRENTLY IF EXISTS idx_products_search_tsv;
CREATE INDEX CONCURRENTLY idx_products_search_tsv ON products USING GIN (search_tsv);
ANALYZE products;
SQL

# Parity check: the fixed evaluation query set must return the recorded top results.
./bin/search-eval --queries eval/search-queries.txt --expect eval/search-expected.txt
echo "Rebuild complete; parity suite green."
```

**Corrects DB-266** — the full index rebuilds from the source of truth by one documented command, exercised in staging with a parity check.
