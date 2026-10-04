---
name: partial-success
description: "Partial Success workflow for coding agents. Use when some checks passed and others failed."
---

# Partial Success

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Name every pass and failure; separate observed symptoms from possible causes.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Lint and units passed; auth integration returned 401.

Response pattern: Lint and unit tests passed. Integration failed with 401; cause unconfirmed.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `summarize_checks` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
