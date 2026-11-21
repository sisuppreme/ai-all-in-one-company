# Example 1 — The model swap that silently scrambled search

## Before

The provider announces a newer embedding model. A developer updates the model name in the search configuration and re-embeds only the documents changed that week. The index now holds vectors from two incompatible models. Search still returns results — plausible-looking, but no longer related to the queries — and the regression is blamed on "the new model being worse." Nothing in the deploy records which vectors came from which model, so the damage cannot even be scoped.

## After

The model change is treated as an index rebuild: the full corpus is re-embedded with the new model into a fresh index whose metadata records the new model name and dimension. The fixed query set runs against both indexes and recall@K for the new index is compared with the recorded baseline before traffic switches. The old index is kept until the new one passes, then removed — never merged.

## Note

Violates AI-083 / BAN-AI-043 (model swapped without a full re-embed); corrected by a full rebuild plus the G-AI-042 recall gate before rollout.
