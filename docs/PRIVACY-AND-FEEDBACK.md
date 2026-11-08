# Privacy and Learning Feedback

## Default behaviour
- The agent works locally. It does not send birth data, names, chart positions, relationship details or report text to a remote AI provider.
- Library synchronization downloads public, versioned content only.
- Feedback is disabled unless the user chooses to rate a section.

## Local learning
- An optional rating (useful / not useful) may update the user's local retrieval weights.
- The training record must contain only a knowledge-card ID, query category, language, rating and a coarse feature vector.
- Never include raw query text, date/time/place of birth, profile name, chart, relationship details or generated report text.
- Local feedback stays on the device by default.

## Sharing training examples
A separate, explicit export action may package anonymized retrieval labels for a contribution. The user must preview and approve the file before upload. A contribution is never uploaded automatically.

## Data minimization
No user-specific information is required to read the public library. Do not use user chart data to expand the public knowledge base. New content comes from licensed/public sources and reviewed editorial contributions.
