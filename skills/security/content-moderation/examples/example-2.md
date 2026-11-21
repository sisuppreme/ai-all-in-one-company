# Example 2 — Classifier flag without an auto-ban

Demonstrates SE-263: automated detection may queue, label, and reduce visibility, but a ban requires a human decision.

## Before

```ts
// Classifier output wired straight to irreversible enforcement
onClassifierResult(async (post, score) => {
  if (score >= 0.9) {
    await db.posts.delete(post.id);
    await db.users.update(post.authorId, { banned: true });
  }
});
```

A false positive — quoted speech, a reclaimed slur, a news photo — permanently bans a user with no human review, no evidence record, and nothing meaningful to appeal.

## After

```ts
// Classifier output feeds the same queue as user reports
onClassifierResult(async (post, score, signals) => {
  if (score >= 0.9) {
    await db.posts.update(post.id, { visibility: "reduced" }); // reversible
    await db.moderationQueue.insert({
      targetType: "post",
      targetId: post.id,
      category: "classifier-flag",
      clauseId: signals.topClauseId,
      tier: 2,
      reporterId: null, // automated source
      evidence: { score, signals },
      status: "pending",
    });
  }
});

// The ban rung exists only behind a human decision in the queue
async function decideBan(queueItemId: string, moderatorId: string) {
  const item = await db.moderationQueue.get(queueItemId);
  await db.transaction(async (tx) => {
    await tx.users.update(item.targetAuthorId, { banned: true });
    await tx.actionLog.insert({
      actor: moderatorId,
      clauseId: item.clauseId,
      action: "ban",
      evidenceRef: item.id,
      createdAt: new Date(),
    });
  });
}
```

Visibility reduction is reversible, the flag carries its evidence into the queue, and the ban itself is a logged human decision the user can appeal.
