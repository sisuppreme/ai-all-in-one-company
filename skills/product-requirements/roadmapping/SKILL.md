# roadmapping

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://www.prodpad.com/glossary/now-next-later-roadmap/
- **Depends on:** discovery, scope-control, acceptance-criteria
- **Feeds into:** user-stories, requirements-writing

## When to use / Do NOT use

- **Use when:** sequencing product work across quarters; publishing or updating an internal or public roadmap; moving an initiative between horizons; answering "when will X ship?" with something honest.
- **Do NOT use when:** the decision is what fits inside one fixed release (use scope-control), or the item has no discovery behind it yet and belongs in the opportunity tree, not on any roadmap horizon (use discovery).

## Rules

1. **PR-241 — Three confidence horizons.** The roadmap uses Now / Next / Later. Now = validated initiatives in active build. Next = problems under active discovery. Later = strategic bets not yet shaped. An item's horizon states the team's confidence, not a delivery slot.
2. **PR-242 — Outcomes, not features.** Every item is framed as an outcome or problem linked to a named objective ("cut time-to-first-report for new accounts"), not as a feature name ("reporting module v2").
3. **PR-243 — No dates outside Now.** Next and Later items carry no calendar dates and no quarter labels presented as commitments. A date on a Later item is a promise the team has not validated.
4. **PR-244 — Now requires discovery.** An item enters Now only after discovery (a target opportunity plus assumption tests, per discovery) and with acceptance criteria attached or explicitly scheduled before build starts.
5. **PR-245 — Entry through the tree and a class.** Items reach the roadmap through the opportunity tree and carry a MoSCoW class from scope-control. Stakeholder volume and seniority are not entry criteria.
6. **PR-246 — Placement by evidence.** Horizon placement is set by the strength of discovery evidence and stated confidence, and the placement rationale is written on the item. Confidence, not optimism, moves items forward.
7. **PR-247 — External is less specific.** The public roadmap is deliberately less specific than the internal one: outcomes and horizons only, no dates, no unvalidated capabilities. Anything public is a product promise.
8. **PR-248 — Every change is recorded.** Each roadmap change records what moved, why, and what it displaced. Silent re-sequencing — in either the internal or the public view — is a defect.
9. **PR-249 — Later items expire.** Later items carry a review interval. An item not reviewed within that interval is flagged for re-triage: re-validate, demote to the opportunity tree, or remove it.
10. **PR-250 — Two views, one truth.** The internal and external roadmaps are generated from the same item list. The external view may say less, but it may never say something different.

## BAN list

- **BAN-PR-121 — Date on an unvalidated item.** Banned: placing a calendar date or committed quarter on a Next or Later item. Defeats: DET-CON-018. Bad: the roadmap shows "Later: AI insights — ships September," discovery has not started, and by October the public page is stale dated copy asserting a present that never arrived. Instead: keep the item in its horizon with its confidence stated (PR-243). Severity: BLOCK.
- **BAN-PR-122 — Public promise ahead of internal validation.** Banned: listing a capability on the public roadmap that the internal roadmap has not validated through discovery. Defeats: DET-CON-028. Bad: the public roadmap promises "Slack integration" to close a sales deal while the internal roadmap has it as an unshaped Later bet with no assumption tests run. Instead: the public entry waits for internal validation, or is framed as an outcome under exploration (PR-247). Severity: BLOCK.
- **BAN-PR-123 — "Coming soon" with no horizon.** Banned: a public "coming soon" feature announcement that names no horizon, no discovery status, and no review date. Defeats: DET-CON-004. Bad: the marketing site gains a "Coming soon: mobile app" tile that sits unchanged for a year, implying a feature exists in the near term when no work is scheduled. Instead: publish through the roadmap's horizons, or do not announce (PR-247). Severity: WARN.
- **BAN-PR-124 — Silent re-sequencing.** Banned: moving, swapping, or dropping roadmap items without a change record stating what moved, why, and what it displaced. Defeats: DET-CON-015. Bad: two Now items trade places after a stakeholder call; the public roadmap still shows the old order, and the site now contradicts itself about what is being built. Instead: record the change under PR-248 in both views. Severity: BLOCK.

## Gates

- **G-PR-121 — Roadmap field check.** Verifies: PR-241, PR-242, PR-244. Check (automated): every item in the roadmap file carries the fields outcome, objective, horizon, and — for Now items — a discovery link; a field-presence scan returns zero incomplete items. Pass: zero incomplete items. Fail: block shipment. Recorded in: progress.md.
- **G-PR-122 — Date scan.** Verifies: PR-243. Check (automated): `grep -nE "20[0-9]{2}-(0[1-9]|1[0-2])|Q[1-4] 20[0-9]{2}" roadmap.md` restricted to the Next and Later sections must return no date or quarter commitments. Pass: zero hits in those sections. Fail: block shipment. Recorded in: progress.md.
- **G-PR-123 — Staleness check.** Verifies: PR-249. Check (automated): each Later item's last-reviewed date is compared against the stated review interval; items past the interval are listed. Pass: zero unreviewed Later items, or each is flagged in the document as awaiting re-triage. Fail: warn. Recorded in: progress.md.
- **G-PR-124 — Two-view consistency diff.** Verifies: PR-247, PR-250. Check (manual): place the public roadmap beside the internal one; every public item must exist internally at the same or greater specificity, and no public item may assert a capability, date, or commitment absent internally. Pass: zero public assertions without an internal source. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Gantt in disguise.** The horizons are renamed Now/Next/Later but each still holds a fixed feature list with implied ship order and dates in the meeting notes. Catch it by reading the items: if swapping two items would "break the plan," it is a Gantt chart wearing horizon labels.
- **Feature parking lot.** Later becomes a guilt-free store for every idea anyone ever suggested, so nothing is ever refused. Catch it with the expiry rule (PR-249): a Later list that only grows is a parking lot, not a strategy.
- **Roadmap as sales collateral.** Items are added to the public view to win individual deals, one promise at a time. Catch it at G-PR-124: any public item whose only internal trace is a sales request fails the two-view test.
- **Horizon inflation.** Everything sits in Now because no team wants to tell a stakeholder "not yet," destroying the signal Now is meant to carry. Catch it by counting: Now should hold only what is actually in build; a Now list longer than the team's active work is inflated.

## Examples

- [Example 1 — The feature-date timeline](examples/example-1.md) — violates/corrects PR-242, PR-243.
- [Example 2 — Promised before it was validated](examples/example-2.md) — violates/corrects PR-247.
- [Example 3 — The quiet swap](examples/example-3.md) — violates/corrects PR-248.

## Recall anchors

- Horizons state confidence, not delivery slots.
- No dates outside Now — a dated Later item is an unvalidated promise.
- The public roadmap may say less, never something different.
- Items enter through discovery and a MoSCoW class, not volume.
- Every move records what it displaced.

## Checklist

- [ ] All items sit in Now, Next, or Later with confidence stated (PR-241).
- [ ] Every item framed as an outcome linked to an objective (PR-242, G-PR-121).
- [ ] No dates or committed quarters on Next/Later items (PR-243, G-PR-122).
- [ ] Every Now item has discovery evidence and acceptance criteria attached or scheduled (PR-244).
- [ ] Entry path recorded: opportunity tree plus MoSCoW class (PR-245).
- [ ] Public view checked against internal view — less specific, never different (PR-247, PR-250, G-PR-124).
- [ ] All changes since last publication logged with reason and displacement (PR-248).
- [ ] No Later item past its review interval unflagged (PR-249, G-PR-123).
