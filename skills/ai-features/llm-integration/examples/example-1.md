# Example 1 — The chatbot that never called a model

## Before

```ts
// SupportChat.tsx — "AI-powered support assistant"
const CANNED: Record<string, string> = {
  refund: "You can request a refund within 30 days from your orders page.",
  shipping: "Orders ship within 2 business days and arrive in 3–5 days.",
  default: "Great question! Our team is here to help with anything you need.",
};

export function answer(question: string): string {
  const key = Object.keys(CANNED).find((k) => question.toLowerCase().includes(k));
  return CANNED[key ?? "default"];
}
```

The widget is marketed as an AI assistant, but no model is ever called: keyword matching picks one of three canned paragraphs, and every unlisted question gets the same generic reply.

## After

```ts
// server/routes/support-chat.ts — the browser talks to our server only
import { llm } from "../llm/client"; // the single wrapper module (AI-001)

const AnswerSchema = {
  type: "object",
  properties: { answer: { type: "string" }, citedPolicy: { type: "string" } },
  required: ["answer"],
} as const;

export async function supportChat(question: string) {
  const result = await llm.complete({
    promptId: "support-chat", // versioned prompt, owned by prompt-engineering
    input: { question, policyContext: await loadPolicyContext(question) },
    schema: AnswerSchema,
  });
  if (result.ok) return { status: 200, body: result.value };
  if (result.error.kind === "refusal") return { status: 200, body: FALLBACK_MESSAGE };
  return { status: 503, body: { message: "Assistant unavailable — try again shortly." } };
}
```

The wrapper makes a real, schema-bound model call with timeout, token cap, and typed errors; failures degrade to an honest message instead of a canned paragraph dressed as AI.

## Note

Corrected under AI-001 and AI-012: canned responses presented as model output violate BAN-AI-001 (DET-FAKE-009); canned text is permitted only inside a visibly labeled demo mode.
