# Example 1 — The help centre that was never inventoried

Rules exercised: CO-282, CO-283 — also G-CO-141 and BAN-CO-141.

## Before

A SaaS company replatforms its marketing site and support help centre from a
legacy CMS to a new one. The migration record (CO-281) names the type as a
replatform, the old and new hosts, the launch window, the owner, and the
rollback owner.

The redirect map, however, is built from one source only: the XML sitemap the
developers hand over for the *new* build. Every URL in that sitemap gets a
row, and the team treats the map as complete.

The old help centre is the casualty. Its articles lived under
`/support/articles/…` on the legacy CMS, were not linked from the new site's
navigation, and do not appear in the new sitemap — so they never enter the
map at all. Several of those articles are the targets of inbound links from
partner documentation and from the product's own in-app help buttons, and
some are regular landing pages from search. None of that is visible, because
nobody pulled the sources that would have shown it.

At launch the old article URLs return 404. There is no recorded disposition,
no approver, and no reason for any of them — the exact failure named in
BAN-CO-141 (the silent disappearance). The breakage is discovered only when
a partner complains that their documentation now links to dead pages.

## After

The inventory is rebuilt as CO-282 requires: the union of every source, each
named in the migration record with its pull date —

- a full crawl of the live (old) site;
- the live XML sitemap(s);
- the Search Console indexed/pages report export;
- server-log / analytics landing-page URLs for the trailing 12 months;
- the known backlink targets from Search Console's Links report.

The union surfaces the `/support/articles/…` URLs that the crawl of the new
build and the new sitemap had missed: orphaned articles with inbound links,
and articles that appear as landing pages in the logs but are linked from
nowhere on the site.

Every one of those URLs then gets exactly one disposition in the map file
under CO-283, with the columns old URL, disposition, new URL, and
approver/reason where applicable:

| Old URL | Disposition | New URL / reason |
|---|---|---|
| `/support/articles/reset-password` | `redirect-1:1` | `/help/account/reset-password` |
| `/support/articles/legacy-billing-faq` | `redirect-merged` | `/help/billing/faq` — merged: content folded into the billing FAQ, reason recorded |
| `/support/articles/retired-importer` | `gone-410` | Removed: the importer it documented was withdrawn; removal reason and approver recorded |
| `/support/articles/` (hub) | `redirect-1:1` | `/help/` |

No row is left unclassified and no row is `TBD`.

Gate G-CO-141 then joins the baseline inventory against the redirect map on
the normalised old URL and asserts: every inventory row has exactly one
disposition, every `redirect-*` row names a new URL, and every `gone-*` row
names a reason and approver. The first run fails — it finds the help-centre
rows that were still missing — and launch is blocked until they are
inventoried and classified. The re-run passes with zero unclassified, zero
duplicate, and zero `TBD` rows, and only then does the migration proceed to
staging redirect verification under G-CO-142.

Note: the Before violates CO-282 (a crawl/sitemap of the new build is not an
inventory) and CO-283 (URLs launched with no disposition), and is BAN-CO-141.
The After corrects both: union inventory first, one recorded disposition per
URL, and G-CO-141 as a launch-blocking check rather than a post-launch
surprise.
