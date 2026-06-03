# Page Types

Use these page shapes as defaults. Adapt only when the corpus clearly needs a different structure.

## `index.md`

Purpose: navigation hub for the entire bank.

Recommended structure:

```md
# Memory Bank

## Scope
- what source set this bank summarizes

## Projects
- [Project Name](projects/example.md): one-line description

## Topics
- [Topic Name](topics/example.md): one-line description

## Tasks
- [Task Name](tasks/example.md): one-line description

## Decisions
- [Decision Name](decisions/example.md): one-line description

## Sources
- [Source Note](sources/example.md): one-line description
```

## `log.md`

Purpose: append-only chronological record of memory-bank refreshes.

Recommended structure:

```md
# Memory Bank Log

## 2026-04-30
- Sources reviewed: `codex_doc/...`, `docs/...`
- Pages created: `projects/...`, `topics/...`
- Pages updated: `index.md`, `tasks/...`
- Notes: contradictions, gaps, or deferred items
```

## `sources/*.md`

Purpose: compact note for one raw source document.

Recommended structure:

```md
# <Source Title>

Source path: `path/to/source.md`
Source type: instruction | thread summary | plan | notes | status | other

## Summary
Short description of the source and why it matters.

## Key Points
- fact or claim
- fact or claim

## Feeds Into
- [Project Page](../projects/example.md)
- [Topic Page](../topics/example.md)

## Related
- nearby source or durable pages
```

## `projects/*.md`

Purpose: durable project or workstream state.

Recommended structure:

```md
# <Project Name>

## Purpose
What this project is trying to achieve.

## Current State
What is true now.

## Key Artifacts
- important files, directories, outputs, or commands

## Important Decisions
- links to decision pages or concise decision bullets

## Open Tasks
- links to task pages or concise unresolved items

## Derived From
- source pages

## Related
- project, topic, or task pages
```

## `topics/*.md`

Purpose: reusable concept, method, or recurring workflow.

Recommended structure:

```md
# <Topic Name>

## What It Covers
Short definition.

## Why It Matters Here
Connection to the repository or projects.

## Known Patterns
- repeatable workflow, convention, or lesson

## Open Questions
- unresolved or context-dependent items

## Derived From
- source pages

## Related
- topic, project, or decision pages
```

## `tasks/*.md`

Purpose: actionable unresolved work.

Recommended structure:

```md
# <Task Name>

Status: active | blocked | proposed | done

## Goal
What needs to happen.

## Inputs
- relevant pages, files, or prerequisites

## Next Actions
- concrete next steps

## Blocking Issues
- blockers or risks, if any

## Derived From
- source pages

## Related
- project, topic, or decision pages
```

## `decisions/*.md`

Purpose: explicit choices that future work should be able to recover quickly.

Recommended structure:

```md
# <Decision Name>

Date: YYYY-MM-DD
Status: accepted | tentative | superseded

## Decision
What was decided.

## Reasoning
Why this choice was made.

## Consequences
- implications for future work

## Derived From
- source pages

## Related
- impacted pages
```

## General Rules

- Keep page titles human-readable and filenames stable.
- Prefer compact sections with high information density.
- If a page becomes long, tighten it before splitting it.
- Split only when a single page is mixing clearly separate concerns.
