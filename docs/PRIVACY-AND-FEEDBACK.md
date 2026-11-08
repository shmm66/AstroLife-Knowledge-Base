# Privacy and Learning Feedback

## Current application behaviour
- The knowledge agent and relevance model run locally.
- Library synchronization downloads public, versioned files from the AstroLife GitHub repository.
- The application resolves the current public commit SHA and downloads files from that immutable commit.
- The application does not upload names, date/time/place of birth, chart positions, relationship data, prompts, reports or feedback to GitHub or a remote AI service.
- No hosted AI API key is required.

## Training data
- The public ranker is trained only on maintainer-authored relevance judgements and public knowledge cards.
- No private chart or personal profile data is used to create the public dataset.
- The current desktop UI does not implement a user feedback collection, model update or contribution upload flow.
- Do not state that the application learns from live users. That feature is not currently implemented.

## Future user contribution design
If a feedback contribution feature is implemented later, it must be opt-in and separate from normal synchronization. It must:
1. show a preview of every field before export;
2. include only a card ID, broad topic, language, relevance rating and minimal non-identifying features;
3. exclude raw query text, date/time/place of birth, profile identifiers, chart contents, relationship details and generated reports;
4. require a separate explicit user approval before any upload;
5. keep raw feedback local by default.

## Data minimization
No user-specific information is required to read the public library. Do not use personal chart data to expand the public knowledge base. Public additions come from licensed sources and reviewed editorial contributions.
