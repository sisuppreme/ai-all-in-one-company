# Example 2 — Uncapped decode replaced by capped decode and re-encode

## Before

```js
// The uploaded buffer is decoded at full size with no limits and the
// original bytes are kept as the "processed" image — payload, EXIF
// and all. A decompression bomb expands until the worker dies.
async function processImage(buffer) {
  const img = await sharp(buffer);
  const meta = await img.metadata();
  return { width: meta.width, height: meta.height, bytes: buffer };
}
```

## After

```js
import sharp from "sharp";

const MAX_PIXELS = 40_000_000; // documented cap; over it, reject — do not try
const OUTPUT_FORMAT = "webp";

async function processImage(buffer) {
  // Read the header first and enforce the pixel cap before full decode.
  const meta = await sharp(buffer, { failOn: "error" }).metadata();
  const pixels = (meta.width ?? 0) * (meta.height ?? 0);
  if (pixels > MAX_PIXELS) {
    throw new ProcessingError("IMAGE_TOO_LARGE", "Image exceeds the pixel limit");
  }
  // Decode and re-encode into the allowed format. Re-encoding drops
  // embedded payloads and, by default here, all EXIF metadata.
  const out = await sharp(buffer, { limitInputPixels: MAX_PIXELS })
    .rotate()
    .toFormat(OUTPUT_FORMAT)
    .toBuffer();
  return { width: meta.width, height: meta.height, bytes: out, format: OUTPUT_FORMAT };
}
```

Note: the slop version decoded unbounded input and shipped the original bytes; the corrected version enforces a pixel cap before decode and re-encodes into an allowed format — BE-243, BE-244.
