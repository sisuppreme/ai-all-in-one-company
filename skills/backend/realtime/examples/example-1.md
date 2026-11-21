# Example 1 — An SSE status feed with Last-Event-ID catch-up

## Before

"Live" order status is a five-second poll, and anything that happens
between polls — or while the tab is throttled — is simply never shown
until the next fetch happens to land:

```js
// client
setInterval(async () => {
  const res = await fetch(`/orders/${id}/status`);
  renderStatus(await res.json());
}, 5000);
```

## After

The server streams status events over SSE. Each event carries its ID; the
browser's EventSource automatically sends `Last-Event-ID` on reconnect,
and the server replays what was missed from its event log:

```js
// server
app.get('/orders/:id/events', async (req, res) => {
  await authorizeOrderAccess(req.session.user, req.params.id); // BE-203

  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    Connection: 'keep-alive',
  });

  const lastId = Number(req.headers['last-event-id'] ?? 0);
  for (const e of await db.orderEvents.since(req.params.id, lastId)) {
    res.write(`id: ${e.id}\ndata: ${JSON.stringify(e)}\n\n`); // catch-up — BE-206
  }

  const unsubscribe = bus.subscribe(`order:${req.params.id}`, (e) => {
    res.write(`id: ${e.id}\ndata: ${JSON.stringify(e)}\n\n`);
  });
  const heartbeat = setInterval(() => res.write(': hb\n\n'), 25000); // BE-207

  req.on('close', () => { clearInterval(heartbeat); unsubscribe(); });
});

// client
const feed = new EventSource(`/orders/${id}/events`);
feed.onmessage = (msg) => renderStatus(JSON.parse(msg.data));
```

Kill the connection mid-delivery and reconnect: the missed events arrive
in order, exactly once, and the client never polls.

Note: corrects BE-206 — reconnect is part of the protocol: backoff, then catch up from the last event ID or resync explicitly.
