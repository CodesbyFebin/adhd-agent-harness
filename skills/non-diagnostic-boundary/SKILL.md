---
name: non-diagnostic-boundary
description: "Non Diagnostic Boundary workflow for coding agents. Use when someone asks whether a response style proves ADHD."
---

# Non Diagnostic Boundary

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Answer no; describe the style as a reading preference and avoid diagnostic inference.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Does this style prove I have ADHD?

Response pattern: No. A writing preference does not diagnose ADHD.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `non_diagnostic_response` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
