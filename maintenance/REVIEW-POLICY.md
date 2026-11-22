# Agent Roles, Review Gates and Source Policy

## Internal roles

1. Source Sentinel — HTTPS availability, canonical URLs, API response shapes and signatures.
2. Astronomy Data Curator — object IDs, units, uncertainties, epoch, time scale, frame, observer/centre and query settings.
3. Research Scout — bibliography discovery only; does not decide whether a paper is correct.
4. Evidence Reviewer — separates measured astronomy, historical doctrine, symbolic reflection and empirical research.
5. Persian–English Editorial Reviewer — checks equivalent meaning, scope, uncertainty and limitations.
6. Release/QA Reviewer — checks schema, source IDs, bilingual parity, licences, hashes and offline client compatibility.

These are responsibilities inside one controller; they do not imply connection to an external agent team.

## Promotion gates

No bot may set a card to approved, edit production payloads, retrain the ranker or publish a release. Every candidate requires canonical-source verification, publisher authority, rights review, complete provenance, explicit uncertainty, bilingual review, tests and human approval recorded in the PR.

## Source handling

JPL Horizons results are time-dependent. Preserve target, centre, observer, start/stop, step, quantities, time scale, frame, corrections and API signature. Do not silently replace Astronomy Engine results or treat live ephemerides as timeless cards.

For JPL physical parameters, compare definitions and units field by field; a page hash change does not authorize a numeric change. Missing uncertainty is not zero uncertainty.

Use IAU material for astronomical nomenclature, not as evidence about astrological validity. For MPC, NASA Exoplanet Archive and Gaia, record data release, schema, query, date and citation; do not bulk-download catalogues. For arXiv/Crossref, retain DOI or stable ID, title, publisher, date and URL only; indexing is not peer review.

## Privacy and security

No user-specific information is needed. The workflow uses the repository GitHub token only for branch and draft PR creation. Never commit API keys. No write-enabled workflow is triggered by untrusted pull-request code. Auto-merge and force-push are prohibited.
