# Example 1 — The pricing page only the sitemap knew about

## Before

The redesigned pricing page is published at `/pricing`, returns HTTP 200, and is listed in `sitemap.xml`. No page on the site links to it: the nav redesign dropped the Pricing item, and no blog post, feature page, or home page section mentions it. The crawl graph shows in-degree 0. Users find pricing only by guessing the URL; the page earns no organic visits in its first month.

## After

Before publish, the page's brief names its inbound links: the home page pricing section ("See pricing plans"), the features page comparison paragraph ("Compare plans and pricing"), and the two highest-traffic blog posts on cost ("What it costs, on the pricing page"). The nav item is restored. The release crawl shows in-degree 4 and depth 1 from home.

Note: violates CO-201 (no orphan pages) and CO-203 (the brief names inbound links first); corrected by adding the planned in-content links before publish.
