# Example 3 — Citation report rebuilt from a fixed prompt panel

## Before

A monthly report contains one slide:

> **GEO is working** — a screenshot of a single ChatGPT answer citing the brand, captured on the 14th, captioned "Cited by ChatGPT ✓".

No prompt set, no other engines, no other runs, no record of answers that did not cite the brand.

## After

The report is rebuilt from the fixed panel of 20 prompts, run three times per engine in the month, with every run logged (date, engine, cited sources):

> | Engine | Runs | Runs citing the brand | Most-cited competing source |
> |---|---|---|---|
> | ChatGPT | 60 | 11 | docs.example-competitor.com |
> | Perplexity | 60 | 17 | en.wikipedia.org |
> | AI Overviews | 60 | 8 | — |
>
> Citation presence is highest on prompts where the guide page carries original release-log data (Example 2). Variance across runs is high; treat single answers as anecdotes.

Note: corrects CO-069, CO-070 — measurement uses a fixed prompt panel with repeated dated runs; a single screenshot is never a report.
