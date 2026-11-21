# Example 3 — Index entry, not a second copy

## Before

DECISIONS.md contains the full text of every record, copied at the time each was written:

```markdown
## ADR-0003 — Session storage

Status: Accepted

Context: Sessions must survive restarts… [full Context, Decision, and
Consequences pasted here, duplicating docs/adr/0003-session-storage.md]
```

ADR-0003 is later superseded by ADR-0016. The record in `docs/adr/` is updated, but the pasted copy in DECISIONS.md is not — the project now states two different "current" decisions about session storage, and a reader cannot tell which one governs.

## After

DECISIONS.md holds one line per record — number, title, status, link — and nothing else:

```markdown
# Decisions

| ADR | Title | Status |
|-----|-------|--------|
| [0003](docs/adr/0003-session-storage.md) | Session storage | Superseded by ADR-0016 |
| [0016](docs/adr/0016-stateless-session-tokens.md) | Stateless session tokens | Accepted |
```

The full Context, Decision, and Consequences live only in the linked files in `docs/adr/`, so there is exactly one canonical copy of each decision and the index can be cross-checked against the records mechanically (G-PM-052).

Note: demonstrates PM-109 — DECISIONS.md is the index that links every record, never a second copy of their content (defeats BAN-PM-054).
