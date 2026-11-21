# Example 3 — Public folder and original names replaced by generated keys

## Before

```js
// Files land in a web-served folder under the name the user picked:
// guessable URLs, path traversal via crafted names, active content
// served from the app's own origin.
app.post("/api/files", upload.single("file"), (req, res) => {
  const dest = path.join(__dirname, "public/uploads", req.file.originalname);
  fs.renameSync(req.file.path, dest);
  res.json({ url: `/uploads/${req.file.originalname}` });
});
```

## After

```js
// The stored name is generated; the bucket is private; the original
// name survives only as display metadata on the record.
const key = `files/${ownerId}/${crypto.randomUUID()}`;
await storage.putObject({ bucket: PRIVATE_BUCKET, key, body: bytes });
await db.files.create({ ownerId, objectKey: key, displayName: originalName });

// Downloads are authorized per request and served via a short-lived
// signed URL — there is no public path to guess.
app.get("/api/files/:id/download", requireAuth, async (req, res) => {
  const file = await db.files.findById(req.params.id);
  if (!file || !canAccess(req.user, file)) {
    return res.status(404).json(problem(404, "Not found"));
  }
  const url = await storage.presignGet(file.objectKey, {
    expiresInSeconds: 120,
    responseContentDisposition: `attachment; filename="${file.displayName}"`,
  });
  res.redirect(302, url);
});
```

Note: the slop version exposed uploads at guessable public paths under user-chosen names; the corrected version generates keys, keeps the bucket private, and authorizes every download — BE-224, BE-225.
