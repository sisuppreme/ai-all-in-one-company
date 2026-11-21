# Example 2 — Channel subscription with authorization

## Before

The socket server subscribes the client to whatever channel name it asks
for. The name is the only credential:

```js
ws.on('message', (msg) => {
  const { subscribe } = JSON.parse(msg);
  bus.subscribe(subscribe, (event) => ws.send(JSON.stringify(event)));
});

// a tenant-A user sends: {"subscribe": "tenant:B:orders"}
// and receives tenant B's live order feed.
```

## After

The handshake authenticates the connection, and every subscription is
checked against the channels that identity may hold. The channel name is a
request; the server decides:

```js
const server = new WebSocketServer({
  server: httpServer,
  verifyClient: ({ req }, cb) => {
    const session = sessions.fromCookie(req.headers.cookie);
    if (!session) return cb(false, 401);              // handshake auth — BE-202
    req.user = session.user;
    cb(true);
  },
});

server.on('connection', (ws, req) => {
  const user = req.user;
  ws.on('message', (msg) => {
    const { subscribe } = JSON.parse(msg);
    if (!canSubscribe(user, subscribe)) {              // per-channel check — BE-203
      audit.denied({ actor: user.id, action: 'realtime.subscribe', target: subscribe });
      return ws.send(JSON.stringify({ error: 'channel_forbidden' }));
    }
    bus.subscribe(subscribe, (event) => ws.send(JSON.stringify(event)));
  });
});

function canSubscribe(user, channel) {
  const [tenantId] = channel.split(':').slice(1);      // "tenant:<id>:orders"
  return user.tenantId === tenantId;
}
```

The same request from tenant A is now refused and logged; tenant B's feed
stays tenant B's.

Note: corrects BE-203 — subscriptions are authorized per channel at subscribe time; a client-supplied channel name is never a grant.
