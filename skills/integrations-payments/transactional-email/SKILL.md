# transactional-email

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Amazon SES, "Complying with DMARC authentication protocol in Amazon SES" — https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dmarc.html ; RFC 7208 (SPF) — https://www.rfc-editor.org/rfc/rfc7208 ; RFC 6376 (DKIM) — https://www.rfc-editor.org/rfc/rfc6376 ; RFC 7489 (DMARC) — https://www.rfc-editor.org/rfc/rfc7489 ; RFC 8058 (one-click unsubscribe) — https://www.rfc-editor.org/rfc/rfc8058
- **Depends on:** webhooks (provider delivery, bounce, and complaint events), api-keys-management (provider credentials)
- **Feeds into:** payments (receipts), subscriptions (billing notices), dunning (failed-payment mail), backend-auth (verification and reset mail)

## When to use / Do NOT use

- **Use when:** the product sends mail a user is waiting for because of something they just did — receipts, email verification, password resets, account and security notices, order and billing confirmations.
- **Do NOT use when:** the message is marketing or lifecycle mail — onboarding sequences, win-back, newsletters, promotional content of any kind. That is D9's lifecycle-email skill, sent on a separate stream under its own consent rules. This skill owns transactional streams only; the boundary is crossed deliberately, in a design decision, never by drift.

## Rules

1. **IN-121 — Authenticate the sending domain before the first send.** The dedicated sending subdomain publishes SPF and DKIM records aligned with the visible From: domain, plus a DMARC record that starts at `p=none` monitoring and progresses to enforcement. Alignment is proven in the `Authentication-Results` header of a real test send, not assumed from DNS records existing.
2. **IN-122 — Transactional and marketing mail use separate subdomains and streams.** A marketing reputation problem must never be able to take password resets down with it; no configuration shares a stream between the two.
3. **IN-123 — Send through a provider, as a background job.** The request handler enqueues a message with a template ID and its data; a worker sends via the email provider. No mail is sent inline in a web request, and none leaves from the app server's own SMTP.
4. **IN-124 — "Email sent" means provider-accepted, with the message ID stored.** The UI may claim a message was sent only after the provider accepts it and the returned message ID is written to the message row. Anything earlier is "sending," and a failed enqueue is an error the user sees.
5. **IN-125 — Delivery outcomes are recorded per message.** Provider delivered / bounced / complaint events return by webhook and are stored against the message row, so "did the reset email arrive" is a database query, never a guess or a support shrug.
6. **IN-126 — Bounces and complaints suppress automatically.** A hard bounce or a spam complaint adds the address to the suppression list inside the send path; no later send to that address leaves until the suppression is deliberately cleared. Re-mailing a hard-bounced address damages the domain for every user.
7. **IN-127 — Templates are versioned in the repo and ship with a plain-text part.** Every transactional template names the action it confirms or requests, the expiry where one applies, and the "this wasn't you" path. Template changes go through the same review as code.
8. **IN-128 — Templates render with tested fallbacks.** Every variable has a defined fallback for missing data; a rendered message never contains a raw template token, an empty gap, or the word "undefined". A seed-send with full and with empty data proves this before a template ships.
9. **IN-129 — Codes and links are single-use, expiring, and rate-limited.** Verification codes and reset links work once, expire on a stated clock, and are rate-limited at both send and confirm. D7 owns the security depth; this skill owns that the mechanism exists and is wired to the real send.
10. **IN-130 — Receipts and confirmations render from the stored, provider-confirmed record.** Amounts, items, and references in a receipt email come from the payment record the provider confirmed — never from template sample data, client-submitted values, or a recomputation that can drift.
11. **IN-131 — Transactional templates carry no marketing content.** No promotional block, cross-sell, or engagement bait in a transactional template: it reclassifies the stream, breaks the consent boundary with lifecycle-email, and trains filters to treat resets as bulk mail.
12. **IN-132 — A promised email that never arrives is a product defect.** Any flow that tells a user to check their inbox is verified end-to-end for arrival before launch, and failed sends retry with backoff into a visible dead-letter state — a silently dropped send is a defect, not an acceptable loss.

## BAN list

- **BAN-IN-061 — Reset toast with nothing behind it.** Banned: showing "Reset link sent" while no provider is called and no token exists. Defeats: DET-FAKE-020. Bad: the forgot-password handler renders a success toast and writes nothing; no email ever leaves. Instead: enqueue a real send through the authenticated provider carrying a single-use, expiring token, and store the message ID (IN-123, IN-124, IN-129). Severity: BLOCK.
- **BAN-IN-062 — The staged "we emailed you" state.** Banned: notification or account state claiming an email was sent when the send is a stub, a log line, or a fixture. Defeats: DET-FAKE-013. Bad: signup marks the account "verification email sent" while the mailer is a console-log stub left from development. Instead: the state is set only from the provider-acceptance record, and delivery advances only from provider events (IN-124, IN-125). Severity: BLOCK.
- **BAN-IN-063 — "Delivered" copied from the send response.** Banned: marking a message delivered because the provider's send API returned success. Defeats: DET-FAKE-022. Bad: the message row flips to `delivered` in the same call that enqueues it; bounces are never seen because nobody reads the events. Instead: acceptance records `accepted` with the message ID; only a provider delivery event records `delivered`, and bounce/complaint events record their own states (IN-125). Severity: BLOCK.
- **BAN-IN-064 — Receipt email rendered from sample data.** Banned: a receipt or invoice email whose amounts or items come from template placeholders or example data rather than the confirmed charge. Defeats: DET-FAKE-019. Bad: the receipt template ships with a hardcoded "$49.00 — Pro plan" body that real customers receive after paying a different amount. Instead: render every figure from the stored provider-confirmed payment record (IN-130). Severity: BLOCK.
- **BAN-IN-065 — Verification that verifies nothing.** Banned: an email-verification step that accepts any code, or marks the address verified without the code check passing. Defeats: DET-FAKE-003. Bad: the confirm endpoint accepts any six digits so testers can get through, and the shortcut ships. Instead: the code is server-issued, single-use, and expiring; the account stays in a pending state until the real check passes (IN-129). Severity: BLOCK.

## Gates

- **G-IN-061 — Authentication check.** Verifies: IN-121, IN-122. Check: automated — query DNS (`dig +short TXT <sending-subdomain>`, the DKIM selector record, and `dig +short TXT _dmarc.<sending-subdomain>`), then send a test message and assert its `Authentication-Results` header shows SPF, DKIM, and DMARC all passing and aligned with the visible From: domain, on a subdomain separate from the marketing stream. Pass: all three pass and align. Fail: block launch; no transactional mail ships from an unauthenticated domain. Recorded in: progress.md. Simulated-provider provision (pre-provisioning): where no production sending domain or provider account exists yet, the DNS queries and header assertions run against a simulated sending setup — a test domain whose DNS records the project controls, configured exactly as the production subdomain will be, with the test send routed through it; the result is recorded as simulated in progress.md and in the product's own documentation, verification against the production sending domain remains required before launch, and simulated results must never be presented as real in any user-facing surface (Real Content Rule).
- **G-IN-062 — Seed-send token scan.** Verifies: IN-127, IN-128. Check: automated — send every transactional template to seed inboxes twice, once with complete data and once with empty optional data, and grep the rendered text and HTML parts for `{{`, `}}`, `undefined`, and `null`. Pass: zero unrendered tokens or placeholder artifacts in any rendering. Fail: block the template release. Recorded in: progress.md.
- **G-IN-063 — Bounce and suppression drill.** Verifies: IN-125, IN-126. Check: automated — send to the provider's bounce-simulator address; assert the message row records the bounce event and the address appears on the suppression list; then attempt a second send to the same address and assert the send path refuses it. Pass: bounce recorded, address suppressed, second send blocked. Fail: block launch. Recorded in: progress.md.
- **G-IN-064 — End-to-end arrival test.** Verifies: IN-123, IN-124, IN-132. Check: automated in staging — complete the signup and password-reset flows; assert a message row exists with a provider message ID and reaches the delivered state via provider events, and that completing the reset actually changes the credential (the old password fails, the new one works). Pass: both flows arrive and the reset takes effect. Fail: block launch. Recorded in: progress.md. Simulated-provider provision (pre-provisioning): where no provider account exists yet, a local simulated provider — a mail double that issues provider-style message IDs, emits delivery events, and captures the messages — stands in for the provider and both flows are verified against it unchanged; the result is recorded as simulated in progress.md and in the product's own documentation, the arrival test against the real provider remains required before public launch, and simulated results must never be presented as real in any user-facing surface (Real Content Rule).

## Anti-patterns

- **The fire-and-forget send.** The provider is called and its return value thrown away, so failures are invisible until a user complains. Catch it: search for send calls whose message ID is never stored.
- **The "just this once" promo block.** A marketing paragraph sneaks into a receipt for one campaign and quietly reclassifies the stream. Catch it: diff transactional templates at review and question any sentence that sells rather than confirms.
- **The console-log mailbox in production.** The development stub transport survives into the production config. Catch it: the launch checklist names the active transport explicitly; "log" or "noop" is a stop.
- **The invisible retry loop.** The worker retries a failing send forever with no cap, no dead-letter, and no alert. Catch it: queue configuration with no maximum attempts or dead-letter destination is unfinished work.

## Examples

- [Example 1 — The reset email that was never sent](examples/example-1.md) — violates/corrects IN-124.
- [Example 2 — "Delivered" copied from the send response](examples/example-2.md) — violates/corrects IN-125.
- [Example 3 — The receipt with sample totals](examples/example-3.md) — violates/corrects IN-130.

## Recall anchors

- "Sent" means the provider accepted it and you stored the ID.
- Delivered is an event, not an assumption.
- SPF, DKIM, DMARC — aligned, or it lands in spam.
- Transactional and marketing never share a stream.
- A promised email that never arrives is a product defect.

## Checklist

- [ ] SPF, DKIM, and DMARC verified passing and aligned on a real test send (G-IN-061).
- [ ] Transactional and marketing mail are on separate subdomains and streams (IN-122).
- [ ] Every send goes through the queue and stores its provider message ID (IN-123, IN-124).
- [ ] Delivered, bounce, and complaint events are stored against each message row (IN-125).
- [ ] Hard bounces and complaints are suppressed automatically in the send path (IN-126).
- [ ] Seed-sends with full and empty data show zero unrendered template tokens (G-IN-062).
- [ ] Signup and password-reset flows verified end-to-end for arrival in staging (G-IN-064).
