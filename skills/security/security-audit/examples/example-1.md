# Example 1 — Evidence-backed verdict

Note: demonstrates SE-203 — every in-scope requirement ends in a verdict with evidence attached (BAN-SE-101, DET-CODE-012).

## Before

```markdown
| Requirement | Verdict | Evidence |
|---|---|---|
| v5.0.0-3.x Session management | PASS | |
| v5.0.0-2.x Authentication      | PASS | reviewed |
```

Two pass verdicts, no evidence. Nothing here lets a reader — or a re-audit —
check what was actually verified; the rows assert a result they never ran.

## After

```markdown
| Requirement | Verdict | Evidence |
|---|---|---|
| v5.0.0-3.x Session management | PASS | `evidence/session-config.txt` (idle timeout 30 min, absolute 12 h); `evidence/session-tests.log` — fixation test: pre-login session ID rejected after login; rotation on privilege change confirmed |
| v5.0.0-2.x Authentication      | FAIL | `evidence/zap-baseline-2026-11-21.txt` finding 10202; no rate limit on `/login` — see Finding F-03 (owner, severity, fix date) |
```

Each verdict points at an artifact a second auditor can open and re-check,
and the failure leaves the table as a tracked finding, not a quiet row.
