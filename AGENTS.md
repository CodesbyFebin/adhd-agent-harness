# Agent guide

This repository is a **pre-optimization** ranking snapshot. It is not the skill.

## Do not

- Do not retune weights to make the candidate pass.
- Do not drop `agent-owned-edit` or `partial-success` to clear the gate.
- Do not claim a later run beat this board unless it uses the same 14 cases, the same rubric, and at least 3 trials.
- Do not state that a writing style diagnoses ADHD.

## Start here

1. Read `README.md` for the rank and the hold.
2. Read `evals/rubric.md` before changing a score.
3. Read `evals/frozen-board.json` for the numbers a later run must beat.
4. Read `evals/cases.json` before adding a case. New cases are a new board, not an edit of this one.

## Source of the frozen numbers

Published 2026-08-02 run of https://github.com/ayghri/i-have-adhd — model `claude-opus-4-8`, Claude Code 2.1.220, blind judge, 3 trials. Cite that repo when quoting a score.
