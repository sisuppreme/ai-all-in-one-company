# Example 1 — The $29 blog post

## Before

The billing configuration was updated in October: Pro moved from $29 to $24/month. In December, a blog post announcing a new feature closes with:

> "…available today on FlowBoard Pro — just $29/month."

The pricing page renders $24 from the billing configuration, checkout charges $24, and the blog says $29. Three surfaces, two prices — a price mismatch created entirely by a hand-typed number.

## After

The blog post is rewritten to carry no typed price:

> "…available today on FlowBoard Pro — see [current pricing](https://example.com/pricing) for the plan that fits your team."

Surfaces that can render from the configuration do so (the pricing page and checkout already did). The price-consistency scan (G-PR-101) now extracts every `$N/mo` string on the site and diffs it against the provider's active prices: the blog's $29 hit is exactly the class of error the scan exists to catch before publication.

## Note

Corrected under PR-205: prices are never hard-coded in page copy, posts, emails, or ads; surfaces render from the billing configuration or link to the pricing page without restating the number.
