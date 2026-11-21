# Example 2 — The secret in the trace

## Before

To "make debugging easier," the feature logs the full raw prompt and model output for every call. A user pastes their account recovery code into the chat; it is written verbatim into the trace store, where it sits in plain text, searchable by anyone with log access, long after the session ended.

## After

Prompts and outputs pass through redaction before any write: secrets and PII are replaced with markers, the input is stored as a hash plus its redacted form, and raw text is kept only where the product's privacy rules explicitly allow. The redaction gate sends a canary secret through the feature and asserts it appears in no trace or log.

## Note

Corrects AI-165: redaction happens before logging, never as a later cleanup.
