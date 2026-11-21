# Example 2 — An in-memory watermark replaced with a durable cursor

## Before

The extraction job keeps its incremental watermark in a local variable and a
text file on the machine that happens to run it:

```python
watermark = open("last_run.txt").read().strip()
records = source.query(f"updated_at > '{watermark}'")
land(records)
open("last_run.txt", "w").write(max(r["updated_at"] for r in records))
```

The job crashes after landing but before writing the file — the next run
re-ingests the same window. Worse, the file is lost when the machine is
replaced, and the restarted job re-ingests everything from the beginning.

## After

The cursor is a row in the database, advanced in the same transaction that
lands the batch:

```sql
CREATE TABLE ingestion_cursors (
  source_system text PRIMARY KEY,
  cursor_value  timestamptz NOT NULL,
  updated_at    timestamptz NOT NULL DEFAULT now()
);
```

```sql
BEGIN;

-- land the extracted batch into raw_orders (insert statements here),
-- stamped with source_system, extraction time, and batch id

UPDATE ingestion_cursors
SET cursor_value = :batch_max_updated_at,
    updated_at   = now()
WHERE source_system = 'orders-api';

COMMIT;
```

If the job crashes, the transaction rolls back: the batch is not landed and
the cursor has not moved, so the retry extracts the same window and lands it
exactly once. The cursor survives machine replacement because it lives with
the data it describes.

Note: corrects DB-343 — the extraction cursor is durable, stored outside the job, and advanced only after its batch is safely landed.
