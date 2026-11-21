# Phase 4 Cross-Review — Cluster F (D16, D17, D18)

Reviewer scope: substance only (format validation already passed 227/227). No skill files were edited.

## Scope covered

**Deep-read (rules, BAN list, gates, metadata, plus at least one example file each):**

- D16 (all 7): site-discovery, page-inventory, design-extraction, asset-harvesting, behavior-cloning, page-reconstruction, fidelity-verification
- D17 (4): llm-integration, ai-safety, rag-retrieval, ai-evaluation
- D18 (4): support-ticketing, trial-conversion, churn-prevention, status-communications

**Skimmed (full-text read at rule/gate/metadata level, no example opened):**

- D17 (6): prompt-engineering, embeddings-search, recommendations, search-relevance, ai-observability, ai-cost-control
- D18 (5): in-app-chat, help-center, user-onboarding, activation-metrics, feedback-loops

**Mechanical checks run across all 26 skills:** grep for model names / prices in D17 (none found); grep for "Click-to-Cancel" in D18 (zero mentions); grep for 24/7 and response-time claims in D18 (only as banned patterns or configuration-gated rules); Depends on / Feeds into cross-checked against `build/catalog.txt` (every named skill exists in the catalog).

## Findings

### BLOCKER

None.

### MAJOR

- **F-1 (MAJOR) — page-reconstruction: Feeds into direction contradicts behavior-cloning.** page-reconstruction's metadata says "Feeds into: fidelity-verification, behavior-cloning", but the actual flow runs the other way: behavior-cloning's own metadata says it feeds page-reconstruction, and its When-to-use section states page-reconstruction "consumes this skill's `unobserved` records". The two skills state opposite directions for the same relationship, so an agent following page-reconstruction's metadata could treat behavior specs as a downstream output of reconstruction instead of an upstream input. Fix: remove `behavior-cloning` from page-reconstruction's Feeds into (keep fidelity-verification); the unobserved-record handoff is already correctly documented on the behavior-cloning side.
- **F-2 (MAJOR) — activation-metrics: cohort-validation gate pass criterion is not decidable.** CX-086 requires activated users to "retain measurably better" than non-activated users, and G-CX-043 passes when "the activated cohort retains measurably better" — but neither the rule nor the gate requires a minimum retention delta (or minimum cohort size) to be recorded in advance. Two reviewers running the same data could reach opposite verdicts, which is exactly the failure mode this department's other gates avoid (compare CX-087's own-baseline discipline). Fix: require the activation definition to record a minimum retention delta and horizon before the validation run; G-CX-043 passes only when the measured delta meets that pre-recorded threshold.

### MINOR

- **F-3 (MINOR) — llm-integration: provider-specific patterns sit inline in gates, not in the dated annex.** AI-009 confines provider specifics to "the wrapper and in a clearly marked, dated provider annex", yet G-AI-001's example greps for one provider's SDK import/endpoint and G-AI-003's secret scan hard-codes that provider's key pattern (`sk-…`). Both are marked as examples and the gates also invoke the project's own scanner, so they work — but they contradict the skill's own annex rule and D17's provider-neutrality pattern. Fix: move the concrete import/key patterns into the dated provider annex and have the gates reference "the annex's patterns for the configured provider".
- **F-4 (MINOR) — trial-conversion: vendor event name embedded in a rule body.** CX-105 names Stripe's `customer.subscription.trial_will_end` event inside the rule text. D18's research open risk requires the model (trial-will-end warning before first charge) to be taught tool-agnostically with vendor specifics confined to examples. The rule's substance is correct and ROSCA is cited correctly in CX-106; only the placement is off. Fix: reword CX-105 to "the billing platform's trial-will-end event" and keep the Stripe event name in the Sources line and Example 1, where it already appears appropriately.
- **F-5 (MINOR) — in-app-chat: checklist assumes an attachment assertion the gate does not state.** The checklist item for G-CX-011 reads "Two-state delivery test passes, including one attachment each way", and an anti-pattern says to "include one attachment in the G-CX-011 delivery test" — but G-CX-011's check text never mentions attachments. An agent running the gate as written would not test attachments while believing the checklist item is covered. Fix: add the attachment assertion to G-CX-011's check text.
- **F-6 (MINOR) — site-discovery: CL-001 wording tangles the pre-authorization exception.** CL-001 bans any "discovery crawl, sitemap fetch beyond the authorization check itself, or archive enumeration" before the record exists. The italic exception is confusing: CL-003 separately requires robots.txt and the sitemap index to be fetched first *after* authorization, and nothing in the skill defines an "authorization check" sitemap fetch. A literal reader could fetch the sitemap pre-authorization and claim the exception. Fix: delete the exception phrase; state plainly that no target request of any kind precedes the record (robots/sitemap fetches are the first *authorized* step under CL-003).
- **F-7 (MINOR) — fidelity-verification: Example 2 baseline-regeneration wording is ambiguous.** Example 2's After text says, for an approved header restyle, "the baseline is regenerated from the source capture reflecting that change". If the approved change is on the rebuild side, a source capture cannot reflect it, and regenerating a baseline so the rebuild passes is precisely BAN-CL-062's pattern unless the deviation record carries it (which the example does log). The example's intent (deviation logged first, approver named) is right, but the sentence can be misread as "regenerate to green". Fix: clarify that the source baseline stays, the accepted deviation record carries the difference, and baselines are regenerated only when the frozen source capture set itself is re-frozen.
- **F-8 (MINOR) — churn-prevention: metadata declares "Depends on: none" while its rules run on D11 mechanics.** CX-149 (dunning: smart retries, card-account updates) is the dunning skill's domain and CX-152/G-CX-073 verify state in "the billing system" owned by subscriptions; the When-to-use section itself defers plan mechanics to D11 subscriptions. "Depends on: none" understates both and breaks the otherwise consistent cross-referencing pattern in D18 (trial-conversion correctly lists subscriptions). Fix: set Depends on to `subscriptions, dunning`.
- **F-9 (MINOR) — design-extraction: G-CL-022 assumes a build-output path.** The orphan-value scan greps `dist/assets/*.css`; projects with a different output layout would run the gate against nothing and pass vacuously. Fix: phrase the target as "the built CSS output (e.g. `dist/assets/*.css`)" and require the gate record to name the actual path scanned — the same "adjusted to the project" phrasing llm-integration's G-AI-001 already uses.

## What is excellent (propagate)

- **D16 authorization discipline is uniform and fail-closed.** Every one of the 7 skills carries an authorization-precedes-work rule (CL-001, CL-041, CL-061, CL-081, CL-101, plus page-inventory's CL-029 and fidelity-verification's frozen-capture-set rule CL-121), each backed by a pre-flight gate that refuses to start. The clone-ethics frame from D14 is never weakened: target code, copy, and protected assets are banned from reuse in site-discovery (CL-010), design-extraction (CL-051 replace-list), asset-harvesting (CL-066/068), behavior-cloning (CL-084/090), and page-reconstruction (CL-106/107) alike.
- **D16 resolves the research open risks instead of ignoring them.** asset-harvesting CL-065 names the lightweight HAR-plus-checksum fallback when WARC tooling is impractical; CL-067 requires a license record with transferability checked, so the skill does not self-approve `licensed` (and its Depends on correctly includes D14 licensing); fidelity-verification CL-122 forces viewports, the ≥95% bar, per-page vs. aggregate scoring, and masking rules to be committed before the first run.
- **D17 is genuinely provider-neutral.** No model names, endpoints-as-method, or prices appear anywhere in the 10 skills; ai-cost-control AI-182 computes cost from metered tokens × the operator's dated price sheet and bans rates in code. ai-evaluation's judge calibration (AI-145/G-AI-072) and dataset contamination scan (G-AI-073), and rag-retrieval's permission-at-retrieval rule (AI-062) with its marker-based leakage test (G-AI-033), are the strongest gate designs in the cluster.
- **D18 support promises are configuration, end to end.** support-ticketing CX-005/CX-006 plus the copy-vs-config diff gate (G-CX-002) make an unstaffed promise mechanically detectable; in-app-chat CX-023 names the vendor 24/7 default explicitly as the thing not to ship. status-communications CX-166/CX-172 build in the solo-operator degraded mode (longer honest cadence, holding templates) that the research flagged as the department's central tension.
- **D18 cancellation law is current and correct.** trial-conversion CX-106 and churn-prevention CX-142 cite ROSCA's duties (clear disclosure, express informed consent, simple cancellation) plus the FTC dark-patterns report and state auto-renewal law via sources; the vacated Click-to-Cancel rule is mentioned nowhere in the department — not even as a banned citation.

## Verdicts

- **D16 Cloning & Replication — sound-with-fixes.** The ethics frame, evidence hierarchy, and fidelity gates are the strongest in the cluster; fix the reversed Feeds into (F-1) and the two minor wording items (F-6, F-7, F-9).
- **D17 AI Features — sound-with-fixes.** No blockers or majors; provider-neutrality, eval discipline, and safety gating all match the research. Only F-3 (annex placement of provider patterns) needs a touch-up.
- **D18 Customer Experience — sound-with-fixes.** Promise-as-configuration, ROSCA-correct cancellation, and operator-set cadence all land as the research required; fix the activation validation threshold (F-2) and the three minor items (F-4, F-5, F-8).
