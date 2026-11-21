# Example 1 — Every page sharing as the homepage

## Before

```html
<!-- /pricing, rendered -->
<meta property="og:title" content="TaskBoard — Organize your team's work">
<meta property="og:description" content="TaskBoard helps teams plan, track, and ship work together.">
<meta property="og:url" content="https://taskboard.example/">
<meta property="og:image" content="https://taskboard.example/images/og-default.png">
```

Every page on the site carries the homepage's og:url, title, and description. A shared pricing link previews as the homepage, attributes to the homepage, and tells the reader nothing about pricing.

## After

```html
<!-- /pricing, rendered -->
<meta property="og:title" content="Pricing — TaskBoard">
<meta property="og:description" content="TaskBoard plans from $0 for small teams: per-seat pricing, feature comparison, and annual billing discounts.">
<meta property="og:url" content="https://taskboard.example/pricing">
<meta property="og:image" content="https://taskboard.example/images/og-pricing.png">
```

og:url is the pricing page's own canonical URL, and the title and description describe the page the link actually opens.

Note: corrects CO-222 (og:url is the page's canonical URL) and CO-223 (per-page og:title and og:description).
