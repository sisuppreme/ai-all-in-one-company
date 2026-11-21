# Example 1 — AEAD field encryption with a fresh nonce

Note: demonstrates SE-145 and SE-146 — sensitive fields use an AEAD construction with a new random nonce per record (BAN-SE-071, DET-CODE-020).

## Before

```js
// "Encrypted" with ECB and a fixed key: identical plaintext blocks produce
// identical ciphertext blocks, and there is no integrity check at all.
const crypto = require("crypto");
const key = Buffer.from(process.env.FIELD_KEY, "hex");

function encryptField(plaintext) {
  const cipher = crypto.createCipheriv("aes-256-ecb", key, null);
  return Buffer.concat([cipher.update(plaintext, "utf8"), cipher.final()]);
}
```

## After

```js
// AES-256-GCM (AEAD) with a fresh 12-byte random nonce per record; the
// nonce and auth tag travel with the ciphertext so tampering is detected.
const crypto = require("crypto");
const key = loadKeyFromKeyStore(process.env.FIELD_KEY_ID); // SE-147

function encryptField(plaintext) {
  const nonce = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv("aes-256-gcm", key, nonce);
  const body = Buffer.concat([cipher.update(plaintext, "utf8"), cipher.final()]);
  return Buffer.concat([nonce, cipher.getAuthTag(), body]).toString("base64");
}
```
