# sms

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Twilio, "Track the Message Status of Outbound Messages" — https://www.twilio.com/docs/messaging/guides/track-outbound-message-status ; Twilio A2P 10DLC registration documentation (checked 2026-11-21)
- **Depends on:** webhooks
- **Feeds into:** none

## When to use / Do NOT use

- **Use when:** a project sends SMS: delivery or account notifications, one-time passcodes, or marketing messages — sender registration, consent, sending, delivery tracking, and opt-out.
- **Do NOT use when:** the message is email (transactional-email), the channel is an in-app notification list (D4 owns the transport; D18 owns the experience), or the question is OTP abuse depth and account-security policy (D7 owns it; this skill owns the provider send and its limits).

## Rules

1. **IN-141 — Recorded opt-in before the first send.** Every send traces to an opt-in recorded for that number and that message category, with source and timestamp stored. No record, no send.
2. **IN-142 — Registered sender identity.** Messages go out from a registered identity for the destination country's regime — in the US, brand and campaign registered through The Campaign Registry via the provider (A2P 10DLC for long codes; toll-free verification and short codes are separate regimes). Identify the regime for each sending country before launch; the US pattern is dated 2026-11-21, not universal law.
3. **IN-143 — Provider send, stored message ID.** The app enqueues the message to the messaging provider and stores the returned message SID against the send record. There is no direct carrier connection and no send path that skips the provider.
4. **IN-144 — Delivery is a terminal callback state.** Each message advances queued → sent → delivered / undelivered / failed through provider status callbacks, stored per message. The provider API's acceptance response means "accepted," never "delivered."
5. **IN-145 — Suppression checked inside the send path.** The send function itself checks the suppression list before enqueueing. A caller cannot bypass opt-out by calling the provider directly, and no send path exists that skips the check.
6. **IN-146 — STOP and HELP handled and test-verified.** Opt-out and help keywords are handled by the provider configuration for the number, and the behavior is proven by a live test from a real handset before launch — not assumed from a console screenshot.
7. **IN-147 — OTP codes are single-use and expire fast.** A verification code is stored hashed, expires within minutes, and is invalidated on first successful use or when a newer code is issued for the same number and purpose.
8. **IN-148 — OTP sends and attempts are rate-limited; codes never logged.** Sends per number and verification attempts per code are capped, with lockout or backoff past the cap, to blunt toll fraud and guessing. The plaintext code appears only in the message body — never in logs, analytics events, or error reports.
9. **IN-149 — Quiet hours per recipient timezone.** Marketing and non-urgent messages are held outside the recipient's local quiet hours, computed from the recipient's timezone, not the server's. Urgent transactional messages (fraud alerts, security codes the user just requested) are exempt by category, not by sender preference.
10. **IN-150 — Categories do not share consent.** Transactional and marketing are separate categories with separate opt-ins and, where the provider supports it, separate numbers or sender registrations. A number collected for delivery updates is not a marketing list.
11. **IN-151 — Failures surface as failures.** A message that reaches undelivered or failed is recorded as such, the user-facing status mirrors the provider state, and retries are bounded and visible. A failed OTP send tells the user it failed; it never leaves a "code sent" screen hanging.
12. **IN-152 — Registration status is launch evidence.** The campaign's approved status is read from the provider (console or API) and recorded in the launch checklist before the first production send. "We submitted the registration" is not approval.

## BAN list

- **BAN-IN-071 — The simulated send.** Banned: showing "text sent" (or logging a notification as sent) without a provider call — a toast, a local row, or an in-app entry standing in for an SMS. Defeats: DET-FAKE-013. Bad: checkout inserts a `notifications` row reading "Your code is 123456" and renders "SMS sent"; no provider is ever called and no phone rings. Instead: enqueue through the provider, store the message SID, and let the callback state drive what the UI claims (IN-143, IN-144). Severity: BLOCK.
- **BAN-IN-072 — Acceptance reported as delivered.** Banned: marking a message delivered, or reporting a delivery rate, from the provider API's acceptance response instead of terminal callback states. Defeats: DET-FAKE-022. Bad: the send handler stores `status = "delivered"` when the API returns 201; the dashboard claims 100% delivery while carriers filtered a third of the traffic. Instead: the row stays at its callback-driven state, and delivery metrics count only messages whose callbacks reached `delivered` (IN-144). Severity: BLOCK.
- **BAN-IN-073 — The ignored STOP.** Banned: continuing to send to a number after it opts out, or treating opt-out as a note a human must remember to apply. Defeats: DET-FAKE-016. Bad: STOP replies land in a spreadsheet reviewed monthly; three more campaign sends go out to opted-out numbers in between, so the user's recorded preference never takes effect. Instead: the provider records the opt-out, the number enters the suppression list immediately and permanently for the category, and the send path checks it on every send (IN-145, IN-146). Severity: BLOCK.
- **BAN-IN-074 — The any-code verification.** Banned: an OTP check that accepts any code, a fixed code, or a code compared only in client-side code. Defeats: DET-FAKE-001. Bad: the verify endpoint returns success for `000000` in the staging build that shipped, and the "check" in production compares against a value bundled in the app. Instead: the server compares the submitted code against the stored hash, enforces expiry and the attempt cap, and invalidates on success (IN-147, IN-148). Severity: BLOCK.
- **BAN-IN-075 — The unregistered launch.** Banned: sending production US A2P traffic before the campaign is approved, then reporting the sends as successful while carriers block or filter them (the symptom is provider error 30034). Defeats: DET-FAKE-022. Bad: launch day sends 2,000 order texts from an unregistered long code; the API accepted them, the status page says "sent," and almost none arrive. Instead: no production send until the approved campaign status is recorded as launch evidence (IN-142, IN-152). Severity: BLOCK.

## Gates

- **G-IN-071 — Status-callback terminal-state test.** Verifies: IN-143, IN-144. Check: automated — send to a test number through the real provider path and poll the send record until it reaches a terminal state; assert the terminal state was written by the callback handler (state history shows queued → sent → delivered with callback timestamps), not by the send call. Pass: the record reaches `delivered` via callbacks only. Fail: block shipment. Recorded in: progress.md.
- **G-IN-072 — Opt-out drill.** Verifies: IN-145, IN-146. Check: automated — from a test handset, reply STOP; assert the number appears on the suppression list; then attempt a send to that number through the normal send path and assert it is refused before enqueueing. Pass: suppression recorded and the send blocked. Fail: block shipment. Recorded in: progress.md.
- **G-IN-073 — OTP abuse test flow.** Verifies: IN-147, IN-148. Check: automated — request a code for a test number, then assert: the correct code verifies once and a replay of the same code fails; an expired code fails; wrong attempts past the cap are locked out; resend requests past the per-number cap are refused. Pass: all four assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-IN-074 — Plaintext-code scan.** Verifies: IN-148. Check: automated — grep application logs captured during G-IN-073 and the codebase's logging calls for the test code value and for OTP variables passed to log statements; assert stored codes are hashes (no plaintext code column value matches the sent code). Pass: zero plaintext occurrences. Fail: block shipment. Recorded in: progress.md.
- **G-IN-075 — Registration evidence check.** Verifies: IN-142, IN-152. Check: manual evidence, scriptable where the provider exposes status — read the campaign status from the provider console or API and record the status, campaign ID, and date checked in the launch checklist. Pass: status is approved for every sending country and number in use. Fail: block the launch. Recorded in: progress.md.

## Anti-patterns

- **The sandbox shrug.** "It worked in the provider sandbox" offered as delivery proof. Catch it: sandbox sends never traverse carrier filtering or registration checks; ask for the G-IN-071 callback trace on the production path.
- **Acceptance-rate vanity.** Reporting messages accepted by the API divided by messages attempted as the "delivery rate." Catch it: recompute from terminal callback states only (IN-144); the gap between the two numbers is the finding.
- **Server-time quiet hours.** The hold window computed in the server's timezone, so "quiet hours" protect the data center's night, not the recipient's. Catch it: pick a test number in a timezone several hours from the server's and check when a queued marketing send releases (IN-149).
- **One number, every purpose.** OTPs, receipts, and promotions all leave from the same long code to save setup time. Catch it: a marketing complaint or filtering problem on that number now takes login codes down with it; categories get separate registrations (IN-150).

## Examples

- [Example 1 — Replacing a simulated send with a provider send](examples/example-1.md) — corrects IN-143.
- [Example 2 — Replacing acceptance-as-delivered with callback terminal states](examples/example-2.md) — corrects IN-144.
- [Example 3 — Replacing a reusable, logged OTP with a hashed, expiring, rate-limited one](examples/example-3.md) — corrects IN-147.

## Recall anchors

- No recorded opt-in, no send — per number, per category.
- The API said "accepted"; only the callback can say "delivered."
- STOP is enforced inside the send path, not remembered by a human.
- A code is hashed, single-use, expiring, rate-limited — and never logged.
- Registration approved is launch evidence, not a hope.

## Checklist

- [ ] Every send traces to a recorded opt-in for that number and category (IN-141).
- [ ] Sender registration approved and recorded for each sending country (IN-142, G-IN-075).
- [ ] Sends go through the provider and store the message SID (IN-143).
- [ ] Message status advances only via callbacks to a terminal state (IN-144, G-IN-071).
- [ ] STOP drill passes: suppression recorded and a later send refused in the send path (IN-145, G-IN-072).
- [ ] OTP flow passes expiry, single-use, attempt-cap, and resend-cap tests (IN-147, IN-148, G-IN-073).
- [ ] No plaintext code appears in logs or storage (G-IN-074).
- [ ] Marketing sends respect quiet hours in the recipient's timezone (IN-149).
