# Contract: D7 → ALL — Security Baseline

- **Backbone link:** #8 of 13 (MASTER_BRIEF.md §3.11) — fan-out
- **Link type:** CONSTRAINS
- **Owner department:** D7 Security
- **Consumer departments:** ALL (D1–D6, D8–D18)
- **Liaisons:** D7 Major Lead (single liaison); each consuming department names one contact in its Phase 2 deliverable map
- **Skills on the owner side:** owasp, secrets-management, security-headers, auth-hardening, dependency-safety (D7)

## Artifact that passes

`SECURITY_BASELINE.md` — the security rules every department's output must satisfy:
authentication and session rules, secrets handling, security headers, input
validation and output encoding, dependency hygiene, and the authorization line
(owner-controlled systems only, written engagement for any penetration testing).

## Format

Markdown baseline, versioned in its header; the enforceable form is the rule and
gate set inside the D7 skills (SE-* IDs). A baseline change is announced to all
consuming departments the same day and applies to new work immediately.

## When it passes

Continuously: the baseline is in force from a project's first commit. Each
department applies it at its own gates; D7 re-issues it on any rule change.

## Acceptance test (how the receiver verifies)

**Joint gate — security.** Each consuming department runs the baseline checklist
for its surface before shipping: no secrets in the repo (scanner output), auth
checks on every route, headers present, dependencies scanned with reachable
critical/high findings at zero. Results are recorded in progress.md per gate.
Under the §5.7 precedence order the baseline outranks every other department's
preference except legal/privacy — a conflict is resolved by satisfying both
(e.g. logging with PII redaction), never by dropping the security rule.

## If the test fails

The output does not ship. A waiver requires a dated risk-acceptance record in
DECISIONS.md naming the rule, the reason, and the expiry — an undocumented
exception is treated as a failure, not a waiver.
