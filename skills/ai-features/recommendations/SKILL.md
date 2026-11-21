# recommendations

## Metadata

- **Owner department:** D17 AI Features (AI)
- **Skill version:** 1.0.0
- **Last verified:** 2026-11-21
- **Sources:** https://cloud.google.com/retail/docs/predict
- **Depends on:** embeddings-search
- **Feeds into:** ai-evaluation, ai-observability

## When to use / Do NOT use

- **Use when:** a surface suggests items to a user from their behavior or from catalog signals — "for you" rails, related-items lists, next-item suggestions — or when an existing recommender's candidates, ranking, fallback, or labels are being added or changed.
- **Do NOT use when:** the task is ranked results for an explicit query (use search-relevance), retrieving documents for a prompt (use rag-retrieval), or computing the embeddings used for content similarity (use embeddings-search). This skill owns what gets recommended, in what order, and under what label — not search, retrieval, or the embedding pipeline.

## Rules

1. **AI-101 — Events before algorithms.** Views, clicks, purchases, and dismissals are logged from launch in one defined schema — user ID, item ID, event type, surface, timestamp, request ID. A recommender with no event stream cannot learn and must not claim to personalize.
2. **AI-102 — Fixed pipeline order.** Serving runs candidate generation, then the hard exclusion filter (AI-103), then ranking, then the response. No stage is skipped, reordered, or merged into another.
3. **AI-103 — Exclusion filtering is deterministic code.** Already-purchased or consumed items, out-of-stock or unavailable items, and items the user is ineligible for are removed by code after candidate generation. Filtering is never delegated to a model or a prompt instruction.
4. **AI-104 — Availability is rechecked at serve time.** Availability and eligibility are verified when the response is built, or read from a cache with a stated TTL. An item that became unavailable after candidate generation is dropped and the slot is backfilled from the remaining filtered candidates.
5. **AI-105 — Every segment has a defined fallback.** Cold-start and low-signal users receive the documented popularity/quality fallback. An empty recommendation slot is a defect, never a shipped state.
6. **AI-106 — Labels tell the truth.** Fallback content is labeled for what it is — "Popular right now", "New in" — and the labels "Recommended for you" / "Picked for you" are used only for lists computed from that user's own signals.
7. **AI-107 — Personalized means computed from the user's signals.** The served list is a function of the user's events and the documented ranking logic. Two users with different histories must be able to receive different lists; identical output for different histories is a failed surface.
8. **AI-108 — Ranking logic is documented and matches production.** Candidate sources, signals, and their order or weights are written down in the serving configuration or a document it references. Behavior nobody can read in the config does not ship.
9. **AI-109 — Every response is logged with its version.** Each served response records the request ID, model/config version, personalized-or-fallback flag, and the item IDs served, so quality can be attributed to a version and a bad version can be rolled back.
10. **AI-110 — Reasons are real and correctable.** Each rail or item carries the true reason it was chosen, taken from the ranking signals that actually fired ("Because you bought X"). Users can dismiss an item or mark "not interested", and the correction changes future output.
11. **AI-111 — Business boosts are explicit configuration.** Boosts and sponsored placements are named entries in the serving config, visible to anyone reviewing it — never hard-coded promotions hidden in code — and boosted items still pass the exclusion filter (AI-103).
12. **AI-112 — Feedback closes the loop.** Impressions, clicks, purchases, and dismissals on recommendations are logged against the serving request ID (AI-109), so the next ranking can learn from them and ai-evaluation can measure whether it did.

## BAN list

- **BAN-AI-051 — One static list under a "For you" label.** Banned: a "Recommended for you" rail that renders the same hard-coded or globally fixed list to every visitor regardless of history. Defeats: DET-FAKE-009. Bad: the home page "Picked for you" rail renders the same six product IDs from a constant array for logged-in users with years of history and for anonymous visitors alike. Instead: compute the list from the user's events (AI-101, AI-107), or serve the fallback under its honest label (AI-105, AI-106). Severity: BLOCK.
- **BAN-AI-052 — Cosmetic exclusion filter.** Banned: exclusion that exists on paper but not in the serving path — purchased or out-of-stock items keep being recommended because filtering is a prompt hint, a UI-side hide, or code that never runs. Defeats: DET-FAKE-017. Bad: the prompt tells the model "avoid items the user owns", and the boots the user bought last week are recommended again, next to a sold-out jacket. Instead: remove owned, consumed, unavailable, and ineligible items in deterministic code after candidate generation, rechecked at serve time (AI-103, AI-104). Severity: BLOCK.
- **BAN-AI-053 — Fabricated recommendation reasons.** Banned: reason text that does not come from a signal that actually fired — template strings like "Because you loved X" attached to items the user never viewed, bought, or rated. Defeats: DET-FAKE-009. Bad: every card in the rail prints "Because you bought the trail shoes" because the template hard-codes it, including for users who have never bought anything. Instead: generate the reason from the logged ranking signal for that item, and omit the reason when no signal fired (AI-110, AI-109). Severity: BLOCK.
- **BAN-AI-054 — Hidden hard-coded promotion.** Banned: a specific product or seller boosted inside a personalized rail by a hard-coded rule in code, with no entry in the serving config and no disclosure. Defeats: DET-FAKE-009. Bad: a developer adds `if (item.id === 4417) score *= 3` before launch; the item tops every user's "For you" rail and nobody reviewing the config can see why. Instead: declare the boost as a named config entry, disclose it where the surface requires, and keep it behind the exclusion filter (AI-111, AI-108). Severity: WARN.
- **BAN-AI-055 — Seed or demo items in a production rail.** Banned: recommendations drawn from seed, fixture, or demo catalog data presented to real users as purchasable products. Defeats: DET-FAKE-014. Bad: the "More like this" rail recommends three seed products with placeholder images that have no product page and cannot be bought. Instead: generate candidates only from the live catalog, and keep demo data behind a visibly labeled demo mode (AI-102). Severity: BLOCK.

## Gates

- **G-AI-051 — Two-user divergence test.** Verifies: AI-107, AI-101. Check (automated): seed two test users through the event API — user A with views and purchases of trail-running items, user B with views and purchases of baking items — then call the recommendations endpoint for each and compare the top-10 item ID lists. Pass: the two lists are not identical. Fail: block shipment. Recorded in: progress.md.
- **G-AI-052 — Exclusion sweep.** Verifies: AI-103, AI-104. Check (automated): for a test user, mark one item purchased and set one item out of stock, then request recommendations 20 times (or exhaust the candidate pool) and assert neither item ID appears in any response. Pass: zero appearances across all responses. Fail: block shipment. Recorded in: progress.md.
- **G-AI-053 — Cold-start fallback test.** Verifies: AI-105, AI-106. Check (automated): create a fresh user with no events, call the recommendations endpoint, and assert (a) the response is non-empty, (b) the items match the documented fallback configuration, and (c) the returned surface label is the fallback label, not "For you". Pass: all three assertions hold. Fail: block shipment. Recorded in: progress.md.
- **G-AI-054 — Serving-log completeness check.** Verifies: AI-109, AI-110, AI-112. Check (automated): make one recommendations request, then query the serving log by that request ID and assert the record carries model/config version, personalized-or-fallback flag, served item IDs, and a reason code per item. Pass: all fields present. Fail: block shipment. Recorded in: progress.md.
- **G-AI-055 — Boost and ranking config audit.** Verifies: AI-111, AI-108. Check (manual): serve recommendations to a neutral test user, list every item whose position is explained by a boost, and confirm each one has a named entry in the serving config and that the documented ranking logic matches the config. Pass: no undeclared boosts; document and config agree. Fail: block shipment. Recorded in: progress.md.

## Anti-patterns

- **Popularity echo.** The ranking over-weights global popularity, so "personalized" lists quietly converge on the same bestsellers for everyone. Catch it in the serving logs: if the overlap between different users' lists keeps climbing, the personal signals are being drowned out — before a reviewer has to notice.
- **Frozen fallback.** The "Popular right now" fallback is a snapshot taken at launch and never refreshed, so it recommends last season's items forever. Catch it by checking the fallback's source: it must be a live query or a config with a refresh date, not a pasted list.
- **Reason drift.** A ranking change ships, but the UI's reason templates still describe the old signals, so explanations stop matching why items were chosen. Catch it by sampling served reasons against the logged reason codes (G-AI-054) after every ranking change.
- **Duplicate slot stuffing.** The same item is placed in several rails on one page to fill space, making a thin catalog look deep. Catch it with a render check that deduplicates item IDs across all recommendation responses on the page.

## Examples

- [Example 1 — The "Picked for you" rail that showed everyone the same six products](examples/example-1.md) — violates/corrects AI-106, AI-107 (BAN-AI-051).
- [Example 2 — Recommended again: the boots you already bought](examples/example-2.md) — violates/corrects AI-103 (BAN-AI-052).
- [Example 3 — The new user who got a blank rail](examples/example-3.md) — violates/corrects AI-105, AI-106.

## Recall anchors

- Events first: no event stream, no personalization claim.
- Filter in code, after candidates — never in a prompt.
- Fallback exists for every segment, and it wears its own label.
- "For you" is a promise: the list must differ by history.
- Log the version with every response, or quality is a rumor.

## Checklist

- [ ] Views, clicks, purchases, and dismissals are logged in the defined event schema from launch (AI-101).
- [ ] Serving runs candidates → exclusion filter → ranking → response, with no stage skipped (AI-102).
- [ ] Purchased, consumed, out-of-stock, and ineligible items never appear in any response; the exclusion sweep passes (AI-103, AI-104, G-AI-052).
- [ ] Two test users with different histories receive different lists (AI-107, G-AI-051).
- [ ] A cold-start user receives the documented fallback, non-empty and labeled as fallback — never "For you" (AI-105, AI-106, G-AI-053).
- [ ] Every response is logged with model/config version, fallback flag, item IDs, and reason codes; feedback events join on the request ID (AI-109, AI-112, G-AI-054).
- [ ] Each item's displayed reason comes from a signal that actually fired, and dismiss / "not interested" corrections change future output (AI-110).
- [ ] All boosts are named serving-config entries; no hard-coded promotion exists in code (AI-111, G-AI-055).
