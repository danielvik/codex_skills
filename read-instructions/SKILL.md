---
name: read-instructions
description: Read and apply repository-local instructions before acting. Use when the user invokes /read_instructions, $read-instructions, or asks Codex to consult codex_doc/instructions.md before implementing, editing, running, or planning work in the current repository.
---

# Read Instructions

## Workflow

1. Locate `codex_doc/instructions.md` relative to the current workspace or repository root.
2. Read the file before making task decisions or edits.
3. Treat the file as repository-specific operating instructions for the current request.
4. Follow those instructions while still obeying higher-priority system, developer, and user instructions.
5. If the file is missing or unreadable, state that clearly and continue with the best available repository context.

## Scope

This skill does not add independent project requirements. It exists to force early loading of the repository instruction file so subsequent work can conform to it.
