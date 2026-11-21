# Example 2 — Live configuration check

Note: demonstrates SE-208 — the deployed configuration is verified live, not inferred from the repository (BAN-SE-102, DET-INF-021).

## Before

```markdown
Finding area: debug and admin surfaces
Verdict: PASS — reviewed the route table in the repository; no debug
routes are registered, and DEBUG is false in the production settings file.
```

The repository is clean, but the deployed build was assembled with a
different settings module — and nothing in this verdict ever touched the
running system.

## After

```markdown
Finding area: debug and admin surfaces
Verdict: FAIL — live probes against https://app.example.com on 2026-11-21:
  curl -s -o /dev/null -w "%{http_code}" https://app.example.com/__debug__/  -> 200
  curl -s -o /dev/null -w "%{http_code}" https://app.example.com/.env        -> 404
The framework debug toolbar is reachable in production (DET-INF-021).
Evidence: evidence/probes-2026-11-21.txt. Finding F-01: severity High,
owner: platform lead, fix by 2026-11-28, re-probe at re-audit (SE-212).
```

The probe output — not the source tree — carries the verdict, and the
mismatch between repo and deployment is itself recorded as the finding.
