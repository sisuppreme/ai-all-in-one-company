# Example 2 — Hotlinked banner vs. local licensed file

## Before

```html
<!-- Rebuild home page -->
<img src="https://target.example/media/hero-banner.jpg" alt="Spring collection">
```

The rebuild renders the hero straight from the source site's CDN. It looks finished in review; three months after launch the original site redesigns, the URL 404s, and the clone's home page ships a broken hero.

## After

The banner is harvested into the WARC capture with a manifest row (source URL, capture date, checksum). Its license record shows the image is the client's own campaign photography, licensed for their web properties including rebuilds — verdict `licensed`. The rebuild ships a local optimized copy from its own asset folder, and the hotlink scan (G-CL-033) confirms zero references to the source domain in the built output.

## Note

Corrected under CL-070: the deliverable never hotlinks the source CDN — assets ship as local, manifest-covered files with a reuse verdict (BAN-CL-033).
