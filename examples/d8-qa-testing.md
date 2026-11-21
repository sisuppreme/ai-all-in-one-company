# D8 Example — A Green Test Suite That Proved Nothing

## Scenario

The checkout from the D4 example is about to ship. Its repository shows a
100% coverage badge and a green CI pipeline. D8's job is to find out
whether any of that means the checkout works — before D6 promotes it.

## Before

```ts
// pricing.test.ts
test("applies discount", () => {
  const svc = new PricingService();
  expect(svc.applyDiscount).toBeDefined();
  expect(true).toBe(true);
});

test("rejects expired card", () => {
  const gateway = fakeGatewayThatAlwaysApproves();  // the double approves everything
  expect(checkout(gateway, expiredCard).ok).toBe(true);
});

// checkout.e2e.ts
test("user can buy", async () => {
  await page.click("#buy");
  await expect(page.locator(".toast")).toHaveText("Order placed!");
});

test.skip("handles declined card", () => { /* fails, will fix later */ });
```

```yaml
# ci.yml
- run: echo "All tests passed"   # the gate prints success; it runs nothing
```

Coverage: 100%. The suite has never been observed failing.

## What the skills caught

- **BAN-QA-001 — Assertion-free coverage gaming**: `expect(true)` and
  `toBeDefined` assert nothing about behavior — **QA-002 — Every test
  asserts a specific expected value**. This is **DET-CODE-012 — Fake
  tests that assert nothing**. The assertion-presence gate **G-QA-003**
  and the seeded-fault (mutation) gate **G-QA-001** both kill this suite:
  break the discount math on purpose and nothing turns red, violating
  **QA-009 — The suite must be able to fail**.
- **BAN-QA-002 — Doubling the unit under test**: the "expired card" test
  wires a gateway that approves everything and then asserts approval —
  the outcome was decided by the fixture, not the code (**QA-006 —
  Doubles live at the unit boundary only**).
- **BAN-QA-022 — Toast-only assertion**: the E2E journey ends at a
  success message. It never checks that an order was written — the exact
  shape of **DET-FAKE-015 — Forms that submit nowhere**. **QA-048 —
  Network write assertion** and **QA-046 — Persistence probe on every
  mutation** are mandatory for this journey; the declined-card path is a
  journey too (**QA-047**), not a skip.
- **BAN-QA-004 — Disabling a failing test to go green**: the `.skip` has
  no ticket, no owner, no expiry. Under **QA-228** quarantine is a
  counted, expiring state with a linked defect — or the test is fixed.
- **BAN-QA-111 — Echo-only pipeline**: a gate that prints "passed" is
  not a gate. **QA-221 — A gate is a command with an exit code**, and
  **QA-222** — its definition predates the work it judges.
- No allocation exists anywhere: **QA-202 — Pyramid allocation in
  numbers** requires the strategy to state how many unit, integration,
  and E2E tests the budget allows, so "critical flows only" (**QA-041**)
  is a decision rather than a drift.

## After

```ts
test("applies a 10% discount to the server-recomputed total", () => {
  const svc = new PricingService();
  expect(svc.total([{ priceCents: 1200, seats: 2 }], "TEAM10")).toBe(2160);
});

test("declined card persists no order and returns the decline problem", async () => {
  const res = await checkout(testGatewayDeclining, validCard);
  expect(res.status).toBe(402);
  expect(await db.orders.count()).toBe(0);
});
```

The E2E journey now clicks buy, asserts the `POST /orders` response is
201, reloads the page, and asserts the order is still there — toast
optional. The declined-card journey runs against the provider's
test-mode decline card (**G-QA-023**). The skipped test became a
quarantined defect with a ticket and a two-week expiry; when the fix
landed, its failing test landed with it (**QA-007**).

CI runs the suites as required checks whose exit codes decide the
build, and the nightly negative-control job seeds a fault — a discount
function that always returns the undiscounted total — and requires the
suite to catch it (**G-QA-111 — Negative-control meta-gate**). Coverage
is still reported, as a floor signal (**QA-008**), never as the proof.

## Skills used

- [unit-testing](../skills/qa-testing/unit-testing/SKILL.md)
- [e2e-testing](../skills/qa-testing/e2e-testing/SKILL.md)
- [test-strategy](../skills/qa-testing/test-strategy/SKILL.md)
- [qa-gates](../skills/qa-testing/qa-gates/SKILL.md)
- [placeholder-scan](../skills/qa-testing/placeholder-scan/SKILL.md)
