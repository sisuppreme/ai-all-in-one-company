# Example 2 — 900 products redirected to the homepage

Rules exercised: CO-284 — also CO-283, CO-285, G-CO-143, and BAN-CO-142.

## Before

An online retailer replatforms its catalogue. During the move, 900 product
URLs from discontinued lines have no counterpart in the new catalogue.
Rather than decide each one, the developer adds a single catch-all rule to
the server configuration:

```
/products/old-line/*  →  301  /
```

Every discontinued product now "redirects successfully." Status checks pass:
each old URL returns a 301 and the homepage returns 200. But a visitor who
follows a bookmark, an inbound link, or a search result for a specific
product lands on a generic homepage that cannot answer the link they
followed, and the homepage absorbs the signals of hundreds of unrelated
product pages. This is BAN-CO-142 (everything redirects to the homepage):
the homepage used as a catch-all instead of a topical equivalent or an
honest 410.

The catch-all also hides a second problem: some of the 900 products are not
discontinued at all — the same product is still sold under a new URL — but
the pattern rule never distinguishes them, so even those send their visitors
and their link equity to `/` instead of to the product page that exists.

## After

The catch-all rule is deleted and the 900 URLs are worked through the map
file, one disposition each under CO-283. For every URL the question under
CO-284 is topical equivalence — *the page a visitor following the old link
would expect* — not path-pattern similarity:

| Old URL | Disposition | New URL / reason |
|---|---|---|
| `/products/old-line/trail-shoe-red` | `redirect-1:1` | `/products/trail-shoe-red` — same product, still sold, new path |
| `/products/old-line/trail-shoe-blue` | `redirect-merged` | `/products/trail-shoe` — colour variants consolidated into one product page; merge reason recorded |
| `/products/old-line/2019-clearance-boot` | `gone-410` | Line withdrawn, no equivalent sold; removal reason and approver recorded |
| `/products/old-line/gift-wrap-addon` | `gone-410` | Add-on service ended, no equivalent page; removal reason and approver recorded |

No row points at `/`, a section hub, or a search page as a catch-all. Where
no equivalent exists, the honest answer is `gone-410`, not a forced match to
an unrelated page (CO-284).

Each `redirect-*` row is then implemented as CO-285 requires — a single-hop
301 (or 308) from the exact old URL to the exact new URL, with the server
configuration generated or checked from the same map file, not maintained as
a second list — and verified on staging by G-CO-142, which requests every
old URL in the map and asserts the full status chain matches its disposition.

Finally, G-CO-143's human sample checks equivalence the status codes cannot:
a reviewer opens at least 25 of the `redirect-*` pairs — a sample that must
include the top 10 baseline URLs by pre-migration clicks (CO-286) — and
confirms each new page is actually the equivalent of the old one. A pair
that returns 301 → 200 but lands on the wrong product fails this gate and is
remapped before launch.

Note: the Before violates CO-284 and is BAN-CO-142 — a catch-all to the
homepage is not a disposition. The After corrects it with per-URL
dispositions under CO-283, topical 1:1 targets or recorded merges and 410s
under CO-284, single-hop permanent redirects under CO-285, and a human
equivalence sample under G-CO-143, because a wrong-but-200 destination is
invisible to status checks alone.
