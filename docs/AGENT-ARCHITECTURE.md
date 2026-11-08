# AstroLife Knowledge Agent Architecture

## Objective
Produce a coherent chart interpretation by combining measured chart facts with a local, versioned, source-attributed knowledge base. Do not call a generative-AI service.

## Runtime pipeline
1. **Input contract**: accept chart positions, houses, aspects, transit events, relationship points, report topic, language, depth and calculation metadata. The agent does not accept raw birth names unless needed for display.
2. **Fact validation**: check that every requested planet, house and aspect is actually present. Missing or unsupported calculation data becomes a visible limitation, not a guessed value.
3. **Candidate selection**: create a compact query from the report topic and actual chart facts. Search the local snapshot first.
4. **Retrieval**: combine character n-gram TF-IDF, tag/topic match and language match. Optional embedding search is an opt-in enhancement; no hosted embedding API is used.
5. **ML reranking**: a small logistic-regression ranker scores candidate cards from retrieval similarity, exact concept match, topic/language match and source/evidence metadata. Its weights are trained from reviewed relevance examples and optional explicit user ratings.
6. **Evidence assembly**: group cards by chart fact and report section. Prefer primary/official sources for astronomy and clearly label classical sources as historical doctrine. Never merge astronomical measurement with symbolic interpretation as if they were the same kind of evidence.
7. **Synthesis**: use deterministic templates and editorial rules to form short or detailed Persian/English prose. Merge repeated ideas and keep only the strongest directly relevant points.
8. **Quality checks**: reject unsupported certainty, deterministic life events, contradictory statements, financial/medical/legal advice and claims without evidence IDs.
9. **Output**: produce a Word document with readable headings, short paragraphs, a chart-facts table, plain-language interpretation, practical reflection questions, limitations and source notes.

## Tone rules
- Write as a clear, thoughtful human educator, not as a medical report or academic paper.
- Prefer ordinary words: e.g. "این موضوع می‌تواند به..." instead of "این جایگاه واجد دلالت بر...".
- Explain one idea per paragraph; avoid long strings of technical terms.
- Keep technical labels (orb, house ruler, transit) in the evidence line or glossary, not in the main explanation.
- Use conditional language: "در سنت طالع‌بینی معمولاً چنین برداشتی می‌شود..." and "می‌تواند موضوعی برای فکرکردن باشد...".
- Never say an event will definitely happen, that a relationship must end, or that a person has a fixed personality because of a chart.
- For career and money topics, give ordinary planning questions, not trading, investment or income predictions.

## Online and offline library access
- Default: bundled seed snapshot.
- Online: fetch the public repository manifest over HTTPS, verify version and SHA-256, then fetch changed files only.
- Offline: continue with the last validated snapshot. A failed update must never delete or corrupt the old snapshot.
- No user data, birth details, chart, prompt or feedback is sent to GitHub. Only a public content request is made.
- Cache by version and keep the previous two verified snapshots for rollback.

## Versioning and release
- Every card has a stable ID and revision.
- Every release has a monotonically increasing semantic version, build date, entry counts and file hashes.
- Client refuses malformed data, unknown source IDs, duplicate IDs, unapproved licenses and hash mismatches.
- Content changes require review; code changes and data changes may have separate release notes.
