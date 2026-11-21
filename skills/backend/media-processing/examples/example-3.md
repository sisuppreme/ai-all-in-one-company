# Example 3 — EXIF-carrying photo replaced by a stripped, provenanced derivative

## Before

```js
// The original file is copied to the public folder untouched. Its
// EXIF block — including GPS coordinates of the user's home — ships
// to every viewer, and nothing records how the file got there.
async function publishPhoto(file) {
  await storage.putObject({ key: `photos/${file.name}`, body: file.bytes });
  return { url: `https://cdn.example.com/photos/${file.name}` };
}
```

## After

```js
// The derivative is re-encoded (which strips EXIF by default), stored
// privately, and recorded with the provenance needed to regenerate it.
async function publishPhoto(asset, derivative) {
  await db.derivatives.create({
    assetId: asset.id,
    kind: "profile-photo",
    objectKey: derivative.key,
    sourceKey: asset.originalKey, // provenance: what it came from
    recipeVersion: PHOTO_RECIPE.version, // provenance: how it was made
    status: "ready",
  });
  await db.assets.update(asset.id, { status: "ready" });
}

// Verified by gate G-BE-124: a fixture photo with GPS EXIF is run
// through the recipe and the output is asserted to contain no
// location tags before the recipe version is allowed to ship.
```

Note: the slop version shipped the original file with its GPS coordinates and no provenance; the corrected version strips location metadata and records source plus recipe for every derivative — BE-246, BE-249.
