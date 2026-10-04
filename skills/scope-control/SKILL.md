---
name: scope-control
description: "Scope Control workflow for coding agents. Use when related work threatens to distract from the active task."
---

# Scope Control

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Complete requested scope; keep secondary findings in a separate backlog.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Fix auth without rebuilding the dashboard.

Response pattern: Keep the auth repair active; record dashboard improvements for later.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `partition_scope` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
