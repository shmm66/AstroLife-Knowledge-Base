# AstroLife Knowledge Base

An open, bilingual (Persian/English) knowledge library and offline-first retrieval agent for AstroLife Pro.

## Design goals
- No paid generative-AI API, account, or API key is required.
- The desktop/mobile application combines its own calculated chart data with this source-attributed library.
- The same versioned knowledge snapshot is available to users worldwide through a public Git repository and is cached locally for offline use.
- Scientific astronomy, historical astrological doctrine, modern symbolic interpretation, and empirical research are separate evidence classes.
- Reports use natural, everyday language and explain what each interpretation is based on.

## Repository layout
- `data/fa/`, `data/en/`: curated knowledge cards in JSON Lines format.
- `sources/`: source registry, rights notes, and retrieval links.
- `schemas/`: machine-readable validation schema.
- `training/`: reviewed relevance examples and opt-in feedback format.
- `tools/`: local validation, indexing, curation, and ML-ranking pipeline.
- `docs/`: agent architecture, editorial rules, and privacy policy.
- `manifest.json`: immutable version, counts, and SHA-256 hashes used by clients.

## How the agent works
1. AstroLife calculates chart positions and aspects locally. Calculation metadata is preserved.
2. The agent selects only knowledge cards matching those chart facts, the user's question, and the selected language.
3. A lightweight multilingual TF-IDF retriever finds related cards. A small supervised ranking model reorders them using reviewed examples and optional user feedback.
4. A deterministic synthesis layer combines overlapping ideas, removes duplicates, and writes a short or detailed explanation in plain language.
5. Each section includes its evidence type and source references. Unsupported or conflicting claims are disclosed instead of guessed.
6. The client checks the public manifest for a new version, downloads only changed files, validates their hashes, and stores a local snapshot. When offline, it uses the last verified snapshot.

## Machine learning boundaries
Machine learning improves topic classification, duplicate detection, retrieval and ranking. It does **not** establish astrological claims as true, learn private birth charts, or invent new facts. New knowledge is first a candidate, then must pass source, license, translation and editorial review before publication.

The initial ranker is intentionally small. It is not advertised as highly accurate until an independent Persian/English test set demonstrates useful Precision@5 and Recall@5. Local relevance feedback is optional and stays on the device unless the user explicitly exports an anonymized training contribution.

## Content and evidence policy
- Astronomy: numerical facts must identify the ephemeris provider, time scale, coordinate frame, settings and tested range.
- Traditional astrology: described as a historical symbolic framework, not as a scientific law.
- Forecasts: describe themes for reflection, not inevitable events, guaranteed dates, diagnoses, investment advice or relationship verdicts.
- Research: report both the original study and important critiques/reanalyses where relevant.
- Copyright: keep links, bibliographic metadata and original summaries; do not scrape or republish protected books, websites, images or datasets.

## Licenses
- Source code: MIT (`LICENSE`).
- Original curated knowledge cards: Creative Commons Attribution 4.0 International (`LICENSE-DATA.md`).
- Third-party sources and model weights retain their own licenses; see `sources/sources.json`.

## Current status
This is the first curated seed release. The corpus is useful as a foundation, not yet an exhaustive astrological encyclopedia. Public publication, application-side sync, and broad relevance evaluation are release gates; do not claim them complete until their checks pass.
