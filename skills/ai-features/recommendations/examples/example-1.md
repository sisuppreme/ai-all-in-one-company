# Example 1 — The "Picked for you" rail that showed everyone the same six products

## Before

```tsx
// HomePage.tsx — "Picked for you" rail
const PICKED_FOR_YOU = [4417, 1203, 882, 5520, 319, 7741];

export function PickedForYouRail() {
  return (
    <section aria-label="Picked for you">
      <h2>Picked for you</h2>
      <ProductRow productIds={PICKED_FOR_YOU} />
    </section>
  );
}
```

The rail renders a constant array. A user with three years of hiking purchases and a first-time anonymous visitor see the identical six products, under a label that promises personalization nobody computed.

## After

```tsx
// HomePage.tsx — the rail renders whatever the recommender serves
export function PickedForYouRail({ userId }: { userId: string }) {
  const recs = useRecommendations(userId, "home-for-you"); // GET /api/recommendations?surface=home-for-you
  if (recs.loading) return <RailSkeleton />;
  return (
    <section aria-label={recs.label}>
      <h2>{recs.label}</h2> {/* "Picked for you" only when recs.personalized is true;
                               otherwise the fallback label, e.g. "Popular right now" */}
      <ProductRow items={recs.items} /> {/* each item carries its reason, e.g. "Because you bought X" */}
    </section>
  );
}
```

The server builds the list per user — candidates from the user's events, exclusion filter, ranking — and returns the label with the data: personalized lists say "Picked for you", the cold-start fallback says "Popular right now". The label can no longer claim more than the pipeline computed.

## Note

Corrected under AI-106 and AI-107: one static list under a "For you" label violates BAN-AI-051 (DET-FAKE-009); a personalized label is earned only by a list computed from that user's signals, and G-AI-051 proves two different histories get different lists.
