---
name: bounded-next-action
description: "Bounded Next Action workflow for coding agents. Use when an unfinished task needs one executable next step."
---

# Bounded Next Action

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Select one unblocked action; include its target and completion check.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: The schema is migrated. What next?

Response pattern: Backfill the new column, then check null counts.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `next_action` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
