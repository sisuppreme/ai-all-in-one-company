# Example 3 — Provider states that seed nothing

## Before

The pact carries the state `"a user with a paid order exists"`. The provider's state handler satisfies it by loading a recorded response body:

```js
// provider-states.js
setState("a user with a paid order exists", () => {
  stubResponse("GET /orders/441", readFixture("order-441.json"));
});
```

Verification passes every run — against the fixture. When the provider's real order query later breaks (a renamed column), verification stays green because the replay never touches the database, and the breakage ships.

## After

The state handler creates the state through the provider's own data layer, and the replay runs against the real provider build:

```js
// provider-states.js
setState("a user with a paid order exists", async () => {
  const user = await db.users.create({ email: "contract-test@example.com" });
  await db.orders.create({ userId: user.id, total: 59.99, status: "paid" });
});
```

Now a renamed column or a broken query fails verification in CI, before the change can deploy — the replay exercises the same code path production uses.

Note: corrects QA-166 (provider states are real setup code).
