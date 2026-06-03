---
name: prune-codebase
description: Prune a repository to the minimum runtime set by first generating an execution schematic, then moving non-required objects into pruned_objects with iterative validation after each move, and finally refreshing requirements.txt and README.md.
---

# Prune Codebase

## Goal

Reduce a repo to only what is required for the application flow, without destructive deletion.

## Workflow

1. Build an execution schematic of the current app flow.
2. Save the schematic artifact to `codex_docs/app_execution_schematics.md`.
3. Identify required files from that schematic.
4. Ignore `docs/` and `codex_docs/` during pruning decisions.
5. For each prune candidate:
   - Move it to `pruned_objects/<original-path>` (never delete).
   - Run a validation pass immediately after the move.
   - If validation fails, restore the object and mark it as required.
6. Repeat until all candidates are processed.
7. Reassess `requirements.txt` and `README.md` against the final pruned structure.
8. Move old `requirements.txt` and `README.md` into `pruned_objects/` before writing updated versions.

## Guardrails

- Prefer one-object-at-a-time pruning for traceability.
- Always keep path structure under `pruned_objects/`.
- Treat unclear dependencies as required unless validation proves otherwise.
- Do not skip validation between moves.

## Example command patterns

```bash
mkdir -p pruned_objects
mkdir -p "pruned_objects/$(dirname path/to/object)"
mv "path/to/object" "pruned_objects/path/to/object"
```

```bash
# restore if needed
mkdir -p "$(dirname path/to/object)"
mv "pruned_objects/path/to/object" "path/to/object"
```

