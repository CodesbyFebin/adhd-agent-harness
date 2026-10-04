---
name: resume-context
description: "Resume Context workflow for coding agents. Use when work resumes after a break."
---

# Resume Context

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Recover verified state, unresolved items, and one next action from saved notes.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Resume yesterday’s migration.

Response pattern: Restate the latest verified checkpoint and remaining work before execution.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `resume_context` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
