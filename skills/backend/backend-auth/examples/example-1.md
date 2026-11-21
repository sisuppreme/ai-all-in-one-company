# Example 1 — localStorage flag replaced by a server session

## Before

```ts
// client
async function login(email: string, password: string) {
  localStorage.setItem("isLoggedIn", "true");
  localStorage.setItem("userEmail", email);
  navigate("/dashboard");
}

// server — "protected" route, no check at all
app.get("/account", async (req, res) => {
  res.json(await db.accounts.findByEmail(req.query.email));
});
```

The password is never verified, "authentication" is a boolean anyone can
type into their own browser storage, and the account endpoint serves any
email address to any caller.

## After

```ts
// server
app.post("/auth/login", async (req, res) => {
  const user = await db.users.findByEmail(req.body.email);
  const hash = user?.passwordHash ?? DUMMY_HASH; // constant-shape work either way
  const ok = await argon2.verify(hash, req.body.password);
  if (!user || !ok) {
    return res.status(401).json(problem(401, "Invalid email or password"));
  }

  const session = await sessions.create(user.id); // high-entropy opaque ID, stored server-side
  res.cookie("session", session.id, {
    httpOnly: true,
    secure: true,
    sameSite: "lax",
    maxAge: SESSION_IDLE_MS,
  });
  res.status(204).end();
});

app.get("/account", requireSession, async (req, res) => {
  res.json(accountView(await db.accounts.findByUserId(req.user.id)));
});
```

Identity is proven server-side against the salted hash, the session lives
in a cookie the client cannot read or forge, and the protected route checks
it on every request — clearing localStorage changes nothing.

Note: corrects BE-101 — authentication is verified server-side on every request and client state is never evidence; and BE-103 — sessions are server-issued IDs in Secure + HttpOnly + SameSite cookies.
