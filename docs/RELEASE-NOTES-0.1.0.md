# AstroLife Knowledge Base 0.1.0

Initial bilingual seed corpus and offline retrieval-agent foundation.

- 44 reviewed editorial cards: 22 Persian and 22 English.
- 11 registered reference and rights records.
- JSON Schema for knowledge cards.
- Offline TF-IDF / character n-gram retrieval features.
- Logistic-regression relevance ranker trained from 80 editorial relevance pairs.
- Candidate grouping and duplicate-detection helper.
- Source and evidence-class notes, privacy rules, contribution guide, and release manifest tooling.
- No remote generative-AI dependency.

Known limitations:
- Seed coverage is intentionally small and not an exhaustive encyclopedia.
- Ranker metrics are preliminary and derived from a small editorial holdout set.
- The public GitHub repository and application-side online sync are not yet activated.
- The initial desktop integration ships a static library snapshot; a future release must implement hash-verified public updates and rollback.
