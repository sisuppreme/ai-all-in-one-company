# Example 1 — Assertion-free test becomes a real assertion

## Before

```js
test("cart total", () => {
  const cart = new Cart();
  cart.add({ price: 1500, qty: 2 });
  cart.add({ price: 1200, qty: 1 });
  cart.total(); // executes the code, asserts nothing — passes even if total() returns 0
});
```

## After

```js
test("cart total sums price × qty across lines", () => {
  const cart = new Cart();
  cart.add({ price: 1500, qty: 2 });
  cart.add({ price: 1200, qty: 1 });
  expect(cart.total()).toBe(4200);
});
```

Note: corrects QA-002 — every test asserts a specific expected value; a test that only executes code is coverage theater (BAN-QA-001).
