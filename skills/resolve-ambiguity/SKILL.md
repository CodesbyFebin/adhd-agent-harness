---
name: resolve-ambiguity
description: "Resolve Ambiguity workflow for coding agents. Use when a required target or constraint is missing."
---

# Resolve Ambiguity

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Ask one focused blocking question containing the missing fields.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Deploy it to production.

Response pattern: Which project and production target should receive this deployment?

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `missing_fields` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
