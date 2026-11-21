# Example 3 — A decision with a policy citation and closure

## Before

Closing a report is a status flip. Nothing records what was decided, why,
or under which rule:

```js
app.post('/mod/reports/:id/close', async (req, res) => {
  await db.reports.update(req.params.id, { status: 'resolved' });
  res.status(204).end();
});
```

The reporter hears nothing, the sanctioned user can appeal against a void,
and an auditor cannot distinguish a reviewed decision from a bulk cleanup.

## After

A decision is a record: action, policy clause, actor, and the two
notifications it owes — closure for the reporter, an appealable notice for
the sanctioned user:

```js
app.post('/mod/reports/:id/decide', async (req, res) => {
  const moderator = req.session.user;
  const { action, policyClause } = req.body; // e.g. 'remove' + 'Harassment §2.1'
  const report = await db.reports.findById(req.params.id);

  await enforcement.apply(report.targetType, report.targetId, action); // real effect, verified by the service
  const decision = await db.decisions.create({
    reportId: report.id,
    action,
    policyClause,
    decidedBy: moderator.id,
    decidedAt: new Date(),
  });

  await db.reports.update(report.id, { status: 'decided', decisionId: decision.id });
  await notify.reporterClosure(report.reporterId, report.id);            // decided — no detail (BE-148)
  await notify.sanctionNotice(report.targetId, { action, policyClause, appealTo: '/appeals' }); // BE-147
  res.status(201).json(decision);
});
```

Every closed report can now answer: what happened, under which policy, who
decided, and how to appeal it.

Note: corrects BE-146 — every enforcement action records the policy clause it rests on, with actor and timestamp.
