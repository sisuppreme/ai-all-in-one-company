# Example 3 — A complete foreign key

## Before

```sql
CREATE TABLE posts (
  id        bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  author_id bigint,              -- a plain integer: no FK, no index, no delete behavior
  title     text
);
-- Orphaned posts survive every deleted author, and "posts by author"
-- is a sequential scan forever.
```

## After

```sql
CREATE TABLE posts (
  id        bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  author_id bigint NOT NULL REFERENCES users (id) ON DELETE RESTRICT,
  title     text NOT NULL
);

CREATE INDEX posts_author_id_idx ON posts (author_id);
```

Corrects DB-004 (every foreign key column is indexed and declares explicit ON DELETE behavior — here RESTRICT, so an author with posts cannot be deleted silently).
