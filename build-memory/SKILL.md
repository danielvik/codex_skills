---
name: build-memory
description: Build or refresh a coherent markdown-only `memory_bank` from repository documents such as `codex_doc`, `docs`, `README.md`, notes, plans, and thread summaries. Use when the user invokes `/build-memory` or `$build-memory`, or asks for a persistent wiki, memory bank, knowledge base, or interlinked summaries that agents can navigate without loading every raw document.
---

# Build Memory

## Purpose

Compile raw repository documents into a maintained `memory_bank/` of concise, interlinked markdown pages.

This skill is intentionally:

- markdown-only
- generative rather than script-driven
- source-preserving
- designed for progressive disclosure rather than bulk loading

Do not introduce databases, embeddings, or automation unless the user explicitly asks for them.

## Default Behavior

Unless the user specifies otherwise:

- treat raw project docs as immutable inputs
- write compiled outputs under `memory_bank/`
- prefer a small number of durable synthesis pages over many shallow summaries
- keep chronology separate from current state

## Source Selection

1. Determine the source set.
   - If the user names a source directory, use it.
   - Otherwise prefer repository knowledge sources such as `codex_doc/`, `docs/`, top-level `README.md`, project `README.md` files, notes, plans, and thread summaries.
   - Exclude generated outputs unless they are themselves important knowledge artifacts.

2. Sample the sources before writing.
   - Identify recurring projects, topics, tasks, decisions, and status updates.
   - Notice contradictions, stale instructions, and duplicate narratives.

3. Preserve the raw/source distinction.
   - Never rewrite the raw source files as part of this skill unless the user separately asks for that.
   - The `memory_bank/` is the compiled layer, not the source of truth.

## Output Layout

Create only the directories needed for the current corpus. Start with:

```text
memory_bank/
  index.md
  log.md
  sources/
  projects/
  topics/
  tasks/
  decisions/
```

Read [references/page_types.md](references/page_types.md) before writing pages.

## Workflow

1. Build the top-level map.
   - Create `memory_bank/index.md` as the navigation entrypoint.
   - Group pages by type and give each page a one-line description.

2. Build source pages.
   - For each important raw document, create a compact page under `memory_bank/sources/`.
   - Capture what the source is, why it matters, its key claims, and what durable pages it should feed.
   - Source pages should be concise. They are waypoints, not full restatements.

3. Build durable synthesis pages.
   - Project pages track stable project state.
   - Topic pages track reusable concepts, workflows, and recurring patterns.
   - Task pages track active or unresolved work.
   - Decision pages record meaningful choices, assumptions, and constraints.
   - Prefer updating an existing durable page over creating a new near-duplicate page.

4. Interconnect the bank.
   - Add `Related:` links between adjacent pages.
   - Add `Derived from:` links back to source pages.
   - Use direct markdown links so an agent can traverse the bank cheaply.
   - Read [references/linking_rules.md](references/linking_rules.md) for link hygiene.

5. Separate state from chronology.
   - `index.md` answers: what exists here?
   - durable pages answer: what is currently true?
   - `log.md` answers: what changed and when?

6. Append a memory-bank log entry.
   - Add a short chronological entry to `memory_bank/log.md` summarizing the ingest or refresh pass.
   - Include the date, source set touched, and major pages created or updated.

## Quality Bar

- Favor synthesis over extraction.
- Keep pages dense and scannable.
- Record contradictions explicitly instead of silently flattening them.
- Avoid duplicating the same prose across multiple pages.
- Prefer a few high-value hub pages over a forest of low-value pages.
- Keep the bank useful to a future agent that has not read the whole repo.

## When To Create New Pages

Create a new page when one of these is true:

- the material represents a distinct project or workstream
- a concept recurs across multiple sources
- a task has ongoing operational value
- a decision materially affects future work

Otherwise, update an existing page.

## Naming Guidance

- Use short, stable slugs.
- Prefer topic or project names over dates, except for chronological decision records when dates matter.
- Avoid filenames that encode transient chat phrasing.

## Final Check

Before finishing:

1. Read `memory_bank/index.md` and confirm it gives a usable overview.
2. Check that major pages link to each other and to their source pages.
3. Check that the bank reflects current state rather than only chronology.
4. Note any obvious coverage gaps or unresolved conflicts to the user.
