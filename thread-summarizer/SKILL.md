---
name: thread-summarizer
description: Summarize the current Codex conversation thread and save a condensed handoff note under ./codex_doc/thread_summaries. Use when the user asks to summarize, archive, save, checkpoint, hand off, or document the current thread, especially when they want main points discussed, actions taken, and the state where work was left off.
---

# Thread Summarizer

## Workflow

Create a durable, concise handoff summary of the current thread.

1. Determine the output location.
   - Use `./codex_doc/thread_summaries/` in the current workspace.
   - Create the directory if it does not exist.
   - Use the local date in `YYYY-MM-DD` format for the base filename: `YYYY-MM-DD_thread_summary.md`.
   - If that file already exists, avoid overwriting it. Add a time suffix such as `YYYY-MM-DD_thread_summary_HHMMSS.md`.

2. Review the visible thread context.
   - Capture only facts available in the conversation and tool results.
   - Do not invent missing history. If important context is absent because of compaction or missing logs, state that briefly.
   - Preserve concrete file paths, commands, decisions, blockers, and verification results when they matter for continuing work.

3. Write the summary using this structure:

```md
# Thread Summary - YYYY-MM-DD

## Main Points
- <condensed discussion points>

## Actions Taken
- <files changed, commands run, artifacts created, decisions made>

## Current State
- <what is complete, what is pending, known blockers, validation status>

## Continuation Notes
- <specific next steps or cautions for a future Codex/user session>
```

4. Save the file.
   - Prefer `apply_patch` for creating the markdown file when practical.
   - Keep the summary concise enough to scan quickly, usually 20-40 lines.
   - After saving, tell the user the exact path and mention any known limitations in the captured context.

## Quality Bar

- Favor dense, factual bullets over narrative.
- Include enough state for another Codex session to continue without rereading the entire thread.
- Separate completed work from proposed or pending work.
- Include verification commands and outcomes when available.
- Do not include private chain-of-thought or hidden reasoning.
