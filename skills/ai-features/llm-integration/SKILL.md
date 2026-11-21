# llm-integration

## Metadata

- **Owner department:** D17 AI Features (AI)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses
- **Depends on:** prompt-engineering
- **Feeds into:** ai-observability, ai-cost-control, rag-retrieval, ai-evaluation

## When to use / Do NOT use

- **Use when:** a feature sends input to a large language model and consumes its output — chat, generation, summarization, extraction, classification — or when an existing model call is being added, moved, or swapped between providers.
- **Do NOT use when:** the task is authoring or revising prompt text (use prompt-engineering), screening inputs/outputs or gating tool calls (use ai-safety), or retrieving documents for the prompt (use rag-retrieval). This skill owns the call path, not the prompt, the guardrails, or the corpus.

## Rules

1. **AI-001 — One wrapper, and it is the only caller.** All model calls go through a single server-side client module that owns provider selection, keys, timeouts, retries, and error mapping. No feature code imports a provider SDK or calls a provider endpoint directly.
2. **AI-002 — Keys exist only server-side.** Provider API keys live only in server-side secrets storage. A key found in client code, a shipped bundle, or a committed file is a release blocker, and the exposed key is rotated, not just removed.
3. **AI-003 — Every call is bounded.** Each call sets an explicit timeout and a maximum output-token budget, both taken from wrapper configuration. A call with no timeout or no token cap is forbidden.
4. **AI-004 — Retries are capped, with backoff.** Transient failures (rate limit, provider 5xx, network timeout) retry with exponential backoff up to a configured attempt cap, sending an idempotency key where the provider supports one. Non-transient failures (refusal, schema-invalid output) never retry as if transient.
5. **AI-005 — Structured output wherever code consumes the reply.** Wherever output feeds code, records, or UI structure, the call carries a JSON Schema and the response is validated against that schema before use. Parsing raw model free text — `JSON.parse`, regex extraction, string splitting — to recover structure is forbidden.
6. **AI-006 — Every failure is a distinct typed error.** Rate limit, timeout, refusal, incomplete response, and schema-invalid output each map to a distinct typed application error the feature can branch on. Refusals and incomplete responses are handled states, not exceptions discovered in production.
7. **AI-007 — Degrade, never fake.** When retries are exhausted, the feature degrades to a smaller or cheaper model, or to a disclosed non-AI fallback, or shows a user-visible failure state with a retry path. It never returns a canned answer presented as model output.
8. **AI-008 — Model IDs and parameters live in config.** Model identifiers, temperature, timeout, and token limits are named values in one configuration place. Scattered literals in feature code are forbidden, so a model deprecation or swap touches config and the wrapper only.
9. **AI-009 — Features program against the contract, not the provider.** Feature code depends only on the internal interface — request in, structured result or typed error out. Provider-specific request and response shapes exist only inside the wrapper and in a clearly marked, dated provider annex to this skill.
10. **AI-010 — Validate before records change.** Model output that will be stored, displayed as fact, or acted on passes schema validation (AI-005) plus the application's own business-rule checks before any write. Invalid output is rejected and logged; it is never written and patched later.
11. **AI-011 — Every call is metered.** Each call records feature name, prompt version, model ID, tokens in and out, and latency, emitted by the wrapper for ai-observability and ai-cost-control. A call path that emits no metering is a defect.
12. **AI-012 — Demos are labeled demos.** Hard-coded or canned responses may exist only behind an explicit demo mode that is visibly labeled as a demo in the UI and named as demo in configuration. Demo mode is never the shipped default.

## BAN list

- **BAN-AI-001 — Canned responses shipped as an AI feature.** Banned: a chat, generator, or summarizer whose answers come from a lookup table, template rotation, or prompt echo, presented to users as model output. Defeats: DET-FAKE-009. Bad: the support chatbot returns one of six canned paragraphs matched by keyword while the page claims it is AI-powered. Instead: route the input through the wrapper to a real model (AI-001), or label the surface a demo (AI-012). Severity: BLOCK.
- **BAN-AI-002 — Provider key in client code or a shipped bundle.** Banned: an API key embedded in browser or mobile code, a built asset, or a committed config file. Defeats: DET-CODE-018. Bad: the chat widget calls the provider directly from the browser with the project's key in the JavaScript bundle, where any visitor can extract and spend it. Instead: the browser calls the project's own server endpoint, and the wrapper calls the provider with the key from server-side secrets (AI-002). Severity: BLOCK.
- **BAN-AI-003 — Unbounded model call.** Banned: a call with no timeout, no output-token cap, or a retry loop with no attempt limit. Defeats: DET-CODE-033. Bad: a summarization call waits indefinitely on a stalled provider response and retries forever on 429s, piling up cost while the user stares at a spinner. Instead: set timeout, token budget, and retry cap from wrapper config on every call (AI-003, AI-004). Severity: BLOCK.
- **BAN-AI-004 — Raw model text parsed and trusted.** Banned: recovering data from free-text model output with `JSON.parse`, regex, or string splitting, then storing or acting on the result. Defeats: DET-CODE-019. Bad: the invoice extractor runs `JSON.parse` on the model's reply and writes the fields to the database; the first reply wrapped in prose breaks the import and corrupts two records. Instead: request schema-constrained output and validate it, plus business rules, before any write (AI-005, AI-010). Severity: BLOCK.
- **BAN-AI-005 — Swallowed provider failure.** Banned: catching a provider error and returning an empty, default, or success-looking result so the failure is invisible. Defeats: DET-CODE-005. Bad: when the provider times out, the catch block returns an empty summary and the UI reports "Summary ready." Instead: map the failure to its typed error and degrade or surface it honestly (AI-006, AI-007). Severity: BLOCK.

## Gates

- **G-AI-001 — SDK containment check.** Verifies: AI-001, AI-009. Check (automated): grep the codebase for the annex's patterns for the configured provider — its SDK imports and endpoint URLs — outside the wrapper module, adjusted to the project's wrapper path. Pass: zero hits outside the wrapper. Fail: block shipment. Recorded in: progress.md.
- **G-AI-002 — Live contract test.** Verifies: AI-005, AI-006, AI-007. Check (automated): run the integration suite against the provider's sandbox or test mode with the real key loaded from secrets: (a) send a schema-bound request and assert the response validates against the schema; (b) stub a 429 and a timeout and assert each maps to its typed error and the fallback path executes; (c) send the refusal fixture and assert the refusal state is handled, not thrown. Pass: all cases pass. Fail: block shipment. Recorded in: progress.md.
- **G-AI-003 — Secret scan.** Verifies: AI-002. Check (automated): scan the repository and the built client bundle for the annex's key patterns for the configured provider, plus the project's secret scanner in CI. Pass: zero matches. Fail: block shipment and rotate any exposed key. Recorded in: progress.md.
- **G-AI-004 — Fault-injection bounds test.** Verifies: AI-003, AI-004. Check (automated): point the wrapper at a stub provider that always returns 429; assert the total attempt count is at most the configured cap plus one, the elapsed time stays within the timeout budget, and the surfaced error is the typed rate-limit error. Pass: all three assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-AI-005 — Demo-mode and probe check.** Verifies: AI-007, AI-012. Check (manual): confirm the production configuration has demo mode off; then, in staging, run the DET-FAKE-009 probe — ask an unusual, specific question only answerable from a supplied document, rephrased twice — and confirm the answers come from the model and vary correctly with the input. Pass: demo off and probe answers track the input. Fail: block shipment. Recorded in: progress.md.

**Provider annex:** concrete per-provider patterns (SDK imports, endpoint URLs, key formats) live in the dated [provider annex](provider-annex.md), per AI-009; G-AI-001 and G-AI-003 use the annex's patterns for the configured provider.

## Anti-patterns

- **Provider-shaped feature code.** Feature logic starts branching on provider-specific response fields outside the wrapper — the contract is leaking. Catch it by searching feature code for provider field names; move the translation into the wrapper before the next feature lands.
- **Inline prompt assembly in feature code.** Prompt strings are concatenated inside handlers in several files, so nobody can say which prompt version produced an answer. Catch it by grepping for prompt fragments outside the versioned prompt source owned by prompt-engineering.
- **Retry storm on permanent errors.** Refusals and schema-invalid replies are retried with the same input, multiplying cost for an answer that cannot change. Catch it in the metering stream: repeated identical calls with refusal outcomes mean the retry policy ignores AI-004's transient/non-transient split.
- **Silent model swap.** The model ID in config changes with no eval run recorded, so a quality regression has no baseline to compare against. Catch it by diffing config changes against ai-evaluation records — every model change needs its eval delta attached.

## Examples

- [Example 1 — The chatbot that never called a model](examples/example-1.md) — violates/corrects AI-001, AI-012 (BAN-AI-001).
- [Example 2 — The API key in the browser bundle](examples/example-2.md) — violates/corrects AI-002 (BAN-AI-002).
- [Example 3 — JSON.parse on raw model text, no timeout](examples/example-3.md) — violates/corrects AI-003, AI-005, AI-006 (BAN-AI-004).

## Recall anchors

- One wrapper calls the model; features never do.
- Keys live server-side, or the release does not ship.
- Every call: timeout, token cap, capped retries.
- Schema first — never parse raw model text.
- Degrade honestly; a canned answer is not a fallback.

## Checklist

- [ ] All model calls route through the single server-side wrapper; no provider SDK import exists outside it (AI-001, G-AI-001).
- [ ] No provider key appears in client code, bundles, or committed files; secret scan is clean (AI-002, G-AI-003).
- [ ] Timeout, token budget, and retry cap are set from config for every call (AI-003, AI-004, G-AI-004).
- [ ] Programmatically consumed output is schema-constrained and validated, plus business-rule checked, before any write (AI-005, AI-010).
- [ ] Rate limit, timeout, refusal, incomplete, and invalid-output failures each map to a typed error, and the degradation path is tested (AI-006, AI-007, G-AI-002).
- [ ] Model IDs and parameters appear only in config; provider specifics are confined to the wrapper and the dated annex (AI-008, AI-009).
- [ ] Every call emits metering: feature, prompt version, model, tokens, latency (AI-011).
- [ ] Demo mode, if present, is labeled in UI and config and is off in production (AI-012, G-AI-005).
