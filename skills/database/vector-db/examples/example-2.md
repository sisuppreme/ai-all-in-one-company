# Example 2 — A model upgrade that mixed two vector spaces

## Before

The embeddings table has no record of which model produced each vector:

```sql
CREATE TABLE document_embeddings (
  document_id bigint PRIMARY KEY,
  embedding   vector(1536)
);
```

The team upgrades the embedding model. The backfill job writes new-model
vectors into the same column, row by row, over a week. During that week — and
forever, for the rows the job missed — the index holds vectors from two
incompatible models. Nearest neighbors are computed across two different
vector spaces; results degrade silently and no query can tell which rows are
stale.

## After

Every row carries its provenance, and the upgrade is a planned swap:

```sql
CREATE TABLE document_embeddings (
  document_id   bigint NOT NULL,
  chunk_index   int    NOT NULL,
  model_name    text   NOT NULL,
  model_version text   NOT NULL,
  embedding     vector(1536) NOT NULL,
  PRIMARY KEY (document_id, chunk_index, model_version)
);
```

The re-embed writes the new version alongside the old; queries filter to
exactly one version:

```sql
SELECT document_id
FROM document_embeddings
WHERE model_version = 'embed-v2'
ORDER BY embedding <=> $1
LIMIT 10;
```

Recall is verified for `embed-v2` (G-DB-142), reads switch to it, and only
then are the `embed-v1` rows deleted. At no point does one index serve two
models unfiltered.

Note: corrects DB-283 — model name and version are stored with every embedding, and versions never share an index without a filter.
