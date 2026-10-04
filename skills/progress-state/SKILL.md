---
name: progress-state
description: "Progress State workflow for coding agents. Use when work spans multiple turns or stages."
---

# Progress State

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Show completed state, current step, and next task without inventing progress.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Step 3 of 5: schema done; backfill next.

Response pattern: Step 3 of 5: schema updated. Next: backfill the column.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `progress_state` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
