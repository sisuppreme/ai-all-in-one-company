# compliance-audit

## Metadata

- **Owner department:** D14 Legal & Privacy (LG)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://cy.ico.org.uk/for-organisations/advice-and-services/audits/data-protection-audit-framework/toolkits/accountability/records-of-processing-and-lawful-basis/ ; https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng/
- **Depends on:** privacy-laws, audit-trails
- **Feeds into:** legal-documents, dsar-handling, cookie-consent

## When to use / Do NOT use

- **Use when:** running the scheduled audit of a product against its obligations register; after any trigger event (new market, new processor class, new regulated feature, a legal change flagged by privacy-laws); before any public compliance claim is published or renewed; preparing the evidence pack for qualified counsel or an external assessor.
- **Do NOT use when:** a legal verdict is needed — this audit maps requirements to tested evidence and prepares the operator for qualified review; it never certifies compliance and never substitutes for counsel (LG-131). Building the register itself is privacy-laws; fixing a failed flow belongs to the skill that owns that flow.

## Rules

1. **LG-121 — Audit against the register, nothing else.** The audit scope is the obligations register: every applicable row is in scope, and anything not in the register is either registered first (privacy-laws) or recorded as out of scope with a reason. An audit of "the product in general" has no scope and proves nothing.
2. **LG-122 — Every control names four things.** For each obligation, the audit record names the control, the test that exercises it, the evidence artifact the test produces, and the last test date. A row missing any of the four is an open finding by definition.
3. **LG-123 — Evidence beats assertion.** A control with no dated test artifact is recorded as failing, whatever the policy, the register, or the team says. Demonstrability is the standard (GDPR Articles 5(2) and 24): if it is not evidenced, it did not happen.
4. **LG-124 — Test flows, not documents.** Pass/fail evidence comes from executing the real user paths — submit the DSAR drill, run the consent matrix, run the license scan, pull an acceptance record, pull an audit-trail entry. Documents are inputs to the audit, never its evidence.
5. **LG-125 — Public claims are in scope.** The audit sweeps every public surface — marketing pages, app-store listings, sales decks, the product itself — and every compliance claim found must map to a tested control supporting its exact wording, or the claim is a finding and is removed.
6. **LG-126 — Frameworks are audited as what they are.** Voluntary trust frameworks (SOC 2, ISO/IEC 27001) are audited inside their own scopes as customer-trust certifications. Their results are never reported as legal compliance, and a legal obligation is never marked satisfied by a framework certificate.
7. **LG-127 — Findings are defects, not percentages.** Every finding carries severity, a named owner, and a remediation date, and is tracked to closure like a bug. The audit never emits a "compliance score" or percentage — a single number hides exactly the gaps the audit exists to expose.
8. **LG-128 — Closure requires re-test.** A finding closes only when the failed test is re-run and the new passing evidence is filed. Intention, a merged fix, or an owner's assurance does not close a finding.
9. **LG-129 — Cadence is risk-based and recorded.** Audits run at minimum on a fixed schedule and on every trigger event (LG-121 scope changes, legal changes flagged by privacy-laws). The schedule and its triggers are written in the audit record, not held as habit.
10. **LG-130 — Stale inputs are findings.** Register rows, dated legal tables, and evidence past their freshness or review windows are findings in themselves. An audit run on stale inputs reports the staleness first and does not pass controls on expired evidence.
11. **LG-131 — The audit prepares; it does not certify.** The audit's output is an evidence pack and a findings list for the operator and qualified counsel. It never issues a compliance certificate, a pass/fail verdict on the product's legality, or wording a reader could mistake for one.
12. **LG-132 — The audit is itself a record.** Scope, tests run, evidence filed, and findings are written to the audit trail (audit-trails) with dates and the auditor's identity. An audit that left no record is treated as an audit that never ran.

## BAN list

- **BAN-LG-061 — The invented compliance score.** Banned: publishing or reporting a percentage or score ("92% GDPR compliant", a green compliance meter) computed from unchecked boxes or partial evidence. Defeats: DET-FAKE-004. Bad: an internal dashboard shows "Compliance: 94%" generated from register rows existing, while no control has ever been test-run. Instead: report the findings list — each gap with severity, owner, and remediation date (LG-127). Severity: BLOCK.
- **BAN-LG-062 — Certification claims with no artifact behind them.** Banned: public wording such as "GDPR compliant", "PCI certified", or "COPPA safe" where no tested control supports the exact claim. Defeats: DET-CON-012. Bad: the landing page footer says "Fully GDPR & SOC 2 Compliant"; the audit file contains no DSAR drill and no SOC 2 report. Instead: publish only what a dated audit artifact proves, worded as what was tested, when, and against what — or remove the claim (LG-125). Severity: BLOCK.
- **BAN-LG-063 — Policy read as proof of a working flow.** Banned: marking a control passed because a policy or notice describes the process, without executing the flow. Defeats: DET-CON-028. Bad: the retention control passes because the privacy policy states a 12-month limit; no deletion job exists and records from three years ago are still live. Instead: run the flow and file its output — the deletion log, the drill result, the scan report (LG-124). Severity: BLOCK.
- **BAN-LG-064 — Stale evidence presented as current.** Banned: citing a test artifact past its freshness window as proof a control currently passes. Defeats: DET-CON-018. Bad: the consent control passes on a consent-matrix run dated 14 months ago, before two banner redesigns. Instead: re-run the test inside its window, or record the control as failing on stale evidence (LG-130). Severity: BLOCK.
- **BAN-LG-065 — Audit report that contradicts its own evidence.** Banned: a summary verdict ("all controls passing") that the filed artifacts do not support. Defeats: DET-CON-014. Bad: the audit summary says the DSAR control passes; the attached drill log shows the export step timed out and was never retried. Instead: the summary is generated from the findings list, and every "pass" links the artifact that proves it (LG-122, LG-132). Severity: BLOCK.

## Gates

- **G-LG-061 — Evidence-completeness check.** Verifies: LG-122, LG-123. Check (automated): script the audit register — every applicable control must have a linked evidence artifact whose file exists and whose test date falls inside its freshness window. Pass: zero controls with missing, unlinked, or expired evidence. Fail: block the audit report — each gap is auto-filed as an open finding. Recorded in: progress.md.
- **G-LG-062 — Claims scan.** Verifies: LG-125, LG-126. Check (automated): scan published marketing pages, legal pages, and store listings against the approved-claims list derived from tested controls; any compliance terminology not on the list fails the check. Pass: zero unapproved claims live. Fail: block publication and file a finding per claim. Recorded in: progress.md.
- **G-LG-063 — Flow-drill execution.** Verifies: LG-124. Check (manual, scripted steps): execute the drill set end to end — one DSAR request through to delivery, the consent matrix across banner states, the license scan, one acceptance-record pull, one audit-trail pull — and file each output as evidence. Pass: every drill completes and its artifact is filed with today's date. Fail: the failing drill's control is recorded as failing; the audit does not close. Recorded in: progress.md.
- **G-LG-064 — Findings-integrity check.** Verifies: LG-127, LG-128. Check (automated): scan the findings list — every open finding has severity, owner, and remediation date; every closed finding links a re-test artifact dated after the finding. Pass: no ownerless or dateless findings, no closure without re-test evidence. Fail: block the audit report. Recorded in: progress.md.
- **G-LG-065 — Audit-record check.** Verifies: LG-129, LG-131, LG-132. Check (manual): read the filed audit record — scope, cadence/trigger for this run, tests run, and findings are all present in the audit trail, and the report's wording contains no certification or legal-verdict language. Pass: all present, no verdict wording. Fail: the audit is re-issued before anyone relies on it. Recorded in: progress.md.

## Anti-patterns

- **Audit theatre.** The audit is scheduled for the week before a sales deadline and scopes itself to whatever already passes. Catch it by comparing scope against the register: any applicable row excluded without a written reason means the audit was staged.
- **Same-hands review.** The person who built a flow also runs its audit test and files the evidence. Catch it in the audit record: tester and builder are the same name on the controls that matter most.
- **Finding evaporation.** Findings from the last audit are absent from this one — neither closed with re-test evidence nor carried over. Catch it by diffing consecutive findings lists; a vanished finding is itself a finding.
- **Evidence hoarding.** Artifacts are filed as screenshots with no date, no test name, and no link from the control they supposedly prove. Catch it by picking one passing control at random and trying to reconstruct what was tested, when, and by whom from the artifact alone.

## Examples

- [Example 1 — The 94% dashboard](examples/example-1.md) — violates/corrects LG-127.
- [Example 2 — The policy that "passed" retention](examples/example-2.md) — violates/corrects LG-124.
- [Example 3 — The footer claim](examples/example-3.md) — violates/corrects LG-125.

## Recall anchors

- Evidence beats assertion: no dated artifact, the control is failing.
- Test the flow, never the document that describes it.
- Findings are defects with owners and dates — never a percentage.
- Closure means the failed test was re-run and passed.
- The audit prepares for qualified review; it certifies nothing.

## Checklist

- [ ] Every applicable register row was in scope, or its exclusion is written with a reason (LG-121).
- [ ] Every control names control, test, evidence artifact, and last test date (LG-122, G-LG-061).
- [ ] Every pass rests on a dated artifact from executing the real flow (LG-123, LG-124, G-LG-063).
- [ ] All public surfaces were swept and every claim maps to a tested control (LG-125, G-LG-062).
- [ ] Framework results are reported inside their own scopes, never as legal compliance (LG-126).
- [ ] Every finding has severity, owner, and remediation date; no score or percentage was emitted (LG-127, G-LG-064).
- [ ] No finding was closed without a filed re-test, and the audit record itself is in the trail with no certification wording (LG-128, LG-131, LG-132, G-LG-065).
