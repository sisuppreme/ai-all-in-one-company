# notifications

## Metadata

- **Owner department:** D4 Backend & APIs (BE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Firebase Cloud Messaging documentation, https://firebase.google.com/docs/cloud-messaging
- **Depends on:** queues-jobs, api-building
- **Feeds into:** transactional-email (D11, email/SMS mechanics), admin-tools

## When to use / Do NOT use

- **Use when:** a product event must reach a user — in-app inbox entries, push notifications (FCM/APNs, web push) — or when token handling, preferences, or dispatch reliability are in question.
- **Do NOT use when:** the channel is transactional email or SMS mechanics (sending infrastructure, templates, provider setup) — that is D11's transactional-email and sms skills, consumed through the same event. This skill owns push and in-app only.

## Rules

1. **BE-261 — Record first.** A domain event creates the notification record before anything is sent. The in-app inbox row is the source of truth; channel dispatch reads from it, never from the raw event alone.
2. **BE-262 — Dispatch from a queue.** Channel sends run as queued jobs. A provider call never executes synchronously inside the request or event that triggered the notification.
3. **BE-263 — Idempotent dispatch.** One event produces at most one notification per recipient per channel. Dispatch is keyed on the event ID, so retries and redeliveries cannot double-notify.
4. **BE-264 — Preferences at dispatch time.** Opt-outs and channel preferences are checked when the dispatch job runs, not when the event fires. A preference changed in between is honored.
5. **BE-265 — Every notification deep-links.** Each notification carries a link to the object it concerns. A notification that lands the user nowhere useful is unfinished work.
6. **BE-266 — Token lifecycle.** Device tokens are stored per user and per device. Tokens a provider reports as invalid are pruned on that feedback, tokens rotate on re-registration, and tokens are removed when a user logs out on a shared device.
7. **BE-267 — Sends leave records.** Every send records the provider's response (accepted, rejected, error) against the notification record. A send with no recorded outcome did not verifiably happen.
8. **BE-268 — Classes are written down.** Each notification type is classified as critical (security, billing) or ordinary. Critical types bypass marketing opt-outs but never a user's channel-blocking rights; the classification lives in one written table.
9. **BE-269 — Read state persists.** Inbox read and unread state is stored per user on the server and survives reloads and device changes.
10. **BE-270 — No staged content.** Inbox content is generated only by real events for that user. A new account's inbox is empty, apart from a clearly labeled welcome message.

## BAN list

- **BAN-BE-131 — The staged inbox.** Banned: rendering a hardcoded list of notifications that no real event generated. Defeats: DET-FAKE-013. Bad: every brand-new account's bell shows "John liked your post" and "Your plan expires soon" from a constants file. Instead: records created by real events only; a new account starts empty (BE-261, BE-270). Severity: BLOCK.
- **BAN-BE-132 — The in-request send.** Banned: calling a push or messaging provider synchronously inside the triggering request, with no queue and no failure path. Defeats: DET-CODE-006. Bad: checkout hangs for eight seconds on a slow push provider, then errors after the order already saved. Instead: write the record, enqueue dispatch, return (BE-261, BE-262). Severity: BLOCK.
- **BAN-BE-133 — The double notify.** Banned: dispatch that can deliver the same event's notification more than once because sends are not keyed to the event. Defeats: DET-CODE-030. Bad: a retried job sends three identical "Payment received" pushes. Instead: idempotency key of event ID + recipient + channel, checked before every send (BE-263). Severity: BLOCK.
- **BAN-BE-134 — The immortal token.** Banned: ignoring provider invalid-token responses so dead tokens accumulate and send failures vanish unrecorded. Defeats: DET-CODE-005. Bad: the provider returns NotRegistered for months of sends; nothing logs it and nothing prunes the token. Instead: record every provider response and prune invalid tokens on feedback (BE-266, BE-267). Severity: WARN.

## Gates

- **G-BE-131 — Trigger test.** Verifies: BE-261, BE-263, BE-270. Check: automated — fire the triggering event on a test account; assert exactly one inbox row exists, exactly one dispatch per enabled channel, and that a freshly created account's inbox is empty. Pass: all assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-BE-132 — Dead-token test.** Verifies: BE-266, BE-267. Check: automated — register a token, invalidate it at the provider, trigger a send; assert the failure is recorded with the provider response and the token is pruned. Pass: both hold. Fail: block shipment. Recorded in: progress.md.
- **G-BE-133 — Preference timing test.** Verifies: BE-264, BE-268. Check: automated — fire an ordinary event, opt the user out before dispatch runs, and assert no send occurs; then fire a critical (security) event and assert it is still delivered. Pass: both hold. Fail: block shipment. Recorded in: progress.md.
- **G-BE-134 — Device receipt check.** Verifies: BE-262. Check: scripted check on a test device or browser — trigger the event from a second session and confirm the push arrives while the triggering request has long finished. Pass: notification received on the device. Fail: block release of the notification feature. Recorded in: progress.md.

## Anti-patterns

- **Badge theater.** The bell badge shows a number computed from a constant, or from every notification ever sent, instead of the user's unread records. Catch it: mark all read and see whether the badge reaches zero.
- **The orphan deep link.** Notifications link to objects that can be deleted, and tapping one lands on a bare 404 with no explanation. Catch it: delete the target of a test notification and tap it.
- **The event-time snapshot.** Preferences are copied onto the event when it fires, so an opt-out recorded a minute later is silently ignored at dispatch. Catch it: compare where the preference read happens against BE-264.
- **Broadcast creep.** The per-user event pipeline gets reused for marketing blasts, skipping the consent and class checks that ordinary notifications pass through. Catch it: ask which table classified the send.

## Examples

- [Example 1 — Hardcoded bell list replaced by event-created records](examples/example-1.md) — corrects BE-261, BE-270.
- [Example 2 — Retry double-send replaced by idempotent dispatch](examples/example-2.md) — corrects BE-263.
- [Example 3 — Dead tokens kept forever replaced by provider-feedback pruning](examples/example-3.md) — corrects BE-266, BE-267.

## Recall anchors

- Record first, dispatch second — the inbox row is the truth.
- Sends run from a queue, never inside the triggering request.
- One event, one notification per recipient per channel.
- Preferences are read at dispatch time, not event time.
- Dead tokens are pruned on provider feedback, not eventually.

## Checklist

- [ ] Events create inbox records before any send (BE-261).
- [ ] Dispatch is queued and keyed on event ID (BE-262, BE-263).
- [ ] Trigger test green: one row, one send per channel, empty new inbox (G-BE-131).
- [ ] Invalid token pruned and its failure recorded (G-BE-132).
- [ ] Opt-out between event and dispatch is honored; critical class still sends (G-BE-133).
- [ ] Every notification deep-links to its object (BE-265).
- [ ] Classification table exists and covers every notification type (BE-268).
