# penetration-testing

## Metadata

- **Owner department:** D7 Security (SE)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** OWASP Web Security Testing Guide, https://owasp.org/www-project-web-security-testing-guide/ ; OWASP API Security Top 10 (2023), https://orca.security/resources/blog/owasp-api-security-top-10/
- **Depends on:** owasp, security-audit
- **Feeds into:** security-audit

## When to use / Do NOT use

- **Use when:** an owner-controlled system needs adversarial validation of its running defenses — authentication, session, authorization/BOLA, injection, business-logic, and configuration weaknesses — under a written engagement.
- **Do NOT use when:** the system belongs to a third party, a provider, a shared-hosting neighbor, or another tenant — never, under any instruction. Do NOT use when the task is verification against a standard on evidence; that is security-audit. Do NOT use without a signed engagement file; there are no exceptions for "quick checks."

## Rules

1. **SE-221 — Engagement file before any tool runs.** No scan, probe, or login attempt happens until a signed engagement file exists naming the authorizing owner, target systems, permitted techniques, testing window, data-handling rules, stop conditions, and the emergency contact. The file is step one of the method, not a footnote.
2. **SE-222 — Owner-controlled or contractually engaged systems only.** Test only systems the project owner owns or is contractually engaged to test. Third-party services, provider infrastructure, other tenants, and payment-provider systems are never targets unless the engagement file names them explicitly.
3. **SE-223 — Scope is a list, not a vibe.** Domains, IP ranges, accounts, and techniques not named in the engagement file are not tested. A newly discovered subdomain, staging host, or API is out of scope until the file is amended in writing.
4. **SE-224 — Test to the OWASP WSTG cases.** Structure the work on the OWASP Web Security Testing Guide: reconnaissance and inventory, authentication and session attacks, authorization and BOLA probing (API targets per the OWASP API Security Top 10, 2023), injection, business-logic abuse, and configuration review.
5. **SE-225 — Staging is the default target; production needs separate consent.** Test a staging environment that faithfully mirrors production unless the engagement file grants explicit additional consent for production, with agreed rate limits and testing hours.
6. **SE-226 — Excluded techniques stay excluded.** Denial-of-service, social engineering, and physical techniques are not used unless each is explicitly written into the engagement file.
7. **SE-227 — Minimize real user data.** Data encountered during a test is evidence to minimize: capture the smallest proof that demonstrates the flaw (ideally with tester-owned accounts and records), never copy datasets out, and report any real-data exposure through the agreed channel immediately.
8. **SE-228 — Honor stop conditions instantly.** When a stop condition triggers — instability, real-user impact, out-of-scope data reached — testing halts and the emergency contact is notified before any further action.
9. **SE-229 — Every finding is reproduced and evidenced.** A finding exists only when the tester has manually reproduced it and recorded the steps, the request/response or screenshot evidence, and a severity rating based on exploitability and impact. Raw scanner output is a lead, not a finding.
10. **SE-230 — Critical and high findings ship with an engineer-followable reproduction.** The reproduction names the account, the exact inputs, and the observed result, so an engineer who was not present can repeat it without asking the tester.
11. **SE-231 — Retest after remediation.** Every critical/high finding is retested after the fix using the original reproduction. A fix with no retest is reported as an unverified fix, never as closed.
12. **SE-232 — Leave nothing behind.** Test accounts, uploaded files, created records, and any temporary access created for the test are removed or disabled at engagement close, and the removal is verified and recorded.

## BAN list

- **BAN-SE-111 — Testing without a signed engagement file.** Banned: running any probe, scan, or attack tool against a target on the basis of a verbal OK, a chat message, or assumed permission. Defeats: DET-NONE — no DET parameter names this signal; governed by SE-221/SE-222. Bad: a tester brute-forces the staging login over a weekend because "the owner said test the app," trips real alerts, and nobody knows whether it is an attack. Instead: obtain the signed engagement file (SE-221) with window, stop conditions, and emergency contact before the first packet. Severity: BLOCK.
- **BAN-SE-112 — Probing anything not named in scope.** Banned: testing a domain, IP, account, or technique the engagement file does not list, including provider infrastructure, other tenants, and "just one quick check" on an adjacent host. Defeats: DET-NONE — no DET parameter names this signal; governed by SE-222/SE-223. Bad: noticing `admin.partner-vendor.example` during recon and testing its exposed admin panel although the engagement covers only the owner's app. Instead: record the observation in the report as an untested note and amend the engagement file in writing before touching it. Severity: BLOCK.
- **BAN-SE-113 — Exfiltrating real data as proof.** Banned: downloading, copying, or screenshotting bulk real user data — full tables, credential stores, other users' records — to prove a flaw. Defeats: DET-NONE — no DET parameter names this signal; governed by SE-227. Bad: exporting 5,000 user rows including password hashes into the findings folder to prove a BOLA flaw. Instead: prove the flaw with tester-owned accounts and the single minimum cross-access, redact identifiers in evidence, and report the exposure immediately (SE-227). Severity: BLOCK.
- **BAN-SE-114 — Reporting scanner output as findings.** Banned: pasting automated scanner results into the report as confirmed vulnerabilities without manual reproduction. Defeats: DET-CODE-012. Bad: 43 "critical" findings copied from a scanner export, half of them false positives the engineers chase for a week. Instead: reproduce each candidate manually; report only what reproduced, with steps and evidence (SE-229), and list unreproduced leads separately as leads. Severity: BLOCK.
- **BAN-SE-115 — Leaving test artifacts in the target.** Banned: closing an engagement with tester accounts still active, uploaded test files or shells still reachable, created records still present, or a security control still disabled from testing. Defeats: DET-INF-021. Bad: a `pentest-admin` account with a known password remains in production three months after the engagement. Instead: remove or disable every artifact, verify removal, and record the cleanup in the engagement close-out (SE-232). Severity: BLOCK.

## Gates

- **G-SE-111 — Engagement-file completeness.** Verifies: SE-221, SE-222, SE-223, SE-226, SE-228. Check (automated): `test -f security/engagement.md && for h in Authorization Scope Techniques Window "Data handling" "Stop conditions" "Emergency contact"; do grep -qi "^## $h" security/engagement.md || echo "MISSING: $h"; done` — plus a manual read confirming the signer owns or is contractually engaged for every named target. Pass: no MISSING lines and the signature covers every in-scope target. Fail: block the engagement; no tool runs. Recorded in: progress.md.
- **G-SE-112 — Scope conformance of executed tests.** Verifies: SE-223. Check (automated): extract every target host from the test tool logs (`grep -rhoE 'https?://[a-zA-Z0-9.-]+' security/test-logs/ | sort -u`) and diff against the host list in the engagement file's Scope section. Pass: zero hosts outside scope. Fail: halt testing, notify the emergency contact, and record the deviation in the report before any resumption. Recorded in: progress.md.
- **G-SE-113 — Finding evidence completeness.** Verifies: SE-229, SE-230. Check (automated + manual): each critical/high finding section in the report contains Reproduction, Evidence, and Severity fields (`grep -c "### Finding"` vs. counts of each field heading); a reviewer follows one reproduction end to end. Pass: every critical/high finding has all three fields and the sampled reproduction succeeds. Fail: the finding is downgraded to a lead and the report does not ship. Recorded in: progress.md.
- **G-SE-114 — Retest closure.** Verifies: SE-231. Check: the report's retest table lists every critical/high finding with a retest date and result; findings without one appear in an explicit "Unverified fixes" section. Pass: no critical/high finding is marked closed without a passing retest. Fail: block engagement close-out. Recorded in: progress.md.
- **G-SE-115 — Cleanup verification.** Verifies: SE-232. Check (automated): for each artifact in the engagement's artifact log (accounts, uploads, records), run the recorded verification (account lookup returns disabled/absent, upload URL returns 404, record query returns empty). Pass: every artifact verified removed. Fail: block engagement close-out until cleanup completes. Recorded in: progress.md.

## Anti-patterns

- **Checklist cosplay.** Working the WSTG headings as a compliance checklist — "tested authentication ✓" — without actually attempting the attacks. That is an audit wearing a pentest's name; if no adversarial attempt happened, no penetration test happened.
- **Noise burial.** Shipping a report where dozens of informational findings bury the one critical BOLA flaw on page nine. Order by severity and lead with what an attacker would actually use.
- **Retest by echo.** Retesting only the exact original payload on the exact original endpoint; the fix passes while the same flaw survives on a sibling endpoint. Retest the flaw class across the surface the finding implicates.
- **Tester-voiced report.** Findings written in tester jargon with no business impact, so engineers cannot prioritize. Every finding states what an attacker gains, in the product's own terms.

## Examples

- [Example 1 — Authorization before tooling](examples/example-1.md) — violates/corrects SE-221.
- [Example 2 — Proving BOLA without taking data](examples/example-2.md) — violates/corrects SE-227.
- [Example 3 — Closing a finding on retest, not on a promise](examples/example-3.md) — violates/corrects SE-231.

## Recall anchors

- No engagement file, no test — the signature is step one, not paperwork.
- Scope is a list, not a vibe: unnamed means untested.
- Minimum proof, zero datasets: demonstrate the flaw, take nothing.
- Scanner output is a lead; only reproduction makes a finding.
- A fix is closed by a retest, never by a reply.

## Checklist

- [ ] Signed engagement file on file, complete per G-SE-111, before any tool ran.
- [ ] Every tested host and technique appears in the engagement scope (G-SE-112).
- [ ] Excluded techniques (DoS, social engineering, physical) unused unless written into the engagement.
- [ ] Evidence uses tester-owned accounts and minimum proof; any real-data exposure reported immediately.
- [ ] Every critical/high finding reproduced, evidenced, and severity-rated (G-SE-113).
- [ ] Every critical/high fix retested; unretested fixes listed as unverified (G-SE-114).
- [ ] All test artifacts removed and removal verified (G-SE-115).
- [ ] Report states scope, window, and limits in its first section.
