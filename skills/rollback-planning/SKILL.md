---
name: rollback-planning
description: "Rollback Planning workflow for coding agents. Use when a migration or release needs recovery steps."
---

# Rollback Planning

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Attach a trigger and recovery action to each risky stage; retain verification.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Move user IDs to UUIDs.

Response pattern: Keep old IDs during dual-read/write and define rollback before switching consumers.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `rollback_plan` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
