# security-audit

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP ASVS 5.0.0, https://asvs.owasp.org/
- **Depends on:** owasp, threat-modelling
- **Feeds into:** penetration-testing, pci-compliance

## When to use / Do NOT use

- **Use when:** verifying a system the project owner owns or is contractually engaged to assess, against OWASP ASVS 5.0.0, with a written engagement scope, before a release, after major changes, or on a scheduled audit cycle.
- **Do NOT use when:** the system is not owner-controlled or no written authorization exists (stop — there is no audit without it); the task is adversarial testing of a running system (use penetration-testing, under its own authorization gate); or the task is a per-release Top 10 control check (use owasp).

## Rules

1. **SE-201 — Written engagement before any checking.** The audit starts only with a scope file signed by the system owner naming the assets in scope, the environments, the audit window, the ASVS level, and the exclusions. No scope file, no audit; systems outside it — third-party infrastructure, other tenants, payment providers — are never touched.
2. **SE-202 — Level chosen by data, recorded with rationale.** ASVS 5.0.0 Level 1 is the floor for a public application; Level 2 applies when the system holds sensitive personal data or payments. The chosen level and its reason are written in the report's scope section.
3. **SE-203 — A verdict with evidence for every in-scope requirement.** Each applicable requirement ends in exactly one verdict — pass, fail, or not-applicable with a written reason — plus its evidence: test output, config excerpt, or code location. A verdict with no evidence does not exist.
4. **SE-204 — Sampling is declared, never silent.** Where a requirement is checked by sampling, the report names the sample rule and size next to the verdict; everything not sampled is stated as fully checked or out of scope.
5. **SE-205 — Findings cite versioned IDs.** Every finding cites the ASVS requirement ID with its version (e.g. `v5.0.0-…`) and the DET parameter where one exists, so the fix can be re-checked against the same text.
6. **SE-206 — Automated evidence is generated inside the audit window.** SAST, dependency scan, ZAP, and header/TLS check outputs are run against the audited build during the audit window and attached with tool, version, target, and date.
7. **SE-207 — Manual review covers what tools cannot judge.** Authorization logic, business-flow abuse paths, and session design are reviewed by hand; the report lists which areas received manual review and which were tool-only.
8. **SE-208 — The deployed configuration is verified live.** Debug and admin surfaces, response headers, TLS, and shipped defaults are checked against the running system (DET-INF-021, DET-INF-022), not inferred from the repository.
9. **SE-209 — Every failure gets a severity, an owner, and a decision.** Each failed requirement is rated by exploitability and impact, assigned a named owner, and closed with a fix-or-accept decision and a date.
10. **SE-210 — Unowned failures are open risks in the summary.** A failed requirement with no owner or no date is reported as an open risk in the report summary — never left only in an appendix table.
11. **SE-211 — The report states scope and limits first.** The first section gives scope, level, window, exclusions, and methods. The report never calls the audit a penetration test, a certification, or proof that the system is "secure."
12. **SE-212 — Re-audit after remediation.** The re-audit covers every previously failed item plus regression checks on adjacent controls; updated verdicts are appended and the original findings stay visible as history.

## BAN list

- **BAN-SE-101 — Evidence-free pass.** Banned: marking a requirement "pass" with no evidence artifact attached to the verdict. Defeats: DET-CODE-012. Bad: the audit table reads "Session management — PASS" with an empty evidence column. Instead: attach the session config excerpt and the fixation/rotation test output, or record the verdict as not checked. Severity: BLOCK.
- **BAN-SE-102 — Repository-only verdict on deployed behavior.** Banned: reporting on headers, TLS, debug surfaces, or defaults from source review without probing the deployed system. Defeats: DET-INF-021. Bad: "No debug endpoints — reviewed the route table in the repo," while the production build serves a framework debug page. Instead: probe the live endpoints, record the responses, and let the probe output carry the verdict. Severity: BLOCK.
- **BAN-SE-103 — Secrets in the evidence pack.** Banned: committing audit evidence that contains live credentials, tokens, session cookies, or unredacted connection strings. Defeats: DET-INF-005. Bad: a full `.env` dump pasted into the report to "prove" config was reviewed. Instead: redact values, keep variable names and settings, and reference the secret store entry by name. Severity: BLOCK.
- **BAN-SE-104 — Audit of a weakened target.** Banned: running audit checks against a build or environment with security controls disabled (auth off, TLS verification off, debug on) and reporting the verdicts as production verdicts. Defeats: DET-CODE-020. Bad: ZAP and header checks run against a staging profile with authentication bypassed, reported as the production result. Instead: audit the production-equivalent configuration, and record any environment difference as a stated limit. Severity: BLOCK.
- **BAN-SE-105 — Recycled scanner evidence.** Banned: attaching scanner output generated outside the audit window, or against a different build, as this audit's evidence. Defeats: DET-INF-025. Bad: last quarter's dependency scan attached to this audit while base images and dependencies have since changed unpatched. Instead: re-run every scanner against the audited build inside the window and attach the fresh output. Severity: BLOCK.

## Gates

- **G-SE-101 — Report completeness check (automated).** Verifies: SE-203, SE-209, SE-210. Check: run a structure pass over the report (script or grep over the findings table): every in-scope requirement row carries a verdict and an evidence reference, and every fail row carries severity, owner, and decision date. Pass: zero incomplete rows. Fail: the audit is not issued until the rows are completed. Recorded in: progress.md.
- **G-SE-102 — Evidence freshness check (automated).** Verifies: SE-206. Check: compare the date and target build recorded in each attached scanner output against the audit window and the audited commit SHA in the scope file. Pass: every output was generated inside the window against that build. Fail: re-run the stale scans before the report ships. Recorded in: progress.md.
- **G-SE-103 — Live surface verification.** Verifies: SE-208. Check: `curl -sI https://<prod-domain>/` for the header verdicts, `curl -s -o /dev/null -w "%{http_code}"` against the framework debug path and `/.env`, and a TLS check (`testssl.sh <prod-domain>` or `openssl s_client -connect <prod-domain>:443`). Pass: recorded probe outputs match the verdicts in the report. Fail: block the report and re-audit the mismatched items live. Recorded in: progress.md.
- **G-SE-104 — Scope and authorization review.** Verifies: SE-201, SE-202, SE-211. Check: manual review — the signed scope file exists, every audited asset is owner-controlled and inside it, the ASVS level rationale is recorded, and the report's first section states scope and limits without penetration-test or certification language. Pass: all four hold. Fail: the audit does not ship. Recorded in: progress.md.

## Anti-patterns

- **Checklist theater.** Verdicts are filled in during one end-of-audit pass from memory, each row marked pass because "we built it that way." Catch it: pick three pass rows at random and ask for the evidence on the spot.
- **Tool-dump report.** Raw scanner output is pasted wholesale with no per-requirement verdicts, so nobody can tell what was actually decided. Catch it: if the report has findings but no verdict table, it is a dump, not an audit.
- **Scanner-says-clean, again.** A clean automated run is treated as covering authorization logic and business-flow abuse — the areas tools cannot judge and where the worst findings live. Catch it: check the report's manual-review list (SE-207) before trusting the clean scan.
- **Scope amnesia.** Mid-audit, checking quietly expands to a neighboring service, a shared tenant, or the payment provider's endpoints "since we're here." Catch it: diff the audited asset list against the scope file; anything extra is unauthorized work, not thoroughness.

## Examples

- [Example 1 — Evidence-backed verdict](examples/example-1.md) — violates/corrects SE-203 (BAN-SE-101).
- [Example 2 — Live configuration check](examples/example-2.md) — violates/corrects SE-208 (BAN-SE-102).
- [Example 3 — Finding with an owner and a decision](examples/example-3.md) — violates/corrects SE-209, SE-210.

## Recall anchors

- No written scope from the owner, no audit.
- Every requirement: a verdict, evidence, or it did not happen.
- Audit the running system, not just the repository.
- A failure without an owner and a date is an open risk in the summary.
- An audit verifies against a standard; it is not a penetration test.

## Checklist

- [ ] Signed scope file exists; every audited asset is owner-controlled and inside it (SE-201).
- [ ] ASVS level chosen, with the rationale recorded in the report (SE-202).
- [ ] Every in-scope requirement has a verdict and evidence; sampling is declared where used (SE-203, SE-204).
- [ ] Findings cite versioned ASVS IDs and DET parameters where they exist (SE-205).
- [ ] All scanner evidence was generated inside the audit window against the audited build (SE-206, G-SE-102).
- [ ] Deployed configuration was probed live — surfaces, headers, TLS, defaults (SE-208, G-SE-103).
- [ ] Every failure has a severity, an owner, and a fix-or-accept date; unowned failures appear as open risks in the summary (SE-209, SE-210).
- [ ] Report's first section states scope and limits; no penetration-test or certification claim anywhere (SE-211).
