# feedback-loops

## Metadata

- **Owner department:** D18 Customer Experience (CX)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.intercom.com/help/en/articles/5256662-how-your-nps-survey-responses-make-intercom-better
- **Depends on:** support-ticketing
- **Feeds into:** user-onboarding, activation-metrics

## When to use / Do NOT use

- **Use when:** launching or auditing any feedback channel — post-resolution CSAT, lifecycle NPS, in-product ratings, feature-request paths; setting survey triggers, frequency caps, and ownership; reporting scores; announcing shipped changes back to the users who requested them.
- **Do NOT use when:** the request is a support issue needing resolution (use support-ticketing — its post-resolution survey is configured here), product usage measurement (use activation-metrics / D12 analytics), or one-off research interviews, which are scheduled conversations, not instrumented surveys.

## Rules

1. **CX-121 — Defined trigger moments only.** Every survey fires at a defined lifecycle moment — after a support resolution, after onboarding completes, at a set account-age interval — recorded in the survey's configuration. A survey with no defined trigger does not launch.
2. **CX-122 — Context is captured with the response.** Every response records the user or account, the triggering event, the product area, and the timestamp at the moment of the experience. A score stored without its context is not actionable and counts as a configuration defect.
3. **CX-123 — Responses attach to the record.** Scores and comments attach to the user or account record in the feedback system. Responses stored only in a detached spreadsheet or export that no workflow reads are treated as not collected.
4. **CX-124 — Frequency caps across all surveys.** A per-user frequency cap is enforced across every live survey combined: a user inside the cooldown window is not re-prompted by any survey. No survey fires on every page load or every session.
5. **CX-125 — Named owner and cadence before launch.** Every survey names an owner and a fixed review cadence in its configuration before it goes live. The owner reviews new responses on that cadence; the last-reviewed date is recorded.
6. **CX-126 — Neutral wording, equal effort both ways.** Survey questions are worded neutrally and every response option — including the most negative — is equally visible and equally easy to submit. Prompts timed or phrased to catch only satisfied users are prohibited (see BAN-CX-063).
7. **CX-127 — Detractors get a human path.** A low score or a comment describing a problem creates a follow-up task for the owning team, and the respondent is told how a human will reach them. Collecting detractor pain with no response path is worse than not asking.
8. **CX-128 — Themes route to the backlog, linked.** Recurring themes from review are entered in the product backlog with the originating responses linked, so any shipped fix can be traced back to the feedback that caused it.
9. **CX-129 — The loop closes visibly.** When a change requested through feedback ships, the users who requested it are notified that it shipped and what changed. An announcement is sent only for changes that actually shipped.
10. **CX-130 — Scores reported with counts and segment.** Every reported score is published with its response count, time window, and segment. A bare average with no count or segment is not a reportable figure.
11. **CX-131 — No unsourced score claims.** A survey score appears in marketing or product copy only if it is real, current, and produced by this feedback system, cited with its count and window (CX-130). Scores from a removed or unowned survey are never quoted.
12. **CX-132 — Unowned surveys are removed.** A survey whose owner leaves, whose cadence lapses, or whose responses nobody reviews is paused or removed within one cadence cycle. A survey nobody reads does not keep running.

## BAN list

- **BAN-CX-061 — Survey that submits nowhere.** Banned: a feedback form or survey whose responses persist to no reviewed system — discarded, or exported to a spreadsheet nobody opens — while the UI thanks the user. Defeats: DET-FAKE-015. Bad: an NPS popup stores responses in a shared spreadsheet last opened at launch and shows "Thanks!" on submit. Instead: persist responses on the user/account record in the feedback system with a named owner and cadence (CX-123, CX-125), or remove the survey. Severity: BLOCK.
- **BAN-CX-062 — Receipt that lies.** Banned: showing a success state ("Thanks — your feedback helps us improve!") before, or regardless of, the response actually being stored. Defeats: DET-FAKE-022. Bad: the survey widget displays its thank-you panel on button click while the submission request fails silently in the background. Instead: show the confirmation only after the store is acknowledged; a failed submission surfaces an error and a retry (CX-123). Severity: BLOCK.
- **BAN-CX-063 — Rigged rating harvest.** Banned: prompts designed to manufacture positive ratings — asking only after a success moment with the negative path hidden, pre-selecting the top score, or wording that shames a low rating. Defeats: DET-FAKE-014. Bad: a "Rate your experience" prompt appears only after a completed purchase, pre-fills five stars, and routes one-star taps to a dead-end page. Instead: ask at defined moments with neutral wording and every option equally submittable (CX-121, CX-126). Severity: BLOCK.
- **BAN-CX-064 — Detractor dead end.** Banned: collecting a low score or problem report with no follow-up task, queue, or human response path behind it. Defeats: DET-FAKE-015. Bad: a CSAT survey asks "What went wrong?" after bad resolutions; the comments are stored but no ticket, task, or owner ever sees them. Instead: route low scores to a follow-up task for the owning team and tell the respondent a human will reach them (CX-127). Severity: BLOCK.
- **BAN-CX-065 — Loop-closure theater.** Banned: announcing "You asked, we shipped" (or equivalent) for a change that did not ship, or notifying users who never requested it while the actual requesters hear nothing. Defeats: DET-FAKE-013. Bad: a release email claims a top-requested feature was added based on feedback; the feature is a settings toggle rename, and the users who filed the requests receive no notification. Instead: announce only shipped changes, linked to their originating responses, to the users who requested them (CX-128, CX-129). Severity: BLOCK.

## Gates

- **G-CX-061 — End-to-end submission trace.** Verifies: CX-121, CX-122, CX-123, CX-124, CX-127. Check (automated): using the survey tool's test mode, trigger each live survey as a test user at its defined moment and submit a low score with a unique marker comment; assert the response lands on the test user's record with its context (trigger event, product area, timestamp), the marker appears in the owning team's review queue, a detractor follow-up task is created, and an immediate second trigger is blocked by the frequency cap. Run on launch and on every survey-config change. Pass: every assertion true for every survey. Fail: block shipment. Recorded in: progress.md.
- **G-CX-062 — Ownership and cadence audit.** Verifies: CX-125, CX-132. Check (automated): export the configuration of every live survey and assert each lists a named owner, a review cadence, and a last-reviewed date within one cadence cycle of today. Pass: zero live surveys missing an owner, cadence, or current review date. Fail: block shipment of new surveys; pause any lapsed survey until ownership is restored. Recorded in: progress.md.
- **G-CX-063 — Loop-closure audit.** Verifies: CX-128, CX-129. Check: sample the changes announced as feedback-driven in the review period; for each, assert a backlog item exists linking the originating responses, the change is present in the shipped product, and the announcement was sent to the users who requested it. Pass: every sampled announcement traces to linked feedback and a real shipped change, with requesters notified. Fail: warn; correct or retract the announcement and record the gap. Recorded in: progress.md.
- **G-CX-064 — Score reporting integrity check.** Verifies: CX-130, CX-131. Check (automated): recompute every published score from the raw responses in the feedback system and diff against the published figure; grep marketing and product copy for score claims and assert each carries its response count, window, and segment and matches the recomputation. Pass: every published figure matches its raw data and carries count, window, and segment. Fail: block shipment of the copy until corrected. Recorded in: progress.md.
- **G-CX-065 — Detractor follow-up test.** Verifies: CX-127. Check (automated): submit a detractor score with a problem comment through each survey's test mode and assert a follow-up task is created in the owning team's queue, assigned to a named human, with the respondent's contact path attached. Pass: a task exists for every survey tested. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Survey sprawl.** Each team launches its own prompt until users are asked something on every visit and response rates collapse. Catch it by counting live surveys and total prompts per user per month against the shared cap (CX-124) — the fix is consolidation, not another survey.
- **Score watching without reading.** The team tracks the average moving up or down but nobody reads the comments, where the actionable content lives. Catch it at review: a cadence meeting with no verbatim responses on the agenda has become a dashboard ritual.
- **Cherry-picked verbatims.** Only glowing comments are quoted in decks and copy while detractor themes stay buried. Catch it by requiring every internal report to pair quoted praise with the period's top detractor theme.
- **Asking again because the first answer was ignored.** A new survey re-asks a question a previous survey already answered, because its responses were never routed anywhere. Catch it by searching existing feedback for the theme before approving a new survey on it.

## Examples

- [Example 1 — The NPS popup nobody read](examples/example-1.md) — violates/corrects CX-123, CX-124, CX-125 (BAN-CX-061).
- [Example 2 — The detractor who heard nothing](examples/example-2.md) — violates/corrects CX-127 (BAN-CX-064).
- [Example 3 — Closing the loop for real](examples/example-3.md) — violates/corrects CX-128, CX-129, CX-130 (BAN-CX-065).

## Recall anchors

- A survey nobody reviews is removed, not left running.
- Feedback attaches to the user record, never to a spreadsheet.
- Caps are per user, across every survey combined.
- Low scores create work for a human, not just a number.
- The loop closes when the requester is told it shipped.

## Checklist

- [ ] Every survey fires at a defined lifecycle moment, recorded in its configuration (CX-121, G-CX-061).
- [ ] Responses land on the user/account record with trigger, area, and timestamp context (CX-122, CX-123, G-CX-061).
- [ ] The shared per-user frequency cap blocks re-prompts across all surveys (CX-124, G-CX-061).
- [ ] Every live survey has a named owner, a cadence, and a current last-reviewed date (CX-125, G-CX-062).
- [ ] Wording is neutral and every score is equally easy to submit (CX-126).
- [ ] A detractor submission creates an assigned human follow-up task (CX-127, G-CX-065).
- [ ] Shipped feedback-driven changes link their originating responses and notify the requesters (CX-128, CX-129, G-CX-063).
- [ ] Every published score matches its raw data and carries count, window, and segment (CX-130, CX-131, G-CX-064).
