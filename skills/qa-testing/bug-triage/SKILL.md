# bug-triage

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** BugReel, "Bug Triage Process Guide" — https://www.bugreel.io/blog/bug-triage-process-guide ; PROJECT_ANATOMY.md, Bug triage and defect management element (severity/priority workflow)
- **Depends on:** test-strategy
- **Feeds into:** qa-gates

## When to use / Do NOT use

- **Use when:** any defect report arrives — from testing, support, monitoring, or users — and whenever the defect queue is reviewed, a release is assessed for escapes, or a defect is proposed for closure.
- **Do NOT use when:** the work is preventing or detecting defects before they are reported (that is test-strategy and the testing skills), or when a report is actually a feature request with no broken behavior — route it to product-requirements instead of triaging it as a defect.

## Rules

1. **QA-261 — One queue, one template.** Every defect enters through the single intake queue on the standard template: reproduction steps, environment, expected vs. actual, and evidence. A report filed anywhere else is moved into the queue, not worked from where it landed.
2. **QA-262 — Reproduce or return.** Triage validates each report: reproduce it, or return it to the reporter naming the specific information needed. An unreproduced report sits visibly in a needs-information state; it is never scheduled and never silently dropped.
3. **QA-263 — Severity is not priority.** Severity (technical impact) and priority (business urgency) are separate fields, set independently at triage. Neither defaults to "high"; a report with either field unset is incomplete and cannot be scheduled.
4. **QA-264 — Named owner at triage.** Every validated defect leaves triage with a named individual owner. A defect still unowned at the next triage session is escalated in that session, not carried silently.
5. **QA-265 — Duplicates link, never vanish.** A duplicate is linked to its canonical defect and counted on it; it is never closed without the link. The canonical defect shows its duplicate count, because that count is user-impact signal.
6. **QA-266 — A decision, recorded.** Every validated defect leaves triage with a fix slot or an explicit won't-fix / defer decision that names the decider and the reason. "Later" with no date and no reason is not a decision.
7. **QA-267 — Closure requires verification.** A defect closes only on verified behavior: the fix's regression test green, or a retest note attached naming the build and environment tested. A merged pull request, by itself, never closes a defect.
8. **QA-268 — Reopen without penalty.** When verification fails, the original defect reopens — it is not refiled as a new ticket. Reopen counts are reported as-is; nobody's metrics improve by suppressing a reopen.
9. **QA-269 — Escapes name their gate.** Every defect found in production records, in its escape field, the gate that should have caught it — or "no gate existed". A gate named by recurring escapes is changed; only fixing the code leaves the hole open.
10. **QA-270 — Fixed cadence, aging reviewed.** Triage runs on a fixed cadence. Aging reports and reopened defects are re-reviewed every session, and no open defect goes longer than one cadence without a state change or a recorded comment.
11. **QA-271 — Evidence or incomplete.** A report carries evidence — screenshot, trace ID, log excerpt, or request/response pair — or it is returned for it. "It broke" with no evidence and no reproduction steps is an incomplete report, not a defect.
12. **QA-272 — Queue numbers are computed.** Every queue figure reported upward — open by severity, escape count, reopen count — is generated from defect fields by query or report. A hand-typed number in a status update is treated as unverified.

## BAN list

- **BAN-QA-131 — Verified-on-paper closure.** Banned: closing a defect as fixed or verified with no regression test result and no retest evidence attached. Defeats: DET-FAKE-022. Bad: the developer merges a fix, moves the ticket to Verified, and the defect ships again in the next release because nobody re-ran the failing case. Instead: attach the green regression test or a retest note naming build and environment, then close (QA-267). Severity: BLOCK.
- **BAN-QA-132 — The silent duplicate.** Banned: closing a report as "duplicate" without linking it to the canonical defect. Defeats: DET-FAKE-011. Bad: four of five reports of the same checkout failure are closed unlinked; the queue shows one minor defect while users keep hitting it daily. Instead: link each duplicate to the canonical defect and let its count rise (QA-265). Severity: BLOCK.
- **BAN-QA-133 — Phantom reports.** Banned: filing or keeping defect tickets that were never reproduced and carry no evidence, so the tracker looks thorough while describing defects nobody has seen. Defeats: DET-FAKE-014. Bad: a generated batch of plausible tickets ("export sometimes fails", no steps, no trace) pads the queue and consumes a triage session. Instead: reproduce the defect or return the report for the specific missing information (QA-262, QA-271). Severity: BLOCK.
- **BAN-QA-134 — Reopen laundering.** Banned: refiling a failed verification as a brand-new defect so the reopen count stays at zero. Defeats: DET-NONE — no DET parameter names this signal; governed by QA-268. Bad: a defect "fixed" three times appears as three unrelated tickets, and the release report claims zero reopens. Instead: reopen the original defect and let its history and reopen count show (QA-268). Severity: BLOCK.

## Gates

- **G-QA-131 — Queue audit.** Verifies: QA-261, QA-263, QA-264, QA-270. Check: script-assisted — sample 10 open defects from the tracker export; each must carry reproduction steps, environment, severity and priority as separate fields, a named owner, and a state change within the triage cadence. Pass: 10 of 10 complete. Fail: the incomplete defects are repaired in the next triage session and the audit re-runs. Recorded in: progress.md.
- **G-QA-132 — Closure-evidence check.** Verifies: QA-267, QA-268. Check: automated — `tracker-export --state closed --since <last-release>` filtered for defects with no linked regression-test result and no retest note; the filter must return an empty list. Pass: zero closed defects lack verification evidence. Fail: each offender reopens and release sign-off is blocked until it is verified or re-triaged. Recorded in: progress.md.
- **G-QA-133 — Escape analysis.** Verifies: QA-269. Check: automated — per release, generate the escape report from defect fields: count of production defects grouped by their named should-have-caught gate. Pass: the report exists and every production defect has a non-empty escape field. Fail: defects with an empty escape field are completed before the release closes. Recorded in: progress.md.
- **G-QA-134 — Duplicate-link check.** Verifies: QA-265. Check: automated — query the tracker for defects closed as duplicate whose canonical-link field is empty. Pass: zero results. Fail: each offender is linked to its canonical defect and the canonical count corrected. Recorded in: progress.md.

## Anti-patterns

- **Triage theater.** A tracker full of well-formatted, plausible tickets that nobody acts on — owners nominal, sessions held, nothing ships. Catch it: the aging report; defects whose state has not changed across two cadences expose it (QA-270).
- **The rubber-stamp session.** Dozens of reports "triaged" in minutes, each validated with no reproduction attempt. Catch it: compare the session's validated count against the reproduction notes actually attached; validation without a note is a stamp, not a check.
- **Severity drift before release.** Severities quietly lowered in the days before a release so the queue looks shippable. Catch it: diff severity values at filing against severity values at release; unexplained downgrades are restored and re-triaged.
- **The needs-information graveyard.** Reports parked in needs-information forever as a soft delete — never returned to, never closed, never counted. Catch it: the needs-information aging list is reviewed every cadence, and each entry is chased, reproduced from other evidence, or closed with the reason recorded (QA-266).

## Examples

- [Example 1 — A merged PR is not a closure](examples/example-1.md) — corrects QA-267.
- [Example 2 — Five wordings, one defect](examples/example-2.md) — corrects QA-265.
- [Example 3 — Everything is "high priority"](examples/example-3.md) — corrects QA-263.

## Recall anchors

- One queue, one template, one cadence.
- Severity is impact; priority is urgency; never one field.
- No reproduction path, no scheduling.
- A merged PR never closes a defect — verified behavior does.
- Duplicates link and count; they never vanish.

## Checklist

- [ ] Every new report entered through the intake queue on the standard template (QA-261).
- [ ] Each report reproduced, or returned naming the specific information needed (QA-262).
- [ ] Severity and priority set as separate fields on every validated defect (QA-263).
- [ ] Every validated defect has a named owner and a recorded fix / won't-fix / defer decision (QA-264, QA-266).
- [ ] All duplicates linked to their canonical defect, counts visible (QA-265, G-QA-134).
- [ ] No defect closed without a green regression test or a retest note (QA-267, G-QA-132).
- [ ] Every production defect names the gate that should have caught it (QA-269, G-QA-133).
- [ ] Queue audit sample passed 10 of 10 (G-QA-131).
