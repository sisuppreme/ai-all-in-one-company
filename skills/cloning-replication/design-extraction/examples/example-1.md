# Example 1 — Guessed palette vs. sampled tokens

## Before

The extractor looks at the source site's screenshots, decides the primary color "is basically Tailwind blue," and writes the token file from memory: `color.primary = #2563eb`, `color.accent = #f59e0b`. Neither value was ever measured; the rebuild drifts further with every page.

## After

Browser automation reads computed styles on the home, pricing, and article templates. The primary button returns `rgb(29, 78, 216)` on 14 elements and `rgb(30, 64, 175)` on hover; the token file records `$value: "#1d4ed8"` with its sample count, page, and selector, plus a separate hover-state token — all values the traceability diff (G-CL-021) can re-verify.

Note: corrects CL-044 / BAN-CL-021 — every token traces to a sampled computed style; invented "close enough" values are banned.
