# requirements-writing

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** ISO/IEC/IEEE 29148:2018, IEEE Standards Association — https://standards.ieee.org/ieee/29148/6937/ ; 29148 tutorial and characteristic list — https://www.xopsschool.com/mod/page/view.php?id=3365
- **Depends on:** discovery, user-research, personas-jtbd
- **Feeds into:** user-stories, acceptance-criteria, scope-control

## When to use / Do NOT use

- **Use when:** stakeholder needs must become a specification a builder can implement and a tester can verify; a requirement set is being drafted, reviewed, or changed.
- **Do NOT use when:** the need itself is still unexplored (discovery and user-research come first) or the work item is an iteration-sized story (user-stories). Do not write requirements to document a design that was already chosen — that reverses the trace.

## Rules

1. **PR-061 — One obligation per requirement.** Each requirement carries exactly one "shall". A requirement containing two obligations is split into two requirements before review.
2. **PR-062 — Mandatory attributes.** Every requirement carries a unique ID, source (stakeholder need or finding), priority, rationale, and verification method. A requirement missing any attribute is incomplete and cannot be baselined.
3. **PR-063 — Vague terms need numbers.** The terms fast, user-friendly, robust, seamless, flexible, and their synonyms are banned unless the same sentence states the measurable criterion the term stands for.
4. **PR-064 — Need, not design.** Requirements state the need. An implementation choice appears only as a labeled design constraint backed by a real external constraint, which is named.
5. **PR-065 — Conflicts resolved on record.** Conflicting requirements are resolved explicitly and the resolution is recorded with its decider. Wording is never averaged to hide a conflict.
6. **PR-066 — Bidirectional traceability.** Every requirement traces back to a stakeholder need and forward to at least one design element and one acceptance test. An orphan in either direction is a defect.
7. **PR-067 — Changes are versioned.** A requirement change goes through review and appears in the version history with date and decider. A silently edited requirement is treated as new and unvalidated.
8. **PR-068 — Set-level completeness.** Before handoff, the set is checked as a whole: every stakeholder need is covered by at least one requirement, and no two requirements contradict each other.
9. **PR-069 — Verifiable by construction.** Each requirement names its verification method (test, demonstration, inspection, or analysis) at the time it is written. A requirement with no method is rewritten until it has one.
10. **PR-070 — Negative requirements are explicit.** What the system must not do — data it must not retain, behaviors it must forbid — is written as requirements, not left implied by the positive ones.
11. **PR-071 — One priority per requirement.** Each requirement carries exactly one priority from the project's scheme. A requirement marked with two priorities is resolved before handoff.

## BAN list

- **BAN-PR-031 — The compound requirement.** Banned: one requirement ID carrying two or more obligations. Defeats: DET-CON-028. Bad: "REQ-14: The system shall send email and SMS notifications and log all deliveries." Instead: three requirements, one obligation each, each with its own verification method. Severity: BLOCK.
- **BAN-PR-032 — The adjective requirement.** Banned: a requirement whose only success test is a vague adjective. Defeats: DET-CON-028. Bad: "The dashboard shall load fast and feel seamless." Instead: "The dashboard shall render first contentful paint within 2.0 seconds on the reference device against the reference dataset." Severity: BLOCK.
- **BAN-PR-033 — The silent edit.** Banned: changing a requirement's text without a version-history entry. Defeats: DET-CON-015. Bad: the seat limit is edited from 5 to 10 in the document; the build team and the copy team keep working from different numbers and the site ends up contradicting itself. Instead: edit, add a history entry (date, decider, reason), and notify the owners of linked artifacts. Severity: BLOCK.
- **BAN-PR-034 — Solution smuggled in as a need.** Banned: prescribing an implementation as a requirement with no external constraint behind it. Defeats: DET-CON-014. Bad: "The system shall use a React single-page app" in the requirements for a content site, where nothing external forces the choice. Instead: state the need ("The configurator flow shall update without full page reloads") or label the item a design constraint and name its external source. Severity: WARN.

## Gates

- **G-PR-031 — Requirement lint.** Verifies: PR-061, PR-062, PR-063. Check: automated — run a script over the requirements file confirming (a) ID, source, priority, rationale, and verification method are present and non-empty for 100% of requirements, (b) each requirement contains exactly one "shall", and (c) every banned vague term is flagged unless its sentence contains a number or unit. Pass: zero violations. Fail: block handoff. Recorded in: progress.md.
- **G-PR-032 — Traceability coverage.** Verifies: PR-066. Check: automated — generate the coverage report: every Must-priority requirement has at least one linked source need and at least one linked acceptance criterion or test. Pass: 100% coverage. Fail: block handoff to build. Recorded in: progress.md.
- **G-PR-033 — Conflict and set review.** Verifies: PR-065, PR-068. Check: manual — review the set against the stakeholder need list: confirm full coverage and read every recorded conflict for its resolution and decider. Pass: no uncovered need, no unresolved conflict. Fail: block handoff. Recorded in: progress.md.
- **G-PR-034 — Change-history audit.** Verifies: PR-067. Check: automated — diff the current requirements against the last baselined version; every changed ID must appear in the version history. Pass: 100% of changes logged. Fail: warn, and unlogged changes revert to unvalidated status until reviewed. Recorded in: progress.md.

## Anti-patterns

- **Gold-plating by adjective.** Requirements padded with "world-class" and "enterprise-grade" that test nothing. Catch it: search for adjectives with no number in the same sentence; each one is a requirement that cannot fail, and therefore cannot pass either.
- **Copy-paste requirement sets.** A template's requirements shipped with the product name swapped in. Catch it: look for obligations referencing capabilities this product does not have, or needs no stakeholder ever stated.
- **The TBD method.** Verification method fields filled with "TBD" to pass a presence check. Catch it: the lint treats "TBD" as empty; if your draft relies on it, the requirement is not yet verifiable by construction.
- **Traceability theater.** Links added in bulk at handoff time to satisfy the coverage report, pointing at tests that do not exercise the requirement. Catch it: open two links at random and read the test; if it would pass with the requirement deleted, the link is theater.

## Examples

- [Example 1 — Splitting a compound requirement](examples/example-1.md) — corrects PR-061.
- [Example 2 — Making a vague requirement measurable](examples/example-2.md) — corrects PR-063.
- [Example 3 — A fully traced requirement](examples/example-3.md) — corrects PR-066.

## Recall anchors

- One shall, one obligation, one requirement.
- No number, no adjective.
- Need first; design only as a labeled constraint.
- Every requirement traces backward and forward.
- A silent edit makes a new requirement.

## Checklist

- [ ] Requirement lint passes with zero violations (G-PR-031).
- [ ] Every requirement carries ID, source, priority, rationale, and verification method (PR-062).
- [ ] Traceability coverage is 100% for Must requirements (G-PR-032).
- [ ] All conflicts carry a recorded resolution and decider (PR-065).
- [ ] Negative requirements are written, not implied (PR-070).
- [ ] Every change since baseline appears in the version history (G-PR-034).
- [ ] The set covers every stakeholder need (PR-068).
