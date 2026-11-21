# DET-CRWL — Evidence Pipeline Parameters (X-Crawl)

Purpose: these parameters gate the evidence pipeline itself. No harvested issue or proposed detection parameter enters the OmniForge system until its evidence record passes the checks below; a record that fails stays out, however interesting the claim.
How to run the check: work the record top to bottom against DET-CRWL-001 through 018 in order. Any blocker failure stops intake for that record until it is fixed, corroborated, relabeled, or dropped and logged.

### DET-CRWL-001 — Source meets the bar
- **Signal:** the record's source fields — author or channel name, publication date, live URL.
- **Failure pattern:** anonymous posts, undated screenshots, and "a video said" entries enter as evidence; nobody can re-check them, so errors become permanent.
- **Professional:** every source is named, dated, and reachable at intake; anything missing a field is returned to the harvester, not filed.
- **Check:** open the URL, confirm the byline or channel name and the date on the page itself match the record.
- **False positives:** a named author writing under a pseudonym — acceptable if the pseudonymous identity is stable and the page is dated and reachable.
- **Severity:** blocker.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** X-Crawl intake review.

### DET-CRWL-002 — Claim is in the source
- **Signal:** the exact passage in the source that supports the recorded claim.
- **Failure pattern:** a summary of a summary drifts at each retelling; the record ends up asserting something the original never said.
- **Professional:** the record quotes or tightly paraphrases the primary source, and the supporting passage is located before filing.
- **Check:** find the claim verbatim or near-verbatim in the cited source; if the record cites a secondary write-up, trace to the primary source and cite that instead.
- **False positives:** a faithful paraphrase that changes wording but not meaning — distinguish by comparing scope and qualifiers, not wording alone.
- **Severity:** blocker.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** Verification & Sources.

### DET-CRWL-003 — Transcript and quotes verified against the original
- **Signal:** quoted lines and transcript excerpts in the record versus the original audio, video, or document.
- **Failure pattern:** auto-captions garble names, numbers, and negations; an unverified quote can invert what the source actually said.
- **Professional:** every quote is checked against the original at its timestamp; caption errors are corrected in the record and the correction is noted.
- **Check:** play or read the original at the recorded timestamp and compare word for word; a mismatch voids the quote until corrected.
- **False positives:** minor caption punctuation or filler-word differences that do not change meaning — note them, do not void the record.
- **Severity:** blocker.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** Verification & Sources.

### DET-CRWL-004 — Corroboration or reproduction
- **Signal:** the record's corroboration field — second source, or a reproduction note.
- **Failure pattern:** a single creator's one-off mistake or staged demo becomes a "known AI failure" and spawns parameters chasing an incident that never recurs.
- **Professional:** an issue enters as established only when a second independent source reports it or the failure is reproduced from the recorded steps.
- **Check:** confirm the second source is independent (not quoting the first) or that the reproduction log exists and matches the recorded steps.
- **False positives:** two outlets reporting the same launch event — that corroborates the event, not the failure claim; the failure itself still needs its own second source.
- **Severity:** major.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** Verification & Sources.

### DET-CRWL-005 — Duplicates merged
- **Signal:** near-identical issues filed under different wording, tools, or dates.
- **Failure pattern:** the same incident counted five times inflates frequency, distorts severity calibration, and produces duplicate parameters.
- **Professional:** duplicates are merged into one record that keeps every source URL and the earliest date; merge history is preserved.
- **Check:** search the base by tool, failure signature, and source before filing; if a match exists, merge instead of creating a new record.
- **False positives:** genuinely distinct incidents with the same failure signature in different tools — keep separate records, cross-link them as related.
- **Severity:** major.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** X-Crawl deduplication pass.

### DET-CRWL-006 — Severity from the shared scale
- **Signal:** the severity field and the scale criterion it cites.
- **Failure pattern:** severity reflects the harvester's mood or the source's outrage; everything loud becomes a blocker and real blockers stop standing out.
- **Professional:** severity is assigned only from the shared scale's criteria (user impact, frequency, detectability), and the criterion used is recorded.
- **Check:** re-derive the severity from the scale using the record's own facts; if the assigned level needs facts not in the record, downgrade or complete the record.
- **False positives:** a genuinely severe but quiet issue (silent data loss) — the scale's impact criterion, not visibility, governs.
- **Severity:** major.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** Verification & Sources severity review.

### DET-CRWL-007 — Provenance fields complete
- **Signal:** URL, publication date, access date, in-source timestamp for audio/video, harvester identity, harvest method.
- **Failure pattern:** a record without an access date or timestamp cannot be re-verified later; when the source changes or vanishes, the claim becomes untestable.
- **Professional:** provenance is captured at harvest time, in full, before the record is filed; incomplete records are held, not filed.
- **Check:** verify every provenance field is present and the URL resolves to the cited content as of the access date.
- **False positives:** sources with no visible publication date — record "undated" explicitly plus the access date; an explicit gap is acceptable, a silent one is not.
- **Severity:** major.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** X-Crawl intake review.

### DET-CRWL-008 — Blocked or paywalled sources dropped and logged
- **Signal:** any record whose source sits behind a paywall, login wall, or crawler block.
- **Failure pattern:** harvesters route around blocks with mirrors, cached scrapes, or shared logins; the pipeline inherits ToS and legal exposure and evidence nobody else can inspect.
- **Professional:** the source is dropped, the drop is logged with reason and date, and harvesting moves on. Blocks are never worked around.
- **Check:** confirm each filed source is openly reachable; confirm the drop log contains every blocked source encountered this cycle.
- **False positives:** a source that was open at harvest and later paywalled — keep the record, annotate the change and the access date; do not re-harvest around the wall.
- **Severity:** blocker.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** X-Crawl, with D14 source review on disputes.

### DET-CRWL-009 — Copyright: summaries only
- **Signal:** the length and form of source material stored in the record.
- **Failure pattern:** full transcripts, chapters, or article bodies get pasted into the base — a copyright violation and an unsearchable data dump.
- **Professional:** records store the pipeline's own summary plus short attributed excerpts only where a quote is the evidence; the full text stays at the source.
- **Check:** scan the record for long verbatim runs; anything beyond a short evidentiary quote is replaced with a summary and a link.
- **False positives:** short verbatim quotes with attribution, and text under an open license — both acceptable; note the license when it applies.
- **Severity:** blocker.
- **Source:** https://www.youtube.com/t/terms?gl=BR
- **Fix:** X-Crawl, with D14 source review.

### DET-CRWL-010 — Stale claims re-verified on schedule
- **Signal:** the record's last-verified date against the re-verification interval for its claim type.
- **Failure pattern:** tool behavior, pricing, limits, and detector accuracy change; last year's verified claim is presented as current fact.
- **Professional:** every record carries a re-verification due date; on the date, the claim is re-checked against the live source or downgraded to historical.
- **Check:** list records past due; for each, re-run DET-CRWL-002 and 003 against the current source and stamp a new verified date.
- **False positives:** claims about fixed historical events (a dated incident) — these do not expire, but their "still current" framing does.
- **Severity:** major.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** Verification & Sources re-verification queue.

### DET-CRWL-011 — Vendor claims flagged as claims
- **Signal:** any claim originating from the maker of the tool, model, or detector being described.
- **Failure pattern:** a vendor's benchmark, accuracy figure, or "solves X" marketing line is filed as measured fact; parameters then calibrate against advertising.
- **Professional:** vendor-originated claims carry a VENDOR CLAIM label until an independent source measures the same thing; the label travels with the claim everywhere it is cited.
- **Check:** identify the claim's origin; if it traces only to the vendor's site, deck, or sponsored content, apply the label before filing.
- **False positives:** vendor documentation of plain mechanics (an API's parameters) — that is reference material, not a performance claim; performance and accuracy assertions are what get labeled.
- **Severity:** blocker when presented as fact without the label; otherwise major.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** Verification & Sources, with D14 source review.

### DET-CRWL-012 — Community anecdotes labeled as anecdotes
- **Signal:** claims sourced from forum posts, comments, social threads, or chat logs.
- **Failure pattern:** one user's unverified story is filed as a field report; the base fills with folklore that parameters then treat as observed behavior.
- **Professional:** community material is labeled ANECDOTE at intake, may motivate a reproduction attempt, and graduates only via DET-CRWL-004.
- **Check:** confirm the label is present and that no downstream parameter cites the anecdote as established evidence.
- **False positives:** a named practitioner posting a detailed, reproducible report in a forum — still an anecdote until reproduced, but flag it as a priority reproduction candidate.
- **Severity:** major.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** X-Crawl intake review.

### DET-CRWL-013 — Unevidenced parameters marked DERIVED
- **Signal:** a proposed parameter with no harvested issue behind it.
- **Failure pattern:** plausible-sounding parameters invented at a desk enter the system indistinguishable from evidence-backed ones, and nobody ever validates them.
- **Professional:** such parameters are marked DERIVED, state the reasoning they derive from, and sit in a validation queue until evidence or a failed validation resolves them.
- **Check:** for every parameter, follow its evidence link; if none exists, confirm the DERIVED mark and a queue entry are present.
- **False positives:** parameters derived directly from a cited standard or official documentation — cite the standard as the source instead; that is sourced, not DERIVED.
- **Severity:** blocker when an unevidenced parameter is presented as evidence-backed; otherwise minor.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** Verification & Sources validation queue.

### DET-CRWL-014 — Crawl permission respected
- **Signal:** the target site's robots.txt and terms, checked before any automated harvesting.
- **Failure pattern:** the crawler ignores disallow rules or site terms; harvesting gets blocked mid-run and the project inherits the reputation and the exposure.
- **Professional:** robots.txt is fetched and honored per the Robots Exclusion Protocol before crawling a domain; terms-restricted sources route to DET-CRWL-008.
- **Check:** confirm a robots.txt check is logged for each crawled domain and that no disallowed path appears in the harvest log.
- **False positives:** a site with no robots.txt — absence means no crawler restrictions stated, not a block; proceed and log the absence.
- **Severity:** blocker.
- **Source:** https://www.rfc-editor.org/rfc/rfc9309.html
- **Fix:** X-Crawl crawl operations.

### DET-CRWL-015 — Dead links recovered or retired
- **Signal:** filed URLs that no longer resolve to the cited content.
- **Failure pattern:** link rot silently hollows out the base; records remain but their evidence is gone, and nobody notices until a parameter is challenged.
- **Professional:** a dead source is recovered through a Wayback Machine snapshot of the same URL and content, or the record is downgraded to unverifiable and its parameters flagged.
- **Check:** re-resolve filed URLs on the re-verification cycle; for each dead one, query the Wayback CDX index for a capture matching the access date and confirm the captured content matches the record.
- **False positives:** a temporarily down site that returns within the cycle — re-check before downgrading; a snapshot whose content differs from the record is not a recovery.
- **Severity:** major.
- **Source:** https://github.com/internetarchive/wayback/blob/master/wayback-cdx-server/README.md
- **Fix:** Verification & Sources, with X-Crawl support.

### DET-CRWL-016 — Harvest method within platform terms
- **Signal:** how each transcript or page was obtained — official captions, API, manual viewing, or a downloader.
- **Failure pattern:** transcripts ripped through tools that violate platform terms contaminate the base; the method is hidden, so the exposure surfaces only when challenged.
- **Professional:** the harvest method is recorded per source and is one the platform's terms permit; prohibited methods void the record regardless of content quality.
- **Check:** audit the method field against the platform's current terms (for YouTube, the Terms of Service restrict downloading and automated access except as expressly authorized).
- **False positives:** a creator's own content downloaded through the platform's provided tools — expressly authorized, and the authorization is what the method field should say.
- **Severity:** blocker.
- **Source:** https://www.youtube.com/t/terms?gl=BR
- **Fix:** X-Crawl, with D14 source review.

### DET-CRWL-017 — Corrections and retractions checked
- **Signal:** the source's current state versus its state at harvest — edits, pinned corrections, retractions, follow-up posts.
- **Failure pattern:** a creator corrects or retracts the original claim, but the base keeps citing the pre-correction version as fact.
- **Professional:** re-verification includes a correction check; corrected claims are amended in the record with the correction noted, and retracted claims are withdrawn and their parameters flagged.
- **Check:** on each re-verification, scan the source and the author's channel for corrections or follow-ups referencing the original claim.
- **False positives:** a follow-up that adds context without changing the claim — annotate the record, do not amend the claim itself.
- **Severity:** major.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** Verification & Sources re-verification queue.

### DET-CRWL-018 — Numbers traced to their measurement
- **Signal:** any statistic, percentage, or benchmark figure in a record.
- **Failure pattern:** figures circulate detached from their study, sample, or methodology; a number from a twelve-person demo ends up calibrating detection thresholds.
- **Professional:** every figure records who measured it, on what, with what method, and when; a figure that cannot be traced is removed or labeled UNTRACED and excluded from calibration.
- **Check:** follow the figure to its primary measurement; confirm the method and sample are recorded and plausibly support the use the parameter makes of it.
- **False positives:** figures from official documentation describing the vendor's own system limits — those are specifications, citable as such, not measurements.
- **Severity:** blocker when an untraced figure is used for calibration; otherwise major.
- **Source:** Derived: MASTER_BRIEF §3.3 + EVIDENCE_BASE.md method.
- **Fix:** Verification & Sources.
