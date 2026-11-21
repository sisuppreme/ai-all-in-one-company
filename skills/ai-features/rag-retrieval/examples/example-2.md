# Example 2 — "Just don't tell them" permissions

## Before

```ts
// server/routes/assistant.ts — one corpus for everyone
const hits = await retrieve(question, { topK: 8 }); // no user, no filter

const result = await llm.complete({
  promptId: "assistant",
  input: {
    system:
      "Answer from the context. Some context is internal-only: " +
      "do not reveal internal documents unless the user is staff.",
    context: hits.map((h) => h.text).join("\n---\n"),
    question,
  },
});
```

Every chunk in the corpus — including internal-only documents — is placed in front of the model for every user, and the only barrier is a sentence asking the model to keep secrets. A customer who asks the right follow-up gets the internal document summarized, because the model was shown it.

## After

```ts
// server/routes/assistant.ts — filter at retrieval, before the prompt exists (AI-062)
const hits = await retrieve(question, {
  topK: 8,
  filter: { aclAny: accessAttributesFor(user) }, // enforced by the index query itself
});

logRetrievalTrace({ query: question, chunkIds: hits.map((h) => h.id), userId: user.id }); // AI-069

const result = await llm.complete({
  promptId: "assistant",
  input: { contextChunks: hits, question }, // only chunks this user may see
});
```

The index query itself excludes chunks the requester cannot access, so unauthorized content never enters the prompt and there is nothing for a clever prompt to extract. G-AI-033 proves it: a restricted marker fact is unanswerable for an unauthorized user.

## Note

Corrected under AI-062: permission-by-instruction violates BAN-AI-032 (DET-FAKE-021); enforcement belongs in the retrieval filter, not in the model's goodwill.
