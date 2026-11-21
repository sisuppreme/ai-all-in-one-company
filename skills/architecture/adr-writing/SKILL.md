# adr-writing

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** MADR — Markdown Architectural Decision Records (template and guidance) — https://adr.github.io/madr/
- **Depends on:** none — standalone: an ADR is written from the decision itself, as made with the user against the codebase at hand; it consumes no other skill's output. The recorded decisions feed stack-selection, system-design, and decision-logs.
- **Feeds into:** stack-selection, system-design, decision-logs

## When to use / Do NOT use

- **Use when:** a significant, hard-to-reverse decision is being made — stack components, tenancy model, API paradigm, pattern adoption, data ownership — or an existing decision is being revisited or reversed.
- **Do NOT use when:** the choice is trivially reversible or purely local (a variable name, a file layout inside one module); record those in code review and move on. Do not use an ADR as the design document itself — the design lives in ARCHITECTURE.md or the contract, and the ADR links to it.

## Rules

1. **AR-241 — One file per decision.** Each record is its own MADR file in `docs/decisions/`, numbered `NNNN-title.md`; a file deciding two questions is split.
2. **AR-242 — Full MADR sections.** Every record carries: title, status, context and problem statement, decision drivers, considered options, decision outcome, and consequences.
3. **AR-243 — At least two considered options.** The rejected alternative and the reason it lost are mandatory. An ADR with one option is incomplete: the rejected option is the record's most valuable content.
4. **AR-244 — At least one negative consequence.** Consequences include at least one negative or cost. An all-positive consequences section means the trade-off was not examined, and the record is sent back.
5. **AR-245 — Immutable once accepted.** An accepted ADR is never edited to change its decision. A change of mind is a new ADR that supersedes the old one, linked in both directions.
6. **AR-246 — Status is maintained.** When a decision is reversed, the old record's status becomes "superseded by NNNN" in the same commit as the new ADR. The folder never holds two contradictory "accepted" records on the same question.
7. **AR-247 — Titles state the decision.** The title is the decision in a sentence — "Use PostgreSQL for the primary store" — not the topic, "Database discussion."
8. **AR-248 — Written with the work.** The ADR lands in the same change as the work it governs, while the alternatives are still genuinely remembered, not reconstructed weeks later.
9. **AR-249 — Decisions, not designs.** The ADR records the choice and its reasoning; the full design lives in ARCHITECTURE.md or the contract, and the ADR links to it instead of copying it.
10. **AR-250 — Every significant decision gets one.** If reversing the choice would cost more than a day's work, it needs an ADR: stack components, tenancy model, paradigm, pattern adoptions, data ownership.
11. **AR-251 — Drivers before options.** Decision drivers and selection criteria are recorded before options are scored against them; criteria written after the winner is known are rationalization.
12. **AR-252 — Links resolve.** Supersedes and superseded-by links, and every referenced diagram, contract, and ADR, point at files that exist.

## BAN list

- **BAN-AR-121 — The silent swap.** Banned: changing a settled, ADR-backed decision with no new ADR recording the change. Defeats: DET-CODE-031. Bad: the accepted ADR says PostgreSQL; a pull request quietly moves the project to MongoDB because a tutorial used it, and six months later nobody can reconstruct why the database changed. Instead: write the superseding ADR with the new decision's drivers and rejected alternatives, and update the old record's status in the same commit. Severity: BLOCK.
- **BAN-AR-122 — Editing history.** Banned: modifying an accepted ADR's decision, options, or consequences in place. Defeats: DET-CODE-032. Bad: after the chosen vendor raises prices, the ADR's consequences section is quietly rewritten to remove the cost warning it originally carried, so the decision looks better than it was. Instead: leave the record untouched; write a new ADR that supersedes it and states what changed. Severity: BLOCK.
- **BAN-AR-123 — The all-positive record.** Banned: a consequences section listing only benefits. Defeats: DET-CODE-021. Bad: "Consequences: faster development, happier team, modern stack" — a record that narrates approval instead of explaining a trade-off, useless to the reader who must later decide whether to reverse it. Instead: name at least one real cost (operational burden, lock-in, a capability given up) and who bears it. Severity: WARN.
- **BAN-AR-124 — Topic titles.** Banned: titling an ADR with its subject area instead of its decision. Defeats: DET-CODE-008. Bad: `0007-database-discussion.md` — the title tells a future reader nothing about what was decided, and the decisions folder becomes unsearchable. Instead: `0007-use-postgresql-for-the-primary-store.md`. Severity: WARN.

## Gates

- **G-AR-121 — ADR lint.** Verifies: AR-242, AR-243, AR-245, AR-252. Check: automated — a script over `docs/decisions/` asserts every file parses, carries a status from the allowed set (proposed, accepted, deprecated, superseded by NNNN), has a considered-options section with at least two options, and that superseded records link to an existing successor. Pass: zero violations. Fail: block merge. Recorded in: progress.md.
- **G-AR-122 — Manifest cross-check.** Verifies: AR-250. Check: automated — every top-level dependency in the project's manifest maps to an ADR (by name or tag match). Pass: every major dependency has a record. Fail: block the dependency addition until its ADR exists. Recorded in: progress.md.
- **G-AR-123 — Reconstruction test.** Verifies: AR-243, AR-244. Check: manual — sample one ADR and confirm a reader who was not present can reconstruct why the choice was made, including what was given up, without interviewing the author. Pass: the reader's summary matches the decision's actual drivers. Fail: warn; the record is expanded before the next release. Recorded in: progress.md.
- **G-AR-124 — Contradiction scan.** Verifies: AR-246. Check: manual — at each release, scan the accepted ADRs for two records deciding the same question differently. Pass: no contradictory pair marked accepted. Fail: block release until one is superseded. Recorded in: progress.md.

## Anti-patterns

- **The ADR graveyard.** Records are written for trivial choices while significant ones go unrecorded, because writing was easier for the small ones. Catch it: sort by consequence — if the folder's biggest file decides a CSS framework and the database has no record, the practice is inverted.
- **Retroactive rationalization.** The ADR is written weeks after the decision, inventing alternatives that were never genuinely considered. Catch it: compare the ADR's commit date with the work it governs (AR-248); a long gap with suspiciously complete options is the tell.
- **The mega-ADR.** One file decides the stack, the topology, and the tenancy model at once, so none of them can be superseded independently. Catch it: count the decisions in the file; more than one means split it.
- **Status rot.** Superseded decisions still read "accepted" because nobody updated them, and a new team member follows a dead decision in good faith. Catch it: the contradiction scan (G-AR-124) exists precisely for this; a folder never scanned is rotting.

## Examples

- [Example 1 — The single-option ADR, completed](examples/example-1.md) — corrects AR-243.
- [Example 2 — A reversal done as a superseding pair](examples/example-2.md) — corrects AR-245, AR-246.
- [Example 3 — Topic title and brochure consequences, fixed](examples/example-3.md) — corrects AR-247, AR-244.

## Recall anchors

- One file, one decision, at least two options.
- The rejected alternative is the most valuable part.
- Every record names a cost.
- Accepted records are immutable; reversal means a new ADR.
- The title is the decision, not the topic.

## Checklist

- [ ] The record is one MADR file, titled with the decision (AR-241, AR-247).
- [ ] Considered options number at least two, with the loser's reason stated (AR-243).
- [ ] Consequences include at least one negative or cost (AR-244).
- [ ] Decision drivers were recorded before options were scored (AR-251).
- [ ] ADR lint passes over `docs/decisions/` (G-AR-121).
- [ ] If this reverses a decision, the old record's status is updated in the same commit (AR-246).
- [ ] The ADR links to the design instead of copying it, and all links resolve (AR-249, AR-252).
