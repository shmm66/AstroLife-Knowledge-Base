# Contributing to AstroLife Knowledge Base

Thank you for helping improve the bilingual library.

## Add a knowledge card
1. Find a reliable primary or authoritative source for the exact claim.
2. Check copyright and data-use terms. When in doubt, publish a bibliographic link and an original summary only.
3. Add parallel Persian and English cards with stable IDs.
4. Separate astronomical facts from historical doctrine, symbolic interpretation and empirical research.
5. Use ordinary language. Avoid deterministic claims and medical, legal or financial instructions.
6. Add source IDs, a plain-language source note, limitations, tags and a reflection question.
7. Run `python tools/validate_kb.py`.
8. Submit the candidate for review. Do not set a new card to `approved` merely because an automated check passes.

## Machine-learning contributions
- Add relevance labels to `training/seed-labels.jsonl` only after human review.
- Include both relevant and hard-negative examples, for Persian and English.
- Never submit raw user prompts, names, birth dates, birth places, chart data or report text.
- Run `python tools/train_ranker.py` and report holdout metrics.
- Do not claim high retrieval quality based only on a small seed set.
- Candidate-discovery tools may suggest duplicates or related topics; a human must approve every new fact.

## Release a new snapshot
1. Run the corpus validator.
2. Train and evaluate the ranker.
3. Rebuild the manifest: `python tools/build_manifest.py`.
4. Review the changes, licenses, hashes and source notes.
5. Update the version and release date in `tools/build_manifest.py`.
6. Publish the commit and create release notes.
7. Verify raw HTTPS file access and SHA-256 hashes from a clean client.

## Code of conduct
Be respectful, disclose uncertainty and correct mistakes publicly. A disagreement about an interpretation is not a reason to suppress a well-sourced historical or scientific result.
