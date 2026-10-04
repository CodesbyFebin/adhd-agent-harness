---
name: safe-preview
description: "Safe Preview workflow for coding agents. Use when a requested operation may delete or overwrite data."
---

# Safe Preview

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. List the exact target and preview consequences before irreversible execution.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Delete ignored and untracked files.

Response pattern: Inspect git clean -ndx output and identify files at risk before deletion.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `destructive_preview` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
