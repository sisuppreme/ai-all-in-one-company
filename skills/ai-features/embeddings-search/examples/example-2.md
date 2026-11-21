# Example 2 — The exact part number semantic search could not find

## Before

A parts catalog ships vector-only semantic search. A customer pastes the exact part number from their invoice, "XR-2041," into the search box. The vector path returns three semantically related parts — similar descriptions, similar categories — but never the XR-2041 record itself, because nothing in a description embedding encodes an arbitrary code exactly. Support tickets call search "broken," and they are right for the queries that matter most.

## After

Retrieval becomes hybrid: the query also runs through the keyword path, and an exact identifier match is merged ahead of vector candidates. Searching "XR-2041" returns the XR-2041 record first, while a descriptive query like "quiet pump for a small aquarium" still benefits from semantic matching. The G-AI-044 test set of real part numbers guards the behavior on every change.

## Note

Violates AI-086 / BAN-AI-045 (vector-only retrieval on a corpus with exact identifiers); corrected by the hybrid keyword path with exact-match precedence.
