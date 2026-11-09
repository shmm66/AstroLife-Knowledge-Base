# AstroLife Knowledge Base 0.3.1

- Merged the public 0.3.0 Solar Hijri cohort methodology with the local bilingual historical and annual-storytelling expansion.
- Corpus: 190 cards, evenly split (95 Persian / 95 English).
- Registry: 52 source records; all card source IDs resolve.
- Added 18 bilingual cards covering Mesopotamian, Ptolemaic/Latin, Arabic-Persian, medieval Hebrew, Jyotisha and Maya source traditions, plus annual-horoscope editorial method and six life-area narrative frameworks.
- Added 20 source records from the local expansion while preserving all public 0.3.0 Solar Hijri annual-return and cohort-method sources.
- Combined the labelled relevance dataset to 228 judgements across 27 bilingual query families and retrained the local relevance ranker.
- Holdout: accuracy 0.823, precision 0.828, recall 0.800, F1 0.814; ranking MRR 1.000 and nDCG@5 0.968. This is a small editorial seed dataset; it is not an independent benchmark and does not validate astrological predictions.
- Validation passed: unique cards, language parity, evidence labels, licence fields, limitations, source resolution, JPL reference schema, planetary units and ranker feature dimensions.
- App bundle consumes this version offline and checks the manifest hashes during library sync.
