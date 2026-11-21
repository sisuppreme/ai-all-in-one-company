# Example 3 — The members' area, enumerated with a borrowed login

## Before

```text
Crawl log (excerpt)
14:02  GET /members/dashboard        200 (session cookie: teammate account)
14:02  GET /members/billing          200
14:03  GET /members/downloads        200
... 47 members-only routes enumerated "so the inventory is complete"
```

The routes are real, but they were obtained with a teammate's personal login that nobody authorized for this work. The discovery record now rests on access the project had no right to use, and every downstream inventory row inherits the problem.

## After

```text
Discovery record (excerpt)
/members/* — GATED. Evidence: sitemap lists /members/ (login redirect),
CDX holds a 2023 capture of the public login page, JS bundle manifest
references 12 client-side /members routes. None fetched.
Recorded as gated; enumeration of the gated space waits for access the
client legitimately provides under the authorization record.
G-CL-005: zero authenticated fetches in the crawl log.
```

## Note

Violates CL-009 (gated space is recorded as gated with its public evidence, never entered with borrowed credentials or by bypass); corrected by logging the gated space from sitemap, CDX, and bundle evidence only, and leaving its enumeration to client-provided access.
