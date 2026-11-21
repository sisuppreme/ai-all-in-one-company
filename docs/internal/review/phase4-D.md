# Phase 4 Cross-Review — Cluster D (D10, D11, D12)

Reviewer: Phase 4 cross-review, cluster D. Date: 2026-11-21.
Scope: substance only (format validation already passed 227/227). No skill files were edited.

## Scope covered

**Deep-read (12 skills, 4 per department)** — full read of SKILL.md (rules, BAN list, gates, anti-patterns, metadata) plus at least one example file opened per skill:

- D10 project-memory: project-templates (examples/example-1.md), decision-logs (examples/example-2.md), progress-tracking (examples/example-2.md), handover (examples/example-1.md)
- D11 integrations-payments: payments (examples/example-1.md), invoicing-tax (examples/example-1.md), oauth-sso (examples/example-2.md), webhooks (examples/example-1.md)
- D12 analytics-observability: product-analytics (examples/example-1.md), event-tracking (examples/example-1.md), alerting (examples/example-1.md), core-web-vitals (examples/example-1.md)

**Skimmed (23 skills)** — rules, BAN list, gates, and metadata read at lower depth:

- D10: documentation-writing, readme-writing, runbook-writing, postmortem-writing, changelog, memory-retrieval
- D11: subscriptions, dunning, refunds-disputes, transactional-email, sms, third-party-apis, api-keys-management, sdk-embeddables
- D12: experimentation-platform, revenue-analytics, logging, monitoring, dashboards, error-tracking, apm, performance-budgets, performance-optimization

**Mechanical checks run:** every Depends on / Feeds into entry in all 35 skills was extracted and matched against `build/catalog.txt`. All entries resolve to real catalog skills, with one exception (MINOR-4 below; two apparent misses were parser artifacts of parenthetical annotations inside an entry, not dangling references).

## Boundary checks required by the assignment — all PASS

- **D10 brief-internal files:** progress-tracking and handover treat progress.md / handover.md as project conventions, not external standards; their sources cite patterns only (a datadef freshness-gate pattern, the Google PRR blog). decision-logs resolves the DECISIONS.md-index vs docs/adr/ duality exactly as D10.md research demanded (PM-109). memory-retrieval (PM-169/PM-170) implements the research's fix: the project owns its own `retrieval-queries.md`; generic template lists are forbidden as the test. postmortem-writing (PM-081) parameterizes triggers per project instead of hardcoding Google/Atlassian values. changelog (PM-130) declares the version source of truth instead of assuming one.
- **D11 invoicing-tax:** fully patterns-only. IN-061/IN-062 ban hardcoded rates; gate G-IN-034 is a no-rate-in-code scan. The only rate figure anywhere ("20% VAT") appears inside BAN-IN-031's Bad example as the banned pattern itself, and example-1.md demonstrates replacing a hardcoded rate with operator configuration.
- **D11 oauth-sso:** IN-172 states OAuth 2.1 is an Internet-Draft, never a standard, with a status re-check rule; the Sources list annotates the draft "(work in progress, not an RFC)". OAuth itself is grounded in RFC 9700 per the research.
- **D11 subscriptions:** IN-028 grounds cancellation parity in ROSCA / FTC Act Section 5 and does **not** cite the vacated Click-to-Cancel rule. dunning (IN-083) presents Stripe's retry default as dated ("checked 2026-11-21") and "a starting configuration to review, not a law".
- **D12 vs D9 boundary:** product-analytics AN-006 states the boundary precisely — D9's web-analytics consumes the one shared tracking plan; no parallel taxonomy — and no D12 skill claims Search Console / GA4-organic ownership.
- **D12 vs D6 boundary:** alerting AN-121 states the split (D12 owns alert policy, D6 owns mechanics) and AN-132 adds the explicit low-traffic mode the D12 research open risks demanded. logging (AN-082/AN-090) and monitoring restate the D6 boundary without redefining infrastructure telemetry. apm likewise defers host/platform telemetry to D6.

## Findings

### BLOCKER
None.

### MAJOR
None.

### MINOR

**MINOR-1 — decision-logs, gate G-PM-054 ("Immutability check") is labeled automated but is not automatable as written.**
The check requires judging which lines of a `git log -p --follow` diff fall outside the Status section of an ADR; no script is supplied, so a checker cannot run it mechanically. *Suggested fix:* ship a small script that parses diff hunks per ADR file and flags any changed line outside the Status section, or relabel the gate manual-assisted.

**MINOR-2 — readme-writing, gate G-PM-021's primary check is a fragile awk sketch.**
The gate's quickstart-extraction check is written as a hand-wavy awk pipeline that will break on ordinary README variation. The gate does name the project's `scripts/readme-quickstart-check.sh` as an alternative, which partially redeems it. *Suggested fix:* make the script the primary check and drop the awk sketch.

**MINOR-3 — api-keys-management, BAN-IN-101's Bad example uses the allowlisted dummy token as if it were a real secret.**
The Bad example shows the literal string `sk_live_EXAMPLE` as a bundled real secret key — but IN-201 and gate G-IN-101 define that exact string as the allowlisted dummy placeholder. A reader (or a scanner test) cannot tell whether the string is banned or blessed. *Suggested fix:* use a redacted realistic form (e.g. `sk_live_51H…`) in the Bad example.

**MINOR-4 — changelog, Feeds into names "release notes", which is not a catalog skill.**
Every other Feeds into / Depends on entry in the cluster names a skill in `build/catalog.txt`; "release notes" is a document artifact, not a skill. *Suggested fix:* remove it from Feeds into (mention release notes in the When-to-use text instead), or point it at the skill that consumes the changelog if one exists.

## Notes on substance quality (worth propagating)

- **Gates are genuinely mechanical across the cluster.** Recurring good pattern: seeded-fault / negative-control tests (e.g. alerting's burn-rate derivation in AN-123 is actually implemented in its example-1.md with the 14.4× fast-burn math; core-web-vitals thresholds match web.dev exactly — LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 at p75, 28-day rolling, per template/device class — and AN-227 correctly records INP replacing FID on 2024-03-12).
- **BAN entries name real domain failure patterns with genuine corrections**, not restatements — e.g. webhooks example-1.md shows the unsigned-POST trust bug and the raw-body signature-verification fix in runnable code; product-analytics example-1.md shows the typed-in dashboard number replaced by a computed metric definition.
- **Research caveats survived drafting.** Dated vendor defaults, draft-vs-standard status, vacated-rule avoidance, and per-project parameterization are all carried into the skills rather than flattened into false certainty. This is the pattern other clusters should be checked against.

## Verdicts

- **D10 project-memory: sound-with-fixes** (MINOR-1, MINOR-2, MINOR-4)
- **D11 integrations-payments: sound-with-fixes** (MINOR-3)
- **D12 analytics-observability: sound** (no findings)

Totals: 12 deep-read, 0 blockers, 0 majors, 4 minors.
