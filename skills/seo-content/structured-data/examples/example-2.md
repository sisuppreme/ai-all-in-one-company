# Example 2 — The generator block that shipped with placeholders

Demonstrates CO-165 (no placeholder values, ever) and BAN-CO-082.

## Before

A block pasted from an online schema generator ships on the live pricing page, unedited:

```json
{
  "@type": "Product",
  "name": "Product Name",
  "image": "https://example.com/logo.png",
  "brand": { "@type": "Brand", "name": "Your Company" },
  "offers": {
    "@type": "Offer",
    "price": "0.00",
    "priceCurrency": "USD"
  }
}
```

Every value is scaffold text. The block parses, so nobody noticed; it describes a product that does not exist at a price that was never charged.

## After

The pasted block is deleted. The page type's template generates markup from the same record that renders the page, and the CI placeholder scan (G-CO-083) fails the build if scaffold patterns ever reappear:

```json
{
  "@type": "Product",
  "name": "Trailhead Insulated Bottle",
  "image": "https://trailhead.example/images/bottle-32oz.jpg",
  "brand": { "@type": "Brand", "name": "Trailhead Supply" },
  "offers": {
    "@type": "Offer",
    "price": "34.00",
    "priceCurrency": "USD"
  }
}
```

All values come from the product record — the same name, image, brand, and price the visitor sees.

Note: corrects CO-165 — placeholder values are build failures, never production content.
