# Example 2 — Search that answered everything with the same results

## Before

The verifier opens the product's search, types the example query suggested
in the placeholder text, and gets a polished page of results with titles,
prices, and ratings. Search is recorded as working.

The probe used the one query the demo was built around. The results were a
canned fixture: the same list returns for every input, and nothing the user
types changes it.

## After

The probe is re-run with novel inputs (QA-067):

1. A gibberish string — "zxqv wobble 9871" — returns the identical result
   list, in the identical order.
2. A unique marker: a new item is created during the pass with the title
   "Marker Kestrel 4417", then searched for by that exact title. It does not
   appear; the canned list returns again.
3. Network tab: the search box fires no request on submit — the fixture is
   bundled with the page.
4. Verdict recorded in progress.md: search — FAKE, matching DET-FAKE-008
   (search with canned results), evidence filed, defect opened (QA-072).

Note: corrects QA-067 — search is probed with inputs the builder never saw; results must track the input.
