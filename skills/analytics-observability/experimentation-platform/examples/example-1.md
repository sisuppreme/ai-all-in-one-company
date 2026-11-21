# Example 1 — Coin-flip bucketing becomes a deterministic hash

## Before

The pricing page assigns its experiment variant in the browser on every page load:

```js
const variant = Math.random() < 0.5 ? 'control' : 'new-pricing';
renderPricing(variant);
```

The same signed-in user sees the new pricing on Monday, the control on Tuesday, and the new pricing again on a second device. Support receives contradictory screenshots, exposure counts per variant are whatever the coin flips produced, and no analysis can say which users actually experienced which price.

## After

Assignment is computed once, from stable inputs, by the single shared assignment function:

```js
function assignVariant(experimentId, userId, split) {
  const bucket = hash(experimentId + ':' + userId) % 10000; // deterministic
  return bucket < split.treatment * 10000 ? 'new-pricing' : 'control';
}

const variant = assignVariant('pricing-2026-11', user.id, { treatment: 0.5 });
logExposure({ experimentId: 'pricing-2026-11', variant, userId: user.id, at: now() });
renderPricing(variant);
```

The same user gets the same variant on every session and device, the assignment is reproducible in the G-AN-021 determinism test, and the exposure event is written at the moment the variant is served.

Note: corrects AN-041 (assignment is a deterministic hash of experiment ID + unit ID; see also BAN-AN-021).
