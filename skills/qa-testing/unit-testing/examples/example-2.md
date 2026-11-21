# Example 2 — Shared mutable fixture becomes isolated arrange

## Before

```js
const user = { credits: 100 }; // one fixture shared by every test in the file

test("spend deducts credits", () => {
  spend(user, 30);
  expect(user.credits).toBe(70); // passes only if it runs before the next test
});

test("spend refuses when credits are insufficient", () => {
  expect(() => spend(user, 150)).toThrow(); // fails if the first test already spent
});
```

## After

```js
test("spend deducts credits", () => {
  const user = { credits: 100 };
  spend(user, 30);
  expect(user.credits).toBe(70);
});

test("spend refuses when credits are insufficient", () => {
  const user = { credits: 100 };
  expect(() => spend(user, 150)).toThrow();
});
```

Note: corrects QA-003 — each test arranges its own inputs; the suite passes shuffled and with any single test run alone.
