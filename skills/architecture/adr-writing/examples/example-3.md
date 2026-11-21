# Example 3 — Topic title and brochure consequences, fixed

## Before

```markdown
# 0007 — Database discussion
Status: accepted
Decision: PostgreSQL.
Consequences: Positive — modern, popular, the team likes it.
```

The title names a topic, not a decision, and the consequences read like an
advertisement: nothing was given up, apparently, and popularity is doing the
arguing.

## After

```markdown
# 0007 — Use PostgreSQL for the primary store
Status: accepted
…
Consequences:
  (+) Row-level security gives platform-enforced tenant isolation (AR-185).
  (+) One store covers relational data and JSON documents, so no second
      database is operated at launch.
  (−) The team's deepest experience is MySQL; the first two migrations took
      measurably longer, and one engineer owns all schema reviews until
      the knowledge spreads.
  (−) Two candidate reporting tools with MySQL-only connectors are
      unavailable to us.
```

Note: corrects AR-247 and AR-244 — titles state the decision, and consequences include at least one negative or cost.
