---
name: evidence-aware-errors
description: "Evidence Aware Errors workflow for coding agents. Use when an error needs a factual report."
---

# Evidence Aware Errors

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. State location and observation; name a cause only when evidence supports it.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: auth.spec.ts:42 expected 200, got 401.

Response pattern: At auth.spec.ts:42: expected 200, got 401. Inspect auth setup; cause unconfirmed.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `error_report` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
