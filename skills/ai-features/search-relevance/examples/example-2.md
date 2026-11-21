# Example 2 — The manager's pinned product

## Before

```ts
// ranking.ts — added after a stakeholder searched "boots" in a review meeting
const PINNED: Record<string, number> = {
  boots: 4417, // "Summit Boot must be #1 — I searched and it was third"
};

export function rank(results: Result[], query: string) {
  const pin = PINNED[query.trim().toLowerCase()];
  if (pin) results.sort((a, b) => (a.id === pin ? -1 : b.id === pin ? 1 : 0));
  return results;
}
```

One anecdote became a hard-coded pin: exactly one query string is "fixed," every similar query ("hiking boots," "boot") is untouched, the boost exists nowhere in configuration or documentation, and no measurement shows whether users are better served.

## After

```yaml
# search/ranking-config.yaml — versioned, reviewed, measured (AI-132)
signals:
  semantic_relevance: 0.45
  keyword_match: 0.30
  popularity: 0.15
  freshness: 0.10
boosts: []   # none: the "boots" complaint traced to a missing keyword field
changes:
  - date: 2026-11-21
    change: "index product category terms as keywords (fixes the boots query class)"
    ndcg10: { baseline: 0.612, candidate: 0.647 }  # judged set v14 (AI-122)
```

The complaint was investigated as a class: "boots" ranked poorly because category terms were not indexed as keywords. Fixing the indexing lifted the whole query class, the change shipped only after its NDCG@10 beat the baseline on the judged set, and the reasoning is recorded where the next tuner can find it.

## Note

Corrected under AI-125 and AI-122: a hard-coded pin for one anecdote query is the boost pattern behind BAN-AI-065 — invisible, unmeasured, and disguised as relevance; a legitimate fix helps the query class and proves it on the judged set first.
