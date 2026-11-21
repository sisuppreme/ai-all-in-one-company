# Example 1 — Report intake that reaches a queue

Demonstrates SE-262 (and BAN-SE-131): a report must create a queue row in a staffed queue, not vanish into an inbox.

## Before

```ts
// Report button handler — sends an email nobody is assigned to read
app.post("/reports", async (req, res) => {
  await mailer.send({
    to: "reports@example.com",
    subject: `Report: ${req.body.category}`,
    text: JSON.stringify(req.body),
  });
  res.status(201).json({ ok: true, message: "Report received" });
});
```

The user sees "Report received," but no queue row exists, no one owns the inbox, there is no priority tier, no response target, and no record to appeal or audit.

## After

```ts
// Report button handler — writes a queue row mapped to a policy clause
app.post("/reports", async (req, res) => {
  const { targetType, targetId, category } = ReportSchema.parse(req.body);
  const clause = POLICY_CLAUSES[category]; // category must map 1:1 to a clause
  if (!clause) return res.status(422).json({ error: "Unknown report category" });

  const row = await db.moderationQueue.insert({
    targetType,
    targetId,
    category,
    clauseId: clause.id,
    tier: clause.defaultTier, // tier 1 = imminent harm / illegal content
    reporterId: req.user.id,
    status: "pending",
    createdAt: new Date(),
  });
  res.status(201).json({ ok: true, trackingId: row.id });
});
```

The report now lands in the tiered queue with the policy clause attached, a tracking ID the reporter can reference, and a response target the SLA gate (G-SE-133) can measure.
