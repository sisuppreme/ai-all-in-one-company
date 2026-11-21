# Example 1 — Drift absorbed silently, replaced with contract check and quarantine

## Before

The loader maps source fields by name and inserts whatever matches:

```python
row = {
    "order_id":     payload["order_id"],
    "total_cents":  payload.get("total_amount"),   # renamed upstream last week
    "currency":     payload.get("currency"),
}
insert("raw_orders", row)
```

The source renamed `total_amount` to `totalAmount`. `.get()` returns `None`,
the column lands as NULL, and the load "succeeds" for three weeks. Revenue
reporting quietly under-reports and nobody gets an error, because the code
was written to never fail.

## After

The batch is validated against the written source contract before anything
loads; a mismatch quarantines the batch and alerts:

```python
CONTRACT = {
    "fields": {"order_id": int, "total_amount": int, "currency": str},
}

def validate_batch(records, batch_id):
    for rec in records:
        missing = CONTRACT["fields"].keys() - rec.keys()
        wrong_type = [f for f, t in CONTRACT["fields"].items()
                      if f in rec and not isinstance(rec[f], t)]
        if missing or wrong_type:
            quarantine(batch_id, reason=f"missing={missing} wrong_type={wrong_type}")
            alert(owner="data-ingestion", batch=batch_id)
            raise IngestionRejected(batch_id)
    land(records, batch_id)
```

The renamed field now stops the batch on day one, with the batch ID and the
reason attached, instead of corrupting a column for a month. The drift gate
(G-DB-171) feeds exactly this payload shape in staging and asserts the
quarantine happens.

Note: corrects DB-342 — schema drift fails loudly into quarantine; it never silently nulls or drops columns downstream.
