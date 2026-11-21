# Example 1 — The whole PDF in the prompt

## Before

```ts
// server/routes/handbook-qa.ts — "Ask the handbook anything"
import handbookText from "../assets/handbook-full-text.json"; // 212 pages, pasted once at project start

export async function askHandbook(question: string) {
  return llm.complete({
    promptId: "handbook-qa",
    input: {
      system: `Answer using this handbook:\n${handbookText}`,
      question,
    },
  });
}
```

The "retrieval" is a snapshot of the handbook pasted into a JSON file when the project started. There is no chunking, no index, and no re-index step: the handbook was revised twice since, and the assistant still answers from the old text — while the context cost of the full document is paid on every question.

## After

```ts
// indexing/handbook-pipeline.ts — run on every handbook change (AI-065)
export async function indexHandbook(doc: SourceDocument) {
  const chunks = chunk(doc.text, { size: RETRIEVAL.chunkSize, overlap: RETRIEVAL.overlap }); // AI-067
  for (const c of chunks) {
    await index.upsert({
      id: `${doc.id}:${c.ordinal}`,
      sourceId: doc.id,
      acl: doc.acl, // access attributes travel with the chunk (AI-062)
      embedding: await embed(c.text), // the one recorded model (AI-068)
      text: c.text,
    });
  }
}

// server/routes/handbook-qa.ts — retrieve, filter, then generate (AI-061, AI-072)
export async function askHandbook(user: User, question: string) {
  const hits = await retrieve(question, { topK: RETRIEVAL.topK, aclFor: user });
  if (hits.length === 0) return ABSTAIN_RESPONSE; // AI-064
  return llm.complete({
    promptId: "handbook-qa",
    input: { contextChunks: hits, question }, // chunks inserted delimited, as data (AI-066)
  });
}
```

The corpus is chunked and indexed with source IDs and ACL metadata, retrieval returns only the relevant passages, and editing the handbook triggers the same pipeline — so a corrected policy corrects the answer (AI-071).

## Note

Corrected under AI-061: a pasted document snapshot is a fixture index, violating BAN-AI-033 (DET-FAKE-008); real retrieval chunks, embeds, indexes, and re-indexes on change.
