---
name: debug-hypotheses
description: "Debug Hypotheses workflow for coding agents. Use when a failure has multiple plausible explanations."
---

# Debug Hypotheses

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Rank hypotheses by supplied evidence; attach a discriminating check to each.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: A request returns 401 with no other evidence.

Response pattern: Check request headers and token validity before asserting a cause.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `rank_hypotheses` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
