# Example 3 — SSRF-safe server-side fetch

## Before

```js
// Fetches any URL the caller supplies — including cloud metadata endpoints
app.post('/link-preview', requireAuth, async (req, res) => {
  const html = await (await fetch(req.body.url)).text();
  res.json({ title: extractTitle(html) });
});
```

## After

```js
import { lookup } from 'node:dns/promises';

const BLOCKED = [/^127\./, /^10\./, /^192\.168\./, /^172\.(1[6-9]|2\d|3[01])\./,
                 /^169\.254\./, /^::1$/, /^::$/];

async function assertPublicHttpUrl(raw) {
  const url = new URL(raw);
  if (url.protocol !== 'https:' && url.protocol !== 'http:') throw new Error('bad scheme');
  const { address } = await lookup(url.hostname);
  if (BLOCKED.some((re) => re.test(address))) throw new Error('private target');
  return url;
}

app.post('/link-preview', requireAuth, async (req, res) => {
  const url = await assertPublicHttpUrl(req.body.url);
  // redirect: 'manual' — each redirect target is re-validated before following
  const resp = await fetch(url, { redirect: 'manual', signal: AbortSignal.timeout(5000) });
  if (resp.status >= 300 && resp.status < 400) {
    const next = await assertPublicHttpUrl(resp.headers.get('location'));
    return res.json(await fetchPreview(next));
  }
  res.json({ title: extractTitle(await resp.text()) });
});
```

Note: demonstrates SE-047 — server-side fetches deny private/loopback/link-local targets and re-validate after redirects (API7/SSRF).
