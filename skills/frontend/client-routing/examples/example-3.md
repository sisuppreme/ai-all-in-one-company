# Example 3 — Guard-only protection replaced by guard plus API authorization

Corrects rule **FE-225** (guards are UX only; the API authorizes).

## Before

```js
// The router guard is the only protection. The API trusts any
// authenticated session, so the "protected" data is one curl away.
export async function loader({ request }) {
  const user = await getSessionUser(request);
  if (!user) return redirect("/login");
  return null; // guard "protects" the page
}

// GET /api/admin/users
export async function listUsers(req, res) {
  const users = await db.users.findAll(); // no role check at all
  res.json(users);
}
```

## After

```js
// The guard still redirects for UX, but the API authorizes
// every request on its own — the guard is not the boundary.
export async function loader({ request }) {
  const user = await getSessionUser(request);
  if (!user) return redirect("/login");
  return null;
}

// GET /api/admin/users
export async function listUsers(req, res) {
  const user = await getSessionUser(req);
  if (!user) return res.status(401).json({ error: "Not signed in" });
  if (user.role !== "admin") return res.status(403).json({ error: "Admins only" });
  const users = await db.users.findAll();
  res.json(users);
}
```

Note: hiding the route never protected the data; the corrected version passes gate G-FE-113 because the endpoint itself refuses unauthenticated and non-admin callers.
