# Example 3 — The confident answer to a question the corpus cannot answer

## Before

```ts
// server/routes/product-qa.ts
const hits = await retrieve(question, { topK: 5 });

const result = await llm.complete({
  promptId: "product-qa",
  input: {
    system: "You are our product assistant. Always give a helpful, specific answer.",
    context: hits.map((h) => h.text).join("\n"),
    question,
  },
});
```

A user asks for the battery capacity of a model the catalog does not carry. Retrieval returns nothing relevant, but the prompt demands a specific answer, so the assistant invents "5,000 mAh, about $349" — stated with the same confidence and formatting as grounded answers, with no way for the user to tell the difference.

## After

```ts
// server/routes/product-qa.ts
const hits = await retrieve(question, { topK: 5 });
const usable = hits.filter((h) => h.score >= RETRIEVAL.relevanceFloor); // AI-067

if (usable.length === 0) {
  return {
    status: 200,
    body: {
      answer:
        "I could not find that in the available product documentation. " +
        "If you can share the exact model name, I can check again, or support can confirm it.",
      citations: [],
    },
  }; // AI-064 — abstention is the correct output
}

const result = await llm.complete({
  promptId: "product-qa",
  input: { contextChunks: usable, question }, // answer only from these, cite chunk IDs (AI-063)
});
```

When the corpus has no answer, the feature says so plainly and offers a next step; when it does answer, every claim traces to a cited chunk. G-AI-032 runs the unanswerable half of the golden set to keep this behavior from regressing.

## Note

Corrected under AI-064 and AI-063: improvising past empty retrieval violates BAN-AI-034 (DET-FAKE-009); the honest outputs are a cited answer or an abstention — nothing between.
