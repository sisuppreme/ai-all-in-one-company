# content-moderation

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.tspa.org/curriculum/ts-curriculum/content-moderation-simulation/
- **Depends on:** auth-hardening, audit-trails (D14)
- **Feeds into:** security-audit, compliance-audit (D14)

## When to use / Do NOT use

- **Use when:** the product accepts user-generated content, user profiles, messages, reviews, or uploads — anywhere a user can report content or an account, or the platform must act on abuse, spam, or illegal content.
- **Do NOT use when:** the site has no user content at all (a static marketing page needs no moderation system); for the legal determination of jurisdiction-specific duties (NCMEC reporting, EU DSA notice-and-action) — implement the technical controls here and route the legal call to D14 privacy-laws / compliance-audit.

## Rules

1. **SE-261 — Policy exists in two forms.** Publish a user-readable policy and keep an internal enforcement guide with a worked example per clause; every enforcement decision cites a clause that exists in both.
2. **SE-262 — Reporting reaches a staffed queue.** Every content item and every account exposes an in-product report action; a submitted report creates a queue row with category, reporter, target, and timestamp, and each priority tier has a written response target.
3. **SE-263 — Automation queues, humans decide the top of the ladder.** Automated detection (spam filters, hash-matching, classifiers) may enqueue, label, and reduce visibility; it never issues a ban or a mass removal without a human decision.
4. **SE-264 — The queue is priority-tiered.** Imminent-harm and illegal-content reports are tier 1 and reviewed before all other tiers; tier order and per-tier review targets are written in the enforcement guide, not improvised per shift.
5. **SE-265 — Enforcement follows the ladder.** Actions escalate in order — label, reduce visibility, remove, suspend, ban — and the chosen rung is proportionate to the clause violated and the account's history; skipping rungs requires a recorded reason.
6. **SE-266 — Every action is logged.** Each enforcement action records actor, policy clause, evidence reference, and timestamp in an append-only log; an action with no log entry is treated as not defensible and is reverted on discovery.
7. **SE-267 — Appeals reach a different reviewer.** Every enforcement notice includes a working appeal path; where staffing allows, the appeal is decided by a reviewer other than the original decision-maker, and the appeal outcome is logged against the original action.
8. **SE-268 — Illegal content is a hard lane, not a policy choice.** Known-CSAM hash matches and credible imminent-harm reports bypass normal tiers: content is preserved for reporting, access is restricted immediately, and escalation follows the runbook; the jurisdiction-specific reporting duty itself is confirmed with D14, never improvised.
9. **SE-269 — Moderation tooling is least-privilege and admin-only.** Queue access is granted per role, enforced server-side on every moderation endpoint, and no moderation route is reachable outside the authenticated admin surface.
10. **SE-270 — Moderator welfare is designed in.** Graphic content is blurred by default with a warning before reveal, queue tooling never autoplays media, and exposure rotation for tier-1 reviewers is defined in the enforcement guide.
11. **SE-271 — Report categories map 1:1 to policy clauses.** Every category offered in the report UI names a clause in the public policy; a category with no clause, or a clause with no category, blocks release until reconciled.
12. **SE-272 — Accountability is measured, not asserted.** The action log produces, per period: report volume by tier, median time-to-first-review per tier against target, and appeal overturn rate; these figures are reviewed on a set cadence and guide fixes are filed from them.

**Minimal tier.** A small product with user content (a single community surface, one moderator role, low report volume) runs the minimal tier of this skill instead of the full operation: an in-product report action on every content item and account (SE-262), one queue with two priorities — the illegal/imminent-harm hard lane (SE-268), which is never simplified away, and everything else under a single written response target — a public policy whose clauses the report categories map to (SE-271), an enforcement ladder with an appeal path, least-privilege admin-only queue access (SE-269), and the action log (SE-272, reduced to report volume and time-to-first-review until volume justifies per-tier reporting). The full tier — priority tiers with per-tier targets (SE-264), moderator-welfare rotation (SE-270), per-tier SLA reporting (G-SE-133) — applies when report volume or reviewer headcount makes a single queue and a single target unworkable, and the tier in force is recorded in the enforcement guide.

## BAN list

- **BAN-SE-131 — Report button that submits nowhere.** Banned: a report control that opens a mailto link, posts to an unmonitored inbox, or returns success without writing a queue row. Defeats: DET-FAKE-015. Bad: the Report button calls `POST /reports`, whose handler sends an email to reports@ and discards the payload. Instead: the handler inserts a queue row (category, target, reporter, timestamp) and returns the row's tracking ID. Severity: BLOCK.
- **BAN-SE-132 — Moderation actions that don't persist.** Banned: queue UI that marks an item "resolved" or "actioned" in local state while writing nothing to the database or action log. Defeats: DET-FAKE-010. Bad: clicking Remove hides the post in the moderator's browser; a reload shows it live again and no log entry exists. Instead: the action commits the state change and its log entry in one transaction, and the UI renders the persisted result. Severity: BLOCK.
- **BAN-SE-133 — Staged review notifications.** Banned: telling a reporter or an author "your report was reviewed" / "action was taken" on a timer or on submission, independent of any actual decision. Defeats: DET-FAKE-013. Bad: the intake endpoint immediately emails the reporter "We've reviewed your report" before the item enters the queue. Instead: notifications are emitted only by the decision event, and state the actual outcome and the appeal path. Severity: BLOCK.
- **BAN-SE-134 — Moderator role enforced only in the UI.** Banned: hiding moderation controls from non-moderators in the client while the moderation endpoints accept any authenticated (or unauthenticated) request. Defeats: DET-FAKE-021. Bad: `/api/moderation/ban` checks only that a session cookie exists because the button is admin-only in the frontend. Instead: every moderation endpoint verifies the moderator role server-side and returns 403 otherwise. Severity: BLOCK.
- **BAN-SE-135 — Intake that swallows failures and reports success.** Banned: a report or appeal handler that catches a queue-write or storage error, logs nothing, and still returns a success response. Defeats: DET-CODE-005. Bad: `try { await queue.insert(report) } catch { /* ignore */ }` followed by `201 Report received`. Instead: a failed insert returns an error to the user, raises an alert, and the report is never acknowledged as received. Severity: BLOCK.

## Gates

- **G-SE-131 — End-to-end report drill.** Verifies: SE-262, SE-266, SE-267. Check: automated workflow test — file a test report through the public UI, trace it to a queue row, a decision, and an appeal, asserting a log entry exists at each step. Pass: all four records exist and link to each other. Fail: block shipment. Recorded in: progress.md.
- **G-SE-132 — Persistence and role test.** Verifies: SE-269, BAN-SE-132, BAN-SE-134. Check: automated API test — perform a removal as a moderator, reload the target from the database and assert the removal and its log entry persisted; repeat the same call as a regular user. Pass: state persisted; non-moderator call returns 403. Fail: block shipment. Recorded in: progress.md.
- **G-SE-133 — Queue SLA report.** Verifies: SE-264, SE-272. Check: automated query over the action log for the last 30 days computing median time-to-first-review per priority tier, compared against the targets in the enforcement guide. Pass: every tier at or under target, or a filed remediation note per breached tier. Fail: warn and escalate to the department lead. Recorded in: progress.md.
- **G-SE-134 — Policy-coverage check.** Verifies: SE-261, SE-271. Check: manual checklist — list every report category in the shipped UI and trace each to a clause in the public policy and an example in the enforcement guide; list every ladder rung and confirm it is reachable in the queue UI. Pass: zero unmapped categories, clauses, or rungs. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Keyword-list theater.** The "moderation system" is an ever-growing banned-word list with no queue, clauses, or metrics. Catch it: ask where a report goes and what the overturn rate is — if neither exists, there is no system.
- **Shadow queue.** Moderators coordinate actions in chat or DMs and apply them without queue entries, so the log shows a fraction of real enforcement. Catch it: sample live enforcement outcomes and try to find their log entries.
- **Rubber-stamp appeals.** Appeals are decided by the original decision-maker in bulk with near-zero overturns and no reasons recorded. Catch it: check the appeal log for reviewer identity and overturn rate before calling the appeal path real.
- **Policy drift.** The team's actual practice evolves (new violation types, new shortcuts) while the public policy and enforcement guide stay frozen. Catch it: compare the last month's cited clauses against the published policy text.

## Examples

- [Example 1 — Report intake that reaches a queue](examples/example-1.md) — violates/corrects SE-262 (BAN-SE-131).
- [Example 2 — Classifier flag without an auto-ban](examples/example-2.md) — violates/corrects SE-263.
- [Example 3 — Logged enforcement with a real appeal](examples/example-3.md) — violates/corrects SE-266, SE-267.

## Recall anchors

- A report button that reaches no staffed queue is a defect, not a feature.
- Automation queues and labels; humans decide bans and mass removals.
- No log entry, no enforcement — unlogged actions get reverted.
- Illegal content is a hard legal lane: preserve, restrict, escalate, let D14 make the legal call.
- Every report category names a public policy clause, or it does not ship.

## Checklist

- [ ] Public policy and internal enforcement guide both exist, with an example per clause (SE-261).
- [ ] Report drill passed end to end: report → queue → decision → appeal, all logged (G-SE-131).
- [ ] Moderation endpoints reject non-moderators server-side with 403 (SE-269).
- [ ] No automated filter can ban or mass-remove without a human decision (SE-263).
- [ ] Median time-to-first-review per tier is within target or has a remediation note (G-SE-133).
- [ ] Every UI report category traces to a public policy clause (G-SE-134).
- [ ] Graphic content is blurred by default in the queue; no autoplay (SE-270).
- [ ] Appeal overturn rate and tier volumes were produced from the action log this period (SE-272).
