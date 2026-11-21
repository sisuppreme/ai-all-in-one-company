# Example 2 — Content-Type trust replaced by layered validation

## Before

```js
// The only check is the Content-Type the client chose to send.
app.post("/api/documents", upload.single("file"), (req, res) => {
  if (req.file.mimetype !== "application/pdf") {
    return res.status(400).json({ error: "PDFs only" });
  }
  saveFile(req.file); // a renamed script sails through
  res.json({ ok: true });
});
```

## After

```js
import { fileTypeFromBuffer } from "file-type";

const ALLOWED = new Map([
  [".pdf", "application/pdf"],
  [".png", "image/png"],
  [".jpg", "image/jpeg"],
]);
const MAX_BYTES = 10 * 1024 * 1024;

async function validateUpload({ originalName, bytes }) {
  // Layer 1: size, before any parsing work.
  if (bytes.length > MAX_BYTES) return fail("File exceeds the size limit");
  // Layer 2: extension allowlist on the decoded filename.
  const ext = path.extname(decodeURIComponent(originalName)).toLowerCase();
  if (!ALLOWED.has(ext)) return fail("File type is not allowed");
  // Layer 3: content signature sniffing — the client's word counts for nothing.
  const sniffed = await fileTypeFromBuffer(bytes);
  if (!sniffed || sniffed.mime !== ALLOWED.get(ext)) {
    return fail("File contents do not match an allowed type");
  }
  return { ok: true };
}
```

Note: the slop version trusted the client-supplied Content-Type; the corrected version layers size, extension allowlist, and signature sniffing — BE-223.
