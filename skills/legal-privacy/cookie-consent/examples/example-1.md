# Example 1 — The pre-ticked analytics toggle

## Before

The preferences layer of the banner ships with every purpose switched on:

```html
<label>
  <input type="checkbox" name="consent-analytics" checked>
  Analytics cookies — help us improve the site
</label>
<label>
  <input type="checkbox" name="consent-marketing" checked>
  Marketing cookies — measure our campaigns
</label>
<button>Save my choices</button>
```

A visitor who opens preferences, changes nothing, and clicks "Save my choices" is recorded as having consented to analytics and marketing. The consent record says the user chose; the user never did.

## After

Every toggle starts off, and only the visitor's own action enables a purpose:

```html
<label>
  <input type="checkbox" name="consent-analytics">
  Analytics cookies — help us improve the site
</label>
<label>
  <input type="checkbox" name="consent-marketing">
  Marketing cookies — measure our campaigns
</label>
<button>Save my choices</button>
```

Saving with nothing enabled records an explicit all-rejected choice; enabling a toggle records consent for that purpose only, with the banner version and timestamp (LG-088).

*Violates/corrects LG-085 (no pre-ticked consent — *Planet49*, C-673/17); see also BAN-LG-041.*
