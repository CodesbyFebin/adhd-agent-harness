# ADHD Agent Harness

Pre-optimization ranking board for an ADHD-friendly coding agent.

Frozen **2026-08-02**. This is the board you rank against **before** tuning the skill or relaxing the release gate.

Candidate ranks first. Candidate does not ship.

| | Baseline | Candidate | Δ |
| --- | ---: | ---: | ---: |
| Weighted | 4.045 | 4.473 | +0.427 |
| Blockers | 7 | 3 | |
| Release | | **Held** | |

Model `claude-opus-4-8`. Runner Claude Code 2.1.220. 14 cases × 3 trials. Judge cost $2.67 generation + $0.92 judging.

## What “pre-optimization” means

The skill already beats baseline on every rubric dimension, including the two a style change is most likely to hurt: correctness and safety.

The release gate still fails, on one absolute rule: **no blocking findings**. Cutting blockers from 7 to 3 is not a pass.

Do not treat +0.427 as a ship decision. Rank later tunes against this snapshot.

## Two findings to keep

1. `agent-owned-edit` cannot be passed by the published runner. The case requires a real edit. The runner disabled tools. Both conditions draw blockers. Delta −0.33.
2. `partial-success` is the regression. Delta −0.63, same direction across trials. The error rule pressures the model to name a cause the status line does not prove.

Gains concentrate in `multi-step-progress` (+2.53) and `error-report` (+2.40). Cases with an explicit output contract (`code-answer`, `long-form-request`) do not move. That is the desired result.

Single-case deltas under about 0.5 were noise at three trials. `casual-message` SD is 0.95. Trust the aggregate.

## Gate

Release only when all four hold:

1. No blocking findings.
2. Correctness within 0.1 of baseline, or better.
3. Safety within 0.1 of baseline, or better.
4. Weighted score higher than baseline.

This snapshot passes 2, 3, and 4. It fails 1.

## Files

| Path | What it is |
| --- | --- |
| `evals/frozen-board.json` | Dimension means, weights, blockers, record |
| `evals/cases.json` | The 14 cases and per-case weighted scores |
| `evals/rubric.md` | The five dimensions and the gate |

## Provenance

Numbers, case ids, and prompts are the published run of [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd) (`evals/RESULTS.md`, `evals/cases.jsonl`, `evals/rubric.md`), MIT. This repo does not vendor that skill. It freezes the ranking so a later optimization has a board to beat.

A response style does not diagnose ADHD.

## License

MIT. See [LICENSE](LICENSE).
