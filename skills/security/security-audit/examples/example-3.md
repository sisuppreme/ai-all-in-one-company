# Example 3 — Finding with an owner and a decision

Note: demonstrates SE-209 and SE-210 — every failure carries severity, a named owner, and a fix-or-accept decision with a date; unowned failures surface as open risks in the summary.

## Before

```markdown
## Appendix C — Other observations

- Login endpoint has no rate limiting.
- Session cookies missing the Secure flag on one subdomain.
- Some error pages show framework version information.
```

Real failures, buried in an appendix: no severity, no owner, no date, and
the summary on page one says the application "is in good shape."

## After

```markdown
## Summary — open risks

F-03 is unowned as of this report and is an OPEN RISK until an owner and
date are assigned (SE-210).

| ID | Requirement | Finding | Severity | Owner | Decision |
|---|---|---|---|---|---|
| F-01 | v5.0.0-… (DET-INF-021) | Debug toolbar reachable in production | High | Platform lead | Fix by 2026-11-28 |
| F-02 | v5.0.0-… (DET-INF-015) | Session cookie without Secure flag on `static.` subdomain | Medium | Backend lead | Fix by 2026-12-05 |
| F-03 | v5.0.0-… (DET-INF-023) | No rate limit on `/login` | High | — unowned — | OPEN RISK |
```

Each failure is rated, owned, and dated — and the one nobody has claimed
is named in the summary, where a reader deciding on the release will see it.
