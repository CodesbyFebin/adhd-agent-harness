---
name: verification-evidence
description: "Verification Evidence workflow for coding agents. Use when a task needs a completion claim."
---

# Verification Evidence

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Attach command, result, and artifact to each claim; mark untested work explicitly.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Is the fix complete?

Response pattern: Report the actual test result and diff, and identify any unverified integration.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `verification_record` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
