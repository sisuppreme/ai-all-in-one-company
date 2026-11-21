# Example 1 — Write asserted from the response, corrected to read-back

## Before

```js
test("PATCH /profile updates the display name", async () => {
  const res = await api.patch("/profile", { name: "New Name" });
  expect(res.status).toBe(200);
  expect(res.body.name).toBe("New Name");
});
```

The handler builds its response from the request payload. The test passes
even after the update call is commented out — nothing ever reads the stored
record, so a profile edit that does not stick (DET-FAKE-016) sails through.

## After

```js
test("PATCH /profile updates the display name", async () => {
  const user = await factories.user();
  const token = await signIn(user);

  const res = await api.patch("/profile", { name: "New Name" }, token);
  expect(res.status).toBe(200);

  // Read back through a different surface: a fresh GET, not the PATCH body.
  const reread = await api.get("/profile", token);
  expect(reread.body.name).toBe("New Name");

  // And through a third surface: the stored record itself.
  const row = await db.query("SELECT name FROM users WHERE id = $1", [user.id]);
  expect(row.name).toBe("New Name");
});
```

Commenting out the update now turns the test red on both read-backs.

Note: corrects QA-024 — every write is read back through a different surface before it counts as persisted.
