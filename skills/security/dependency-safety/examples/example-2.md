# Example 2 — Muted critical vs. VEX note

## Before

```toml
# .osv-scanner.toml
[[IgnoredVulns]]
id = "GHSA-xxxx-yyyy-zzzz"
reason = "probably fine"
```

A critical finding in a shipped dependency is silenced with no analysis, no owner, and no expiry — it will never be looked at again.

## After

```markdown
# VEX note — GHSA-xxxx-yyyy-zzzz (critical, package: example-lib 2.3.1)
- Status: not_affected — vulnerable function `parseLegacy()` is never called;
  verified by code search over src/ (0 call sites) on 2026-11-21.
- Scanner suppression expires: 2027-02-21, or immediately if any call site appears.
- Owner: backend lead. Re-check is part of the quarterly dependency review.
```

The finding stays visible, the exemption is written, dated, and expires.

Note: corrects SE-104 and SE-112; the "before" is BAN-SE-052.
