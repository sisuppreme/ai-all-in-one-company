# Provider Annex — llm-integration

Dated annex to the llm-integration skill, per AI-009. Provider-specific patterns live here and inside the wrapper only — never in feature code and never inline in the skill's rules or gates. When the configured provider changes, update this annex and re-date it; the gates (G-AI-001, G-AI-003) reference "the annex's patterns for the configured provider."

- **Annex date:** 2026-11-21
- **Configured provider:** OpenAI

## SDK containment patterns (for G-AI-001)

Grep patterns identifying this provider's SDK imports and endpoint URLs outside the wrapper module:

- SDK import: `from openai`
- Endpoint URL: `api.openai.com`

Example check (adjust the wrapper path to the project): `grep -rn "from openai\|api.openai.com" src/ --include="*.ts" | grep -v "src/llm/"`

## Key patterns (for G-AI-003)

Regex identifying this provider's API keys in the repository and built client bundle:

- Key pattern: `sk-[A-Za-z0-9_-]{20,}`

Example check: `grep -rE "sk-[A-Za-z0-9_-]{20,}" dist/ src/` — run alongside the project's secret scanner in CI.
