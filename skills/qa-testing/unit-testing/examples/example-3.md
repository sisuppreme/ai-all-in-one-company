# Example 3 — Wall-clock dependency becomes injected time

## Before

```js
test("token is expired after 15 minutes", () => {
  const token = issueToken();
  // reads the real clock: passes or fails depending on when the suite runs,
  // and can never test the 15-minute boundary without waiting 15 minutes
  expect(isExpired(token, Date.now())).toBe(false);
});
```

## After

```js
test("token is expired 15 minutes after issue", () => {
  const issuedAt = 1_700_000_000_000; // fixed instant, injected — no real clock
  const token = issueToken(issuedAt);
  expect(isExpired(token, issuedAt + 14 * 60_000)).toBe(false);
  expect(isExpired(token, issuedAt + 15 * 60_000)).toBe(true);
});
```

Note: corrects QA-004 — time is injected, never read from the wall clock, so the boundary itself is testable.
