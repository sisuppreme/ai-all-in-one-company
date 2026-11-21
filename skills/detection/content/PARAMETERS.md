# X-Content Detection Parameters (DET-CON)

Purpose: give any agent a repeatable way to tell whether a site's copy and data are real, edited, and internally consistent — or AI-generated filler and fabrication shipped as fact.
How to run: crawl every public page's visible text plus `<title>`, meta description, OG/Twitter tags, JSON-LD, and alt text; check each parameter in order; record parameter ID, URL, and the exact quoted string for every hit. A parameter passes only when its Check step finds nothing.
Severity rule: any fabricated testimonial, statistic, review, credential, or person is a **blocker** (Real Content Rule) — one hit fails the whole content pass.

### DET-CON-001 — Lorem ipsum in production
- **Signal:** Body copy, headings, or `<title>` containing "lorem ipsum" or any variant fragment.
- **AI-typical:** Whole paragraphs of filler left where generated copy was never replaced.
- **Professional:** Every visible string is final copy a human approved for that slot.
- **Check:** Full-text search of rendered pages and titles for `lorem`, `ipsum`, `dolor sit amet`.
- **False positives:** A design-history or typography article quoting lorem ipsum as its subject — distinguish by surrounding context discussing the filler itself.
- **Severity:** major (blocker on checkout, pricing, or payment pages).
- **Source:** https://docs.squirrelscan.com/rules/content/placeholder-text
- **Fix:** placeholder-scan, real-content

### DET-CON-002 — Template and CMS defaults
- **Signal:** "Hello world!" posts, "Just another WordPress site", sample pages, theme demo copy, "Add a description here".
- **AI-typical:** Scaffold or theme content published untouched because generation filled every slot with something.
- **Professional:** Demo content is deleted at setup; every shipped page was written for this business.
- **Check:** Search for known default strings from the stack in use; list all pages created by the installer.
- **False positives:** A tutorial site demonstrating a fresh install — distinguish by framing that names it as a demo.
- **Severity:** major.
- **Source:** https://www.verifixscan.com/problems/placeholder-text-in-production
- **Fix:** placeholder-scan, real-content
- **See also:** DET-CODE-024 (unadapted boilerplate in code and routes is CODE-024's scope; CON-002 owns default content published as pages)

### DET-CON-003 — Unrendered template syntax and leaked values
- **Signal:** Visible `{{name}}`, `${title}`, `%s`, or the literal words `undefined`, `null`, `NaN`, `[object Object]` in prose or titles.
- **AI-typical:** Generated templates printed without the data ever being wired up.
- **Professional:** Rendering is verified end-to-end; missing values are guarded, never printed.
- **Check:** Regex the rendered HTML and `<title>` for template delimiters and stringified-value tokens.
- **False positives:** Developer documentation showing template syntax inside code blocks — exclude `<code>`/`<pre>` elements.
- **Severity:** major.
- **Source:** https://docs.squirrelscan.com/rules/content/placeholder-text
- **Fix:** placeholder-scan

### DET-CON-004 — Developer markers left in copy
- **Signal:** `TODO`, `FIXME`, `xxxxx`, `test test`, "coming soon", "content to follow" in fields, meta, or alt text.
- **AI-typical:** Draft annotations carried into the shipped string because no editorial pass read the fields.
- **Professional:** Drafts keep markers in the repo, never in published fields.
- **Check:** Search body text, meta descriptions, and alt attributes for the marker strings.
- **False positives:** A changelog honestly announcing a "coming soon" feature — distinguish by a date or roadmap context and no implication the feature exists now.
- **Severity:** minor (major in meta descriptions or structured data).
- **Source:** https://www.verifixscan.com/problems/placeholder-text-in-production
- **Fix:** placeholder-scan

### DET-CON-005 — Placeholder contact details
- **Signal:** `example.com` / `example@example.com` addresses, 555-01xx phone numbers, "123 Main Street" in live contact blocks.
- **AI-typical:** Theme contact blocks shipped unedited; generated footers inventing plausible-looking details.
- **Professional:** Every contact detail is real, tested, and reaches a monitored inbox or line.
- **Check:** Search for `example.`, `555-01`, and template addresses; send a test message to each published address.
- **False positives:** Code samples and documentation, where example.com is the correct reserved domain — distinguish by context being instructional.
- **Severity:** major (blocker on contact and checkout pages).
- **Source:** https://docs.squirrelscan.com/rules/content
- **Fix:** placeholder-scan, real-content
- **See also:** DET-CODE-024 (sample entities left in code are CODE-024's scope; CON-005 owns placeholder contact details in live content)

### DET-CON-006 — Generic marketing filler
- **Signal:** Sentences like "revolutionize your workflow", "unlock the power of", "take your business to the next level" with no product-specific fact attached.
- **AI-typical:** Benefit claims that could be pasted onto any competitor unchanged — because they were generated from the category, not the product.
- **Professional:** Claims name the mechanism, the user, and a verifiable outcome.
- **Check:** Highlight every benefit sentence; for each, ask "could a competitor print this verbatim?" On interior pages, flag yes-answers with no specific within one sentence either side. On homepages and landing heroes, apply the test at page level: flag only when the whole page stays at that altitude — a generic hero block or feature trio surrounded by specific copy elsewhere on the page does not fail.
- **False positives:** Deliberately broad taglines and hero/feature copy are normal professional register — distinguish by the page as a whole: specifics anywhere on the page (product detail, named mechanisms, real figures) clear individual generic sentences; flag when no part of the page descends to specifics.
- **Severity:** minor (major when it is the page's only substantive copy).
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** copywriting, content-strategy

### DET-CON-007 — AI vocabulary cluster
- **Signal:** Dense co-occurrence of delve, tapestry, landscape (metaphorical), realm, furthermore, moreover, "it's important to note", "in today's fast-paced world" in one page.
- **AI-typical:** Default model register: the same connective scaffolding and elevated filler words recur because nothing was edited out.
- **Professional:** Vocabulary follows the subject and the house style, not a model's defaults.
- **Check:** Count cluster terms per 1,000 words per page; flag pages where several cluster terms and both stock openers appear together.
- **False positives:** Academic or literary writing where these words are native — distinguish by density across the whole site, not a single page, and by co-occurring parameters (006, 008, 009).
- **Severity:** minor alone; major as corroboration with 008/009.
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** copywriting

### DET-CON-008 — Repetitive structure across pages
- **Signal:** Pages or posts sharing the same skeleton: identical heading patterns, same paragraph count and order, sentences differing only in swapped keywords.
- **AI-typical:** One prompt template stamped out per page; structure repeats because generation, not an editor, set it.
- **Professional:** Structure varies with the material; recurring formats (e.g. release notes) vary in substance.
- **Check:** Compare heading sequences and paragraph shapes across any five same-type pages; flag near-identical skeletons with keyword-only differences.
- **False positives:** Legitimately templated content like spec sheets or event listings — distinguish by whether the variable fields carry real, page-specific data.
- **Severity:** major (also a scaled-content-abuse risk).
- **Source:** https://developers.google.com/search/docs/essentials/spam-policies
- **Fix:** content-strategy, copywriting

### DET-CON-009 — Hedge stacks
- **Signal:** Chains like "may potentially help to possibly improve", "can sometimes generally tend to" — three or more qualifiers protecting one claim.
- **AI-typical:** The model avoids committing, so claims dissolve into stacked modality instead of being verified or cut.
- **Professional:** Claims are either substantiated and stated plainly, or removed; a single honest qualifier where uncertainty is real.
- **Check:** Search for qualifier clusters (`may`/`might`/`can`/`potentially`/`possibly` within five words of each other) around product claims.
- **False positives:** Regulated copy (health, finance) where hedges are legally required — distinguish by whether a substantiated, specific claim exists alongside.
- **Severity:** minor.
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** copywriting

### DET-CON-010 — Fabricated testimonials
- **Signal:** Quoted praise from named people with no verifiable existence: no company, no link, no matching profile, generic five-star wording.
- **AI-typical:** Invented quotes with plausible names ("Sarah M., Marketing Manager") generated to fill a social-proof section.
- **Professional:** Every testimonial traces to a real customer who gave it, with permission, in a form the business can produce.
- **Check:** For each testimonial, require a source record (email, review-platform link, signed quote). Search the exact quote text on the open web — duplicates on unrelated sites confirm fabrication.
- **False positives:** Genuinely anonymized quotes for privacy — distinguish only when the business holds the underlying named source record; absence of any record is a fail.
- **Severity:** blocker.
- **Source:** https://workingmarketer.com/articles/ai-content-disclosure-rules/ (FTC rule bans fake testimonials, including AI-generated ones)
- **Fix:** real-content
- **See also:** DET-VIS-027 (the avatar tell that accompanies fabricated testimonials; CON-010 owns the verdict on the quote itself)
- **See also:** DET-FAKE-014 (the same invented people shipped as seed data are FAKE-014's scope; CON-010 owns the testimonial verdict)

### DET-CON-011 — Fabricated or unsourced statistics
- **Signal:** Precise numbers in copy — "87% faster", "trusted by 10,000+ teams", "4.9/5 rating" — with no source, study, or internal data behind them. Third-party claims (ratings, market share, comparisons against others) are the highest-risk class; self-attested first-party counters ("84 million accounts") are a separate class, handled differently in the Check.
- **AI-typical:** Round, impressive figures generated to make copy sound evidenced; numbers differ between pages (see 015).
- **Professional:** Every number cites its source or the dataset it came from, and one canonical figure is used site-wide.
- **Check:** List every quantitative claim and classify it. (a) Third-party/market claims — ratings, market share, benchmark or comparison figures: demand the citation or dataset; provenance may live anywhere on the same domain (annual letter, status page, docs), not necessarily on the page — no provenance anywhere, no pass. (b) Self-attested first-party usage counters: their dataset is the operator's own systems, which no external check can inspect — do not fail them for a missing citation; route them to the consistency check (DET-CON-015) and require a fact-sheet entry, flagging only when contradicted elsewhere or implausible on their face.
- **False positives:** Clearly labeled illustrative examples ("imagine a team of 50…") — distinguish by hypothetical framing and no presentation as measured fact. Self-attested operational counters from an identifiable, operating business are first-party data, not fabrication — distinguish them from invented figures by consistency across the site and a fact-sheet entry, not by an external citation that cannot exist.
- **Severity:** blocker for third-party/market claims with no provenance anywhere; major for first-party counters that are contradicted or facially implausible. Unsourced-but-consistent first-party counters are a fact-sheet gap, not a fail.
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** real-content, fact-sheet
- **See also:** DET-VIS-035 (the visual tell — a uniform band of round numbers; CON-011 owns the fabrication verdict, and a VIS-035 hit must escalate to this check)

### DET-CON-012 — Fabricated credentials, awards, and press
- **Signal:** "As featured in" logos, award badges, certifications, or partnership claims with no corresponding announcement, listing, or certificate.
- **AI-typical:** Trust furniture generated to complete a landing-page layout; logos of outlets that never covered the product.
- **Professional:** Each badge links to the actual coverage, award listing, or verifiable credential.
- **Check:** For every logo/badge/claim, follow it to independent confirmation on the issuer's or outlet's own site. Unconfirmed equals fabricated.
- **False positives:** Expired certifications still within a grace period — distinguish by a real, checkable history with the issuer; no history at all is fabrication.
- **Severity:** blocker.
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** real-content
- **See also:** DET-VIS-034 (the visual tell in the logo row; CON-012 owns the fabrication verdict, VIS-034 covers rendering of real marks)

### DET-CON-013 — Fake review patterns
- **Signal:** On-site reviews that are uniformly five-star, similarly phrased, posted in date clusters, from reviewers with no verifiable purchase or presence elsewhere.
- **AI-typical:** A generated review block written to look like demand; sentiment and sentence shape barely vary.
- **Professional:** Reviews come from a platform or a verified-purchase flow, include critical ones, and match the product's real rating distribution.
- **Check:** Sample the reviews; check phrasing overlap, date clustering, and whether any review exists on an independent platform. Cross-check the displayed average against the actual set.
- **False positives:** A genuinely new product with few, enthusiastic early reviews — distinguish by small count and identifiable reviewers; volume plus uniformity is the tell.
- **Severity:** blocker.
- **Source:** https://www.jdsupra.com/legalnews/a-guide-to-understanding-ftc-s-4503495/ (FTC Endorsement Guides and the Consumer Reviews and Testimonials Rule, 16 CFR Part 465)
- **Fix:** real-content
- **See also:** DET-VIS-027 (uniform avatar presentation is the visual tell; CON-013 owns the fake-review verdict)
- **See also:** DET-FAKE-014 (seed reviews shipped as real demand overlap FAKE-014's scope; CON-013 owns the review-pattern verdict)

### DET-CON-014 — Copy contradicts the fact sheet
- **Signal:** Any published claim — founding date, feature, price, capability, location — that differs from the project's fact-sheet.md entry for the same fact.
- **AI-typical:** Each page generated independently, so each invents or drifts on the facts it needed.
- **Professional:** Copy is written from the fact sheet; one source of truth, checked at review.
- **Check:** Extract every checkable fact from copy; diff against fact-sheet.md line by line. Every mismatch is a hit, whichever side is wrong.
- **False positives:** None for the mismatch itself — a legitimate recent change means the fact sheet is stale; fix the stale side and record which was corrected.
- **Severity:** major (blocker when the fact is price, capability, or a credential).
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** fact-sheet, real-content

### DET-CON-015 — Site contradicts itself
- **Signal:** Two pages stating different values for the same fact: founded 2019 vs 2021, "team of 12" vs "team of 50", different user counts, different addresses.
- **AI-typical:** Pages generated at different times with no shared memory, each rounding or inventing independently.
- **Professional:** Canonical facts live in one place and are reused, not re-typed.
- **Check:** Build a fact table (entity, value, page) for company age, size, counts, addresses, names; flag every entity with two or more values.
- **False positives:** Dated content legitimately reflecting its publication time ("our team of 12", 2022 post) — distinguish by visible date context; undated evergreen pages must agree.
- **Severity:** major.
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** fact-sheet, content-strategy

### DET-CON-016 — Price mismatch
- **Signal:** A price, plan name, or billing term on marketing pages that differs from the pricing page, FAQ, or checkout for the same plan.
- **AI-typical:** Pricing copy generated per page; a discount or tier invented for one landing page and never reconciled.
- **Professional:** Prices render from one data source; every mention matches the checkout amount exactly.
- **Check:** Tabulate every price mention per plan across the site; compare against the pricing page and a test checkout total.
- **False positives:** Time-limited promotions — distinguish by visible promotion dates and terms; an undated cheaper price elsewhere is a mismatch.
- **Severity:** blocker.
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** fact-sheet, real-content

### DET-CON-017 — Name inconsistencies
- **Signal:** The company, product, feature, or a person's name spelled or styled differently across pages ("TaskBoard" vs "Taskboard" vs "Task Board").
- **AI-typical:** Names re-generated rather than copied, drifting in capitalization, spacing, and spelling.
- **Professional:** A naming list exists and every surface follows it exactly.
- **Check:** Extract all proper nouns; cluster near-identical variants; flag any entity with more than one live form.
- **False positives:** Deliberate rebrands with dated announcements — distinguish by the announcement and consistent post-rebrand usage; silent mixed usage fails.
- **Severity:** minor (major for legal names, prices' plan names, and people's names).
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** fact-sheet, copywriting

### DET-CON-018 — Stale dated copy
- **Signal:** "Register now" for a past event, "new for 2024" on evergreen pages, expired sale banners, copyright years far behind, deadlines already passed.
- **AI-typical:** Time-anchored copy generated once and never revisited; the page asserts a present that has ended.
- **Professional:** Dated claims carry owners and review dates; expired promotions come down on schedule.
- **Check:** Extract every date-bearing claim; compare each against today's date and the fact sheet. Flag anything asserting a past event as upcoming or current.
- **False positives:** Archived, clearly dated posts and past-event recaps — distinguish by archive framing and past-tense presentation.
- **Severity:** major.
- **Source:** https://docs.squirrelscan.com/rules/content
- **Fix:** content-strategy, real-content

### DET-CON-019 — Stock-photo people presented as the real team
- **Signal:** Team or "about us" photos that are stock images or generated portraits, captioned with employee names and roles.
- **AI-typical:** A generated team grid completes the page; the people do not exist or are models.
- **Professional:** Team photos are of the actual people, or the page uses no portraits rather than substitutes.
- **Check:** Reverse-image-search each team portrait; check whether the same face appears on stock libraries or unrelated companies' pages.
- **False positives:** A real employee who also does stock modeling — distinguish by the person's own verifiable profile (e.g. LinkedIn) matching name, role, and photo.
- **Severity:** blocker.
- **Source:** https://workingmarketer.com/articles/ai-content-disclosure-rules/ (invented author personas and AI portraits treated as deceptive)
- **Fix:** real-content
- **See also:** DET-VIS-023 (imagery depicting nothing real is VIS-023's tell; CON-019 owns the verdict when stock faces are captioned as the team)
- **See also:** DET-VIS-027 (placeholder/AI avatar presentation is VIS-027's tell; CON-019 owns the named-team-member verdict)
- **See also:** DET-FAKE-014 (seed people presented as customers are FAKE-014's scope; CON-019 owns stock photos presented as the actual team)

### DET-CON-020 — Missing or fabricated authorship
- **Signal:** Blog posts with no byline, or bylines naming people with no profile, no history, and no existence outside the site.
- **AI-typical:** Posts published authorless, or under an invented persona complete with headshot and bio, to simulate an editorial team.
- **Professional:** Every post names a real author whose role and identity the publisher can evidence.
- **Check:** List all bylines; for each, require an author page plus one independent trace (staff page, professional profile). No trace, no pass.
- **False positives:** House bylines ("The Support Team") on genuinely collective content like release notes — distinguish by the byline being an accountable team, not a fake individual.
- **Severity:** major (blocker when the persona carries credentials — see 012).
- **Source:** https://workingmarketer.com/articles/ai-content-disclosure-rules/ (Google's Who/How/Why guidance on accurate bylines)
- **Fix:** real-content, content-strategy

### DET-CON-021 — One voice, many authors
- **Signal:** Posts credited to different authors with indistinguishable voice: same sentence rhythms, openers, transitions, and structural habits.
- **AI-typical:** One model wrote everything; bylines were assigned afterward for appearance.
- **Professional:** Different authors read differently, or a single author is honestly credited.
- **Check:** Take two posts by "different" authors; compare first sentences, transition words, and paragraph structure side by side. Near-identical fingerprints across three or more authors is a hit.
- **False positives:** A strong house style guide plus one editor — distinguish by whether the credited authors are real people (020) who confirm writing their pieces.
- **Severity:** major.
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** content-strategy, real-content

### DET-CON-022 — Title and meta description mismatch
- **Signal:** `<title>` or meta description promising content the page does not contain: different topic, product, offer, or a default string ("Add a description here").
- **AI-typical:** Metadata generated from the keyword target rather than the finished page, or left as template defaults.
- **Professional:** Metadata is written from the final page and describes exactly what the visitor gets.
- **Check:** For each page, read title + description against the H1 and first section; flag topic, offer, or entity mismatches and any default strings.
- **False positives:** Intentional campaign landing pages with ad-matched titles — distinguish when the page body delivers the titled promise under different wording.
- **Severity:** major.
- **Source:** https://www.verifixscan.com/problems/placeholder-text-in-production
- **Fix:** structured-data, copywriting

### DET-CON-023 — OG and social card mismatch
- **Signal:** `og:title`, `og:description`, or `og:image` naming a different product, old branding, another page's content, or template text.
- **AI-typical:** Social tags generated once at scaffold time and never updated as pages changed; shares preview the wrong thing.
- **Professional:** Social metadata is per-page, current, and matches what the link actually opens.
- **Check:** Dump all OG/Twitter tags site-wide; compare each against its page's title, topic, and current branding; flag cross-page duplicates with different destinations.
- **False positives:** A deliberate site-wide default OG image — distinguish image reuse (acceptable) from wrong titles/descriptions (not).
- **Severity:** major.
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** social-open-graph, structured-data

### DET-CON-024 — Structured data contradicts the page
- **Signal:** JSON-LD fields disagreeing with visible content: `aggregateRating` with no reviews on the page, prices, dates, or author names that differ from what renders.
- **AI-typical:** Schema generated as decoration, importing impressive values the page itself never claims.
- **Professional:** Structured data is generated from the same data as the visible page and says nothing the page doesn't.
- **Check:** Parse every JSON-LD block; diff each field against the rendered page and the fact sheet. Any field with no visible counterpart is a hit.
- **False positives:** Legitimately page-external data like organization founding date — distinguish by verifying it against the fact sheet instead of the page.
- **Severity:** blocker when ratings, reviews, or prices are fabricated; otherwise major.
- **Source:** https://developers.google.com/search/docs/essentials/spam-policies
- **Fix:** structured-data, real-content

### DET-CON-025 — Scaled near-duplicate pages
- **Signal:** Sets of pages identical except a swapped city, keyword, or product name, each thin and adding no page-specific information.
- **AI-typical:** A location/keyword matrix generated to capture search traffic rather than serve readers.
- **Professional:** Every indexed page exists because its content is substantively different and useful.
- **Check:** Cluster pages by text similarity; for each cluster over three pages, read two fully — if swapping the keyword back makes them interchangeable, flag the set.
- **False positives:** Genuinely local pages with real local data (staff, stock, pricing, regulations) — distinguish by the volume of verified page-specific fact.
- **Severity:** major.
- **Source:** https://developers.google.com/search/docs/essentials/spam-policies (scaled content abuse)
- **Fix:** content-strategy

### DET-CON-026 — Unsubstantiated superlatives
- **Signal:** Measurable ranking claims — "#1", "largest by revenue", "best-rated", "the leading provider" — with no ranking, survey, or criteria anywhere behind them. Unmeasurable comparative puffery ("most comprehensive", "sets a new standard", "easiest-to-use") is ordinary marketing register and out of scope here (a minor copy note at most).
- **AI-typical:** Superlatives are the model's default register for product copy; nobody checked whether the claim could be defended.
- **Professional:** Comparative claims name the comparison set and source, or are rewritten as plain descriptions.
- **Check:** Search copy for superlative terms and classify each. Measurable claims (a rank, a share, a rated position): demand the substantiation link or record — none available, claim comes out. Unmeasurable puffery: record as a minor copy note, not a finding. Where a superlative wraps a sourced figure, test the figure's provenance under DET-CON-011 and treat the adjective as puffery.
- **False positives:** Clearly subjective puffery in an opinion context ("our favorite release yet") and unmeasurable comparatives in a house voice ("the famously straightforward…") — distinguish measurable market claims from register; only the former can fail this check.
- **Severity:** major for unsubstantiated measurable ranking claims; unmeasurable puffery is a minor copy note, not a finding under this parameter.
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** copywriting, real-content

### DET-CON-027 — Alt text and captions that don't describe the media
- **Signal:** Alt text reading `DSC_0001`, "image", "photo", a keyword string, or describing content the image does not show; captions naming the wrong person or event.
- **AI-typical:** Alt fields filled generically at generation time, or written from the prompt rather than the actual image.
- **Professional:** Alt text is written from the rendered image and says what a sighted reader sees.
- **Check:** Sample images per page; compare each alt/caption against the actual image content. Flag defaults, keyword strings, and any description mismatch.
- **False positives:** Decorative images correctly carrying empty alt (`alt=""`) — distinguish intentional emptiness from a wrong description.
- **Severity:** minor (major when the caption misidentifies a person — see 019).
- **Source:** https://docs.squirrelscan.com/rules/content
- **Fix:** placeholder-scan, copywriting

### DET-CON-028 — Promises with no backing process
- **Signal:** Copy promising "24/7 support", "money-back guarantee", "cancel anytime", "response within one hour" where no policy page, process, or terms exist to honor it.
- **AI-typical:** Trust phrases generated because the layout needed reassurance, never checked against operations.
- **Professional:** Every operational promise links to the policy or workflow that makes it true.
- **Check:** List every service promise; for each, find the backing policy page or documented process. A promise with no backing artifact is a hit.
- **False positives:** Aspirational roadmap language clearly framed as future ("we're working toward round-the-clock support") — distinguish by tense and framing; present-tense promises must be real.
- **Severity:** blocker when the promise affects purchase decisions (guarantees, refunds); otherwise major.
- **Source:** Derived: PROJECT_ANATOMY.md Part 1/6/12
- **Fix:** real-content, fact-sheet
