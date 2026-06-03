# Linking Rules

The memory bank should behave like a navigable wiki for future agents.

## Core Rules

- Every durable page should link back to at least one source page.
- Every source page should point forward to the durable pages it informs.
- Prefer direct links to the most relevant page instead of link spam.
- Use relative markdown links so the bank stays portable across repositories.

## Recommended Link Sections

Use these labels consistently:

- `Derived From`
- `Feeds Into`
- `Related`

Use `Important Decisions` or `Open Tasks` when those relationships are stronger than a generic related link.

## Linking Heuristics

- Link projects to topics when the topic generalizes beyond one project.
- Link tasks to projects when the task belongs to a workstream.
- Link decisions to every project or topic materially affected.
- Link source pages only to the few pages they truly support.

## Avoid

- linking every page to every other page
- repeating the same long explanation across multiple pages
- storing raw source excerpts when a concise paraphrase is enough
- burying major pages that are never reachable from `index.md`

## Contradictions

When two sources disagree:

1. note the conflict on the durable page where it matters
2. link both source pages
3. state which interpretation seems current, if the evidence supports that
4. leave it explicit when the conflict is unresolved

## Progressive Disclosure

Design links so a future agent can usually answer a question by reading:

1. `memory_bank/index.md`
2. one or two durable pages
3. only then the most relevant source pages

If a page forces the reader to open many raw sources just to understand the basics, the page is not doing enough synthesis.
