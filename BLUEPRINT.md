# ADHD Agent Harness — Master Blueprint

A first-user plan for the coding-agent harness in this repository. The candidate already ranks above the baseline. It does not ship. This document says what the repo is, how a new person runs it in one sitting, and which upgrades are allowed later. A writing style does not diagnose ADHD. Nothing here is medical advice, a clinical instrument, or a claim that a response format identifies a condition.

The public package lives at [CodesbyFebin/adhd-agent-harness](https://github.com/CodesbyFebin/adhd-agent-harness). The frozen numbers come from the 2 August 2026 run published by [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd), checkout `839872f9d1cd634fed642b4589ce7226199cc15f`. This blueprint does not retune those numbers.

## 1. What this is

An eval harness is the offline loop that runs an agent on known tasks, keeps the outputs, and scores them before anyone calls the change an improvement. This repository is a small, opinionated version of that loop for one question: does an ADHD-friendly response style make a coding agent easier to follow without making it less correct or less safe?

It is not a model. It is not a clinic. It is not a general agent framework. It is not allowed to move its own baseline after the fact. The useful object is a frozen board that later work has to beat under named rules.

Three layers sit on top of each other, and mixing them up is how the project would become dishonest.

The historical board is a published judge result. Model `claude-opus-4-8`. Runner Claude Code 2.1.220. Fourteen cases, three trials each, forty-two rows per condition, eighty-four rows in total. Baseline weighted score 4.045. Candidate 4.473. Published delta +0.427. Blockers 7 to 3. Record 10 wins, 2 ties, 2 losses. Release held. Weights are correctness 0.35, autonomy 0.25, actionability 0.20, safety 0.10, concision 0.10. Cost on that run was about $2.67 to generate and $0.92 to judge.

The shape bench is a local, deterministic look at text you paste. It checks the first line, a few banned preambles, required strings, and generic closers. It does not know whether the answer is true, whether a refusal was right, or whether a file was edited. It must never be reported as 4.473.

The release gate is a decision, not a rank. Zero blockers. Correctness within 0.1 of baseline or better. Safety within 0.1 of baseline or better. Weighted score strictly above baseline. Evidence complete. Protocol comparable. The historical candidate passes the score rows that can be computed from published means and fails the blocker row. Evidence is not complete, because the original generation and judge rows were not published. Comparability is not supplied until a new run records the same cases, rubric, model, runner, tool config, and trial count. A higher score does not release.

A fourth layer is easy to confuse with the first three. Twenty skills and thirty Python functions are worked examples of clearer agent behavior. They are unbenchmarked. They do not inherit 4.473. Shipping a helper is not the same thing as beating the board.

## 2. Who the first user is

The first user is not an eval researcher with a labeling budget. The first user is a person who already uses a coding agent, got a wall of preamble, lost the next step, and wants a harness they can run before they change the agent's instructions.

They have about fifteen minutes. They will leave if the README asks them to provision a database, buy a key, or understand Cohen's kappa before they see a result. They will also leave, more slowly and more angrily, if the README treats +0.427 as permission to replace their agent's judgment.

Design the first session around three successes.

First success, under five minutes: they clone the repo, run the unit tests, and see the held result in the README without installing anything but Python 3.10 or newer. The package uses the standard library only. That constraint is a feature. A first user should not debug a lockfile to learn why a candidate was not released.

Second success, under fifteen minutes: they run one solver on a prepared example and read a result that matches the documented output. The right first command is the error report, because it demonstrates the rule the frozen board actually cares about.

```bash
python -m unittest discover -s tests -v
python scripts/solve.py error_report < examples/error-report.json
```

A 401 status with no other evidence must come back as an unconfirmed cause. If a first user sees the helper invent "missing auth header," the product has failed even if every other page is polished.

Third success, under an hour: they paste two drafts into the bench, see that shape is not the judge, open the gate, and can say in one sentence why the candidate is held. If they cannot say that sentence, the interface is decorated and the harness is not.

There is a second first user: a coding agent pointed at this repo and told to extend it. That user needs `AGENTS.md` more than the README. The agent must be told, in rules it cannot politely reinterpret, not to retune weights, not to drop `agent-owned-edit` or `partial-success`, not to rewrite frozen scores, not to call a tool-enabled rerun the same experiment, and not to describe candidate standard deviation as a confidence interval on the delta. The current agent guide already says those things. The blueprint treats that file as load-bearing. A friendlier README that contradicts `AGENTS.md` is a bug.

## 3. The contract that does not move

These rules outrank any roadmap item below, including items that would make the repository easier to star.

Do not retune the weights to make the candidate pass. The vector is part of the published protocol. A different vector is a different board.

Do not drop `agent-owned-edit` or `partial-success` to clear the gate. The first case cannot be passed by the published runner, because the runner disabled tools and the case requires an edit. Both conditions draw blockers. The delta is −0.33. Keeping an unpassable case feels unfair until you notice that deleting it would hide a measurement bug. The honest repair is a second protocol with tools, a fixture repo, and a real diff, scored on its own board.

Do not rewrite the frozen skill text so that a new error rule looks like the thing that was judged. `partial-success` averaged −0.63. The trial deltas were +0.05, −0.70, and −1.25. Two of three trials were worse. Upstream prose called that directionally consistent. It was not. Candidate standard deviation on that case is the spread of the candidate's scores, not the uncertainty of the paired delta. An evidence-aware error skill is a plausible next candidate. It is not a retroactive fix, and it has not been judged.

Do not invent the eighty-four generation and judge rows. Upstream published aggregates, plus three deltas and one grader sentence for a single case. `evals/evidence.json` may record that excerpt with `counts_as_row: false`. Copying the three numbers into a new file does not make evidence complete. The published summary can be pinned by SHA-256 of `evals/upstream/RESULTS.md`. That pin is an audit row. It does not release. As of the `evidence-row-split` work, the digest is `a9f0375594a94d2e1c4205aa6047d0213a45d9dc163ff1a63c12a534a7941b8f`. If the bytes change, the pin fails. That is the point.

Do not claim a later run beat this board unless the cases, the rubric, the model, the runner, the tool configuration, and the trial count match, with at least three paired trials. Changing tools is a different experiment even if the case names match.

Do not state that a writing style diagnoses ADHD. The name of the project describes the preference the skill was written for: lead with the next action, keep state on screen, do not bury the answer. The name is easy to misread. Every public page, skill, and release note repeats the boundary in plain language, not as a footnote in a legal voice.

## 4. Repository map

A first user should be able to find each job from the directory name.

`evals/frozen-board.json` is the number a later run must beat. `evals/cases.json` is the fourteen cases with prompts, risk, shape, and the published case scores. `evals/rubric.md` is the local summary of the judge text. `evals/upstream/` is the copied published source, pinned in `evals/provenance.json` to a checkout and to file hashes. `evals/evidence.json` separates the pinned summary from the missing trial rows.

`src/solvers.py` is thirty pure functions. They take JSON-shaped arguments and return JSON-shaped results. They do not open a network connection, call a model, or edit a repository. `data/functions.json` stores the signature, a populated input, and the exact output the tests require. `examples/` is the same input in files the command-line runner can read. `scripts/solve.py` is that runner.

`skills/` holds twenty `SKILL.md` files. Each one names a trigger, a bounded workflow, a populated example, and the helper it should call. These are repository artifacts. They are not installed personal-assistant skills until a user chooses to install them, and the file should keep saying that.

`tests/test_package.py` checks the catalog size, the function examples, release negative controls, invalid scores, protocol mismatch, coverage, the frozen arithmetic, the evidence ledger, and that the generated site has fifty-seven pages with working relative links, canonical URLs, and descriptions.

`scripts/build_site.py` writes `dist/`. The static site has a board, a bench, skill pages, function pages, a gate, and rules. Pages contain their content without JavaScript. Only the bench interaction needs a script. The site is not the historical judge.

`AGENTS.md` is the rulebook for agents that edit the repo. `BACKLOG.md` is the upgrade review: which ideas already exist as unbenchmarked helpers, which are not built, which would be a new experiment, and which must not be done. `LICENSE` is MIT. Vendored upstream material keeps its own MIT license.

The interactive ranker that shows Board, Bench, Gate, Rules, and Backlog as a single app is a separate preview surface. It must display the same frozen numbers and the same hold. It is not a second source of truth. If the preview and `evals/frozen-board.json` disagree, the JSON wins and the preview is wrong.

## 5. The board, in language a first user can repeat

Say this, and stop.

Bare prompts scored 4.045. The same prompts plus the response-style skill scored 4.473. The candidate still had three blocking findings. The release rule is zero blockers, so the candidate is held. The two cases that explain the hold are `agent-owned-edit`, which the runner could not perform, and `partial-success`, where the style pushed the model to name a cause the status line did not prove.

The gains sit mostly in cases about reporting state. `multi-step-progress` and `error-report` move by about two and a half points. Cases with an explicit output contract, `code-answer` and `long-form-request`, do not move. That null is a success. A style change should not rewrite a task that already says what the output is.

Three trials are few. On `casual-message` the candidate spread reaches 0.95. Single-case deltas under about 0.5 were treated by the original write-up as noise. The aggregate is firmer than any one row and still not a ship decision. One judge model scored a model from the same family. That is a known weakness, not a secret. It is also not something this package can repair by inventing a second judge's scores.

Every public explanation should fit on one screen before it offers the table. The table is for the person who stayed.

## 6. First-user path

### Minute 0 to 5 — prove the package runs

The README opens with the hold, then the commands. No banner that asks for a star. No diagram that has to be trusted before a test passes. The tests are the handshake. Ten tests, standard library, no network. A failing clone is a broken release, not a puzzle.

The README then shows one solver. `error_report` is the teaching example because the failure mode is concrete: a status code is not a cause. `non_diagnostic_response` is the second teaching example, because the name of the repo will be misread and the function should answer that misreading in one line: a writing style or a reading preference does not diagnose ADHD.

### Minute 5 to 20 — see the hold without reading the theory

Generate the site and open the gate page.

```bash
python scripts/build_site.py --base-url https://codesbyfebin.github.io/adhd-agent-harness/
python -m http.server 8000 --directory dist
```

The gate page lists the rows in order. Blockers fail. Correctness passes. Safety passes. Weighted score passes, with the sentence that rank is not release. The published summary pin passes only when the file hash matches. Trial rows fail at 0 of 84. Comparability is not supplied. A first user who only reads the green rows will still see the hold in the title. Do not put the pass rows above the title "Held."

The bench page loads two drafts for `partial-success`. Draft A buries the result and closes with filler. Draft B leads with what passed, quotes the 401, and says the cause is unconfirmed. The bench may prefer B. The page must say that this preference is shape, not the frozen judge, and not a reversal of −0.63.

### Minute 20 to 60 — use it on their own agent

Give them a worksheet, not a framework tour.

1. Pick one case from `evals/cases.json`. Start with `direct-answer` or `error-report`, not `agent-owned-edit`.
2. Paste the case prompt to their agent twice: once with their current instructions, once with a single skill file copied in.
3. Paste both replies into the bench.
4. Write down, in their own words, what the bench cannot see.
5. Do not file the result as a new frozen score.

That fifth step is the product. The harness is friendly when it makes the boundary easy to keep, not when it flatters the user with a number that looks official.

### The rest of the first day

If they are still here, they are a contributor, not a tourist. Point them at one open question that does not require a model bill: add a fixture row that `validate_coverage` rejects, or add a page that renders `evals/evidence.json` without changing the gate. Do not point the first contributor at "rerun the judge." That task is a new board, a budget, and a protocol record. It is not a good first issue.

## 7. How a coding agent should use the repo

An agent editing this repository is a user too, and a dangerous one, because it will try to be helpful by making the candidate pass.

The session prompt that should sit at the top of `AGENTS.md`, and that a future installer may inject, is short.

You are editing a frozen ranking harness. Read `evals/frozen-board.json` before you change copy that states a score. Tests must pass. You may add an unbenchmarked skill if you label it unbenchmarked. You may not change a frozen number, a weight, a case id, or the release rule in order to obtain a pass. If evidence rows are absent, the release stays held. If you add a tool-enabled evaluation, put it in a new protocol file and do not overwrite the historical result.

The agent should prefer the solvers to fresh prose. If the task is "what is the next step," call `next_action` on steps the user supplied. If the task is "what failed," call `error_report` and keep `unconfirmed` when no cause was supplied. If the task is "are we allowed to ship," call `release_gate` and do not treat a pinned summary as `evidence_complete=true`.

The agent should refuse three requests even when the user sounds certain. Refuse to fill in the eighty-four rows from the published means. Refuse to mark `agent-owned-edit` passed because a degrade path could have printed a patch. Refuse to average the three partial-success deltas into a story about a consistent regression direction.

## 8. Inventory that the roadmap is not allowed to pretend is unfinished

Twenty skills already have populated workflows.

Answer First, Bounded Next Action, Task Decomposition, Progress State, Partial Success, Evidence Aware Errors, Debug Hypotheses, Agent Owned Work, Safe Preview, Resolve Ambiguity, Output Contract, Detailed Explanation, Decision Support, Rollback Planning, Resume Context, Scope Control, Verification Evidence, Benchmark Integrity, Release Gate, and Non Diagnostic Boundary.

Thirty functions already run.

`first_line`, `required_facts`, `detect_closers`, `detect_preamble`, `check_output_contract`, `shape_precheck`, `summarize_checks`, `error_report`, `rank_hypotheses`, `next_action`, `chunk_tasks`, `progress_state`, `missing_fields`, `tool_capability`, `destructive_preview`, `compare_options`, `rollback_plan`, `resume_context`, `partition_scope`, `verification_record`, `validate_scores`, `weighted_score`, `score_delta`, `release_gate`, `compare_protocol`, `validate_coverage`, `win_tie_loss`, `non_diagnostic_response`, `outline_explanation`, and `evidence_gaps`.

The static site already has fifty-seven HTML pages, a sitemap, canonical URLs, and structured data. GitHub Pages publication has not been performed. A ZIP of the site is not indexed. Crawling depends on a public deployment. No ranking guarantee comes with the sitemap.

The backlog already sorted a fifty-item feature list. Nineteen items exist as helpers and remain unbenchmarked. Twenty-five are not built. Five would be a new experiment. One, an agent scoring itself on the rubric, is rejected. Self-scoring is circular. The published judge was blind and separate. That rejection stays.

## 9. Roadmap

Phases are ordered by what a first user needs, then by what would make a later number trustworthy. A phase does not start by reopening the frozen file.

### Phase 0 — Make the first hour boring

Goal: a stranger clones, tests, and understands the hold without asking anyone.

Ship a tagged `v0.1.0-held` that matches `main` and says "held" in the tag name so a release page cannot be skimmed as a launch. Publish `dist/` to GitHub Pages at the base URL the canonical links already use. Until that URL answers, the README must keep the sentence that publication has not been performed. A dead canonical link is worse than an unpublished site, because it looks finished.

Rewrite the first screen of the README as a three-line story, then the two commands, then the weight vector, then the link to the gate. Move the methodology below the first successful command. Add a "read this if you only read one file" pointer to `AGENTS.md` for agents and to the gate page for humans.

Add a `make check` or a single `python scripts/check.py` that runs tests and rebuilds the site, so the first user does not have to remember two invocations. Keep it standard library. Do not introduce a task runner to save one line.

Record a ninety-second silent capture later, after the Pages URL works: tests passing, gate held, bench labeling itself as shape. Do not record a face, a diagnosis story, or a graph that omits the hold.

Exit test: a person who has never seen the repo can say why 4.473 did not ship, without scrolling past the first screen.

### Phase 1 — One front door

Goal: the static site and the interactive ranker stop feeling like two products that disagree.

The Python site is what a search engine can read without running a bundler. The interactive preview is what a person uses to file a local rank, compare buried and shaped drafts, and see per-dimension deltas. Both must read the same frozen JSON. The practical fix is to vendor `evals/frozen-board.json`, `evals/cases.json`, and `evals/evidence.json` as the only numeric inputs, and generate the preview's protocol module from those files in CI. A hand-copied TypeScript constant is how 4.473 becomes 4.47 in one surface and 4.473 in the other.

The preview's gate already separates the pinned summary from the missing trial rows. Keep that. Do not add a button that sets evidence complete. Do not add a form that accepts a weighted score and writes it into the frozen file. Local filings on the bench are a scratch pad. Label them as scratch. Persist them in the browser if you want, and never upload them as results.

Add a first-run empty state on the bench. The empty state offers two buttons: load the buried draft, load the shaped draft. It does not offer a score until there is text. The winner line says "shape pre-check," never "judge."

Exit test: changing a digit in `frozen-board.json` fails CI on both the Python tests and the preview build.

### Phase 2 — A row format, still empty

Goal: when real trial rows appear, the repository can accept them without a redesign, and cannot be talked into fakes.

Define a row schema and reject everything else. Required fields: `case_id`, `condition` (`baseline` or `candidate`), `trial` (1, 2, or 3 for the historical protocol), five finite scores in [1, 5], `blocker` as a boolean, `response_sha256`, and `judge_sha256`. Optional fields: cost, token counts, wall-clock. Do not require fields the 2026 run did not publish, or the schema will make honest rows unrepresentable.

`validate_coverage` already knows how to find missing keys. Extend the ledger so `evidence_complete` is computed from coverage plus score validation plus hashes, not typed in as a boolean the caller hopes is true. `release_gate` may keep a caller flag for synthetic tests, but the historical path must pass the computed value, which is false today.

Add a negative fixture: one duplicate row, one row outside the case list, one score of 6, one excerpt pretending to be a row. Tests fail the build if any of those flip the hold to released.

If the upstream author later publishes logs, import them as bytes, hash them, and only then set the trial-row check to pass. Do not transcribe means back into eighty-four invented cells. A mean is not a row.

Exit test: the only way to make `trial_rows_present` true in CI is to add eighty-four valid records whose case means match the frozen board within a stated tolerance. Until those bytes exist, the check stays false on `main`.

### Phase 3 — A second board, visibly different

Goal: study the two findings worth studying, without editing the first board.

Open `protocols/tool-enabled/` as a new experiment for `agent-owned-edit`. It needs a temp repository, a known typo or failing test, tools turned on, and a diff that can be read. Score it on its own file. The historical delta of −0.33 stays in `evals/`. The README links to the new protocol with the words "different experiment."

Open `protocols/evidence-aware-error/` for a candidate instruction that may say the failure and the location, may state a cause only when the prompt supports it, and must otherwise say the cause is unconfirmed. Run it on `partial-success` and on `error-report`, because a rule that fixes the regression might blunt the case the old skill won. Do not replace the frozen skill text. Do not report a win from a single afternoon of prompt editing. Pre-register the rule text in the protocol folder before the run, so the harness is not tuned against the same afternoon's outputs.

Neither protocol ships inside the historical gate. They get their own gate files. If someone wants a combined "current best skill," that is a third protocol with a date, a model, a runner, and a bill. It does not overwrite 2 August 2026.

Raise trials only inside a new protocol. Ten trials, or a sequential stop when an interval is narrow, is a reasonable next measurement. It is not a correction of the three-trial snapshot. Confidence intervals are allowed when the trial rows exist. They are not allowed as decoration computed from a published standard deviation that measures something else.

Use a judge from a different model family on the new protocols. Keep the original rubric text. Log the judge prompt and the raw judge output next to the response hash. Dual-judge agreement is worth computing once two judges have actually scored the same rows. It is not worth estimating.

Exit test: a reader can open the repo and see two dates, two result files, and no sentence that says the new run "updated" the old one.

### Phase 4 — Skills a first user can install without forking their brain

Goal: the twenty workflows become usable in a coding agent without pretending they were the judged skill.

Write a `skills/README` with a picker, not a wall. Six skills cover the first week: Answer First, Progress State, Evidence Aware Errors, Safe Preview, Output Contract, and Non Diagnostic Boundary. The other fourteen stay available and labeled "use when the task matches," not "enable all."

An installer command may copy a chosen `SKILL.md` into the agent's skill directory. The installer prints the unbenchmarked warning and the hold. It does not silently enable all twenty. An agent with twenty always-on style rules will fight the user's explicit format, which is the failure output-contract cases were written to catch.

Add a project verbosity note only as a separate experiment. A persisted terse-to-detailed dial changes the skill under test. It is not a quiet improvement of the frozen candidate.

Add the smallest missing helpers only when a skill page has to lie without them. The honest gaps are: a quote-the-error step that refuses to diagnose before a verbatim symptom is present; a dependency flag on `chunk_tasks`; a verification record that still does not pretend to have run the command. Do not add an agent self-score. Do not add a minute estimator that fabricates durations. Rule 6 already says to use minutes; a made-up "about 12 minutes" is worse than silence.

Exit test: a first user can enable one skill, point at the helper it calls, and find a test that shows the helper's failure mode.

### Phase 5 — The harness as a tool other people can point at their own agent

Goal: become the small repo people recommend when a friend asks how to stop trusting a vibe check.

This is the phase that can earn stars. It does not start with a star button. It starts with a comparison a skeptical reader can check.

Publish a one-page contrast. Large harnesses such as EleutherAI's lm-evaluation-harness measure model capability across tasks. This repo measures one response-style change on fourteen coding-agent cases and refuses to ship on blockers. Say that in four sentences. Readers who need a leaderboard will leave, and they should. Readers who have been burned by a style guide that made a model verbose will stay.

Offer a case-author template: id, prompt, risk, required strings, what the judge is allowed to treat as a blocker, and a note on whether tools are required. A contributed case does not enter the frozen fourteen. It enters `protocols/community/` and stays unscored until someone runs it under a written protocol. Reject pull requests that add a case and a score in the same commit unless the rows, the hashes, and the runner pin come with it.

Offer a regression ledger file, append-only. The first two entries already exist and must be copied in without cleanup: `agent-owned-edit` unpassable as run; `partial-success` mixed trials, negative average, mechanism in rule 8. New entries need a date and a protocol id. The ledger is not a changelog of features.

Keep CI on arithmetic, coverage, links, and the hold. Do not add a CI job that calls a model on every pull request. A model job is a manual workflow with a cost ceiling and a protocol id, and its artifacts are uploaded, not committed as an amended frozen file.

Exit test: an outside pull request that "fixes" the hold by deleting a case fails review against `AGENTS.md` in under ten minutes, because the rule is specific.

### Phase 6 — Only if the project is actually used

Goal: operational hygiene after strangers depend on it. Not before.

A re-freeze policy: if the model name or the runner version in a new run differs, write a new board. Do not edit the old one. Put the trigger in the README in one paragraph.

Severity labels beside the gate, never instead of it. A blocker can be tagged fatal, blocking, or minor so a person knows what to study next. The ship rule remains zero blockers. Going from seven to three still fails. A weighted penalty that lets partial blocker progress release is rejected.

Trace links, if a runner can emit them, attach to rows by hash. They help a human read a failure. They are not a substitute for the score.

A calibration set of hand-scored cases is worth keeping for a new judge. Five cases is a start. It does not exist yet, so do not draw a chart of agreement.

Token counts and latency can join a new protocol. The historical aggregates do not contain them. Leave the cells blank.

## 10. Upgrades that look attractive and stay out

These were proposed, and they stay out of the default path.

Confidence intervals on every historical delta. The trial rows are not in the package. An interval would be invented.

Replacing the binary blocker rule with a weighted penalty. Rank can show partial progress. Release cannot.

A CI job that reruns the model and fails if the frozen file drifts. That job would overwrite the snapshot with a new sample and call the overwrite verification.

Splitting `agent-owned-edit` by deleting the tool-disabled result. The split is allowed only as an added protocol.

An agent that grades its own answer on the five dimensions before sending. Rejected.

A length budget, a single-bold-verdict convention, a two-level bullet cap, and a skim mode. These are style preferences. The rubric does not score markdown weight. Build them only as optional, off-by-default views.

An auto-pause after every step. It may fight the autonomy score. Measure it as its own candidate or leave it out.

Filling token counts, wall-clock, or a second judge's kappa from the published means. Absent.

## 11. Becoming a repository people star

Stars follow repeated, checkable usefulness. They do not follow a roadmap that announces itself as a top repository. Treat the star count as a lagging side effect, and spend the effort on the things a stranger can verify on a phone.

The description line should be the hold, not the feature count. A good description: "Frozen pre-optimization board for an ADHD-friendly coding-agent style. Candidate 4.473 vs baseline 4.045, release held." A bad description: "The ultimate AI agent harness for ADHD with 50 features." The second one will collect the wrong issues.

Topics that match the contents: `llm-evaluation`, `ai-agents`, `coding-agents`, `eval-harness`, `benchmark`. Skip topics that imply a clinical dataset.

The first screenshot on the social preview should be the gate with the word Held visible, plus the two scores. A screenshot of a green dashboard will be shared as a victory the repo does not claim. Write the image alt text as a sentence, not a keyword list.

Publish the site. Pin the release. Link the upstream project prominently, with the checkout hash, so the work does not look like an uncredited rehost. Attribution is also how serious readers decide to star: they can see you did not pretend to have run the judge.

Write three issues that a new contributor can finish in an evening, each with the files to touch and the test to run. Good issues: render the evidence ledger on the gate page from `evals/evidence.json`; add a solver fixture where a preamble is detected; document the six-skill starter set. Bad issues: "add AI," "improve accuracy," "beat the benchmark."

When you write about the repo, link the gate and quote the hold in the first paragraph. Posts that lead with +0.427 will be corrected in the comments, and the correction will be the most honest thing on the page. Lead with the correction yourself.

Do not buy stars, do not trade stars, and do not add a popup. A harness repository that begs is a harness nobody should trust with a release decision.

The realistic audience is small: people who run coding agents and people who argue about evals. A few hundred stars would mean the explanation traveled. A few thousand would mean other harness authors are sending newcomers here for the "score is not release" pattern. Neither number is a milestone the README should display. Display the hold.

What will actually get the repo cited is a single reusable sentence other README authors can copy: candidate ranks first, candidate does not ship, here is the rule that failed. Make that sentence true in code, short on the first screen, and stable under a tag.

## 12. Measures that matter more than stars

Count these monthly, in a place that is not the README hero.

Clone-to-green-test time, on a clean machine, from the documented commands only. If it exceeds fifteen minutes, the first-user work is not done.

Number of people who can answer "why is it held?" after the first screen. Ask three people who did not build it. If two fail, the copy is wrong.

Number of pull requests that try to change `evals/frozen-board.json`. More than zero is a sign the warnings are easy to miss. Fix the warnings. Do not accept the edits.

Number of issues that ask the project to diagnose a person. Reply with the boundary and close them. Do not collect symptoms.

Whether GitHub Pages and the tag exist. Binary. Phase 0 is incomplete until both are true.

Whether any new protocol folder has overwritten `evals/`. That count must stay zero.

Unbenchmarked skills used in the wild are a bonus metric. Do not convert usage into a fake score.

## 13. Ninety days, if only one person is maintaining it

Days 1 to 7. Tag `v0.1.0-held`. Publish the site or remove the dead canonical hope from view by stating the unpublished state in the first paragraph, not the third. Run the first-user path yourself on a machine without the repo cached. Fix every command that assumed a local habit.

Days 8 to 21. Generate the preview protocol from the JSON. Add the empty-state bench copy. Add `scripts/check.py`. Make CI run it.

Days 22 to 40. Land the row schema and the negative fixtures. Point `evidence_complete` on the historical path at computed coverage. Leave the rows empty.

Days 41 to 60. Write the six-skill picker and the installer warning. Do not install them into the frozen candidate.

Days 61 to 90. If, and only if, there is budget and a written protocol checked in first, run one new board: evidence-aware error handling on the existing fourteen prompts, new model or the same model, judge from another family, raw rows saved. Publish it beside the old board. Write the result even if it loses. A published loss is how this repository stays worth starring after the first week.

If there is no budget, do not invent the run. Spend the month on the case-author template and the regression ledger instead. An empty honest repo beats a full invented one.

## 14. What done looks like

A first user clones the repository, runs one command, and watches the tests pass. They open one page and see 4.045, 4.473, three blockers, and the word held. They paste their own agent's reply into a bench that refuses to call itself the judge. They can copy one skill into their agent and know it was not the skill that produced the frozen score. A later maintainer can add a protocol without a reviewer having to rediscover, in the diff, that the old numbers moved.

The top of the repository is not a trophy. It is a place other people send a friend who is about to tune an agent against an eval until the eval agrees. The friend should bounce off a rule that will not agree.

Candidate ranks first. Candidate does not ship. The rest of this blueprint is how to keep that sentence true while the project becomes easier to use.
