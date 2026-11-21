# Example 1 — Mass assignment closed by an allowlist schema

## Before

```ts
app.patch("/users/me", requireAuth, async (req, res) => {
  // Whatever the client sends becomes the update:
  const user = await db.users.update(req.user.id, req.body);
  res.json(userView(user));
});
```

```http
PATCH /users/me
{ "displayName": "Sam", "isAdmin": true, "balanceCents": 1000000 }
```

The handler binds the body directly to the record, so two fields the
profile form never renders are written anyway — the account promotes itself
and mints itself a balance.

## After

```ts
const profileUpdateSchema = z.object({
  displayName: z.string().min(1).max(80),
  locale: z.enum(["en", "ur"]).optional(),
  marketingOptIn: z.boolean().optional(),
}).strict(); // .strict() = unknown fields are rejected, not ignored

app.patch("/users/me", requireAuth, async (req, res) => {
  const parsed = profileUpdateSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(422).json(validationProblem(parsed.error));
  }
  const user = await db.users.update(req.user.id, parsed.data);
  res.json(userView(user));
});
```

The schema enumerates exactly the fields a profile update may touch. The
same request now fails with a 422 naming `isAdmin` and `balanceCents` as
unrecognized fields, and nothing is written.

Note: corrects BE-043 — allowlist over denylist: write endpoints enumerate accepted fields and reject unknown ones, blocking mass assignment.
