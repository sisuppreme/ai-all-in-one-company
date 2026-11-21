# lifecycle-email

## Metadata

- **Owner department:** D9 SEO & Content (CO)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://support.google.com/mail/answer/14229414 ; http://braze.com/docs/user_guide/messaging/campaigns/creating_campaign ; https://www.ftc.gov/business-center/resources/can-spam-act-compliance-guide-business
- **Depends on:** fact-sheet, real-content
- **Feeds into:** growth-experiments, web-analytics

## When to use / Do NOT use

- **Use when:** designing, editing, or auditing a behavior-triggered message program — onboarding, activation, engagement, retention, or win-back journeys across email, push, or in-app — including its authentication, consent, suppression, and measurement setup.
- **Do NOT use when:** the message is transactional (receipts, password resets, security alerts — that is D11's transactional-email skill, on its own stream), when the message is an incident or status communication (D18), or when the task is a one-off page or post (copywriting).

## Rules

1. **CO-141 — Authentication before volume.** SPF, DKIM, and an aligned DMARC record (minimum p=none) exist and verify on every sending domain before any program sends from it; no journey launches on an unauthenticated domain.
2. **CO-142 — Consent is a send-time check.** Every send verifies the profile's current opt-in status for that message type at send time; a signup-time consent memory never substitutes for the check, and an opt-out recorded anywhere suppresses everywhere for that type.
3. **CO-143 — Streams are never mixed.** Marketing journeys send only from the marketing stream and subdomain; transactional mail never carries marketing content to borrow transactional consent or deliverability, and marketing mail never rides the transactional stream.
4. **CO-144 — Every journey is fully specified.** Each journey names its lifecycle stage, entry event, exit events (stored on the user profile), conversion goal, owner, and one primary metric before it is built; an unspecified journey is not launched.
5. **CO-145 — Every journey carries a control group.** A fixed holdout of eligible users receives no journey messages, so the journey's effect on its primary metric is measured against the control, never assumed from opens or clicks alone.
6. **CO-146 — Merge fields ship with tested fallbacks.** Every personalization field has a fallback value or a fallback rendering (e.g. a greeting that works with no first name), and the fallback path is exercised in testing, not just written.
7. **CO-147 — Seed-send after every edit.** After any journey or template edit, the full sequence is sent to seed accounts on every channel it uses, and the rendered messages are read before the edit goes live.
8. **CO-148 — Suppression is part of the journey definition.** Each journey's exit and exclusion logic is event-based: win-back excludes anyone who purchased or was active inside the stage's window, and re-entry is blocked while a user is inside another conflicting journey.
9. **CO-149 — Frequency caps stop stage collisions.** A per-user cap across all journeys (per day and per week) is enforced by the sending platform, so onboarding, engagement, and win-back messages can never stack on the same user in the same window.
10. **CO-150 — Subject lines and headers are honest.** No deceptive subject lines, no fake "Re:" or "Fwd:" prefixes, no sender names implying a person or relationship that does not exist; the subject states what the message actually contains (CAN-SPAM).
11. **CO-151 — Lists are earned and sunset.** Recipients come only from the product's own opt-in capture — never purchased, rented, or scraped lists — and profiles with no engagement inside the documented sunset window are suppressed from regular sends and eventually removed.
12. **CO-152 — Unsubscribe is one click and honored fast.** Marketing mail carries one-click unsubscribe (RFC 8058 List-Unsubscribe-Post) where the bulk-sender regime applies, every opt-out is honored within 48 hours (inside the CAN-SPAM 10-business-day legal floor), and the sending domain's spam rate is kept under 0.3%.

## BAN list

- **BAN-CO-071 — Unrendered merge field in production.** Banned: a live message containing raw template tokens or stringified empty values. Defeats: DET-CON-003. Bad: "Hi {{first_name}}, your plan renews soon" delivered to 4,000 users. Instead: give every field a tested fallback and pass the seed-send rendering test before the edit goes live (CO-146, CO-147). Severity: BLOCK.
- **BAN-CO-072 — Fabricated familiarity.** Banned: personalization that asserts a history, tenure, or preference the profile does not record. Defeats: DET-CON-014. Bad: "As a loyal customer since 2019…" sent to an account created last week. Instead: render tenure and history claims only from profile fields, and omit the claim when the field is absent (CO-146). Severity: BLOCK.
- **BAN-CO-073 — Invented social proof in email copy.** Banned: statistics, ratings, or customer counts in a message with no source record behind them. Defeats: DET-CON-011. Bad: "Join 50,000 happy customers" in a win-back email when the business has 900 accounts. Instead: use only figures with a fact-sheet.md entry that agree everywhere they appear, or cut the claim (real-content). Severity: BLOCK.
- **BAN-CO-074 — Deceptive subject line.** Banned: a subject that promises an outcome, reply, or document that does not exist. Defeats: DET-CON-028. Bad: "Re: Your refund is ready" on a promotional email to users with no refund. Instead: write a subject that states the message's real content and offer (CO-150). Severity: BLOCK.
- **BAN-CO-075 — Behavior-blind win-back.** Banned: a generic "we miss you" journey whose audience is defined by signup date alone, with no event-based suppression. Defeats: DET-CON-006. Bad: "We miss you!" delivered to a user who purchased yesterday. Instead: define entry and suppression by events — exclude recent purchasers and active users inside the stage window (CO-148). Severity: WARN.

## Gates

- **G-CO-071 — DNS authentication check.** Verifies: CO-141. Check: automated in CI for every sending domain — `dig +short TXT example.com` shows an SPF record, `dig +short TXT selector._domainkey.example.com` returns the DKIM key, `dig +short TXT _dmarc.example.com` returns a DMARC record, and the DMARC domain aligns with the From domain. Pass: all three records present and aligned. Fail: block sending from that domain. Recorded in: progress.md.
- **G-CO-072 — Seed-send rendering test.** Verifies: CO-146, CO-147. Check: automated — after any journey edit, send the full sequence to seed accounts, capture the rendered messages, and scan them for unrendered tokens: `grep -E '\{\{|}}|undefined|null|NaN' rendered/` returns nothing. Pass: zero token hits on every channel. Fail: block the edit from going live. Recorded in: progress.md.
- **G-CO-073 — Journey audit.** Verifies: CO-144, CO-145, CO-148, CO-149. Check: manual checklist per journey — stage, entry event, exit events, conversion goal, owner, primary metric, control group, event-based suppression, and the cross-journey frequency cap are all present in the journey definition. Pass: every field present. Fail: journey stays in draft. Recorded in: progress.md.
- **G-CO-074 — Consent and deliverability check.** Verifies: CO-142, CO-151, CO-152. Check: automated pre-send audience assertion — every profile in the send list has a current opt-in record for the message type and is not on the suppression or sunset list — plus a weekly spam-rate review per sending domain. Pass: 100% of recipients verified opted-in, spam rate under 0.3%. Fail: halt the send and clean the audience. Recorded in: progress.md.

## Anti-patterns

- **One automation for everyone.** A single newsletter-style sequence stands in for a lifecycle program; catch it by asking which stage each message serves — if the answer is "all of them", the program is undifferentiated and gets split by stage.
- **Set-and-forget journeys.** Journeys run for a year with no owner reading results; catch it by checking each journey's last review date against its primary metric — no review, no continued sending.
- **Open-rate as the goal.** Subjects and send times are tuned for opens while the conversion goal quietly flatlines; catch it by reading the journey's primary metric against its control group before any creative change.
- **Rescue-by-volume.** Falling engagement is answered with more messages to the same list instead of sunset and hygiene; catch it in the spam-rate trend — rising complaints with rising volume means the list, not the copy, is the problem.

## Examples

- [Example 1 — Win-back journey with suppression and a tested fallback](examples/example-1.md) — violates/corrects CO-146, CO-148.
- [Example 2 — Sending domain authenticated before the first program](examples/example-2.md) — violates/corrects CO-141, CO-152.
- [Example 3 — Deceptive subject and invented count replaced](examples/example-3.md) — violates/corrects CO-150, and BAN-CO-073's rule via real-content.

## Recall anchors

- Authenticate before volume: SPF, DKIM, aligned DMARC, or nothing sends.
- Consent is checked at send time, never remembered from signup.
- If it renders `{{first_name}}` to a real user, the release failed.
- Win-back excludes yesterday's buyer — by event, not by hope.
- Every journey has a holdout; unmeasured effect is assumed effect.

## Checklist

- [ ] SPF, DKIM, and aligned DMARC verify on every sending domain (CO-141, G-CO-071).
- [ ] Every journey names stage, entry/exit events, goal, owner, and primary metric (CO-144).
- [ ] Every journey has a control group and event-based suppression (CO-145, CO-148).
- [ ] Send-time opt-in check and cross-journey frequency cap are enforced (CO-142, CO-149).
- [ ] Seed-send rendering test passes with zero unrendered tokens (G-CO-072).
- [ ] One-click unsubscribe present and opt-outs honored within 48 hours (CO-152).
- [ ] No purchased or scraped addresses anywhere in the audience (CO-151).
- [ ] Every statistic or social-proof claim in copy has a fact-sheet entry (BAN-CO-073).
