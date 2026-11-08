# Release 0.1.1 — 2026-11-09

## Included
- 52 bilingual knowledge cards: 26 Persian and 26 English.
- Coverage across all 12 houses, planetary themes, aspects, transits, synastry, and interpretation limitations.
- Versioned manifest with file sizes, entry counts, and SHA-256 checksums.
- Source registry, evidence labels, editorial policy, and separate code/data licenses.
- Bundled lightweight logistic-regression relevance ranker and training/validation utilities.
- Public GitHub distribution path designed for HTTPS-only client synchronization.

## Validation
- Corpus validation passed: unique IDs, language parity, evidence labels, source references, and license fields.
- Initial ranker seed set: 80 labelled examples (64 training, 16 holdout).
- Preliminary holdout metrics: accuracy 0.875, precision 1.000, recall 0.600, F1 0.750. The holdout set is small; these results are not a claim of production-grade retrieval quality.
- Desktop integration in AstroLife Pro 0.8.3 includes checksum verification, staged version snapshots, atomic activation, offline fallback, and rollback.

## Known limitations
- The corpus is a starter library, not an exhaustive reference work.
- Retrieval quality needs a larger independently labelled Persian/English test set.
- New entries require source and editorial review; the model does not autonomously publish facts.
- User-feedback collection/export is not enabled in the current desktop UI.
- Astrology is treated as a symbolic tradition; astronomical calculation accuracy does not establish predictive validity.

## Privacy and licensing
The public repository contains authored knowledge content, metadata, tools, and model artifacts. It does not contain individual birth profiles, charts, prompts, or generated reports. Original content is CC BY 4.0; tools are MIT; third-party components retain their own terms.
