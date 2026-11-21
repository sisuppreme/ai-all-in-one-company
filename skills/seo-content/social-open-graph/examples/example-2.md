# Example 2 — The logo that previewed a pricing page

## Before

```html
<!-- /pricing, rendered -->
<meta property="og:image" content="/assets/logo.png">
```

The pricing page's share image is a relative path to the site's 240×80 logo. Crawlers cannot resolve the relative URL, and where a platform guesses, the preview is a tiny logo on a blank field — the page's actual offer never appears.

## After

```html
<!-- /pricing, rendered -->
<meta property="og:image" content="https://taskboard.example/images/og-pricing.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

og:image is an absolute production URL to a purpose-built 1200×630 share image showing the pricing tiers — an image that represents this page and resolves for every crawler.

Note: corrects CO-224 (og:image is absolute and page-appropriate, at full share size).
