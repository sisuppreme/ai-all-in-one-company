# Example 1 — Hardcoded bell list replaced by event-created records

## Before

```js
// The bell renders the same staged list for every account, including
// accounts created a second ago. No event ever created these.
const NOTIFICATIONS = [
  { id: 1, text: "John liked your post", read: false },
  { id: 2, text: "Your plan expires soon", read: false },
  { id: 3, text: "You have 3 new followers", read: false },
];

app.get("/api/notifications", requireAuth, (req, res) => {
  res.json(NOTIFICATIONS);
});
```

## After

```js
// A domain event creates the record first; the inbox reads real,
// per-user records; dispatch is enqueued from the same transaction.
async function onPostLiked({ postId, likerId }) {
  const post = await db.posts.findById(postId);
  if (post.ownerId === likerId) return; // never notify about your own action
  const record = await db.notifications.create({
    userId: post.ownerId,
    type: "post.liked",
    eventId: `post.liked:${postId}:${likerId}`,
    deepLink: `/posts/${postId}`,
    read: false,
  });
  await queue.add("notification.dispatch", { notificationId: record.id });
}

app.get("/api/notifications", requireAuth, async (req, res) => {
  const rows = await db.notifications.listForUser(req.user.id);
  res.json(rows); // a new account gets an empty list, honestly
});
```

Note: the slop version staged the same fabricated feed for everyone; the corrected version creates a stored record per real event and reads only that user's records — BE-261, BE-270.
