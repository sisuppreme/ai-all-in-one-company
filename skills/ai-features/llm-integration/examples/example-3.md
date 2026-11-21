# Example 3 — JSON.parse on raw model text, no timeout

## Before

```ts
// extract-invoice.ts
export async function extractInvoice(pdfText: string) {
  const res = await provider.complete({
    prompt: `Extract the invoice fields as JSON: ${pdfText}`,
    // no timeout, no token cap, no schema
  });
  const fields = JSON.parse(res.text); // throws when the reply has prose around the JSON
  await db.invoices.insert(fields); // unvalidated model output written straight to records
}
```

The first reply that wraps its JSON in an explanation crashes the import; a reply with a wrong total or an invented field is written to the database unchecked, and a stalled provider response hangs the job forever.

## After

```ts
// extract-invoice.ts — calls only the wrapper (AI-001)
import { llm } from "../llm/client";

const InvoiceSchema = {
  type: "object",
  properties: {
    vendor: { type: "string" },
    totalCents: { type: "integer" },
    dueDate: { type: "string", format: "date" },
  },
  required: ["vendor", "totalCents", "dueDate"],
} as const;

export async function extractInvoice(pdfText: string) {
  const result = await llm.complete({
    promptId: "invoice-extract",
    input: { pdfText },
    schema: InvoiceSchema, // provider constrains output; wrapper validates it (AI-005)
    // timeout, token budget, and capped retries come from wrapper config (AI-003, AI-004)
  });
  if (!result.ok) return { failed: true, reason: result.error.kind }; // typed error (AI-006)
  const fields = result.value;
  if (fields.totalCents <= 0) return { failed: true, reason: "business-rule" }; // AI-010
  await db.invoices.insert(fields);
  return { failed: false };
}
```

Output is schema-constrained and validated before use, business rules are checked before the write, and every failure mode — timeout, refusal, invalid output — surfaces as a typed, handleable result instead of a crash or a corrupt record.

## Note

Corrected under AI-003, AI-005, and AI-006: parsing raw model text violates BAN-AI-004 (DET-CODE-019), and an unbounded call violates BAN-AI-003 (DET-CODE-033).
