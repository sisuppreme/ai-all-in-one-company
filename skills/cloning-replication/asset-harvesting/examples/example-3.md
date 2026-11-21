# Example 3 — Logo in the asset folder vs. logged replacement

## Before

The target's logo SVG and wordmark are saved into the rebuild's `src/assets/brand/` folder alongside the harvested photography, "so the header matches." The rebuild is the operator's own new storefront, and it launches wearing the target's trademark.

## After

The logo and wordmark get manifest rows with verdict `replace`: source URL, capture date, checksum, measured size and header placement noted, and a pointer to the replace-list. Reconstruction builds the header slot to those measurements and the operator supplies their own mark. G-CL-034 confirms no `replace`-verdict file exists in the ship folders.

## Note

Corrected under CL-068: trademarks and logos are logged so reconstruction knows what to replace — they are never harvested for reuse (BAN-CL-032).
