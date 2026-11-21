# Example 2 — The API key in the browser bundle

## Before

```ts
// SummarizeButton.tsx — runs in the browser, ships in the public bundle
import Provider from "provider-sdk";

const client = new Provider({ apiKey: "sk-EXAMPLE-KEY-IN-CLIENT-CODE" });

export async function summarize(text: string) {
  const res = await client.complete({ model: "model-id", prompt: `Summarize: ${text}` });
  return res.text;
}
```

The provider key is embedded in JavaScript every visitor downloads: anyone can extract it and run up charges on the project's account, and the model ID is a literal scattered in a component.

## After

```ts
// Browser side: call our own server endpoint — no key, no provider SDK
export async function summarize(text: string) {
  const res = await fetch("/api/summarize", { method: "POST", body: JSON.stringify({ text }) });
  if (!res.ok) throw new Error("Summarize unavailable");
  return (await res.json()).summary as string;
}

// server/llm/client.ts — the only module that imports the provider SDK
import Provider from "provider-sdk";
import { config } from "../config"; // model ID, timeout, token cap live here (AI-008)

const client = new Provider({ apiKey: process.env.PROVIDER_API_KEY }); // server-side secret

export async function complete(req: LlmRequest): Promise<LlmResult> {
  // timeout, capped retries with backoff, schema validation, typed errors,
  // and metering are implemented once, here, for every feature (AI-003…AI-011)
  // …
}
```

The key now exists only in the server's secrets, the browser holds no provider credential, and a provider or model swap touches this one module and its config.

## Note

Corrected under AI-002: a provider key in client code violates BAN-AI-002 (DET-CODE-018); G-AI-003's secret scan over the built bundle must return zero matches before release.
