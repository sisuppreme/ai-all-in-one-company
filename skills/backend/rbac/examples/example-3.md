# Example 3 — Tenant added to the permission check

## Before

The check validates the caller's role and stops there:

```js
app.patch('/projects/:id', requirePermission('projects:write'), async (req, res) => {
  const project = await db.projects.findById(req.params.id);
  await db.projects.update(project.id, req.body); // tenant A's admin edits tenant B's project
  res.json(project);
});
```

An admin of tenant A who learns or guesses a tenant B project ID can edit
it. The role is real; the scope is missing.

## After

The tenant is part of every check and every query. The record is loaded
inside the caller's tenant scope, so a foreign ID simply does not resolve:

```js
app.patch('/projects/:id', requirePermission('projects:write'), async (req, res) => {
  const tenantId = req.session.user.tenantId; // from the server-side record
  const project = await db.projects.findOne({ id: req.params.id, tenantId });
  if (!project) return res.status(404).end(); // foreign and missing look identical

  await db.projects.update(project.id, sanitize(req.body));
  res.json(await db.projects.findOne({ id: project.id, tenantId }));
});
```

Role grants rights inside one tenant context, never across tenants — and
the scoping lives in the data access, so a future handler cannot forget it.

Note: corrects BE-126 — tenant scope is part of the authorization check, not an assumption behind it.
