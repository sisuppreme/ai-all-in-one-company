# Example 2 — The launch offer that never ended

## Before

Homepage banner, still live fourteen months after launch:

> "Launch offer — 50% off your first year!"

No start date, no end date, no terms page. New customers reasonably read it as a standing price; the billing configuration has charged full price since month two, so the banner advertises a discount nobody can get.

## After

The banner is replaced at the point of display with a dated, termed promotion:

> "Spring offer — 50% off your first year on annual plans, for new accounts created 2026-03-01 through 2026-03-31. Renews at the standard annual rate; [full terms](https://example.com/promo-terms)."

The promotion exists as a coupon in the billing configuration with the same start and end dates, so the banner, the terms, and checkout agree. When the end date passes, the banner comes down on schedule and the promotion date sweep (G-PR-103) verifies no undated offer remains anywhere on the site.

## Note

Corrected under PR-208: promotions and discounts carry visible dates and terms wherever the promotional price appears; an undated promotional price is treated as an error and removed.
