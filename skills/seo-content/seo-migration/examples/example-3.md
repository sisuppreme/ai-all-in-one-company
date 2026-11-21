# Example 3 — Perfect redirects onto noindexed templates

Rules exercised: CO-287, CO-289 — also CO-286, CO-290, CO-291, CO-292,
G-CO-144, G-CO-145, and BAN-CO-146.

## Before

A publisher migrates to a new CMS. The redirect work is done well: the
inventory is complete, every old URL has a disposition, and on staging every
`redirect-*` row resolves in one 301 hop to its mapped new URL, which returns
200.

What nobody checks is what those new pages carry. The new templates were
built on staging, where every page is served with
`<meta name="robots" content="noindex">` to keep the preview out of search
results — and the tag is part of the template, so it ships to production
unchanged. The same build also drops the old pages' curated meta
descriptions: the new template emits one default description for a whole
section, and several article templates emit none at all.

The migration launches "blind" in a second way too: no pre-migration
baseline was captured, so when indexed pages start falling out there is no
CO-286 record to compare against — no per-URL titles, directives, or
structured-data types, and no Search Console pre-period figures — only the
team's impression that "the redirects all worked." Every old URL lands
exactly where the map says. It lands on a page engines are told not to
index. This is BAN-CO-146 (staging protections carried live), compounded by
BAN-CO-145 (launching blind: no baseline, recovery judged by anecdote).

## After

Two checks are added to the launch sequence, before DNS is switched.

**1. Carry-over diff on staging (CO-287, sampled by G-CO-143).** Every
`keep` and `redirect-1:1` URL's new page is diffed against its CO-286
baseline for title, meta description, H1, canonical, robots directives,
hreflang set where present, and structured-data types. The diff surfaces
both defects as launch blockers, not post-launch surprises:

```
URL: /guides/spring-cleaning  (redirect-1:1)
  robots:    baseline "index, follow"  →  staging "noindex"        DEFECT
  meta desc: baseline (curated, page-specific) → staging (section default, duplicated)  DEFECT
  title/H1/canonical/structured-data types: match baseline
```

Each difference must be either an intentional change recorded in the map or
a defect to fix. The `noindex` is a defect: it is removed from the
production template set. The default descriptions are a defect: the
curated descriptions are carried over per page.

**2. Promotion indexability diff at launch (CO-289).** Technical-seo's
promotion diff (CO-005 / G-CO-001) runs as part of this skill's launch
sequence and asserts that no staging protection survives: no staging
`noindex`, no `Disallow: /` in robots.txt, no auth wall, and no
staging-host canonicals — and that robots.txt on the new host does not block
the new URLs or their render assets.

**Baseline and monitoring, decided before launch.** The CO-286 baseline is
captured before the switch — per-URL status, canonical, title, meta
description, H1, robots directives, structured-data types, and internal-link
counts, plus Search Console clicks, impressions, and average position for
the stated 28-day pre-period and the indexed-page count — so every
post-launch claim is baseline-vs-current, never anecdote. The CO-291
schedule and triggers are written into the migration record in advance:

- checks daily for the first 7 days, then weekly until day 28, each logged
  against the baseline (G-CO-145 reviews the log at day 7 and day 28);
- trigger (d) — staging protections found live at any point — fires the
  CO-292 response immediately, as do a wrong disposition on any mapped URL,
  an indexed-count fall not recovering across two consecutive checks after
  day 7, a spike in 404s on baseline URLs that had clicks or inbound
  links, or section-level clicks falling beyond the record's agreed drop
  threshold across two consecutive checks;
- the rollback mechanism, who can invoke it, and the fix-forward alternative
  (patch the template/directives in place, named owner and deadline) are
  recorded before launch, per CO-292.

**Launch verdict by crawl diff (CO-290, G-CO-144).** Within 24 hours of
launch, production is crawled with the same tool and settings as the
baseline crawl and diffed against the map and the baseline fields. The
report lists mismatches by URL; "the migration went well" is not accepted
as a substitute. In this run the diff confirms every baseline URL's live
outcome matches its mapped disposition and no new page carries the staging
directives — and because the baseline and monitoring log exist, the day-7
and day-28 reviews can state recovery (or loss) as figures against the
baseline, with property, period, and source named.

Note: the Before violates CO-287 (carry-over assumed, never diffed) and
CO-289 (staging protections promoted live) and is BAN-CO-146, made worse by
the missing baseline banned in BAN-CO-145. The After corrects it by diffing
carry-over on staging, running the promotion diff inside the launch
sequence, capturing the CO-286 baseline first, and holding the launch to the
CO-290 crawl diff and the CO-291 monitoring triggers instead of a narrative.
