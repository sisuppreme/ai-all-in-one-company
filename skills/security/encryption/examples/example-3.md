# Example 3 — HTTPS-only internal call that fails closed

Note: demonstrates SE-143 and SE-152 — sensitive traffic uses verified HTTPS and fails closed instead of falling back to plaintext (BAN-SE-072, DET-INF-014).

## Before

```js
// The billing service's certificate expired, so the call was switched to
// plain HTTP "temporarily" — card tokens now cross the network in clear.
async function chargeCard(token, amount) {
  const res = await fetch("http://billing.internal/charge", {
    method: "POST",
    body: JSON.stringify({ token, amount }),
  });
  return res.json();
}
```

## After

```js
// Verified HTTPS only. If the certificate or transport is broken, the
// charge fails and is queued for retry — it never downgrades to HTTP.
async function chargeCard(token, amount) {
  const res = await fetch("https://billing.internal/charge", {
    method: "POST",
    body: JSON.stringify({ token, amount }),
  });
  if (!res.ok) throw new Error(`billing charge failed: ${res.status}`);
  return res.json();
}
```
