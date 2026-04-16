---
name: rename-thread
description: Rename the current VS Code Codex extension thread by updating the Codex session index. Use when the user asks to rename, retitle, title, label, or summarize the active Codex thread, either with an explicit new name or by asking Codex to choose a concise name from the conversation.
---

# Rename Thread

## Workflow

Rename the active Codex thread from inside a VS Code Codex extension session.

1. Choose the new thread name.
   - If the user provided a name, use it exactly after trimming surrounding whitespace.
   - If the user did not provide a name, summarize the current thread into a concise title.
   - Prefer 3-8 words, concrete nouns, and no terminal punctuation.
   - Keep the name under 80 characters unless the user explicitly requests a longer name.

2. Confirm there is an active thread id.
   - Prefer the environment variable `CODEX_THREAD_ID`.
   - If `CODEX_THREAD_ID` is empty, ask the user for the thread id or explain that the active extension session did not expose one.

3. Run the bundled script:

```bash
python ~/.codex/skills/rename-thread/scripts/rename_codex_thread.py --name "New Thread Name"
```

To rename a known thread id instead of the active thread, pass `--thread-id`:

```bash
python ~/.codex/skills/rename-thread/scripts/rename_codex_thread.py --thread-id "019..." --name "New Thread Name"
```

4. Report the result, including the final thread name and backup path printed by the script.

5. Tell the user to reload the VS Code or code-server window if the sidebar does not refresh immediately.

## Implementation Notes

The script writes a rename overlay into `~/.codex/session_index.jsonl`. If the thread already has an index row, it updates `thread_name`; otherwise it looks up the thread in `~/.codex/state_5.sqlite` and appends a row with the thread's existing `updated_at` value.

Before every write, the script creates a timestamped backup under `~/.codex/session_index_manual_backup/`.
