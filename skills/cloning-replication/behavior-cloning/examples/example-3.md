# Example 3 — The borrowed filter widget

## Before

```js
// rebuild/src/components/ProductFilter.jsx
// Adapted from the source site's bundle (deobfuscated) so the
// filtering behaves exactly like the original.
function applyFilters(t, e) { /* target's minified logic, renamed */ }
```

The target's own code was lifted into the rebuild to guarantee identical behavior. The clone now ships the source's copyrighted implementation, whatever the behavior specs said.

## After

```text
Behavior spec: tests/product-filter.spec.ts (observed, frozen set)
  - Checking a brand checkbox filters the grid without reload;
    URL gains ?brand=<slug>; result count updates.
  - Combining brand + price range intersects both filters.
  - Clearing all filters restores the full grid and bare URL.
Rebuild: filtering re-implemented from this spec in the project's
own component code; G-CL-044 code-fingerprint scan: zero hits.
```

## Note

Violates CL-084 (behavior is re-implemented in original code from observation specs; the target's code is never copied or deobfuscated into the rebuild); corrected by specifying the observed behavior and writing original code against the spec.
