# AstroLife Knowledge Base 0.2.0 — 2026-11-09

## Content
- Expanded the bilingual corpus to 128 reviewed seed cards: 64 Persian and 64 English.
- Added technical cards on ephemerides, observer centres, coordinate frames, civil time and time scales, uncertainties, apparent retrograde motion, zodiac reference conventions, IAU constellations, precession, house systems, chart angles, lunar nodes, planet classification and birth-data quality.
- Added history summaries for Babylonian astronomy and the transmission of Ptolemy's Tetrabiblos.
- Added evidence summaries for zodiac/personality testing, 2024 well-being research, Swedish marriage/divorce register analysis, double-blind study debate and research methodology.
- Added 12 bilingual sign cards and modern symbolic summaries for Uranus, Neptune and Pluto, clearly separated from physical astronomy.
- Extended the source registry to 20 entries, including NASA/JPL, IAU, Oxford, PAL and peer-reviewed studies.

## Structured astronomical reference
- Added `data/reference/planetary-parameters.json`.
- Contains 8 IAU planets and 5 dwarf planets listed by the JPL table: Ceres, Pluto, Eris, Makemake and Haumea.
- Includes equatorial/mean radii, masses, bulk densities, sidereal rotation/orbital periods, V(1,0), geometric albedo, equatorial gravity and escape velocity where listed.
- Includes explicit uncertainties only where the JPL table publishes them.
- The dataset is a physical reference table, not a time-specific ephemeris or an astrological interpretation.

## ML ranker
- Replaced the legacy training labels with 168 maintainer-curated bilingual relevance judgements across 17 query families.
- Split by bilingual concept family to prevent Persian and English translations of the same query from leaking between training and holdout.
- Training: 13 families; holdout: 4 families / 40 candidate judgements.
- Preliminary holdout classification: accuracy 0.900, precision 1.000, recall 0.800, F1 0.889.
- Preliminary ranking: Precision@3 1.000, Recall@3 0.625, MRR 1.000, nDCG@5 0.996.
- These small, manually curated results measure retrieval relevance only; they do not prove interpretive or astrological accuracy.

## Desktop integration
- Target desktop package version: AstroLife Pro 0.8.4.
- Knowledge agent recognises astronomy, research, history, signs, relationships and forecast topics.
- The agent can answer selected physical-parameter queries from the structured JPL file in Persian or English.
- Synchronization resolves the latest GitHub commit SHA, pins the complete download to that immutable commit, verifies all manifest sizes and SHA-256 values, validates the 8+5 planetary dataset and activates the snapshot atomically.
- Offline fallback and the previous verified snapshots remain available.

## Known limitations
- 128 cards are a seed corpus, not an exhaustive astrological encyclopedia.
- Only selected physical parameters are included; consult JPL for the full source table and updates.
- House-system support and historical birth-time conversion still require wider test coverage across high latitudes and historical time-zone changes.
- Ranker evaluation uses a small maintainer-curated set; it needs a larger, independent bilingual benchmark.
- User-feedback collection/export is not enabled in the current UI.

## Privacy and licensing
No birth data, chart, name, prompt or report is published. The knowledge cards are CC BY 4.0; tools are MIT; third-party sources and model weights retain their own terms.
