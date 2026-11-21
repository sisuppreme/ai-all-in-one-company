# Example 3 — Logged enforcement with a real appeal

Demonstrates SE-266 and SE-267: every action records actor, clause, evidence, and timestamp, and the appeal reaches a different reviewer.

## Before

```ts
// Admin button deletes the post; nothing is recorded, no appeal exists
app.post("/admin/posts/:id/delete", requireAdmin, async (req, res) => {
  await db.posts.delete(req.params.id);
  res.json({ ok: true });
});
```

Afterward nobody can say who removed the post, under which rule, or on what evidence — and the author gets a generic "content removed" message with no way to contest it.

## After

```ts
// Removal writes its justification in the same transaction as the action
app.post("/admin/queue/:id/decide", requireModerator, async (req, res) => {
  const item = await db.moderationQueue.get(req.params.id);
  const { action } = DecideSchema.parse(req.body); // label | reduce | remove | suspend | ban

  await db.transaction(async (tx) => {
    await tx.enforcement.apply(item.targetType, item.targetId, action);
    const logEntry = await tx.actionLog.insert({
      actor: req.user.id,
      clauseId: item.clauseId,
      action,
      evidenceRef: item.id,
      createdAt: new Date(),
    });
    await tx.notifications.insert({
      userId: item.targetAuthorId,
      kind: "enforcement",
      body: `Your content was actioned under policy clause ${item.clauseId}.`,
      appealUrl: `/appeals/${logEntry.id}`, // appeal is decided by a different reviewer
    });
  });
  res.json({ ok: true });
});

// Appeal assignment excludes the original decision-maker
async function assignAppeal(actionLogId: string) {
  const original = await db.actionLog.get(actionLogId);
  const reviewer = await db.moderators.nextAvailableExcept(original.actor);
  await db.appeals.insert({ actionLogId, assignedTo: reviewer.id, status: "pending" });
}
```

The removal is defensible (actor, clause, evidence, timestamp), the author learns the actual outcome and gets a working appeal link, and the appeal is routed away from the person who made the original call.
