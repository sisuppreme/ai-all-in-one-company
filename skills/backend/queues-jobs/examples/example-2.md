# Example 2 — A retry policy and DLQ for webhook delivery

## Before

The queue is created with no options. BullMQ's defaults apply: one attempt,
no backoff, and a failed job is just a log line:

```js
const webhookQueue = new Queue('webhooks');
await webhookQueue.add('deliver', { webhookId, eventId });
// a 500 from the receiver, a DNS hiccup, a restart — delivery is simply lost
```

## After

The job type is registered with an explicit policy: bounded attempts,
exponential backoff with jitter, permanent failures routed straight to the
dead-letter queue, and the DLQ itself alerted and replayable:

```js
const webhookQueue = new Queue('webhooks', {
  defaultJobOptions: {
    attempts: 5,
    backoff: { type: 'exponential', delay: 5000, jitter: 0.3 },
    removeOnComplete: true,
    removeOnFail: false, // failed jobs stay inspectable — they ARE the DLQ
  },
});

new Worker('webhooks', async (job) => {
  const webhook = await db.webhooks.findById(job.data.webhookId);
  const res = await postSigned(webhook.url, job.data.eventId);
  if (res.status >= 400 && res.status < 500) {
    // permanent: the receiver rejects this payload — retrying cannot help
    throw new UnrecoverableError(`receiver returned ${res.status}`);
  }
  if (!res.ok) throw new Error(`receiver returned ${res.status}`);
});

webhookQueue.on('failed', (job, err) => {
  if (job.attemptsMade >= job.opts.attempts || err instanceof UnrecoverableError) {
    alerts.fire({ type: 'webhook.dlq', jobId: job.id, reason: err.message });
    // replay: an operator fixes the receiver and re-queues from the DLQ view
  }
});
```

A transient failure retries; a permanent one parks, alerts, and waits for a
human — neither disappears.

Note: corrects BE-183 — max attempts, backoff, and permanent-failure classes are declared, never left to library defaults.
