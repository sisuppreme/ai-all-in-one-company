# user-stories

## Metadata

- **Owner department:** D1 Product & Requirements (PR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Mike Cohn / Mountain Goat Software, "What Makes a Good User Story?" (INVEST) — https://www.mountaingoatsoftware.com/agile/user-stories/good-user-stories
- **Depends on:** personas-jtbd, requirements-writing
- **Feeds into:** acceptance-criteria, scope-control

## When to use / Do NOT use

- **Use when:** validated needs and requirements must become iteration-sized work items a team can build and confirm; a backlog is being refined.
- **Do NOT use when:** the work has no user-visible benefit (label it a task under PR-084), or the need behind the item has not been validated (return to discovery). Do not use story format to give technical work borrowed legitimacy.

## Rules

1. **PR-081 — Template is mandatory.** Every story reads: "As a [role], I want [capability], so that [benefit]." All three parts are present and non-empty.
2. **PR-082 — The role is a named persona.** The role names a persona or segment from the persona set. Bare "user" is allowed only when the capability serves every segment identically, and the story states that reason on its face.
3. **PR-083 — The benefit clause is real.** The "so that" states an outcome the role values. A clause that restates the capability ("so that I can use the feature") fails.
4. **PR-084 — Tasks are labeled tasks.** Work with no user-visible benefit — endpoints, migrations, refactors — is labeled a task and planned as one. It never wears story format.
5. **PR-085 — One iteration maximum.** A story too big to finish in one iteration is split before estimation, along workflow steps or business rules — never along technical layers.
6. **PR-086 — No story without criteria.** A story enters build only with at least one linked acceptance criterion (see acceptance-criteria).
7. **PR-087 — The conversation is recorded.** Decisions from the story conversation (card–conversation–confirmation) are written on the story before build. An unrecorded agreement does not exist.
8. **PR-088 — Splits keep value whole.** Each story produced by a split still delivers a complete, usable slice of value to its role. A split producing a fragment nobody can use is re-split.
9. **PR-089 — Stories trace upward.** Each story links to its parent opportunity ID or requirement ID, which must resolve.
10. **PR-090 — INVEST is a diagnostic, not a score.** Independent, Negotiable, Valuable, Estimable, Small, and Testable are checked at refinement; a failing letter triggers a fix or a recorded exception — never a points chase.

## BAN list

- **BAN-PR-041 — The bare-user story.** Banned: "As a user…" where segments differ in need, permission, or outcome. Defeats: DET-CON-028. Bad: "As a user, I want to export reports" — only dispatchers may export; drivers must not, and the story hides the rule. Instead: "As a dispatch lead, I want to export the filtered order list, so that I can send month-end totals to finance." Severity: BLOCK.
- **BAN-PR-042 — The disguised task.** Banned: technical work dressed as a story to borrow its legitimacy. Defeats: DET-CON-028. Bad: "As a user, I want an API endpoint for bulk import, so that the system has an endpoint." Instead: label it a task, link it to the story it enables, and plan it as engineering work. Severity: WARN.
- **BAN-PR-043 — The benefit-less story.** Banned: a story with no "so that" clause, or a clause that restates the capability. Defeats: DET-CON-028. Bad: "As a manager, I want a dashboard so that I can see the dashboard." Instead: "As a dispatch lead, I want late orders flagged on one screen, so that I can reassign drivers before customers call." Severity: BLOCK.
- **BAN-PR-044 — The epic in story's clothing.** Banned: estimating or scheduling, as a single story, work that cannot finish in one iteration. Defeats: DET-CON-028. Bad: "As a dispatcher, I want full reporting" enters the sprint and is still "in progress" three iterations later, its behavior never defined. Instead: split along the workflow (view late orders → export totals → schedule recurring sends) and estimate the pieces. Severity: WARN.

## Gates

- **G-PR-041 — Story template lint.** Verifies: PR-081, PR-082, PR-083. Check: automated — run a regex over every story confirming the "As a [role], I want [capability], so that [benefit]" shape, and that the role matches a persona name or carries the all-segments note. Pass: 100% of stories conform. Fail: block refinement sign-off. Recorded in: progress.md.
- **G-PR-042 — Criteria linkage.** Verifies: PR-086. Check: automated — run a tracker query confirming no story in "in build" status has zero linked acceptance criteria. Pass: zero violations. Fail: block the status change until criteria are attached. Recorded in: progress.md.
- **G-PR-043 — Split review.** Verifies: PR-085, PR-088. Check: manual — every story estimated above the team's one-iteration threshold shows its split, and each child story delivers usable value on its own. The review also judges each story's benefit clause: a benefit that merely repeats the capability text (a semantic judgment no lint can make) is sent back for rewriting. Pass: all oversized stories are split into whole-value pieces and no benefit clause repeats its capability. Fail: block estimation. Recorded in: progress.md.
- **G-PR-044 — Traceability spot check.** Verifies: PR-089. Check: automated — run a script confirming every story carries an opportunity or requirement ID that resolves in its source file. Pass: 100% resolve. Fail: warn, and fix before build. Recorded in: progress.md.

## Anti-patterns

- **Story as mini-spec.** The card carries paragraphs of solution detail, killing the conversation it exists to start. Catch it: if the card text is longer than the recorded conversation notes, the card became the spec.
- **Horizontal slicing.** "Build the database part" written as a story. Catch it: ask who can use the finished slice; if the answer is "nobody yet," re-split vertically along the workflow.
- **Persona name-dropping.** The story names a persona, but the benefit is the business's, not the persona's. Catch it: read the benefit clause aloud from the persona's seat; if the persona would not say it, rewrite.
- **Solution-first wording.** The capability names the implementation ("I want a modal dialog…") instead of the outcome sought. Catch it: replace the named widget with its purpose; if the story collapses, it was a design instruction, not a story.

## Examples

- [Example 1 — Replacing the bare "user" with a named persona](examples/example-1.md) — corrects PR-082.
- [Example 2 — Relabeling a disguised task](examples/example-2.md) — corrects PR-084.
- [Example 3 — Splitting an epic along the workflow](examples/example-3.md) — corrects PR-085, PR-088.

## Recall anchors

- As a named persona, I want a capability, so that a real benefit.
- No benefit clause, no story.
- Tasks are tasks — label them honestly.
- Split along the workflow, never along the layers.
- No criteria, no build.

## Checklist

- [ ] Every story passes the template lint (G-PR-041).
- [ ] Every role is a named persona or carries the all-segments reason (PR-082).
- [ ] Every benefit clause states an outcome, not the capability restated (PR-083).
- [ ] Technical work is labeled as tasks, not stories (PR-084).
- [ ] No story in build has zero acceptance criteria (G-PR-042).
- [ ] Oversized stories are split into whole-value pieces (G-PR-043).
- [ ] Every story traces to an opportunity or requirement ID (G-PR-044).
