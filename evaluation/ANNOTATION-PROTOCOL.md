# Independent bilingual relevance evaluation — v0.1

## Status

This is an **unlabelled, blind annotation queue**, not an evaluation result. It contains 12 new query families, 24 Persian/English queries and 192 query–card candidate pairs. The blank label fields must be completed by independent reviewers before any metrics are reported. These rows are not training data and must not be used to retrain the 0.3.1 ranker.

## Annotation procedure

1. Recruit two reviewers who can read Persian and English fluently. They must not have authored the current training labels or the ranker.
2. Give both reviewers the same queue independently. Hide ranker scores, retrieval order, model predictions and the other reviewer's labels.
3. For each query–card pair, enter **1** only when the card substantively helps answer the query as written; enter **0** when it is merely topically adjacent, tangential or unrelated. Judge the card's actual content, not its title alone.
4. Record short evidence notes for borderline decisions. Do not infer a card's contents from its ID.
5. A third reviewer adjudicates disagreements without seeing model scores. Preserve both original labels and the adjudicated label.
6. Keep every Persian/English translation pair in the same held-out partition. Do not move these query families into training after inspecting results.

## Evaluation

- Freeze the 0.3.1 ranker and candidate-generation procedure before annotation is unblinded.
- Report Precision@3, Recall@3, MRR and nDCG@5, macro-averaged overall and separately for Persian and English.
- Report the number of query groups and candidate judgements per language, inter-annotator agreement (Cohen's kappa), adjudication rate and bootstrap confidence intervals grouped by query family.
- Compare against a simple lexical baseline. Report any candidate-selection or language-parity failures.
- Keep the evaluation set versioned and immutable after labels are revealed. Corrections require a new revision and an audit note.

## CSV fields

- `query_group`: bilingual family identifier; all translations stay together.
- `candidate_slot`: fixed blind display slot, not a model rank.
- `candidate_card_id`: card to inspect in the matching language.
- `annotator_a_relevant`, `annotator_b_relevant`: independent binary labels (0 or 1).
- `adjudicated_relevant`: final label after disagreement review.
- Note fields: concise evidence supporting the label.

No user profiles, birth data, prompts or generated reports are included.
