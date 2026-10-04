---
name: detailed-explanation
description: "Detailed Explanation workflow for coding agents. Use when the user explicitly asks for depth."
---

# Detailed Explanation

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Explain the mechanism, example, tradeoffs, and verification with navigable sections.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Explain OAuth PKCE in detail.

Response pattern: Cover verifier, challenge, authorization redirect, code exchange, and threat model.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `outline_explanation` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
