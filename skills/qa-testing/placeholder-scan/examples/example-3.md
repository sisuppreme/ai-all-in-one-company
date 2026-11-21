# Example 3 — A fixture array rendered as the live product catalog

## Before

The static sweep's import check flags a production bundle chunk that
includes the seed module:

```
src/catalog/ProductGrid.tsx:3:  import { products } from "../seed/products";
src/seed/products.ts:           export const products = [
                                  { id: 1, name: "Aurora Lamp", price: 49,
                                    rating: 5, quote: "Changed my home!" },
                                  ... 11 more invented entries
                                ];
```

The storefront renders this literal as its catalog — invented names,
prices, and testimonial quotes. The fresh-account probe confirms the same
twelve products appear for every visitor, and adding a product in the
admin panel changes nothing on the storefront (DET-FAKE-014, BAN-QA-143).

## After

1. The seed import is removed from production code; the grid fetches from
   the real catalog endpoint. Seed data remains available to development
   and test environments only, behind the environment guard.
2. The bundle is rebuilt and the sweep re-run: no seed or fixture module
   appears in the production bundle's module list.
3. The dynamic probes are re-executed: a product created in the admin
   panel appears on the storefront after reload (persistence test), and a
   fresh store with no products shows the designed empty state instead of
   staged inventory.

Note: corrects QA-291 — seed and fixture files must not be imported by, bundled into, or reachable from production code paths; the sweep checks imports and bundle contents, not just visible copy.
