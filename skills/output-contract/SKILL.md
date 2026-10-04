---
name: output-contract
description: "Output Contract workflow for coding agents. Use when the user specifies an exact response format."
---

# Output Contract

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Honor code-only, JSON-only, or other explicit constraints ahead of style defaults.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Return only a TypeScript code block.

Response pattern: Return the requested code block without an introduction or closer.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `check_output_contract` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
