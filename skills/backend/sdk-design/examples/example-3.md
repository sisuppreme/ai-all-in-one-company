# Example 3 — Hanging call given a mandatory, configurable timeout

## Before

```ts
const client = new ApiClient({ baseUrl: "https://api.example.com" });
// no timeout configured anywhere — the HTTP library's default is "wait forever"

await client.reports.generateMonthly(); // server stalls; this never returns
```

A stalled connection freezes the calling process indefinitely: the batch
job holds its worker and its locks for hours, and nothing in the logs says
why, because no error ever occurs.

## After

```ts
const client = new ApiClient({
  baseUrl: "https://api.example.com",
  timeoutMs: 10_000, // finite default, documented, overridable per client…
});

// …and per call, for operations that legitimately run long:
await client.reports.generateMonthly({ timeoutMs: 60_000 });
```

When the bound is exceeded the SDK aborts the request and throws its typed
timeout error (`ApiError` with `type: "…/problems/timeout"`), so the caller
can log it, retry deliberately, or fail the job — instead of hanging on a
dead connection forever.

Note: corrects BE-085 — every call has a mandatory, configurable timeout with a finite documented default; no SDK call can hang forever.
