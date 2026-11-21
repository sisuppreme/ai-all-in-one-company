# architecture-patterns

## Metadata

- **Owner department:** D2 Architecture & System Design (AR)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** Microservices.io pattern language (Saga, CQRS, event sourcing, transactional outbox, database per service) — https://microservices.io/ ; Fowler, "What do you mean by 'Event-Driven'?" — https://www.martinfowler.com/articles/201701-event-driven.html
- **Depends on:** system-design, adr-writing
- **Feeds into:** api-architecture, event-driven, domain-driven-design

## When to use / Do NOT use

- **Use when:** a distributed-systems or structural pattern (Saga, CQRS, event sourcing, transactional outbox, database per service, and their kin) is proposed for a project, or an existing design claims a pattern that needs auditing.
- **Do NOT use when:** the choice is a routine local design decision with no cross-component consequences — record it in code and move on. Do not use this skill to pick libraries or frameworks; that is stack-selection.

## Rules

1. **AR-161 — Named catalog only.** Patterns are selected from a named catalog (the microservices.io pattern language, Fowler's pattern writings) and cited by their catalog name; invented pattern names are not adopted.
2. **AR-162 — Problem before pattern.** No pattern is adopted without a stated problem it solves in this project. "For scale" without a load figure is not a problem statement.
3. **AR-163 — Four-part adoption record.** Before adoption, the ADR fills in all four parts from the catalog entry: the problem, the forces, the solution shape, and the consequences for this project.
4. **AR-164 — The hard part is the deliverable.** Adopting Saga requires named compensating transactions; CQRS requires the read-model synchronization design; event sourcing requires the event store and replay procedure. The label without the mechanism is not an adoption.
5. **AR-165 — No decorative infrastructure.** A queue or broker in the diagram while all interactions remain synchronous request/response is decoration and fails review.
6. **AR-166 — Consequences accepted in writing.** Every adoption records the consequences it accepts — eventual-consistency window, operational components added, new failure modes — in the ADR.
7. **AR-167 — Simplest variant first.** Prefer choreography before orchestration for short sagas and a single read model before multiple. The ADR records what measured change would trigger the complex variant.
8. **AR-168 — One pattern at a time.** Patterns are adopted incrementally, each behind its own ADR; a big-bang re-architecture introducing several at once is not approved.
9. **AR-169 — Default composition.** The default for a typical web application is a modular monolith with feature modules. A distributed composition must cite the requirement that forces it.
10. **AR-170 — Exit cost noted.** Every adoption records what removing or replacing the pattern would cost, so the decision can be revisited honestly.
11. **AR-171 — The mechanism must exist in code.** A pattern claimed in ARCHITECTURE.md must have its mechanism findable in the codebase — the outbox table, the compensating handlers, the read model. A claim without a mechanism is marked false.
12. **AR-172 — Module boundaries are enforced.** Modules and contexts expose public interfaces; cross-module imports of internals are forbidden and checked mechanically.

## BAN list

- **BAN-AR-081 — Pattern adopted "for scale".** Banned: adopting a distributed pattern with no stated problem and no load figure behind it. Defeats: DET-CODE-015. Bad: a three-user internal tool is split into six services with a saga "because it will need to scale," and every deploy now takes an afternoon. Instead: state the problem the pattern solves here, with the number that proves it, or stay with the modular monolith. Severity: BLOCK.
- **BAN-AR-082 — Decorative broker.** Banned: installing a queue or broker while every interaction stays synchronous request/response. Defeats: DET-CODE-003. Bad: RabbitMQ runs in production, the architecture page says "event-driven," and the only producer sends messages that a consumer immediately answers while the HTTP request blocks waiting. Instead: either adopt a named event pattern with its contract and consumers, or remove the broker and the claim. Severity: BLOCK.
- **BAN-AR-083 — Saga without compensations.** Banned: claiming the Saga pattern with no compensating transaction defined for each step. Defeats: DET-CODE-006. Bad: the checkout saga reserves stock, charges the card, then fails at shipping — and nothing releases the stock or refunds the charge, because the compensations were "phase two." Instead: name and implement the compensation for every step before the saga ships; a step with no compensation is a step the saga may not take. Severity: BLOCK.
- **BAN-AR-084 — Reach-around imports.** Banned: one module importing another module's internal files, bypassing its public interface. Defeats: DET-CODE-014. Bad: the billing module imports `orders/internal/pricing.ts` directly, so the orders team cannot refactor pricing without breaking billing. Instead: consume the module's published interface, or propose the missing capability as part of that interface. Severity: BLOCK.

## Gates

- **G-AR-081 — Pattern audit.** Verifies: AR-164, AR-171. Check: manual — for each pattern claimed in ARCHITECTURE.md, find its mechanism in code (outbox table, compensating handlers, read model) or mark the claim false. Pass: every claimed pattern has a mechanism. Fail: block release until the mechanism exists or the claim is removed. Recorded in: progress.md.
- **G-AR-082 — Dependency-rule check.** Verifies: AR-172. Check: automated — CI lint rules forbid cross-module imports except through public interfaces. Pass: lint exits 0. Fail: block merge. Recorded in: progress.md.
- **G-AR-083 — Adoption record completeness.** Verifies: AR-162, AR-163, AR-166, AR-170. Check: manual — each adopted pattern's ADR contains the problem with its evidence, the forces, the accepted consequences, and the exit cost. Pass: all four parts present for every adopted pattern. Fail: block adoption. Recorded in: progress.md.
- **G-AR-084 — Simplicity review.** Verifies: AR-167, AR-169. Check: manual — for each adoption of Saga, CQRS, or event sourcing, confirm the ADR states why the simpler default was insufficient and what trigger would justify the complex variant. Pass: both statements present. Fail: warn; the adoption proceeds only with the trigger recorded. Recorded in: progress.md.

## Anti-patterns

- **Pattern bingo.** CQRS, event sourcing, and a saga all appear in a CRUD application whose hardest query is a filtered list. Catch it: count the patterns; each one should be able to name the problem that forced it, and most CRUD apps force none.
- **Resume-driven architecture.** Technologies chosen because the builder wants to learn them, with the project paying the tuition. Catch it: the ADR's forces section talks about the team's growth, not the project's constraints.
- **The distributed monolith.** Services split by technical layer, deployed together, chatting synchronously on every request — distribution's costs with none of its benefits. Catch it: if all services must deploy in lockstep to work, it is a monolith with network calls.
- **Cargo-cult topology.** Copying a hyperscaler's architecture at three orders of magnitude less load. Catch it: compare the design's load figures with the figures in the case study it imitates.

## Examples

- [Example 1 — "For scale" becomes a forcing-requirement test](examples/example-1.md) — corrects AR-162, AR-169.
- [Example 2 — The decorative queue, made real or removed](examples/example-2.md) — corrects AR-165.
- [Example 3 — A saga adoption with its compensations named](examples/example-3.md) — corrects AR-164.

## Recall anchors

- Problem before pattern, always.
- The hard part is the deliverable, not the label.
- A broker with only synchronous calls is decoration.
- Simplest variant first; record the trigger for the complex one.
- If the mechanism is not in the code, the pattern is not in the system.

## Checklist

- [ ] Every adopted pattern is cited by its catalog name (AR-161).
- [ ] Every adoption's ADR states the problem, with the load figure or evidence behind it (AR-162).
- [ ] Compensations, read-model sync, or replay procedure are named for Saga, CQRS, or event sourcing adoptions (AR-164).
- [ ] Accepted consequences and exit cost are recorded per adoption (AR-166, AR-170).
- [ ] Pattern audit passed: every claimed pattern's mechanism found in code (G-AR-081).
- [ ] Dependency-rule lint exits 0 (G-AR-082).
- [ ] The simplest variant is in place, with the complex variant's trigger recorded (AR-167).
