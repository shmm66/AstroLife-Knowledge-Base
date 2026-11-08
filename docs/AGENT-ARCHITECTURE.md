# AstroLife Knowledge Agent Architecture

## Objective
Combine measured chart facts with a local, versioned, source-attributed library. The agent does not call a hosted generative-AI service and must not turn symbolic astrology into a scientific or deterministic claim.

## Runtime pipeline
1. **Input contract:** accept chart positions, houses, aspects, transit events, relationship points, language, report depth and calculation metadata. Do not collect raw birth names unless needed for display.
2. **Fact validation:** check that each requested object, house and aspect is actually present. Missing inputs become explicit limitations, not guessed values.
3. **Topic and language routing:** identify astronomy, research, history, signs, relationships, forecasting and reflective topics; search the requested language corpus.
4. **Retrieval:** combine character n-gram similarity, token overlap, title/tag/entity match, source coverage and topic/language features.
5. **ML reranking:** the small logistic-regression model orders relevant cards. It is a retrieval ranker, not a text-generating model and not a judge of whether astrology is true.
6. **Evidence assembly:** preserve the four evidence classes: astronomical measurement, historical tradition, symbolic reflection and empirical research. Never use a historical or symbolic source to support a physical measurement or a predictive validity claim.
7. **Structured physical reference:** for planet radius, mass, density, sidereal periods, V(1,0), albedo, equatorial gravity and escape velocity, use `data/reference/planetary-parameters.json`. Preserve units and explicit uncertainties. This reference table is not a time-specific ephemeris.
8. **Synthesis:** deterministic templates produce concise or detailed Persian/English prose. Merge duplicate ideas and keep the source note and limitations.
9. **Quality checks:** reject unsupported certainty, fatalistic life events, diagnosis, relationship verdicts, investment advice and claims without evidence IDs.
10. **Output:** produce a Word/HTML report with readable sections, chart facts, interpretation, practical reflection prompts, limitations and source notes.

## Search and source strategy
- Prefer official technical documentation for numerical astronomy (NASA/JPL, IAU).
- Prefer academic catalogues and peer-reviewed sources for intellectual history and empirical research.
- Each card must point to one or more registered source IDs.
- New content is a candidate until source rights, language parity, factual accuracy and editorial review pass.
- Search snippets are discovery aids only; verify the underlying source before adding numerical or methodological claims.
- Keep bibliography metadata separate from the authored summary.

## ML training and evaluation
- Training labels are maintainer-created relevance judgements, not private user data.
- Each query family must include both Persian and English variants and positive/negative candidates.
- Train/holdout split is by the complete bilingual query family, preventing translated versions of the same intent from leaking across the split.
- Report classification metrics and ranking metrics (Precision@3, Recall@3, MRR and nDCG@5).
- The current holdout includes only four bilingual query families; results are exploratory and not an external benchmark.
- Metrics measure retrieval relevance only. They do not measure interpretation quality, chart accuracy or predictive validity.
- Do not advertise the ranker as production-grade until a larger independently annotated bilingual benchmark is available.

## Online and offline library access
- Default: bundled snapshot.
- **Online sync:** call the public GitHub commits endpoint to resolve the current `main` commit SHA; validate that it is exactly 40 lowercase hexadecimal characters; fetch `manifest.json` and all allowed release files from that one immutable commit path.
- Verify byte length and SHA-256 before parsing. Validate source IDs, language counts, unique card IDs, model feature count and structured reference shape.
- Stage the whole release, then atomically activate the new version. Never mix files from different commits.
- **Offline:** continue with the last verified snapshot. A failed download or validation must not delete or corrupt the previous active version.
- Keep the previous two verified snapshots for rollback.
- User birth data, chart, prompt, report and personal profile are never sent to GitHub; only public release files are downloaded.

## Versioning and release
- Every card has a stable ID and revision.
- Every release includes semantic version, release date, language counts, file sizes and SHA-256 hashes.
- Source/data schemas are machine-readable and versioned.
- Client refuses malformed data, unknown source IDs, duplicate IDs, unapproved licenses and hash mismatches.
- Content changes require editorial review; model weights and knowledge cards are released atomically through the same manifest.
