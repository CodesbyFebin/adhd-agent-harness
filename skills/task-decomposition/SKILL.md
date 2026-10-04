---
name: task-decomposition
description: "Task Decomposition workflow for coding agents. Use when a large task needs manageable steps."
---

# Task Decomposition

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Split by observable outcomes; retain dependencies and rollback points.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Break down a documentation release.

Response pattern: Draft → review links → build → publish approved version.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `chunk_tasks` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
