# Example 3 — The new user who got a blank rail

## Before

```ts
// recommend.ts — no fallback defined
export async function recommend(user: User, surface: string) {
  const history = await eventsFor(user.id);
  if (history.length === 0) return { items: [], label: "Picked for you" };
  // ...personalized path
}
```

```tsx
// HomePage.tsx
{recs.items.length > 0 && <ProductRow items={recs.items} />}
```

A first-time user has no history, so the endpoint returns nothing and the rail silently vanishes — the newest users, the ones the fallback exists for, get an empty slot and a page with a hole in it.

## After

```ts
// serving-config.ts — the fallback is a documented, named configuration
export const FALLBACKS = {
  coldStart: {
    source: "popularity-quality-7d", // live query: top items by purchases + rating, last 7 days
    label: "Popular right now", // never "For you" — nothing about this user was computed
  },
};
```

```ts
// recommend.ts — every segment lands somewhere defined
export async function recommend(user: User, surface: string) {
  const history = await eventsFor(user.id);
  if (history.length < MIN_SIGNALS) {
    const items = await fallbackItems(FALLBACKS.coldStart); // still passes AI-103's filter
    return logAndServe(user, surface, items, { personalized: false, label: FALLBACKS.coldStart.label });
  }
  // ...personalized path
}
```

Cold-start users receive the documented popularity/quality fallback: non-empty, still exclusion-filtered, logged as fallback, and labeled "Popular right now" so the page never claims a personalization it did not perform. G-AI-053 asserts all three properties for a fresh user.

## Note

Corrected under AI-105 and AI-106: an undefined segment with an empty slot is a defect, and fallback content under a "For you" label would violate BAN-AI-051 (DET-FAKE-009) — the fallback exists, and it wears its own label.
