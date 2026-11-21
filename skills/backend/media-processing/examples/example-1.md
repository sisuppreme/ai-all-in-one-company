# Example 1 — Failed transcode silently serving the raw file

## Before

```js
// When the transcode fails, the error is logged and the raw upload is
// served anyway. Users see a "video"; the pipeline sees success.
async function publishVideo(asset) {
  try {
    asset.renditions = await transcode(asset.originalKey, LADDER);
    asset.status = "ready";
  } catch (err) {
    console.log("transcode failed, serving original", err);
    asset.renditions = [{ url: asset.originalUrl, label: "original" }];
    asset.status = "ready";
  }
  await db.assets.save(asset);
}
```

## After

```js
// Failure is a first-class state: visible, retryable, and never
// disguised by serving the raw original in the derivative's place.
async function runTranscodeJob(job) {
  const asset = await db.assets.findById(job.payload.assetId);
  try {
    const renditions = await transcode(asset.originalKey, LADDER);
    await db.assets.update(asset.id, {
      status: "ready",
      renditions: renditions.map((r) => ({
        ...r,
        sourceKey: asset.originalKey,
        recipeVersion: LADDER.version,
      })),
    });
  } catch (err) {
    await db.assets.update(asset.id, {
      status: "failed",
      failureReason: err.code ?? "TRANSCODE_ERROR",
    });
    throw err; // the queue applies its bounded retry policy
  }
}
```

Note: the slop version swallowed the failure and served the raw file as the finished video; the corrected version records an honest failed state with a retry path — BE-247.
