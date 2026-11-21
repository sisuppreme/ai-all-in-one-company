# Example 2 — Retry double-send replaced by idempotent dispatch

## Before

```js
// The dispatch job sends unconditionally. When the worker retries
// after a timeout, the user gets the same push again — once per retry.
queue.process("notification.dispatch", async (job) => {
  const n = await db.notifications.findById(job.data.notificationId);
  await push.send(n.deviceToken, { title: n.title, body: n.body });
});
```

## After

```js
// Dispatch is keyed on the event: a deliveries row per
// (notification, channel) is claimed before sending, so a retry
// finds the claim and stops instead of sending a duplicate.
queue.process("notification.dispatch", async (job) => {
  const n = await db.notifications.findById(job.data.notificationId);
  const claimed = await db.deliveries.claim({
    notificationId: n.id,
    channel: "push",
    idempotencyKey: `${n.eventId}:${n.userId}:push`,
  });
  if (!claimed) return; // already sent or in flight — do not send again
  const response = await push.send(n.deviceToken, { title: n.title, body: n.body });
  await db.deliveries.complete(claimed.id, { providerResponse: response });
});
```

Note: the slop version re-sent on every retry; the corrected version claims a keyed delivery record before sending, so one event yields one notification per recipient per channel — BE-263.
