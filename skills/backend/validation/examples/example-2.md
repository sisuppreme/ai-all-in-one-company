# Example 2 — Canonical-form validation of an uploaded filename

## Before

```ts
function isSafeFilename(name: string): boolean {
  return !name.includes("..") && !name.includes("/");
}
```

The check runs against the raw string the client sent. The filename
`%2e%2e%2fsecret.txt` contains neither `..` nor `/`, passes — and becomes
`../secret.txt` the moment anything downstream URL-decodes it.

## After

```ts
import path from "node:path";

const ALLOWED_EXTENSIONS = new Set([".png", ".jpg", ".pdf"]);

function validateUploadFilename(rawName: string): string {
  // 1. Decode to the canonical form first — this is the value we validate.
  let decoded = rawName;
  for (let i = 0; i < 3 && /%[0-9a-f]{2}/i.test(decoded); i++) {
    decoded = decodeURIComponent(decoded);
  }
  decoded = decoded.normalize("NFC");

  // 2. Validate the decoded value: bare name only, allowlisted extension.
  const base = path.basename(decoded);
  if (base !== decoded) {
    throw new ValidationError("filename", "path separators are not allowed");
  }
  if (!ALLOWED_EXTENSIONS.has(path.extname(base).toLowerCase())) {
    throw new ValidationError("filename", "file type is not allowed");
  }
  return base; // display metadata only — the stored name is server-generated
}
```

Every encoding layer is peeled before the check, so the value that is
validated is the value that will be used. The decoded traversal name fails
the basename test and is rejected with a 422.

Note: corrects BE-045 — validate the decoded, canonical form of input, never the raw string.
