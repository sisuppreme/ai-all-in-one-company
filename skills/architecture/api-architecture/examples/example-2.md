# Example 2 — Cursor pagination replacing an unbounded list

## Before

`GET /customers` returns the entire collection in one array. At launch that is 200 records; a year later it is 40,000, the response is 30 MB, and the endpoint times out — but adding pagination now changes the response shape for every existing client.

## After

The endpoint paginates from its first version, per the house profile:

```text
GET /v1/customers?limit=50&cursor=eyJpZCI6MTAwMH0
200 OK
{
  "items": [ ... ],
  "next_cursor": "eyJpZCI6MTA1MH0"
}
```

Ordering is stated in the contract (ascending by `id`, stable), `limit` defaults to 50 and caps at 200, and the last page returns `"next_cursor": null`.

## Note

Corrects AR-064 (every list endpoint paginates — cursor preferred — and states its ordering; unbounded lists are forbidden).
