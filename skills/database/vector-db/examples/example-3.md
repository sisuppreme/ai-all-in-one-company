# Example 3 — Recall measured before the parameter change shipped

## Before

Search latency is high, so an engineer lowers the HNSW query-time parameter
in configuration:

```text
SET hnsw.ef_search = 20;   -- was 100
```

Latency improves. Nobody measures recall. On the project's real query set,
recall@10 has fallen from 0.97 to 0.71 — nearly a third of the true nearest
neighbors no longer appear — and the only symptom is users reporting that
"search feels worse lately."

## After

The change is gated on a recall measurement against exact search, run on a
fixed sample of real queries stored with the project:

```sql
-- Exact top-10 for one sample query (index disabled)
SET LOCAL enable_indexscan = off;
SELECT document_id
FROM document_embeddings
WHERE model_version = 'embed-v2'
ORDER BY embedding <=> $1
LIMIT 10;

-- ANN top-10 for the same query, with the candidate parameters
SET LOCAL hnsw.ef_search = 40;
SELECT document_id
FROM document_embeddings
WHERE model_version = 'embed-v2'
ORDER BY embedding <=> $1
LIMIT 10;
```

recall@10 is the overlap of the two sets, averaged over the sample set. The
recorded threshold is 0.95: `ef_search = 40` measures 0.96 and ships;
`ef_search = 20` measures 0.71 and does not. The measurement, the threshold,
and the parameter value are recorded together in progress.md (G-DB-142), so
the next tuning change starts from evidence instead of folklore.

Note: corrects DB-284 — ANN recall is measured against exact search before launch and after any index-parameter change.
