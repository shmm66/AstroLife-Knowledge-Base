# AstroLife Knowledge Base

An open, bilingual Persian/English knowledge library and offline-first retrieval agent for AstroLife Pro.

**Release:** 0.3.1
**Curated corpus:** 190 reviewed seed cards — 95 Persian and 95 English  
**Registered sources:** 52  
**Structured planetary reference:** 8 IAU planets + 5 JPL-listed dwarf planets  
**Release date:** 2026-11-09

## What is included
- Bilingual knowledge cards covering planets, houses, signs, aspects, transits, relationships, Solar Hijri month-cohort horoscopes, solar whole-sign houses, personal Solar Returns, calendar boundaries, annual-revolution history, wellbeing boundaries, astronomical methods and empirical research.
- A structured NASA JPL planetary-parameters dataset with units, published uncertainties where available, and separate dwarf-planet classification.
- Source registry, machine-readable card schema, licensing notes, editorial policy and privacy rules.
- A small offline logistic-regression relevance ranker trained on maintainer-curated bilingual query families.
- A versioned manifest with SHA-256 checksums and a public GitHub distribution endpoint for other apps and agents.

## How an agent can use it
1. Read `manifest.json` and select the desired language corpus.
2. Validate every downloaded file against the listed byte length and SHA-256 before use.
3. Parse JSON Lines cards using `schemas/knowledge.schema.json`.
4. Resolve each card's `source_ids` against `sources/sources.json`.
5. For physical and orbital parameters, read `data/reference/planetary-parameters.json` and preserve units and any published uncertainty.
6. Use the bundled ranker in `artifacts/ranker-model.json` for relevance ordering, not for generating or validating scientific claims.
7. Preserve the evidence class: astronomical measurement, historical tradition, symbolic reflection or empirical research.

A client should pin all files for a release to one immutable Git commit, verify hashes, stage the snapshot and only then activate it. The AstroLife Pro desktop client does this and keeps a previous verified snapshot for offline fallback and rollback.

## Evidence and content boundaries
- **Astronomy:** numerical statements are attributed to official sources such as NASA/JPL and the IAU. A coordinate requires its epoch, time scale, reference frame and observing centre.
- **History:** sources such as Oxford reference works and the Ptolemaeus Arabus et Latinus project document what historical traditions taught; historical influence is not proof of predictive validity.
- **Symbolic astrology:** sign and planet interpretations are original reflective summaries, not measured personality traits or guaranteed outcomes.
- **Empirical research:** the library records specific study designs, samples and outcomes. Findings are not extrapolated beyond the claims that were tested.
- **Copyright:** protected source texts and data are not copied into this repository. It contains source links, bibliographic metadata and original summaries.

## Machine-learning evaluation
The 0.3.1 ranker was trained on 228 maintainer-curated relevance judgements spanning 27 bilingual query families. Persian and English variants remain grouped together to avoid cross-language family leakage. The current group-disjoint evaluation uses 20 training groups and 7 holdout groups (62 candidate judgements).

Holdout results: classification accuracy 0.823, precision 0.828, recall 0.800 and F1 0.814; ranking Precision@3 0.857, Recall@3 0.607, MRR 1.000 and nDCG@5 0.968.

These are preliminary results on a small, maintainer-labelled holdout, not an independent external benchmark. They measure retrieval relevance only—not the scientific validity of astrology or the correctness of an interpretation. The holdout is useful for regression checks but should not be described as independent validation. More independently authored Persian and English query families, blind double annotation and adjudication are required before describing the ranker as production-grade.

## Privacy
The public repository contains no birth profiles, names, charts, prompts, relationship details or generated reports. The desktop app downloads public library files only. User chart data is not uploaded to GitHub. The current UI does not collect or upload feedback for model training.

## Licenses
- Source code and tools: MIT (`LICENSE`).
- Original curated cards and editorial summaries: Creative Commons Attribution 4.0 International (`LICENSE-DATA.md`).
- Third-party works and model artifacts retain their own licenses; see `sources/sources.json`.

## Release status
- Public repository: published at https://github.com/shmm66/AstroLife-Knowledge-Base. Client sync pins one immutable commit and verifies SHA-256.
- Offline-first AstroLife Pro integration: downloads a public snapshot pinned to one immutable Git commit, verifies manifest byte counts and SHA-256 values, stages all seven allowlisted payloads, validates the snapshot, then atomically activates it. Failed updates retain the prior active snapshot for offline fallback.
- Manifest, source references, content parity and SHA-256 validation: release gates. The 0.3.1 planetary-reference schema manifest entry was corrected to the live file's 3,902-byte size and SHA-256 `561e41a0cdcb28ec99185d6fa305396f345c6afd2417566d8cf74e6e9233d809`.
- Independent bilingual evaluation, broader content expansion and additional blind annotation: ongoing.

This is a growing reference library, not an exhaustive encyclopedia. Correct astronomical calculations do not establish predictive astrological validity.

 
## Chart and report taxonomy (0.2.0)

AstroLife routes reports by **chart type**, then labels the **astrological tradition**, then the optional **interpretive lens**. These dimensions must not be mixed:

- Chart types: natal, transits, progressions, solar return, lunar return, synastry, composite, horary and electional.
- Traditions: Western tropical, Vedic/sidereal and Chinese astrology.
- Interpretive lenses: psychological, traditional and evolutionary.
- Reports: natal overview; planets in signs and houses; angles and chart ruler (only when birth time supports them); major aspects with exact orbs; elements/modalities; detected house emphasis; synthesis and reflection prompts.
- Relationship reports: synastry compares two charts; composite treats the relationship as a derived chart. Do not reduce either to a deterministic compatibility verdict.

Synergy and Astrology is used as a Persian-facing taxonomy reference; Astro.com and Cafe Astrology are additional practitioner references for chart-type and report structure. Their text is not copied. Medical astrology is excluded from health advice and diagnosis. These categories describe astrological traditions and are not scientific validation of predictive claims.


## Solar Hijri yearly horoscope method (0.3.0)

This release adds bilingual method cards for general Solar Hijri birth-month cohort readings. The cohort horoscope is deliberately distinct from a personal natal chart and from a personal Solar Return:

- Cohort reports use a conventional month-to-sign reference and solar whole-sign houses. This is a general grouping method; exact Sun-sign boundaries can fall within the end of a Solar Hijri month.
- Personal Solar Return reports require the exact return of the transiting Sun to an individual's natal solar longitude and a defined reference location.
- The annual transit windows in AstroLife are based on weekly samples from Astronomy Engine 2.1.19. Their dates are approximate windows, not exact ingress or station timestamps; they are not represented as JPL Horizons calculations.
- Wellbeing content remains limited to general routines, rest and stress management. It does not diagnose or predict disease, pregnancy, death, surgery or treatment outcomes.
- New source records document Solar Hijri calendar history, Solar Return taxonomy, annual-transit report structure, Abu Ma'shar's annual revolutions and historical scholarship.

The 0.3.0 methodology remains part of the 0.3.1 corpus. The current 0.3.1 release contains 95 Persian and 95 English cards and 52 registered sources. All manifest byte counts and SHA-256 values must match the exact bytes at the pinned commit before the app activates a new snapshot.
