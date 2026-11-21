# discovery

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Torres, Opportunity Solution Tree — https://www.chameleon.io/blog/opportunity-solution-tree ; Torres, *Continuous Discovery Habits* (Product Talk Press, 2021), method summary — https://glasp.co/posts/teresa-torres-how-to-master-continuous-discovery-for-product-success-glasp-talk-31
- **Depends on:** none — standalone: discovery starts from raw customer evidence gathered directly (interviews, support tickets, usage notes the user supplies); no other skill's output is an input. Its findings feed user-research, personas-jtbd, requirements-writing, and roadmapping.
- **Feeds into:** user-research, personas-jtbd, requirements-writing, roadmapping

## When to use / Do NOT use

- **Use when:** a product or major feature is being shaped; the team must decide what to build next; a backlog is filling with solutions nobody has traced to a customer need.
- **Do NOT use when:** the work is a defined fix or a committed delivery item with acceptance criteria already attached — go to user-stories and acceptance-criteria instead. Do not use discovery to re-litigate a decision already recorded with its evidence.

## Rules

1. **PR-001 — One desired outcome per tree.** The Opportunity Solution Tree carries exactly one desired outcome at its root; every opportunity, solution, and assumption test hangs from that outcome.
2. **PR-002 — Opportunities are needs, not solutions.** Every opportunity node is framed as a customer need, pain, or desire in the customer's terms. A node naming a feature or build task is reclassified as a solution and moved down the tree.
3. **PR-003 — No backlog entry without an opportunity.** A solution enters the backlog only with a non-empty opportunity ID linking it to a node on the tree.
4. **PR-004 — Evidence is specific-moment stories.** Interview evidence is recorded as stories about specific past moments (who, when, what happened). Summarized opinions and feature requests are recorded as interpretation, never as evidence.
5. **PR-005 — Weekly customer touchpoints.** While the product is in active development, discovery runs at least one customer touchpoint per week; a week with none is logged as a gap in the discovery record.
6. **PR-006 — Assumption list before commitment.** Every candidate solution carries an explicit assumption list covering desirability, usability, feasibility, and viability before any build commitment is made.
7. **PR-007 — Riskiest assumption first.** Assumption tests are ordered by importance multiplied by lack of evidence; the most important, least-evidenced assumption is tested before all others.
8. **PR-008 — Target opportunity chosen by comparison.** The target opportunity is selected by comparing at least two candidate opportunities on size, frequency, and strategic fit, and the comparison is recorded on the tree.
9. **PR-009 — No test, no cycle.** A discovery cycle that produces no assumption test is incomplete and cannot close, however many interviews it ran.
10. **PR-010 — Degradation path when no customers are reachable.** When no real customers can be interviewed, evidence comes only from user-supplied material (interview notes, support tickets, analytics exports). Anything inferred beyond that material is labeled UNVERIFIED and cannot be cited by personas-jtbd or requirements-writing.

## BAN list

- **BAN-PR-001 — Solution-first backlog.** Banned: a backlog item naming a feature with no opportunity ID on the tree. Defeats: DET-CON-028. Bad: "Add push notifications" enters the sprint with no parent opportunity. Instead: frame the opportunity ("I need to know my ride is arriving before it reaches my stop") and attach the solution to it. Severity: BLOCK.
- **BAN-PR-002 — Opinion recorded as evidence.** Banned: writing summarized opinions ("users love dashboards") into the evidence record as if they were interview findings. Defeats: DET-CON-014. Bad: the research file states "Customers want better reporting" with no moment, participant, or date. Instead: record the specific story ("On March 3, the dispatcher re-exported the CSV three times because totals were missing"). Severity: BLOCK.
- **BAN-PR-003 — Invented interview findings.** Banned: writing findings, quotes, or participant counts for interviews that never happened. Defeats: DET-CON-011. Bad: "12 of 15 users asked for dark mode" with no study behind it. Instead: mark the claim UNVERIFIED with no downstream citation rights, or run the interviews. Severity: BLOCK.
- **BAN-PR-004 — Feature-request transcription.** Banned: converting one customer's feature request directly into a backlog commitment without mapping it to an opportunity and testing its assumptions. Defeats: DET-CON-028. Bad: one enterprise prospect asks for an SSO export and it ships next sprint, untested. Instead: place the underlying need on the tree, compare candidate solutions, and test the riskiest assumption first. Severity: WARN.

## Gates

- **G-PR-001 — Backlog opportunity lint.** Verifies: PR-003. Check: automated — run a script over the backlog export confirming every item has a non-empty `opportunity_id` field whose value exists on the tree. Pass: 100% of items carry a valid ID. Fail: block intake of the items missing IDs. Recorded in: progress.md.
- **G-PR-002 — Assumption map presence.** Verifies: PR-006, PR-007. Check: manual — for the target opportunity, confirm an assumption map exists, the riskiest assumption is named, and a test is attached to it. Pass: all three present before build starts. Fail: block build start. Recorded in: progress.md.
- **G-PR-003 — Evidence format audit.** Verifies: PR-004, PR-010. Check: manual — sample 5 evidence entries; each names a specific moment or carries the UNVERIFIED label with a user-supplied source. Pass: 5 of 5 conform. Fail: warn; an entry failing twice is removed from the record. Recorded in: progress.md.
- **G-PR-004 — Cycle completeness.** Verifies: PR-009. Check: manual — review the cycle record for at least one assumption test whose result is written back onto the tree. Pass: test and result both present. Fail: the cycle stays open and blocks handoff to delivery planning. Recorded in: progress.md.

## Anti-patterns

- **Interview theater.** Many interviews run, stories get summarized into opinions, and no assumption is ever tested. Catch it: count tests per cycle — zero means the cycle was theater, whatever the interview count says.
- **Tree as decoration.** The tree exists, but backlog items are created directly in the tracker and back-linked later, or never. Catch it: check creation order — the opportunity ID must exist before the backlog item does.
- **Solution-shaped opportunities.** Nodes are phrased as "add X" so every opportunity maps one-to-one to a feature. Catch it: read the nodes aloud; if a node could be a ticket title, it is a solution.
- **Cherry-picked stories.** Only stories supporting the favored solution make it into the record. Catch it: look for disconfirming stories in the evidence file; their complete absence is the tell.

## Examples

- [Example 1 — Framing an opportunity as a need](examples/example-1.md) — corrects PR-002.
- [Example 2 — Recording evidence as a specific-moment story](examples/example-2.md) — corrects PR-004.
- [Example 3 — Assumption list with the riskiest assumption tested first](examples/example-3.md) — corrects PR-006, PR-007.

## Recall anchors

- One outcome, one tree.
- Opportunities are needs; features are solutions.
- Stories about moments, not opinions.
- Test the riskiest assumption first.
- No test, no cycle.

## Checklist

- [ ] The tree root is a single desired outcome (PR-001).
- [ ] Every opportunity node is a need, not a solution (PR-002).
- [ ] Backlog lint passes: 100% of items carry a valid opportunity ID (G-PR-001).
- [ ] The target opportunity was chosen by recorded comparison (PR-008).
- [ ] The assumption map names the riskiest assumption with a test attached (G-PR-002).
- [ ] Evidence entries are specific moments or labeled UNVERIFIED (PR-004, PR-010).
- [ ] The cycle closes only with a recorded test result (PR-009).
