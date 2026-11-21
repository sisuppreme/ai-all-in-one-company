# Example 2 — Stub endpoint replaced by a real write path

## Before

```ts
app.post("/support/messages", async (req, res) => {
  // TODO: wire up storage later
  console.log("support message:", req.body);
  res.status(200).json({ ok: true, message: "Message sent" });
});
```

The form reports "Message sent," the network tab shows a request, and the
message is gone forever — nothing persists it and no one can retrieve it.
This is a stub presented as a finished endpoint.

## After

```ts
app.post("/support/messages", requireAuth, async (req, res) => {
  const parsed = supportMessageSchema.safeParse(req.body);
  if (!parsed.success) {
    return res.status(422).json(validationProblem(parsed.error));
  }

  const message = await db.supportMessages.create({
    data: {
      userId: req.user.id, // from the session, never from the body
      subject: parsed.data.subject,
      body: parsed.data.body,
      status: "open",
    },
  });

  await queue.add("notify-support", { messageId: message.id });
  res.status(201).json({ id: message.id, status: message.status });
});
```

The submission is validated, written to the store in the same request, and
retrievable by support staff; the notification is a queued job, not a
blocking call. Success is now backed by a record that survives reload.

Note: corrects BE-002 — a write endpoint is done only when its effect persists and is visible from a second session; a success response alone is not evidence.
