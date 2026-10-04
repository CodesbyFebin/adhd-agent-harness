---
name: agent-owned-work
description: "Agent Owned Work workflow for coding agents. Use when the agent is asked to edit a repository."
---

# Agent Owned Work

## Workflow

1. Identify the requested outcome and the supplied evidence.
2. Inspect the target, make the authorized edit with tools, verify the diff, report actual results.
3. Verify the result against the explicit user contract.
4. Report only completed work as completed; name one next action if work remains.

## Example

Request: Fix the README typo.

Response pattern: Edit the typo and verify the diff; if tools are unavailable report that limitation.

## Guardrails

Preserve facts, uncertainty, safety requirements, and user-requested detail. Do not infer a diagnosis from preferences. Do not claim tools ran without execution evidence. This new skill is unbenchmarked; the frozen board remains held.

## Deterministic helper

Use `tool_capability` in `src/solvers.py` from the repository root. Read its catalog entry in `data/functions.json` for input and output examples. The helper transforms supplied data; it does not execute an agent task or replace a judge.
