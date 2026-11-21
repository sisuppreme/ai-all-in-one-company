# dunning

## Metadata

- **Owner department:** D11 Integrations & Payments (IN)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Stripe, "Automate payment retries" — https://docs.stripe.com/billing/revenue-recovery/smart-retries ; Stripe, "Automatic collection" — https://docs.stripe.com/invoicing/automatic-collection
- **Depends on:** subscriptions, webhooks, transactional-email
- **Feeds into:** subscriptions, refunds-disputes

## When to use / Do NOT use

- **Use when:** a recurring charge fails and the product must recover the payment — retries, customer notices, grace period, and the end state — without surprising the customer or improvising access. This skill owns the failed-payment sequence from first decline to resolution.
- **Do NOT use when:** the failure is a first purchase (payments), the customer is voluntarily canceling (subscriptions), or money is moving back to the customer (refunds-disputes). Do not use it to design prices or plan terms; dunning executes the terms the product already published.

## Rules

1. **IN-081 — Dunning is one configured sequence.** Retries, customer contact, grace window, and end state are defined once, in provider and product configuration, before the first failure. A failure handled by ad-hoc support action or an engineer's judgment call is a defect in the sequence, not a rescue.
2. **IN-082 — The first failure notifies the customer the same day.** The first declined renewal sends a failed-payment email that day carrying a hosted payment-update link. Silent retrying burns the window in which a card update is most likely; the customer learns of the failure from the product, never from losing access.
3. **IN-083 — Retries are smart, finite, and configured.** The provider's smart retry machinery is enabled where offered, or a custom schedule is set, sized to the product's billing period. (Stripe's documented new-account default — up to 8 retries within 2 weeks, checked 2026-11-21 — is a starting configuration to review, not a law.) An unbounded or inherited-by-accident retry schedule is a finding.
4. **IN-084 — Hard declines exit retries immediately.** A hard decline (stolen card, closed account, do-not-honor) leaves the retry sequence at once and enters the contact layer; retrying it is cost without chance. Soft declines stay in the retry schedule.
5. **IN-085 — Card-updater features are enabled where offered.** Provider card-updater and network-token features are turned on, so reissued and replaced cards retry against current credentials — many "failures" are reissued cards, not unwilling customers.
6. **IN-086 — The payment-update path works and writes to the provider.** The update link lands on a hosted, login-light page (signed link, no full re-login gauntlet); submitting a new card stores it at the provider, and a successful update triggers an immediate retry rather than waiting for the next scheduled one.
7. **IN-087 — One past_due access rule, written and uniform.** During the grace window the product grants exactly one of full access, read-only access, or no access — stated in the published terms and enforced identically by every entitlement check. No page, endpoint, or export improvises its own variant.
8. **IN-088 — Dunning copy states facts and only real consequences.** Every notice names the amount, what happens next, and the deadline. Copy never threatens an action the sequence will not actually take — no deletion warnings on a sequence that pauses, no "final notice" that is not final.
9. **IN-089 — The sequence ends in exactly one configured state.** At the end of the window the subscription is canceled, marked unpaid, or paused — the one outcome chosen per product — executed at the provider, mirrored locally, and communicated to the customer with what it means for their access and data.
10. **IN-090 — Contact stops the moment payment succeeds.** A successful retry or card update halts the sequence immediately: no further reminders, no lingering banner, mirror back to active. A "your payment failed" email arriving after a successful charge is a sequence bug.
11. **IN-091 — Recovery is measured and reconciled.** The recovery rate (recovered ÷ failed renewals) is reported per period and reconciled against the provider's failed and recovered counts; involuntary churn is reported separately from voluntary cancellation, never blended into one churn number.
12. **IN-092 — Every dunning surface reads the mirrored state.** The banner, the emails, and the billing page all render from the mirrored provider subscription state (subscriptions, IN-021). No surface computes its own "days overdue" or paid status from local dates.

## BAN list

- **BAN-IN-041 — Silent retries.** Banned: a retry sequence that runs for days with no customer notice, so the first signal of a failed renewal is the end state. Defeats: DET-FAKE-013. Bad: the provider retries for two weeks, every attempt declines, the subscription is canceled, and the customer's first email is "your account has been closed" — the recovery window was spent in silence. Instead: the first failure notifies the customer the same day with a working update link (IN-082). Severity: BLOCK.
- **BAN-IN-042 — The update link that updates nothing.** Banned: a payment-update page that accepts a new card but never stores it at the provider, so retries keep hitting the old declined card. Defeats: DET-FAKE-016. Bad: the customer updates their card twice, gets a "Card updated" toast each time, and is canceled anyway because the form wrote to a local table the billing flow never reads. Instead: the hosted update writes the new payment method to the provider and triggers an immediate retry against it (IN-086). Severity: BLOCK.
- **BAN-IN-043 — Threat copy the sequence will not perform.** Banned: dunning notices claiming a consequence — deletion, legal action, a deadline — that the configured sequence does not actually carry out. Defeats: DET-FAKE-022. Bad: three emails warn "your data will be permanently deleted on Friday," while the configured end state is pause with data retained; the state the copy claims never exists. Instead: copy states the amount, the real next step, and the real deadline (IN-088). Severity: BLOCK.
- **BAN-IN-044 — The UI-only access cut.** Banned: ending dunning by hiding the app behind a paywall screen while the API, exports, or shared links still serve the account — or the reverse, a banner claiming access is cut while nothing enforces it. Defeats: DET-FAKE-021. Bad: the web app shows "subscription ended," but the mobile API keeps returning full data because only the frontend checks the flag. Instead: the end state changes entitlement at the one mirrored-state check every surface reads (IN-087, IN-092). Severity: BLOCK.
- **BAN-IN-045 — Locally "recovered" revenue.** Banned: marking a past_due subscription paid or active in local state — by support edit, admin toggle, or a retry stub — without a confirmed charge at the provider. Defeats: DET-FAKE-006. Bad: an admin "mark recovered" button flips the row to active so the dashboard looks healthy; no charge ever succeeded, and the customer is never billed again because the mirror says active. Instead: recovery exists only when the provider confirms the charge and the webhook converges the mirror (IN-090, IN-092). Severity: BLOCK.

## Gates

- **G-IN-041 — Decline-card test-clock walk.** Verifies: IN-082, IN-083, IN-087, IN-089. Check: automated — in test mode with a provider test clock, run a renewal against a test decline card and advance the clock through the configured window; assert in order: the first-failure email fires the same day with a working update link, retries occur on the configured schedule, the past_due banner shows, the grace access rule holds, and the sequence lands in the one configured end state. Pass: every step occurs as configured. Fail: block shipment. Recorded in: progress.md.
- **G-IN-042 — Mid-sequence recovery stop test.** Verifies: IN-086, IN-090. Check: automated — fail a renewal in test mode, advance the clock into the sequence, then update the card through the hosted update link; assert an immediate retry runs against the new card, succeeds, the mirror returns to active, and no further dunning notice is sent afterward. Pass: recovery is immediate and contact stops. Fail: block shipment. Recorded in: progress.md.
- **G-IN-043 — Hard-decline exit test.** Verifies: IN-084. Check: automated — run a renewal against a provider test card that returns a hard decline and inspect the resulting schedule. Pass: zero further retry attempts are scheduled and the contact layer is entered on the first failure. Fail: block shipment. Recorded in: progress.md.
- **G-IN-044 — Recovery-report reconciliation.** Verifies: IN-091. Check: automated — generate the period recovery report and diff recovered and failed counts against the provider's invoice outcomes for the same period. Pass: counts match exactly and involuntary churn is reported as its own line. Fail: block the report; the metric is part of the feature. Recorded in: progress.md.

## Anti-patterns

- **Retry-forever configuration.** The schedule is copied from a tutorial or left at a default nobody chose, and declines retry until the provider gives up on its own. Catch it: open the configuration and read the actual retry count and window; if nobody can say why those numbers, the schedule was never designed (IN-083).
- **Email-only dunning.** Notices go out by email while the product itself shows nothing, so a customer who misses the email discovers the failure at the access cut. Catch it: sign in as a past_due test user — if no banner or billing-page state is visible in-product, the contact layer has one channel too few.
- **Copy drift toward menace.** Each rewrite of the dunning emails sounds tougher than the sequence behind it, because tougher "feels" more effective. Catch it: read every consequence the copy names and point to the configuration line that performs it; an unmatched consequence is a BAN-IN-043 hit, not a style choice.
- **The sympathetic extension.** Support quietly extends grace for loud customers by editing dates, so identical failures get different treatment and the end state stops meaning anything. Catch it: sample past_due rows and compare time-to-end-state; variance with no configured reason is improvisation (IN-087).

## Examples

- [Example 1 — The two silent weeks](examples/example-1.md) — corrects IN-082.
- [Example 2 — The update link that saved nothing](examples/example-2.md) — corrects IN-086.
- [Example 3 — Four pages, four grace periods](examples/example-3.md) — corrects IN-087.

## Recall anchors

- First failure, same-day email, working update link.
- Smart retries, finite window, hard declines exit at once.
- One grace rule, one end state — both written in the terms.
- Copy threatens only what the sequence actually does.
- Recovery is a reconciled number, not a feeling.

## Checklist

- [ ] Retry machinery enabled and the schedule explicitly configured for this product (IN-083).
- [ ] Card-updater / network-token features enabled where the provider offers them (IN-085).
- [ ] Decline-card test-clock walk passes end to end (G-IN-041).
- [ ] Mid-sequence card update recovers immediately and stops all contact (G-IN-042).
- [ ] Hard declines schedule zero retries (G-IN-043).
- [ ] The past_due access rule is in the published terms and enforced by the one entitlement check (IN-087).
- [ ] Every dunning notice's stated consequence exists in the configured sequence (IN-088).
- [ ] Recovery report reconciles against provider counts, involuntary churn on its own line (G-IN-044).
