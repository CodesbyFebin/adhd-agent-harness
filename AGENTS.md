# Agent guide

This repository is a pre-optimization ranking harness. The frozen board is historical. New skills are unbenchmarked.

## Do not

- Do not retune weights to make the candidate pass.
- Do not drop `agent-owned-edit` or `partial-success` to clear the gate.
- Do not rewrite frozen scores or the historical skill text to fit a new rule.
- Do not claim a later run beat this board unless cases, rubric, model, runner, tool config, and trial count match, with at least 3 trials. A tool-enabled rerun is a different experiment.
- Do not treat candidate SD as uncertainty on the paired delta. It is the standard deviation of the candidate’s trial scores.
- Do not say `partial-success` moved the same direction every trial. The average is −0.63. Trial deltas are +0.05, −0.70, −1.25: two of three worse.
- Do not state that a writing style diagnoses ADHD.
- Do not release when generation or judge rows are missing. `released: false` in JSON is not the gate. Run `release_gate`.

## Start here

1. Read `README.md` for the rank, the hold, and how to run tests.
2. Read `evals/provenance.json` for the pinned upstream checkout and file hashes.
3. Read `evals/upstream/rubric.md` for the historical judge text. `evals/rubric.md` is the local summary.
4. Read `evals/frozen-board.json` for the numbers a later run must beat.
5. Run `python -m unittest discover -s tests -v` before proposing a score or gate change.

## Source of the frozen numbers

Published aggregates from the 2026-08-02 run of https://github.com/ayghri/i-have-adhd, checkout `839872f9d1cd634fed642b4589ce7226199cc15f`. Model `claude-opus-4-8`, Claude Code 2.1.220, blind judge, 3 trials. Original response and judge rows are not in this package.
