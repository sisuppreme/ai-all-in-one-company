# Example 1 — The staging noindex that shipped to production

## Before

The redesigned site is promoted from staging to production on Friday. The
staging template carries `<meta name="robots" content="noindex, nofollow">`
to keep the preview out of search results, and nobody removes it — the
production pages ship with the same tag. The launch is declared a success.
Over the next two weeks organic sessions fall to near zero, and the team
starts debugging content quality before anyone fetches a page header.

## After

The release runs the promotion indexability diff first. The script fetches
robots.txt, response headers, and meta robots for the top route templates on
both environments and reports one line:

```
PROD /  meta robots: "noindex, nofollow"  == STAGING value — BLOCKER
```

The tag is removed from the production template, the diff re-runs clean, and
only then does the release proceed. Search Console coverage is checked a week
later: pages indexed, no exclusion spike to triage.

Note: corrects CO-005 — staging and production are diffed on indexability directives before every release, and any staging protection in production blocks it.
