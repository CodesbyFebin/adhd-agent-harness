---
name: benchmark-integrity
description: "Benchmark Integrity workflow for coding agents. Use when a new run is compared with the frozen board."
---

# Benchmark Integrity

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Require matching case, rubric, model, protocol, and coverage identities; never alter history.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Did this candidate beat the snapshot?

Response pattern: Check comparability and release criteria before making a ranking claim.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `compare_protocol` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
