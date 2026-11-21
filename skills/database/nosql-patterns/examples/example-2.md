# Example 2 — Capping document growth

## Before

```javascript
// Every comment is embedded in the post document — growth is unbounded.
// A popular post eventually exceeds the engine's document size limit and writes fail.
db.posts.updateOne(
  { _id: postId },
  { $push: { comments: { author: "reader-7", body: "...", at: new Date() } } }
);
```

## After

```javascript
// Design cap: a post document holds at most a 3-comment preview plus a count.
// The unbounded side lives in its own collection, referenced by postId.
db.comments.insertOne({ postId: postId, author: "reader-7", body: "...", at: new Date() });
db.posts.updateOne(
  { _id: postId },
  {
    $inc: { commentCount: 1 },
    $push: { recentComments: { $each: [{ author: "reader-7", body: "..." }], $slice: -3 } }
  }
);
// Full comment list: db.comments.find({ postId }).sort({ at: 1 }) — paginated, bounded per page.
```

Corrects DB-044 (growth per document is capped by design; unbounded embedded arrays are forbidden).
