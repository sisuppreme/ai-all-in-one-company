# Example 3 — Offset pagination replaced by cursors on a live feed

## Before

```text
GET /events?offset=100&limit=50
```

The feed gains new events every second. Between the client's page 2 and
page 3 requests, five events arrive at the head of the list, so the offset
window slides: the client sees five events twice and never sees five others.
Counts and pages disagree with the results shown.

## After

```text
GET /events?limit=50
→ 200
{
  "data": [ …50 events… ],
  "nextCursor": "eyJpZCI6OTEyMzQ1fQ",
  "hasMore": true
}

GET /events?cursor=eyJpZCI6OTEyMzQ1fQ&limit=50
→ the 50 events strictly after event 912345, in stable order
```

The cursor names a position in a stable ordering (here, the last event ID
seen), so inserts at the head cannot shift the window: no duplicates, no
skips, and `limit` is capped by the convention sheet's maximum page size.
Offset pagination remains acceptable for small, static, admin-style lists —
the convention sheet says which style applies where, and the whole API
follows it.

Note: corrects BE-026 — one pagination style from day one, cursor preferred for large or fast-changing collections.
