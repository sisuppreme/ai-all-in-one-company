# Example 1 — The avatar upload that discarded the file

## Before

```js
// Avatar "upload": the file is read into a local object URL for the preview
// and never sent anywhere. The success toast is unconditional.
function onAvatarSelected(file) {
  const previewUrl = URL.createObjectURL(file);
  avatarImg.src = previewUrl;
  toast("Upload successful");
  // Nothing is stored. After reload, the placeholder avatar returns.
}
```

## After

```js
// 1. The app authorizes and registers the intent; the client gets a
//    short-lived presigned URL. Bytes never pass through the app server.
app.post("/api/uploads/intent", requireAuth, async (req, res) => {
  const key = `avatars/${req.user.id}/${crypto.randomUUID()}`;
  await db.uploads.create({
    ownerId: req.user.id,
    objectKey: key,
    originalName: req.body.filename, // display metadata only
    status: "pending",
  });
  const url = await storage.presignPut(key, {
    expiresInSeconds: 300,
    maxBytes: 5 * 1024 * 1024,
    contentType: req.body.contentType,
  });
  res.status(201).json({ uploadId: key, url });
});

// 2. Completion is claimed only after the object provably exists.
app.post("/api/uploads/complete", requireAuth, async (req, res) => {
  const row = await db.uploads.findByKey(req.body.uploadId, req.user.id);
  if (!row) return res.status(404).json(problem(404, "Unknown upload"));
  const exists = await storage.head(row.objectKey);
  if (!exists) return res.status(409).json(problem(409, "Upload not received"));
  await db.uploads.update(row.id, { status: "stored" });
  res.status(200).json({ status: "stored" });
});
```

Note: the slop version reported success with no server copy; the corrected version stores the object and verifies its existence before claiming completion — BE-221, BE-222.
