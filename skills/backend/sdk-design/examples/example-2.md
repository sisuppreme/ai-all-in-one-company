# Example 2 — Catch-and-null replaced by a typed exception

## Before

```ts
async function getInvoice(id: string): Promise<Invoice | null> {
  try {
    const res = await http.get(`/invoices/${id}`);
    return res.data;
  } catch {
    return null; // not found? declined? server down? caller cannot tell
  }
}
```

A missing invoice, an expired credential, and a server outage all arrive at
the caller as the same `null`. Callers write `if (!invoice)` flows that
treat an outage as "no such invoice" and act on it.

## After

```ts
export class ApiError extends Error {
  constructor(
    readonly status: number,
    readonly type: string,        // problem-details `type` URI
    readonly detail: string,
    readonly correlationId: string,
  ) { super(detail); }
}

async function getInvoice(id: string): Promise<Invoice> {
  const res = await http.get(`/invoices/${id}`).catch(async (err) => {
    const problem = err.response?.data;
    throw new ApiError(
      err.response?.status ?? 0,
      problem?.type ?? "about:blank",
      problem?.detail ?? "Request failed",
      problem?.correlationId ?? "unknown",
    );
  });
  return invoiceSchema.parse(res.data);
}
```

Failure is now unmissable and specific: the caller can branch on `status`
and `type`, and support can find the server-side record from the correlation
ID the exception carries.

Note: corrects BE-086 — errors surface as typed exceptions mapped from problem details, preserving status, type, and correlation ID; never swallowed, never null.
