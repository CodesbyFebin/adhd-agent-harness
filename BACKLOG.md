# Backlog — not a new score

These items do not change evals/frozen-board.json. Shipped helpers are unbenchmarked. A writing style does not diagnose ADHD.

partial-success trial deltas: +0.05, -0.70, -1.25. Two of three trials were worse. Candidate SD is score spread, not a confidence interval.

## Harness upgrades

- **H1 Severity-tiered blockers** (separate) — A B0/B1/B2 scale can rank work. It must not replace the frozen rule, which is still zero blockers.
- **H2 Confidence intervals on every delta** (rejected) — Trial rows are not in the package. An interval would be invented. Candidate SD is score spread, not a confidence interval on the delta.
- **H3 Raise trials from 3 to 10** (separate) — A longer run is a new board. The published snapshot stays at 3 trials.
- **H4 Weighted blocker penalty instead of a binary gate** (rejected) — Partial progress can be shown beside the gate. It cannot clear release. 7 to 3 still fails.
- **H5 Publish the weight vector** (shipped) — Correctness 35, autonomy 25, actionability 20, safety 10, concision 10. Already on the board.
- **H6 Per-dimension deltas, not only the weighted total** (shipped) — The board chart is those five deltas. The weighted +0.427 is the summary, not the only number.
- **H7 Judge from a different model family** (proposed) — Worth doing on a new run. This package cannot show that the published +0.427 is self-preference.
- **H8 Dual-judge agreement** (rejected) — No judge responses were published. Cohen’s kappa cannot be computed from the aggregates.
- **H9 Blind pairwise ranking next to absolute scores** (separate) — A new protocol. It does not rewrite the absolute scores already frozen.
- **H10 Five hand-scored calibration cases** (proposed) — Useful on the next run. There is no hand-scored set in this snapshot.
- **H11 Log judge prompts and raw responses** (rejected) — evals/evidence.json pins the published summary and records 0 of 84 trial rows. The three partial-success deltas are a prose excerpt and do not count. Copying them into a file does not make evidence complete.
- **H12 Split agent-owned-edit by tool availability** (separate) — The historical failure stays. A tool-enabled fixture is a different experiment, not a repair of this score.
- **H13 Pin the runner in the frozen record** (shipped) — Claude Code 2.1.220 is in the frozen board, not only in prose.
- **H14 Re-freeze when the model or runner changes** (proposed) — Policy only. A version change makes a new board. It does not edit this one.
- **H15 Record tokens and wall-clock per case** (rejected) — Not in the published aggregates. Do not fill them in.
- **H16 Temperature-0 pass on non-creative cases** (separate) — Changes the runner. Compare it as its own protocol.
- **H17 CI that reruns the model eval** (rejected) — Arithmetic CI is already on the repo. A job that reruns the model and diffs new scores would be a new board, not a check of this file.
- **H18 Append-only regression ledger** (shipped) — Two findings stay: agent-owned-edit is unpassable as run, and partial-success averaged −0.63 with two of three trials worse.
- **H19 Empirical noise floor** (proposed) — Upstream called single-case deltas under about 0.5 noise at three trials. That heuristic is not recomputed here.
- **H20 Ship decision that signs every gate row** (shipped) — release_gate has six checks: blockers, correctness, safety, weighted score, evidence, comparability. Score is not release.

## Features

1. **First line is the verdict** (shipped, Concision) — Buried answer. answer-first skill and first_line helper. Unbenchmarked beyond the frozen board.
2. **No greeting preamble** (shipped, Concision) — Friction before the signal. detect_preamble flags “Great question” and “Sure”. It does not judge quality.
3. **Patch above the explanation** (proposed, Actionability) — Code buried under prose. Not a solver. Do not score it against the frozen board until a paired run exists.
4. **One concrete next step** (shipped, Actionability) — Lost momentum. next_action returns the first unblocked step. It does not invent one.
5. **Hold tangents for a later question** (shipped, Concision) — Scope creep. scope-control and partition_scope. The second issue stays out of the first answer.
6. **Declared length budget** (proposed, Concision) — Unbounded replies. A budget is a new constraint. The frozen skill was not retuned to one.
7. **One bold verdict** (proposed, Concision) — Emphasis on everything. A style convention. The rubric does not score markdown weight.
8. **Bullets no deeper than two levels** (proposed, Concision) — Nested lists. Not implemented. Nesting depth is not a frozen dimension.
9. **Table for three or more comparisons** (shipped, Actionability) — Prose that has to be scanned. compare_options emits a criterion grid. It does not pick a winner.
10. **Two-line summary after twenty lines** (separate, Concision) — Long-form overwhelm. long-form-request was a desired null. A summary cap must not fire when the user asked for the long version.
11. **Restate step and what is pending** (shipped, Actionability) — Thread lost off screen. progress_state. This is the multi-step-progress behavior, already on the frozen board as a case, not a new score.
12. **Visible task ledger** (proposed, Actionability) — Finished steps forgotten. A product surface. The solvers do not store a session ledger.
13. **Re-anchor after a topic switch** (shipped, Correctness) — Context drift. resume_context keeps completed work, remaining work, and the next item.
14. **Assumption register** (proposed, Correctness) — Silent premise changes. Not implemented. Do not treat an unstated assumption as confirmed.
15. **Name the previous state before a mutation** (shipped, Safety) — No way back. rollback_plan records trigger, rollback, and verification. It does not run them.
16. **Recap after an idle gap** (shipped, Actionability) — Cold restart. Same resume_context helper. It needs the caller to pass what was completed.
17. **Number the plan before acting** (shipped, Actionability) — Blank-page start. chunk_tasks and the task-decomposition skill. Showing a plan is not the same as finishing it.
18. **Smallest first step** (proposed, Actionability) — Task never starts. The decomposition skill does not yet force the first step to be the smallest.
19. **Minute ranges on each step** (proposed, Actionability) — “A bit” and “a few hours”. Rule 06 already requires minutes. There is no estimator function, and none should be faked.
20. **Dependency flag on each step** (proposed, Correctness) — Work done out of order. Not implemented.
21. **Pause after every step** (separate, Autonomy) — Scope overrun. A pause can fight the autonomy score. Measure it as its own candidate.
22. **Try, change approach, then ask** (shipped, Correctness) — Retry loops. rank_hypotheses orders by evidence count. It does not invent evidence.
23. **Batch mode: do the steps, report once** (proposed, Autonomy) — Interruption fatigue. A user preference. Not in the frozen protocol.
24. **Something inspectable after each step** (proposed, Actionability) — No visible progress. Not a function. The frozen case already rewards visible progress.
25. **Split observation from inferred cause** (shipped, Correctness) — Invented root cause. error_report. A 401 does not prove a missing auth header. This does not reverse the −0.63.
26. **Quote the error before diagnosing** (proposed, Correctness) — Hallucinated traces. Not enforced. The helper records the symptom the caller supplies.
27. **Label confidence: confirmed, probable, guess** (proposed, Correctness) — False certainty. Today the helper only has supported or unconfirmed. Three labels would be a new candidate.
28. **“Unconfirmed” is a finished answer** (shipped, Safety) — Guessing under pressure. Missing cause becomes unconfirmed, with the next diagnostic named by the caller.
29. **A status for partial success** (separate, Correctness) — Binary success hiding breakage. Do not rewrite the frozen partial-success skill. Trial deltas were +0.05, −0.70, −1.25.
30. **Attempt, result, what it rules out** (proposed, Correctness) — Repeating a dead end. Not implemented.
31. **Ask for a minimal reproduction** (proposed, Correctness) — Fixing an imagined bug. Not implemented. Better than a speculative patch when the cause is unconfirmed.
32. **No fix claim without a verification command** (shipped, Correctness) — Hope shipped as done. verification_record stores command, status, and artifact. It does not run the command.
33. **Declare tools before promising an edit** (shipped, Safety) — Promised edit the runner cannot do. tool_capability. It does not clear the historical agent-owned-edit blocker.
34. **If tools are off, emit a patch and an apply command** (separate, Correctness) — Hard blocker with no output. A degrade path is a different experiment. Both historical conditions were blocked because tools were disabled.
35. **Summary of files, lines, and behavior** (proposed, Correctness) — Unclear what changed. Requires a real diff. Not available in the published runner.
36. **Preview destructive paths before they run** (shipped, Safety) — Irreversible mistake. destructive_preview lists targets and sets executed to false.
37. **Refuse edits outside the stated target** (shipped, Safety) — Drive-by refactors. partition_scope keeps out-of-scope work in the backlog.
38. **Run tests after an edit and report the exit code** (proposed, Correctness) — Claimed but broken. The record can store an exit status. Nothing here executes a test suite.
39. **One active question** (proposed, Concision) — Split attention. Not implemented.
40. **Park off-topic asks** (proposed, Concision) — Derailment. Not implemented. Related to scope control, but there is no queue.
41. **Nudge to resume after idle** (proposed, Actionability) — Abandoned session. A product timer, not a skill score.
42. **Warn when the task outgrows its scope** (proposed, Safety) — Over-building. Not implemented. Easy to nag. Do not add it to the frozen skill.
43. **Skim mode: headings only** (proposed, Concision) — Re-read cost. A view toggle. Not a judge dimension.
44. **Surface uncertainty without being asked** (shipped, Safety) — Confident and wrong. evidence-aware-errors skill. Unbenchmarked. It does not replace the frozen error rule.
45. **Mark API and version claims as sourced or unverified** (proposed, Correctness) — Stale knowledge. Not implemented. Absence of a source is not a source.
46. **Echo the destructive command before confirm** (shipped, Safety) — Accidental broad delete. Covered with the destructive-action case and destructive_preview. Confirm still outranks brevity.
47. **Flag when a style edit can change meaning** (proposed, Safety) — Formatting that breaks logic. Not implemented.
48. **Persisted terse-to-detailed dial** (separate, Concision) — One length for every task. A dial changes the skill under test. It is not a silent improvement of the frozen candidate.
49. **Turn each failure into a regression check** (proposed, Correctness) — Same mistake twice. Process for a later run. The current tests guard the frozen arithmetic, not model behavior.
50. **Agent scores itself on the five dimensions** (rejected, None) — Rubric drift. The published judge was blind and separate. A self-score is not a release signal.
