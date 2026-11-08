# AstroLife Knowledge Base

An open, bilingual (Persian/English) knowledge library and offline-first retrieval agent for AstroLife Pro.

**Current release:** 0.1.1  
**Corpus:** 52 curated cards — 26 Persian and 26 English  
**Published:** 2026-11-09

## Design goals
- No paid generative-AI API, account, or API key is required.
- The application combines locally calculated chart facts with this source-attributed library.
- The public, versioned knowledge snapshot can be cached locally and used offline.
- Astronomy, historical astrological doctrine, symbolic interpretation, and empirical research are separate evidence classes.
- Reports use natural language and explain the basis and limitations of interpretations.

## Repository layout
- `data/fa/`, `data/en/`: curated knowledge cards in JSON Lines format.
- `sources/`: source registry, rights notes, and retrieval links.
- `schemas/`: machine-readable validation schema.
- `training/`: reviewed relevance examples and candidate templates.
- `tools/`: validation, indexing, curation, and ML-ranking tools.
- `docs/`: agent architecture, editorial rules, and privacy policy.
- `manifest.json`: version, language counts, file sizes, and SHA-256 hashes used by clients.

## How the agent works
1. AstroLife calculates chart positions and aspects locally. Calculation metadata is preserved.
2. The agent selects knowledge cards that match the actual chart facts, question, and chosen language.
3. Local lexical retrieval and a small supervised ranking model order candidate cards.
4. A deterministic synthesis layer combines relevant ideas, removes duplicates, and produces a short or detailed explanation.
5. The output identifies evidence classes, sources, and limitations.
6. The client checks the public GitHub manifest, verifies downloaded files against SHA-256 values, and activates a validated versioned snapshot. Offline use falls back to the last verified snapshot.

## Machine-learning status and limits
The bundled logistic-regression ranker is an initial relevance model, not a mature general-purpose language model. Its seed evaluation used 80 labelled examples (64 training and 16 holdout); the observed holdout metrics are preliminary and too small to establish robust Persian/English retrieval quality. More independently labelled examples and broader evaluation are required.

Machine learning improves retrieval and ranking. It does **not** establish astrological claims as true, infer facts that are absent from a chart, or autonomously publish new factual content. New knowledge must pass source, rights, language, and editorial review. User-feedback collection and contribution upload are not enabled in the current desktop UI.

## Content and evidence policy
- Astronomy: numerical facts must identify the ephemeris provider, time scale, coordinate frame, settings, and tested range.
- Traditional astrology: described as a historical symbolic framework, not as a scientific law.
- Forecasts: themes for reflection, not inevitable events, guaranteed dates, diagnoses, investment advice, or relationship verdicts.
- Research: report study design and limitations, including important critiques or reanalyses where relevant.
- Copyright: keep links, bibliographic metadata, and original summaries; do not scrape or republish protected books, websites, images, or datasets.

## Privacy
The application requests public library files only. Birth details, chart data, prompts, profiles, and generated reports are not uploaded to this repository for synchronization.

## Licenses
- Source code and tools: MIT (`LICENSE`).
- Original curated knowledge cards: Creative Commons Attribution 4.0 International (`LICENSE-DATA.md`).
- Third-party sources and model weights retain their own licenses; see `sources/sources.json`.

## Release status
- **Public repository:** published.
- **Bilingual seed corpus and manifest:** published as version 0.1.1.
- **Desktop synchronization:** implemented in AstroLife Pro 0.8.3, with SHA-256 validation, staged snapshots, atomic activation, offline fallback, and rollback.
- **Broad independent retrieval evaluation:** still in progress.

This is a curated foundation, not an exhaustive astrological encyclopedia. Astronomy calculations and astrological interpretations have different evidence standards; a correct chart calculation does not prove that a symbolic interpretation predicts real-world events.
