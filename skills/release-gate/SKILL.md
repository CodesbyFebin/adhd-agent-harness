---
name: release-gate
description: "Release Gate workflow for coding agents. Use when a scored candidate is considered for release."
---

# Release Gate

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Require zero blockers and all score criteria; hold on incomplete or invalid evidence.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Weighted score improved but one blocker remains.

Response pattern: Held: one blocking finding remains.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `release_gate` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
