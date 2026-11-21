# Example 1 — A gate that had never failed

## Before

The visual-regression gate has been a required check for three months and has never once reported red. Nobody treats this as suspicious until a release ships with the site header shifted 40 pixels: the comparison step was pointing at a baseline directory that the pipeline never updated and the app no longer rendered, so every comparison silently compared the baseline against itself. The gate existed, ran, and exited 0 — it just never judged anything.

## After

The gate's creation checklist now includes a witnessed failure: a seeded-fault branch shifts the header by a known amount, the pipeline runs, and the gate exits non-zero with the diff artifact attached. The same seeded fault joins the nightly negative-control suite (G-QA-111), so if the comparison ever degrades into comparing a file against itself again, the meta-gate goes red and files the defect against the gate, not the header.

Note: demonstrates QA-225 — every gate has a witnessed failure via a seeded fault, repeated on a schedule.
