# Example 1 — The deleted pricing page

## Before

The pricing page was deleted from the live site last year. The builder finds a blog post with a screenshot, rebuilds the page from that screenshot and a generic three-tier layout, and marks the inventory row "rebuilt from archive." No CDX query was ever run, although three dated Wayback captures of the page exist.

## After

The builder queries the Wayback CDX index first and finds three captures. The latest capture's timestamp and `digest` are recorded in the inventory row, the page is rebuilt from that capture's structure, and the row is labeled `captured`. The blog screenshot is used only to sanity-check one section the capture rendered without its stylesheet.

## Note

Demonstrates CL-102 and CL-110: the highest evidence tier is checked and recorded before any lower tier is used, and a capture counts as evidence only with its digest and timestamp on record.
