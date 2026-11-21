# Example 3 — Flag-hidden admin feature gets real authorization

## Before

```tsx
// UI: the button is the only "protection"
{flags.isOn("admin_tools", user) && (
  <button onClick={() => download("/admin/export")}>Export all users</button>
)}
```

```ts
// API: no authorization at all — the flag was treated as the control
app.get("/admin/export", requireAuth, async (req, res) => {
  res.json(await db.users.findMany());
});
```

Any authenticated user who learns the URL — from the page source, a shared
screenshot, or guessing — exports the entire user table. The flag controlled
what was *shown*, not what was *allowed*.

## After

```ts
app.get(
  "/admin/export",
  requireAuth,
  requirePermission("users:export"), // server-side RBAC check, every request
  async (req, res) => {
    await auditLog.record({ actor: req.user.id, action: "users:export" });
    res.json(await db.users.findMany());
  },
);
```

The flag may still roll the feature out to staff gradually, and the button
may still be hidden by it — but the endpoint enforces the permission itself,
for every caller, whether or not they ever saw the button.

Note: corrects BE-068 — flags never replace authorization; a flag may hide a feature, while the API still enforces who may use it.
