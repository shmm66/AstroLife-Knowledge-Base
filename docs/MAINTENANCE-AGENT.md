# AstroLife Knowledge Maintenance Agent

The repository includes a source-maintenance process distinct from the desktop retrieval agent. The desktop client remains offline-first and consumes verified immutable snapshots. The maintenance agent runs in GitHub Actions to monitor authoritative external sources.

Control path: scheduled/manual run → HTTPS checks and literature metadata discovery → fingerprints and metadata-only candidates → draft PR → human scientific, source-rights and bilingual editorial review → validator → separate release decision.

The agent never modifies the production corpus, ranker or manifest, and never auto-merges. See maintenance/README.md and maintenance/REVIEW-POLICY.md.

JPL Horizons and JPL physical-parameter sources are already registered in the library. MPC, NASA Exoplanet Archive, ESA Gaia, arXiv and Crossref remain discovery sources until source-rights and citation reviews are completed.
