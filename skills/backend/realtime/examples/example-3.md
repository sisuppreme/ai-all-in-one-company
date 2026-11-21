# Example 3 — Presence counted from real connections

## Before

The "watching now" figure is a random walk rendered in the client. It
moves whether or not anyone is connected, and two visitors see different
numbers:

```js
// client
let viewers = 47;
setInterval(() => {
  viewers += Math.floor(Math.random() * 7) - 3;
  el.textContent = `${viewers} watching now`;
}, 2000);
```

## After

Presence is a server-side registry of live connections, maintained by
connect, heartbeat, and close — and broadcast as an event like any other:

```js
const presence = new Map(); // channel -> Set<connectionId>

function joinPresence(channel, connId) {
  if (!presence.has(channel)) presence.set(channel, new Set());
  presence.get(channel).add(connId);
  publishPresence(channel);
}

function leavePresence(channel, connId) {
  presence.get(channel)?.delete(connId);
  publishPresence(channel);
}

function publishPresence(channel) {
  const count = presence.get(channel)?.size ?? 0;
  bus.publish(channel, { type: 'presence', count }); // every client sees the same number
}

// on connect:    joinPresence(channel, conn.id)
// on heartbeat timeout or close: leavePresence(channel, conn.id)
```

Open the page in two browsers: both show 2. Close one: both show 1. The
number is the system describing itself, not decorating itself.

Note: corrects BE-210 — live indicators derive from real connection and event state, never from timers.
