# Example 3 — The 0.8 threshold copied from a tutorial

## Before

A developer follows a semantic-search tutorial and copies its similarity threshold of 0.8 into the project's configuration. On this corpus and this embedding model, genuine matches routinely score between 0.55 and 0.75, so most correct results are filtered out and search appears empty; a few irrelevant high-scoring chunks slip through and erode trust further. Nobody can say what the threshold should be, because it was never measured against this data.

## After

The team builds a fixed query set from real search logs — queries paired with the documents users actually needed — and sweeps candidate thresholds against it, recording precision and recall at each value. The chosen cutoff is the one the measurements support for this corpus and model, and the sweep results are committed alongside the configuration. When the model or corpus changes, the sweep re-runs under G-AI-042 instead of the old number being trusted by inertia.

## Note

Violates AI-087 (threshold copied, never measured); corrected by tuning the cutoff on the fixed real-query set and recording the measurements.
