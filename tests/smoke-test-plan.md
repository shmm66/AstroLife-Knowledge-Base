# Knowledge Base Release Smoke Test

- [ ] Both JSONL corpora parse successfully.
- [ ] Persian and English cards have matching stable concepts.
- [ ] No duplicate card IDs.
- [ ] Every source ID resolves in sources.json.
- [ ] No secrets, birth data, names, prompts or private report content exist in the repository.
- [ ] Original authored text is CC BY 4.0; third-party source content is not copied without permission.
- [ ] Ranker training uses only reviewed editorial examples.
- [ ] Holdout metrics are recorded and labelled preliminary when the dataset is small.
- [ ] manifest.json hashes match all released files.
- [ ] Desktop app loads all bundled cards while fully offline.
- [ ] Online update fetches public files only and never uploads user data.
- [ ] Hash mismatch or network interruption does not replace the last known-good snapshot.
- [ ] Report sections cite relevant knowledge cards and distinguish symbolic content from empirical research.
- [ ] Word export opens in Word/compatible office software and remains editable.
- [ ] At least 20 Persian and 20 English query cases are checked by a human before promoting the ranker.
