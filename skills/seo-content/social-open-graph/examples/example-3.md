# Example 3 — The scaffold's name in og:site_name

## Before

```html
<!-- every page, rendered -->
<meta property="og:site_name" content="Acme Starter Kit">
<meta property="og:image" content="https://cdn.acme-starter.example/demo/og-cover.jpg">
```

The site was built from a starter template and the social tags were never replaced: shares name a product that is not this site, and the preview image is served from the template vendor's demo domain.

## After

```html
<!-- every page, rendered -->
<meta property="og:site_name" content="TaskBoard">
<meta property="og:image" content="https://taskboard.example/images/og-default.png">
```

og:site_name carries this site's own current name from the fact sheet, and the default share image is a real asset on this site's own domain.

Note: corrects CO-226 (og:site_name is this site's own name) and CO-229 (tags generated from this site's own data, not a scaffold).
