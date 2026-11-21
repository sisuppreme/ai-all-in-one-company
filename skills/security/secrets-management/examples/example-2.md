# Example 2 — Secret shipped to the browser

## Before

```ts
// checkout page (client bundle) — privileged key exposed to every visitor
const res = await fetch("https://api.provider.example/v1/charges", {
  headers: { Authorization: `Bearer ${import.meta.env.VITE_PAYMENTS_SECRET}` },
});
```

The `VITE_` prefix inlines the value into the shipped JavaScript, where anyone can read it in devtools and spend with it.

## After

```ts
// checkout page — the browser talks only to our own server route
const res = await fetch("/api/charges", { method: "POST", body: formData });
```

```ts
// server route — the real secret stays server-side
export async function POST(req: Request) {
  const key = process.env.PAYMENTS_SECRET_KEY; // server-only env, no client prefix
  // ... make the privileged provider call with `key` here
}
```

Note: demonstrates SE-085; the Before is BAN-SE-043 (defeats DET-INF-006).
