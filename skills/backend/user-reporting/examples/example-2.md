# Example 2 — Severity routing at intake

## Before

Every report joins one FIFO queue in arrival order:

```js
await db.reports.create({ ...report, status: 'received' });
await queue.push(report.id); // position = arrival order, for every category
```

A child-safety report filed at 09:00 waits behind 300 spam and
"rude comment" reports filed earlier. Arrival order is treated as priority.

## After

Category sets the tier at intake, and severe tiers bypass the standard
queue entirely:

```js
const SEVERE = new Set(['child_safety', 'credible_threat', 'illegal_material']);

async function routeReport(report) {
  if (SEVERE.has(report.category)) {
    report.tier = 'escalation';
    await escalationQueue.enqueue(report);       // reviewed first, immediately
    await alerts.pageOnCall({ reportId: report.id, category: report.category });
  } else {
    report.tier = 'standard';
    await moderationQueue.enqueue(report);       // FIFO is fine within a tier
  }
  await db.reports.update(report.id, { tier: report.tier, status: 'received' });
}
```

Spam still flows in order; the reports that cannot wait never do.

Note: corrects BE-144 — severe categories route to the escalation path immediately, ahead of arrival order.
