# Example 1 — A report button that writes the record

## Before

The report dialog is a frontend ceremony. Submit shows a confirmation and
discards everything:

```js
// client only — no request is ever sent
function submitReport(itemId, reason) {
  showToast('Thanks — our team will review this.');
  closeDialog();
}
```

No record exists. Nothing can be reviewed, counted, appealed, or audited;
the feature is a promise rendered as a toast.

## After

The handler resolves the target, snapshots the content as it stands, and
persists the structured record before the reporter sees any confirmation:

```js
app.post('/reports', async (req, res) => {
  const reporter = req.session.user;
  const { targetType, targetId, category } = req.body;

  const target = await resolveTarget(targetType, targetId);
  if (!target || !canView(reporter, target)) {
    return res.status(422).json({ error: 'target_not_reportable' });
  }

  const report = await db.reports.create({
    reporterId: reporter.id,               // never disclosed to the target (BE-143)
    targetType,
    targetId: target.id,
    category,
    snapshot: snapshotOf(target),          // evidence survives later edits (BE-150)
    status: 'received',
    createdAt: new Date(),
  });

  await moderationQueue.enqueue(report);   // routed before confirmation (BE-145)
  res.status(201).json({ reportId: report.id, status: report.status });
});
```

The toast now describes something that actually happened: a record in a
queue, traceable end to end.

Note: corrects BE-141 — a report action writes the structured record before any confirmation is shown.
