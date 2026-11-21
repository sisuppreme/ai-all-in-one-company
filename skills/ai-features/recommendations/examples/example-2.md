# Example 2 — Recommended again: the boots you already bought

## Before

```ts
// recommend.ts — filtering delegated to the model
export async function recommend(user: User) {
  const candidates = await candidateGeneration(user);
  const prompt =
    `From these products, pick 10 for this user. ` +
    `Do not include anything they already own or anything out of stock.\n` +
    candidates.map((c) => `${c.id}: ${c.name}`).join("\n");
  return llm.complete({ prompt }); // model usually complies — until it doesn't
}
```

Ownership and stock live only in a prompt sentence. The model has no reliable access to either, so the boots the user bought last week come back as a recommendation, next to a jacket that sold out yesterday.

## After

```ts
// recommend.ts — filter in deterministic code, rank after
export async function recommend(user: User, surface: string) {
  const candidates = await candidateGeneration(user); // behavior + content similarity
  const owned = await ownedItemIds(user.id); // purchases and consumed items
  const eligible = candidates.filter(
    (c) => !owned.has(c.id) && c.stock > 0 && isEligible(user, c),
  ); // hard filter: code, not a prompt (AI-103)
  const ranked = rank(eligible, user, loadServingConfig()); // documented signals (AI-108)
  const fresh = await recheckAvailability(ranked.slice(0, 10)); // serve-time check (AI-104)
  return logAndServe(user, surface, fresh); // version + reason codes recorded (AI-109)
}
```

Owned, consumed, out-of-stock, and ineligible items are removed by code after candidate generation and rechecked at serve time. The model never gets a vote on facts only the database knows, and G-AI-052 sweeps responses to prove the excluded items never appear.

## Note

Corrected under AI-103: exclusion by prompt hint instead of deterministic code violates BAN-AI-052 (DET-FAKE-017) — a filter that only exists in the instructions is a cosmetic filter.
