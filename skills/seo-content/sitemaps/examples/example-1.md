# Example 1 — The launch-day sitemap, one year later

## Before

At launch, a developer generates `sitemap.xml` once with an online tool and
commits it to the repo as a static file. The site then lives for a year:
products are added and discontinued, the blog grows from 12 posts to 140, a
docs section is retired. Nobody touches the sitemap. It still lists the
scaffold's sample page and 96 discontinued products, and none of the 128
newer posts appear in it. Search Console shows a flat "Discovered" count
that stopped matching the site months ago, and the team blames crawl budget.

## After

The static file is deleted from the repo. The build generates the sitemap
from the route and content inventory on every publish event: a new post
appears in the sitemap in the same deploy that publishes it, and a retired
docs page disappears in the deploy that unpublishes it. The count
reconciliation in the build log reads:

```
inventory: 1,214 indexable URLs
sitemap:   1,214 URLs
excluded:  38 drafts, 6 noindex landing pages, 19 redirects — all by design
```

Nobody edits the output; a wrong entry is fixed in the inventory or the
generator filter, and the regeneration-on-change test proves the wiring on
every release.

Note: corrects CO-181 — the sitemap is a build artifact generated from the route/content inventory at publish time, never a hand-maintained file.
