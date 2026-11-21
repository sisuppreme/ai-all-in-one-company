# Example 1 — Baseline regeneration to green

## Before

A developer tightens the dashboard sidebar from 260px to 232px as an unplanned side effect of a refactor. The visual job fails on six dashboard screenshots. The developer runs the snapshot-update command inside the same feature PR, the job goes green, and the PR description says only "fix tests." The layout change — which pushes the data table into horizontal scrolling at laptop widths — is never reviewed as a design decision and ships.

## After

The visual job fails and the developer opens the diff images: the sidebar shift is real and unintended. The refactor is fixed so the sidebar keeps its width, and the suite returns to green against the existing baselines. When a later, deliberate redesign does change the sidebar, it lands as a baseline-only PR whose description states "sidebar narrows 260px → 232px per design ticket" and a reviewer reads every diff image before approving.

Note: demonstrates QA-082 — baselines change only through a reviewed PR naming the intentional design change.
