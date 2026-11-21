# realtime

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** MDN, "EventSource" (SSE, Last-Event-ID) — https://developer.mozilla.org/en-US/docs/Web/API/EventSource ; MDN, "WebSocket" — https://developer.mozilla.org/en-US/docs/Web/API/WebSocket
- **Depends on:** backend-auth, queues-jobs
- **Feeds into:** notifications, frontend-state

## When to use / Do NOT use

- **Use when:** the product must push changes to clients as they happen — status feeds, notifications, progress, chat, collaboration, presence — and the transport, authentication, and reconnect behavior are being designed.
- **Do NOT use when:** data changes rarely and a fetch on view is honest; not everything deserves a socket. Do not present polling as a realtime implementation — polling is a labeled degraded fallback (BE-211), never the design.

## Rules

1. **BE-201 — Transport matches direction.** Server→client streams (feeds, notifications, progress) use server-sent events. Bidirectional traffic (chat, collaboration) uses WebSocket. The choice is recorded with its reason.
2. **BE-202 — Authenticate at the handshake.** Connections authenticate during the handshake, with the session cookie or a short-lived token. A long-lived credential never appears in a connection URL, where it would be logged and shared.
3. **BE-203 — Authorize per channel.** A client may subscribe only to channels its identity is authorized for, checked at subscribe time. Tenant channels are scoped to the tenant; a client-supplied channel name is a request, not a grant.
4. **BE-204 — Re-check on change.** When a user's permissions or tenant membership change, their live subscriptions are re-evaluated and unauthorized channels are dropped. Connecting once does not grant a stream forever.
5. **BE-205 — Events carry IDs.** Every event has an ID and a per-channel sequence number, so a reconnecting client can prove exactly what it missed.
6. **BE-206 — Reconnect is part of the protocol.** Clients reconnect with exponential backoff and jitter, then catch up from the last event ID (e.g. `Last-Event-ID`) or receive an explicit resync signal. A silent gap is a defect.
7. **BE-207 — Heartbeats both ways.** Connections heartbeat on an interval; peers that stop answering are detected and closed, so presence and fan-out never target ghosts.
8. **BE-208 — A backplane beyond one instance.** Once more than one instance serves traffic, fan-out runs through a pub/sub backplane (for example Redis). Per-process subscription memory is a single-instance trap.
9. **BE-209 — Backpressure is capped.** Slow consumers get a bounded buffer. Past the cap, the consumer is dropped with a resync signal — never allowed to grow server memory without limit.
10. **BE-210 — Live means live.** Presence, typing indicators, and "live" figures derive from real connection and event state. Nothing time-based or randomized renders as live.
11. **BE-211 — The degraded mode is designed.** On hosts that restrict long-lived connections, the fallback (SSE-only, then polling) is implemented, labeled in the UI as delayed where it is, and tested — not improvised during an outage.

## BAN list

- **BAN-BE-101 — Polling dressed as realtime.** Banned: a `setInterval` poll presented to users as "real-time" or "live" sync. Defeats: DET-FAKE-022. Bad: the client fetches `/status` every five seconds while the UI badge reads "Live — synced"; between polls the badge lies, and with the tab throttled it lies for minutes. Instead: push over SSE or WebSocket (BE-201); if polling is the fallback, label the state "delayed" (BE-211). Severity: BLOCK.
- **BAN-BE-102 — Timer-driven live indicators.** Banned: viewer counts, presence dots, or "someone is typing" rendered from timers or random drift with no connection or event source behind them. Defeats: DET-FAKE-018. Bad: the "128 watching now" figure random-walks between 40 and 60 on an empty stream. Instead: derive every live indicator from the connection registry and real events (BE-210). Severity: BLOCK.
- **BAN-BE-103 — Unauthenticated connections.** Banned: accepting a socket or SSE connection with no handshake authentication, or carrying a long-lived API key in the connection URL. Defeats: DET-CODE-020. Bad: `wss://app.example.com/feed?key=sk-live-…` connects for anyone holding the link, and the key sits in proxy logs. Instead: authenticate at the handshake with the session cookie or a short-lived, single-purpose token (BE-202). Severity: BLOCK.
- **BAN-BE-104 — Open channel subscription.** Banned: honoring any client-supplied channel name without an authorization check, so any client can subscribe to another tenant's stream. Defeats: DET-FAKE-021. Bad: a tenant-A user subscribes to `tenant:B:orders` and watches a competitor's order feed in real time. Instead: check the subscription against the identity's authorized channels at subscribe time (BE-203). Severity: BLOCK.

## Gates

- **G-BE-101 — Two-session live update test.** Verifies: BE-201, BE-210. Check: automated — open two authenticated sessions; perform an action in one and assert the other reflects it via the realtime channel, with no refresh and no polling requests in the network log. Pass: the update arrives over the stream. Fail: block shipment. Recorded in: progress.md.
- **G-BE-102 — Drop-and-reconnect test.** Verifies: BE-205, BE-206. Check: automated — connect, note the last event ID, force a disconnect, emit three events, reconnect. Pass: the client receives exactly the three missed events, or one explicit resync — no gaps, no duplicates. Fail: block shipment. Recorded in: progress.md.
- **G-BE-103 — Connection authorization test.** Verifies: BE-202, BE-203. Check: automated — attempt a connection with no credentials, with expired credentials, and subscribe a tenant-A client to a tenant-B channel. Pass: all three rejected. Fail: block shipment. Recorded in: progress.md.
- **G-BE-104 — Slow-consumer test.** Verifies: BE-209. Check: automated — connect a client that never reads, publish past the buffer cap, and observe. Pass: the server drops the consumer with a resync signal and server memory stays bounded. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Broadcast everything.** Every event goes to every connection and clients filter locally — other tenants' activity crosses the wire to anyone listening. Catch it: inspect one client's received frames for events outside its channels.
- **The immortal connection.** No heartbeat, so dead clients hold presence and subscriptions forever. Catch it: kill a client without closing it cleanly; if presence still shows it an hour later, heartbeats are missing (BE-207).
- **Reconnect without memory.** The client reconnects and simply starts from "now", silently losing everything in between. Catch it: read the reconnect path — no last-event ID and no resync request is the tell (BE-206).
- **Single-instance amnesia.** Realtime works perfectly in development, then production splits into per-instance islands where half the users see nothing. Catch it: check for the backplane in the deployment configuration, not in the demo (BE-208).

## Examples

- [Example 1 — An SSE status feed with Last-Event-ID catch-up](examples/example-1.md) — corrects BE-206.
- [Example 2 — Channel subscription with authorization](examples/example-2.md) — corrects BE-203.
- [Example 3 — Presence counted from real connections](examples/example-3.md) — corrects BE-210.

## Recall anchors

- Direction picks the transport: SSE one-way, WebSocket two-way.
- Authenticate at the handshake; authorize every channel.
- Events carry IDs; reconnect means catch up or resync — never a gap.
- Presence is connection state, not a timer.
- Past one instance, fan-out needs a backplane.

## Checklist

- [ ] The transport matches the traffic direction; polling is only a labeled fallback (BE-201).
- [ ] Two-session test: updates arrive over the stream, with no polling (G-BE-101).
- [ ] Drop-and-reconnect: no missed or duplicated events (G-BE-102).
- [ ] Unauthenticated, expired, and cross-tenant attempts are all rejected (G-BE-103).
- [ ] A slow consumer is dropped with a resync signal; memory stays bounded (G-BE-104).
- [ ] Live indicators read connection and event state only (BE-210).
- [ ] A pub/sub backplane is configured wherever more than one instance runs (BE-208).
