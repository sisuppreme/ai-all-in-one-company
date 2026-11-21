# contract-testing

## Metadata

- **Owner department:** D8 QA & Testing (QA)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://docs.pact.io/university/introduction/step13
- **Depends on:** integration-testing
- **Feeds into:** qa-gates

## When to use / Do NOT use

- **Use when:** two separately deployable units (web app and API, two services, mobile app and API) integrate over HTTP and either side can change without the other; every consumer expectation a provider must survive is in scope.
- **Do NOT use when:** the integration never crosses a process or network boundary (use integration-testing), or the provider is a third party you cannot run verification against (use its sandbox plus integration-testing instead).

## Rules

1. **QA-161 — Consumer scope only.** The contract records only the interactions and response fields the consumer actually reads, asserted with type matchers, never literal copies of the provider's full response.
2. **QA-162 — Additions pass, breakages fail.** Adding a field to a provider response must never fail a contract; removing or retyping a field a consumer uses must fail provider verification. A contract that cannot tell these apart is rewritten until it can.
3. **QA-163 — Tests generate the pact.** The consumer's suite runs its real HTTP client against the Pact mock server and the pact file is the recorded output of that run; a hand-written or hand-edited pact file is not a contract.
4. **QA-164 — Versioned publication.** Every generated pact is published to the broker (hosted PactFlow or the self-hosted open-source broker) tagged with the consumer version — commit SHA and branch — in the same pipeline run that generated it; an untagged pact is not publishable.
5. **QA-165 — Provider verifies in its own CI.** The provider build fetches every consumer pact for the target environment, replays each interaction against the real provider build, and publishes the verification result back to the broker; no other job may mark a contract verified.
6. **QA-166 — Provider states are real setup code.** Each `given` state is implemented as setup through the provider's own data layer — seeded records, configured tenants, stubbed downstreams — versioned with the provider code; a state never returns a canned response body.
7. **QA-167 — Deployment reads the verdict.** The promotion step runs `pact-broker can-i-deploy` for the exact version and target environment, and a non-zero exit blocks promotion exactly like a failing test; bypass requires a written waiver with owner and expiry recorded in the project log.
8. **QA-168 — Seeded-break negative control.** On every release (and at least weekly), a deliberate retype of a consumer-used field in a scratch provider build must fail provider verification and flip can-i-deploy to not deployable; if it does not, the contract suite itself is treated as broken and blocks release.
9. **QA-169 — Single-repo variant is first-class.** In a one-repo full-stack project the broker is optional and pacts live as files in a named directory, but consumer test, provider verification, and the deploy check still run as three separate, ordered pipeline steps — never merged into one test run.
10. **QA-170 — Errors are interactions.** Contracts cover the non-200 responses the consumer handles — validation errors, 404s, empty lists — with the same matchers, not only happy-path 200s.
11. **QA-171 — Pact changes are reviewed diffs.** A changed pact merges only with a diff description naming the consumer change that caused it; a provider-side regeneration with no consumer change behind it is rejected in review.
12. **QA-172 — Freshness of results.** can-i-deploy is evaluated against verification results for the exact provider version being deployed and the consumer versions live in the target environment; results recorded against an older provider SHA do not satisfy the gate.

## BAN list

- **BAN-QA-081 — Verification against a stub of the provider.** Banned: provider "verification" that replays contracts against recorded responses or a hand-written mock of the provider, so the real provider build never runs. Defeats: DET-FAKE-009. Bad: CI step `verify-contracts` runs the replay against `fixtures/provider-responses.json` and reports success. Instead: provider CI boots the real provider build, replays each interaction against it, and publishes the result to the broker (QA-165). Severity: BLOCK.
- **BAN-QA-082 — A deploy gate that never reads the verdict.** Banned: a pipeline that claims "contracts verified" while can-i-deploy is absent, suffixed with `|| true`, set to continue-on-error, or its exit code ignored. Defeats: DET-INF-002. Bad: deploy job contains `pact-broker can-i-deploy ... || true` and promotes on red verdicts. Instead: the step's exit code gates promotion directly; a red verdict stops the deploy (QA-167). Severity: BLOCK.
- **BAN-QA-083 — Provider states that serve fixtures.** Banned: a provider-state handler that returns or injects a canned response body instead of creating the state through the provider's real data path, so replay exercises fixture data the provider never produced. Defeats: DET-FAKE-017. Bad: state "a user with an order exists" loads `order-fixture.json` straight into the response stub. Instead: the state handler seeds a real user and order through the provider's own models or API, and the replay queries them (QA-166). Severity: BLOCK.
- **BAN-QA-084 — The contract stub shipped as the integration.** Banned: deploying the app wired to the Pact mock or stub server, so users are served canned contract responses presented as the live API. Defeats: DET-FAKE-008. Bad: production build ships with `API_BASE_URL` pointing at the stub server from the contract tests. Instead: stubs exist only inside test runs; the deployed build points at the real provider, whose compatibility the broker verdict certifies (QA-165, QA-167). Severity: BLOCK.

## Gates

- **G-QA-081 — can-i-deploy deploy gate.** Verifies: QA-167, QA-172. Check: the deploy job runs `pact-broker can-i-deploy --pacticipant <provider> --version <provider-sha> --to-environment <env>` before promotion and the job's success requires its exit code. Pass: exit 0 for the exact version and environment being promoted. Fail: block promotion; no merge or manual override without a recorded waiver. Recorded in: progress.md.
- **G-QA-082 — Seeded-break negative control.** Verifies: QA-162, QA-168. Check: scripted change retypes one consumer-used response field in a scratch provider build, then provider verification and can-i-deploy both run. Pass: verification exits non-zero AND can-i-deploy exits non-zero; scratch change reverted afterward. Fail: block the release and treat the contract suite as broken. Recorded in: progress.md.
- **G-QA-083 — Publication completeness.** Verifies: QA-163, QA-164. Check: `pact-broker describe-version --pacticipant <consumer> --version <consumer-sha>` (or broker API query) for every consumer, compared against the count of consumer contract suites in the repo. Pass: every suite has a broker version whose SHA equals the consumer commit under build. Fail: block the provider verification stage until publication is complete. Recorded in: progress.md.
- **G-QA-084 — Pipeline wiring inspection.** Verifies: QA-167. Check: `grep -rn "can-i-deploy" .github/workflows/` (or the project's CI config) returns a step in the deploy job, and `grep -rn "can-i-deploy.*|| true" .github/workflows/` plus a scan for `continue-on-error` on that step return nothing. Pass: step present, unmasked, positioned before promotion. Fail: block release until the gate is wired honestly. Recorded in: progress.md.
- **G-QA-085 — Provider-state reality check.** Verifies: QA-166. Check: `grep -rn "fixtures/" provider-states/` and a grep for response-body literals (`res.json(`, `send(body`) inside state-handler files both return no hits; two sampled states are traced to data-layer seed calls. Pass: states create data through the provider's own models or API only. Fail: block provider verification sign-off until states are real setup code. Recorded in: progress.md.

## Anti-patterns

- **Snapshot contract.** The pact mirrors the provider's entire current response, so a harmless new field "breaks" it and the team learns to ignore red results; catch it by diffing pact fields against the fields the consumer code actually reads.
- **Happy-path-only contracts.** Every interaction is a 200; the consumer's error handling is integrated against nothing and fails first in production. Catch it by listing the status codes the consumer handles and checking each has an interaction.
- **Local-only pacts.** Pacts are generated in a developer's test run and committed by hand, so provider CI verifies a stale file while the broker holds nothing; catch it when the broker has no version matching the consumer's HEAD SHA.
- **Quarantined contract tests.** A failing contract test is parked as "flaky" instead of fixed, and its verification results quietly age out while deploys continue; catch it by counting quarantined contract suites — the count must be zero at release.

## Examples

- [Example 1 — The contract that broke on a harmless field](examples/example-1.md) — violates/corrects QA-161, QA-162.
- [Example 2 — Green pipeline, unread verdict](examples/example-2.md) — violates/corrects QA-167.
- [Example 3 — Provider states that seed nothing](examples/example-3.md) — violates/corrects QA-166.

## Recall anchors

- The contract holds what the consumer uses — nothing more.
- Verification results are worthless unread: deployment reads the verdict.
- A state that serves a fixture tests the fixture, not the provider.
- Break it on purpose, on schedule, or it is already broken silently.
- Additions pass; removals and retypes of used fields fail.

## Checklist

- [ ] Every pact was generated by a consumer test run, none hand-written (QA-163).
- [ ] Pacts published to the broker tagged with the consumer commit SHA (QA-164).
- [ ] Provider CI replayed against the real provider build and published results (QA-165).
- [ ] Provider states seed through the real data layer; no fixture responses (QA-166).
- [ ] Deploy job runs can-i-deploy unmasked for this version and environment (QA-167, G-QA-084).
- [ ] Seeded-break control failed verification and can-i-deploy as designed (QA-168, G-QA-082).
- [ ] Error and empty-state interactions exist for every status the consumer handles (QA-170).
