# Example 4 — A generated recall fixture

## Before

A project launches semantic search before it has real user queries to
measure with. The team defers the recall check — "we will measure once real
queries exist" — and tunes `ef_search` by feel in the meantime. When real
queries finally arrive, nobody can say what recall the index shipped with,
and there is no fixture to re-run after the next parameter change.

## After

The recall fixture is generated inside the test itself, from synthetic data
only — no production records, no copied query logs. A fixed seed makes the
fixture identical on every run:

```python
# tests/test_recall_fixture.py — all data synthetic, generated in-test
import random

SEED = 20261121
DIM = 64            # small synthetic dimension for the fixture
N_DOCS = 5_000
N_QUERIES = 50
K = 10
THRESHOLD = 0.95    # the recall bar recorded with the index (DB-284)

def make_fixture():
    rng = random.Random(SEED)
    # 20 synthetic topic centers; each document vector is a center plus noise
    centers = [[rng.uniform(-1, 1) for _ in range(DIM)] for _ in range(20)]
    docs = []
    for i in range(N_DOCS):
        c = centers[i % len(centers)]
        docs.append([v + rng.gauss(0, 0.05) for v in c])
    # Paraphrase queries: a document vector perturbed in-test, so the true
    # neighbors are known by construction, not by assumption
    queries = []
    for q in range(N_QUERIES):
        base = docs[rng.randrange(N_DOCS)]
        queries.append([v + rng.gauss(0, 0.02) for v in base])
    return docs, queries
```

The test loads the generated vectors into a scratch table, builds the ANN
index with the candidate parameters, and computes recall per query:

```text
for each generated query:
    exact_top_k = top-K by cosine distance with the index disabled
    ann_top_k   = top-K by cosine distance through the ANN index
    recall@K   += |ann_top_k ∩ exact_top_k| / K
recall = recall@K / N_QUERIES
assert recall >= THRESHOLD
```

Because the fixture is regenerated from the seed on every run, the same
check runs before launch and after any index-parameter change, and the
tenant-filtered variant (DB-290) reuses the same generator with a synthetic
tenant column added. The measured figure and the threshold are recorded
together in progress.md (G-DB-142). Once real queries exist, they join the
sample set alongside the fixture — the fixture is the floor, not a
substitute for production-shaped measurement.

Note: corrects DB-284 — recall is measured against exact search on a fixed sample set, generated synthetically in the test when no production query set exists yet.
