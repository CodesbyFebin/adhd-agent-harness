---
name: decision-support
description: "Decision Support workflow for coding agents. Use when the user needs to choose between alternatives."
---

# Decision Support

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Compare relevant options against explicit criteria; state uncertain inputs.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Choose merge or rebase.

Response pattern: Compare shared-history safety, linear history, and conflict handling.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `compare_options` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
