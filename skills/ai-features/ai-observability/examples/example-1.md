# Example 1 — The untraceable bad answer

## Before

A user reports that the support assistant invented a refund policy. The team checks the logs and finds one line per request: `AI call ok (812 ms)`. No prompt version, no model, no retrieved chunks, no tokens. Nobody can tell which prompt produced the answer, what it retrieved, or whether the answer can be reproduced — so the "fix" is a guess and the same failure recurs a week later.

## After

The same request produces one trace: feature `support-assistant`, prompt version `support-v3.2`, model ID as returned by the provider, tokens in/out, latency, computed cost, child spans for retrieval (chunk IDs, including the outdated policy chunk), the guardrail verdict, and the final outcome. The team replays the trace, sees the stale chunk, fixes the corpus, and adds the case to the golden dataset.

## Note

Corrects AI-161 and AI-163: one complete trace per call, with the full chain as child spans, so a bad answer is reproducible from its trace alone.
