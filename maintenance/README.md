# Astronomy Knowledge Maintenance Agent

A metadata-first source-maintenance agent for AstroLife Knowledge Base. It watches authoritative astronomy services and scholarly metadata feeds, records source changes and creates review proposals.

## Monitored sources

NASA/JPL Horizons and planetary physical parameters; IAU resolutions and constellation references; Minor Planet Center List API; NASA Exoplanet Archive TAP; ESA Gaia DR3 TAP; arXiv exoplanet/stellar research; Crossref astrology-research bibliography metadata; and NASA ADS API documentation.

## Safety boundary

The agent does not modify the bilingual corpus, planetary payload, source registry, ranker or release manifest. It does not approve claims, copy source text or abstracts, download complete catalogues, or collect profiles, birth data, charts, prompts or reports. It never auto-merges or publishes a release.

A changed page hash is only a review signal. A literature-feed entry is only a research lead.

## Local use

Python 3.10+, standard library only:

    python maintenance/agent.py

The first run establishes a fingerprint baseline. Later runs write metadata-only JSON candidates under maintenance/candidates when watched pages, table counts or literature IDs change. Run reports are in maintenance/reports/run-report.json; state is in maintenance/state/source-state.json.

Requests are HTTPS-only, time out, are capped at 8 MiB and reject redirects to unapproved hosts. arXiv/Crossref candidates retain bibliographic metadata, not abstracts or full text.

## Scheduled operation

GitHub Actions runs weekly and can be triggered manually. When fingerprints or candidates change, it commits them to a bot branch and opens a draft PR. It never writes to main. Every run uploads a report artifact.

## Human promotion sequence

Verify the canonical source and its authority; check licence and redistribution terms; preserve units, uncertainties, epoch, time scale, frame, observer/centre and query parameters; assign the evidence class; draft equivalent original Persian and English summaries; complete independent review; run the corpus validator; then make a separate versioned release.

The ranker is not retrained automatically. Training labels remain human-reviewed and must never include user prompts or chart data.
