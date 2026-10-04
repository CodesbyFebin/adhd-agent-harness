---
name: answer-first
description: "Answer First workflow for coding agents. Use when a direct question needs an answer before context."
---

# Answer First

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Put the supported answer in the first line; preserve the requested output format.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: What is 17 multiplied by 6?

Response pattern: 102.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `first_line` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
