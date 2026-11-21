# Example 2 — Coin-flip bucketing replaced by deterministic hashing

## Before

```ts
function inRollout(user: User): boolean {
  // 25% rollout of the new pricing page
  return Math.random() < 0.25;
}
```

The coin is flipped per request: the same user sees the new pricing page,
then the old one, then the new one again — sometimes inside a single
checkout. Support cannot reproduce what any user saw, and the experiment's
data mixes both variants for every user.

## After

```ts
import { createHash } from "node:crypto";

function inRollout(flagKey: string, userId: string, percent: number): boolean {
  const digest = createHash("sha256").update(`${flagKey}:${userId}`).digest();
  const bucket = digest.readUInt32BE(0) % 100; // stable per flag + user
  return bucket < percent;
}

// usage, through the single toggle router:
const on = flags.isOn("new_pricing", user, () =>
  inRollout("new_pricing", user.id, 25),
);
```

The bucket is a pure function of the flag key and the stable user ID, so a
user is in or out consistently across requests, devices, and services — and
raising the percentage only ever adds users, never reshuffles them.

Note: corrects BE-065 — percentage rollouts bucket deterministically by hashing a stable user key; a user never flickers between variants.
