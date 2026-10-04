# ADHD Agent Harness: user-first coding harness master blueprint

Version: planning edition 1.0. Author and maintainer: Febin Francis, CodesbyFebin. Prepared 4 October 2026. This document is a product and engineering proposal grounded in the uploaded preview and the earlier skills-and-solvers package. It does not claim the future runtime exists, that a new model evaluation has passed, or that GitHub popularity is guaranteed.

## 1. The product promise

Build a coding-agent harness that makes the current task easy to understand, safe to execute, and possible to verify. The user should be able to answer four questions at any point: What am I trying to finish? What has actually happened? What is blocking progress? What can happen next? The harness should carry that context across interruptions rather than require the user to reconstruct it from a long transcript.

The proposed public positioning is: “Clear steps. Real edits. Verified outcomes.” Keep ADHD Agent Harness as the recognizable project name, while describing it as useful for people who prefer explicit state, low distraction, bounded actions, and honest uncertainty. Do not require an ADHD diagnosis to use it. Do not claim that presentation preferences diagnose ADHD, treat ADHD, or demonstrate clinical benefit. Accessibility preferences belong to the user, and different users may prefer different levels of detail.

Success means a person can start a real task, review an actual change, understand the evidence, and resume later without losing control. A prettier chat transcript is insufficient. The product should eventually combine context continuity, governed tool execution, source changes, verification, and evidence export. These capabilities need explicit implementation and qualification; the current package supplies a starting preview and deterministic helpers, not a finished autonomous execution system.

## 2. What exists today

The uploaded app uses React, TanStack Start and Router, TypeScript, Tailwind, and Zustand. The package scripts include development, type checking, linting, tests, and production build commands. The build command also invokes database migration tooling, so it should not be treated as a pure compilation command in future release automation. The app contains platform preview, authentication, database, and PWA scaffolding. Their presence does not establish that the harness uses an authenticated execution backend.

The harness-specific application is concentrated in `app/src/components/harness/app.tsx`, with a separate backlog component. Protocol metadata, case definitions, fixtures, presets, heuristic scoring, and local persistence live under `app/src/lib/harness/`. Board, Bench, Gate, Rules, and Backlog are selected through component view state. Only the index route is apparent in the uploaded harness routes. Separate views therefore need explicit routes before they can become independently crawlable documentation destinations.

The preview’s scoring function produces five dimension-shaped values and a weighted local number through regular expressions. It checks patterns such as preambles, required words, destructive commands, uncertainty phrases, and claims of editing. It does not invoke a model judge or inspect a repository diff. A response saying “fixed README” can receive favorable autonomy treatment without an executed edit. A refusal word can interact with unsafe text in ways that a regex cannot reliably interpret. These are known heuristic limitations, not validated safety decisions.

The Zustand store persists filings under `adhd-agent-harness-v1` in local browser storage and caps them at eighty. This differs from the earlier static toolkit Bench, which does not persist drafts. The interface must distinguish the two implementations. A privacy notice should say what the active implementation actually does rather than repeat a generic local-only claim. Browser storage can contain sensitive pasted material, so users need a visible reset and export path.

The earlier toolkit provides twenty repository skill folders, thirty Python functions, populated examples, and fifty-seven static HTML pages. It is included separately under `toolkit/` in this master package. It is not installed into a personal ChatGPT skill directory. The preview references helper-related backlog items, but that does not mean the Python helpers are imported into the React app. This package intentionally preserves both codebases without pretending they have been integrated.

## 3. Preserve benchmark integrity

The historical board remains the published 2 August 2026 result: baseline weighted 4.045, candidate weighted 4.473, published delta +0.427, blockers seven versus three, and a record of ten wins, two ties, and two losses across fourteen cases and three trials. The frozen candidate is held. A higher weighted score does not clear the zero-blocker rule. These historical facts must stay visible even when the product becomes more capable.

The tool-disabled `agent-owned-edit` case cannot demonstrate a real edit. Preserve the old result and create a separately identified tool-enabled experiment with a fixture repository. The fixture should contain an exact typo, expose only allowed operations, and require a verified filesystem diff. Record tool availability, workspace hash, runner version, command results, and cleanup behavior. A changed tool protocol must never be presented as an identical reproduction of the historical board.

The partial-success regression deserves a targeted candidate change. Require the response to preserve lint and unit-test passes, name the integration failure and location, and avoid inventing its cause. The reported trial deltas were +0.05, −0.70, and −1.25, so describe a negative mean with two negative trials rather than claiming every trial regressed. Candidate standard deviation is score spread, not a confidence interval on paired improvement. Original response and judge rows are required before computing intervals or agreement statistics.

New evaluation protocols should pin cases, exact judge rubric, model identities, runner versions, tool configuration, skill body, trial counts, and applicable environment settings. Preserve failed calls and incomplete groups. Missing data must remain missing rather than become a zero score or a silent exclusion. Comparability requires more than matching a runner alias. Cross-model judging, longer runs, and new accessibility scenarios are valuable extensions, but each needs a separately named protocol and a clearly described comparison scope.

## 4. Design the first five minutes

The first screen should offer three understandable choices: try a populated example, inspect the historical board, or start a local coding task when execution is available. Do not require sign-in to read documentation or use a text-only demo. Show a concise product explanation and a visible capability label. A demo that checks text should say “Shape preview”; an execution workspace should say “Local task workspace.” A disabled runtime must never look like a ready agent waiting for a prompt.

For the first successful demo, use partial-success because it demonstrates the project’s most important reasoning boundary. Show the input status, a buried response, and a shaped response. Explain that the shaped version preserves the two passes and leaves the cause unconfirmed. Let the user edit either draft and observe individual shape checks. Avoid a single large number that resembles the published benchmark score. Add an adversarial example that passes string matching while remaining substantively wrong, making the limitation tangible.

When real execution is available, begin with a small documentation edit in an isolated example repository. Show the target file, intended change, allowed tools, and verification command before execution. Afterward show the diff and actual command exit status. Give the user a clear choice to keep or discard the example. The first-run flow should teach control and evidence, not request production credentials or encourage immediate deployment.

Suggested usability acceptance targets are that a new participant can explain the difference between preview and judge, find the remaining failure, locate the reset control, and identify whether an edit really occurred. Measure completion and misunderstanding with voluntary user testing. Time-to-first-result goals are product hypotheses, not fabricated current metrics. Record testing conditions and report failures alongside successful sessions.

## 5. Build an accessible working interface

Organize the future workspace around Task, Changes, Checks, and Evidence. Keep one current task prominent while allowing a collapsible backlog. A user should not have to scan a hundred-line chat to find the next unresolved issue. Show a short state card containing goal, current step, completed outcomes, blocker, and next action. Maintain a chronological event view for people who need the full detail, with a simple way to return to the task state.

Offer concise, standard, and detailed display modes as preferences. These modes change presentation, not hidden reasoning quality or permissions. Detailed explanations must remain available for architecture decisions, security concerns, and explicit long-form requests. Never silently discard relevant information to satisfy a five-item cap. Group long lists, retain the complete record, and make additional items discoverable through predictable controls.

Use clear labels, visible focus states, sufficient contrast, stable navigation, and understandable error recovery. Do not rely only on green and red to communicate pass and fail. Respect reduced-motion preferences and avoid attention-grabbing animation in the work surface. Ensure modal dialogs restore focus, interactive controls have accessible names, and progress announcements do not repeatedly interrupt screen-reader users. A keyboard-only user must be able to run the example, inspect results, export, and reset.

WCAG 2.2 provides the standards reference; W3C cognitive accessibility guidance supplies additional patterns for understandable controls and clear content. The project should test these requirements rather than claim compliance from a visual inspection. Include checks at mobile widths and browser zoom. Accessibility reports should describe what was checked, which assistive technologies were used, and what remains unresolved. Invite feedback without asking contributors to disclose medical history.

## 6. Target architecture and boundaries

Keep the interface, execution control, and evidence logic separate. The UI should render task state and request operations; it should not possess unrestricted shell authority. A local controller should own policy evaluation, workspace selection, tool invocation, cancellation, and event emission. Runner adapters should translate model output into a constrained protocol. Tools should execute only through a gateway that checks scope and records results.

A proposed task state machine is draft, ready, running, waiting-for-input, waiting-for-approval, verifying, completed, failed, and canceled. A paused state can be added when reliable resume semantics exist. Every transition needs an allowed source state, reason, timestamp, and responsible component. UI state must derive from recorded transitions. A model’s textual claim that a task is completed cannot transition the controller directly to completed without verification evidence.

The evidence bundle should connect goal, source revision, patch, tool calls, test results, policy decisions, and final response. Events need stable task and run identifiers, sequence numbers, schema versions, and correlation identifiers. Start with an append-only local journal and a documented export format. An append-only journal is not automatically tamper-proof; later hash chaining or signing can add integrity properties, with explicit key management and verification rules.

Avoid premature distributed orchestration. First support one user, one workspace, one active task, and one model runner. Introduce background queues only when interruption and retry behavior are defined. Add team access after isolation, identity, and authorization are demonstrated. A local-first design can remain useful without a hosted account system, which lowers initial onboarding complexity and reduces the amount of sensitive repository content that must leave the machine.

## 7. Deliver actual coding autonomy safely

For filesystem operations, restrict all paths to a selected workspace. Resolve symlinks and reject traversal outside that root. Treat model-generated paths as untrusted input. Record the inspected file version and detect concurrent edits before overwriting. Apply small patches and show the resulting diff. Prefer an isolated worktree or disposable fixture for qualification so the user’s active checkout is preserved.

For command execution, represent commands as an executable and argument array, not an interpolated shell string. Set working directory, timeout, output limit, environment allowlist, and cancellation behavior explicitly. Read-only diagnostics and irreversible mutations require different policy handling. A policy classification based solely on a command name is insufficient: arguments, target paths, shell expansion, and subprocess behavior affect the risk.

The user must approve concrete high-impact changes when authorization is absent, such as destructive operations or production deployment. Approval records should bind to the exact command, target, source revision, and expiration. A later modified request must not reuse an unrelated approval. Routine authorized edits should proceed without repeated confirmation; unnecessary prompts undermine the intended low-friction experience.

Verification should run the project’s appropriate checks and preserve their exit statuses. Do not claim that every task needs a full integration suite, and do not equate a passing formatter with product correctness. Define task-specific checks before execution where practical. For a README typo, inspect the exact diff. For an authentication repair, use relevant unit and integration evidence. Distinguish tests that ran from checks that were unavailable, skipped, or blocked by infrastructure.

## 8. Make skills useful rather than numerous

The existing twenty skills cover answer-first responses, next actions, decomposition, state reporting, partial success, errors, hypotheses, agent-owned work, safe previews, ambiguity, output contracts, detail, decisions, rollback, resume, scope, verification, benchmark integrity, release gates, and diagnostic boundaries. These are modular workflows, not proof that an agent has acquired reliable execution abilities. Each skill should have a narrow trigger and explicit limits.

Add a registry with stable IDs, version, description, compatible protocol versions, linked deterministic functions, examples, and evaluation status. The registry should separate authored, validated-format, behavior-tested, and benchmark-qualified states. Do not use “verified” to mean only that a Markdown file exists. Skill versions must be content-addressed for evaluations so an edit cannot silently change the candidate behind an old score.

Introduce routing gradually. Begin with explicit user selection or simple transparent matching, then record which skills were activated and why. Test conflicts, such as answer-first versus an output-only code request, or concise display versus a requested detailed explanation. User intent and safety constraints win over stylistic defaults. Avoid loading every skill into every prompt because excessive instructions increase conflicts and make attribution difficult.

Future skill additions should target observed failures: dependency-upgrade verification, flaky-test triage, source-backed API guidance, patch review, recovery after interrupted execution, and secret-aware export. Each addition needs a concrete motivating example, a negative control, and a maintenance owner. Publishing fewer robust workflows is more valuable than producing hundreds of nearly identical pages. Keep the original twenty discoverable while clearly marking experimental additions.

## 9. Turn helpers into well-defined libraries

The thirty Python helpers are deterministic transformations of caller-supplied data. Some validate score ranges and coverage; others create structured reports or plans. Their outputs are useful building blocks, but they do not independently establish that an event happened. A caller passing a cause into error_report is asserting that cause. A caller setting evidence_complete to true is asserting completeness. Future code should replace important assertion flags with validated evidence objects.

Define schemas for inputs and outputs, consistent error handling, and stable serialization. Add property tests where inputs have large edge-case spaces, such as coverage keys, Unicode text, numeric scores, and protocol identity comparisons. Preserve null for unknown values. Reject booleans where integer scores or counts are expected, non-finite numeric values, malformed trial identifiers, and duplicate evidence rows. Document whether empty inputs are allowed and what they mean.

Choose one authoritative scoring and gate implementation. If the product adopts TypeScript for the controller, port the relevant Python logic with shared fixtures and parity tests instead of maintaining divergent formulas. Keep a Python package or CLI only if users need it. The React regex score and the Python four-check shape pre-check currently have different semantics; name and version them separately until a deliberate consolidation is implemented.

Expose a small CLI for offline inspection and integration. Proposed commands include validate, inspect, compare, gate, export, and verify-bundle. Commands must have meaningful exit codes and machine-readable output. A future execute command should remain unavailable until the tool gateway passes its safety tests. Provide shell-independent examples so Windows, macOS, and Linux contributors can reproduce the same deterministic checks.

## 10. Qualification, security, and privacy

Create separate test layers for deterministic logic, model behavior, tool execution, accessibility, and deployment. Unit tests should protect calculations and invariants. Scenario tests should verify actual workspace effects. Model evaluations should preserve outputs and judge evidence. Browser tests should exercise complete user journeys rather than only confirm that a page loads. Every test layer should communicate what it cannot establish.

Threat-model prompt injection in repository content, unsafe tool arguments, secret leakage in logs, malicious archive import, cross-workspace access, and false completion claims. Imported files are data, not instructions with authority over the controller. Protect exports by scanning likely credential material and letting the user inspect exclusions. Do not silently claim perfect redaction: secrets can appear in unexpected formats, so document residual risk and avoid collecting unnecessary environment values.

Keep repository contents, prompts, and traces local by default. When a model provider is used, disclose the provider destination and exactly which data categories will be sent. Make telemetry opt-in and aggregate where possible. Do not collect medical information, diagnoses, or user identity for an anonymous demo. Deletion controls should clear both application records and relevant local storage; exported files remain under the user’s control.

Security reporting needs a supported channel and an honest response commitment. Use GitHub private vulnerability reporting if the maintainer enables it, with a fallback contact process that does not publish sensitive details in issues. Before claiming production readiness, complete hostile fixture tests, verify approval binding and cancellation, test least-privilege boundaries, and demonstrate recovery from process failure. A successful happy-path demo is only one part of that qualification.

## 11. A staged delivery roadmap

Treat the schedule as a suggested sequence for a small team, not a commitment. Each milestone needs an owner, dependencies, acceptance evidence, and a stop condition. Dates should be adjusted after the first implementation spike. Preserve a working demo throughout the transition so contributors can understand the project while the execution backend is still being built.

Days 1–14: establish a trustworthy foundation. Separate historical board, heuristic preview, and new candidate data in types and UI. Add protocol and scorer tests. Document browser persistence and reset behavior. Inventory platform-specific scaffolding without deleting it prematurely. Verify build scripts in a controlled environment and separate compilation from migrations. Exit when a contributor can run the deterministic checks and correctly explain every score label.

Days 15–30: improve the first-run journey. Add route-addressable Board, Bench, Skills, Functions, Methodology, and Roadmap pages. Add exported examples, import validation, a reset control, keyboard coverage, and mobile checks. Implement a task state view using simulated events explicitly labeled as fixtures. Exit when voluntary usability participants can find current state, distinguish heuristic from judge results, and recover from invalid input without maintainer intervention.

Days 31–60: implement one local runtime adapter and a scoped tool gateway. Start with inspect, patch, and test actions in disposable repositories. Build cancellation, timeout, path-boundary, approval-binding, and event-recording tests. Add an actual agent-owned-edit qualification fixture. Exit when real diffs and test results appear in evidence bundles and adversarial tests reject forbidden access. Do not open arbitrary production execution during this milestone.

Days 61–90: implement evaluation orchestration. Add resumable generation, blinded judge requests, complete-row validation, cost reporting, and protocol hashing. Run the historical text protocol as a reproduction attempt only if the pinned runner and model are genuinely available; otherwise report incompatibility. Run the tool-enabled protocol separately. Exit when another contributor can verify one new evidence bundle and reproduce its aggregate from the recorded rows.

Months 4–6: stabilize release candidates and integration points. Add a second runner, richer regression scenarios, signed or hash-linked exports, editor integration experiments, and optional preference persistence. Prioritize issues from real use. Introduce hosted collaboration only after a documented isolation and authorization review. Publish release notes with limitations and migration instructions. A 1.0 release requires qualification evidence, supportable maintenance scope, and a reliable newcomer path.

## 12. Grow a repository people choose to star

Stars are an optional expression of interest, not a delivery guarantee or technical quality gate. The practical growth strategy is to solve a recognizable problem, explain it quickly, make evaluation possible, and respond to useful feedback. Avoid purchased engagement, reciprocal-star campaigns, fake performance claims, unsupported competitor comparisons, and keyword-stuffed documentation. Those tactics damage the project’s central promise of verifiable work.

Make the README demonstrate one concrete before-and-after task, then give the shortest honest quick start. Link the live demo only after checking that it is deployed. Show a capability table that distinguishes working features from planned ones. Provide a small architecture explanation and links to deeper documentation. Use badges only for real workflows and published package versions; a badge-shaped image is not evidence of passing checks.

Add a license, contribution guide, security policy, code of conduct, issue forms, pull-request template, changelog, and release process. GitHub’s community profile makes these contribution signals visible, but completing the profile does not promise traffic. Keep issue templates focused on reproduction evidence and user outcomes. Label starter work only when the task has a bounded scope, a maintainer available, and clear acceptance criteria.

Use accurate repository topics such as coding-agent, agent-harness, developer-tools, accessibility, local-first, evaluation, and typescript when they match shipped work. Publish technical walkthroughs explaining actual failures: why a 401 is insufficient to prove a missing header, why regex scoring can reward a fabricated edit, and how coverage validation prevents silent benchmark exclusions. Invite readers to try the reproducible example and contribute a specific improvement. A single optional request to star the repository is reasonable; repeated demands are distracting.

## 13. Search, documentation, and answer-engine clarity

Give public documents stable URLs and meaningful titles. Skills and functions should have distinct explanations, examples, inputs, outputs, limitations, and related links. Generate catalog pages from a single registry so names and descriptions do not drift. Do not publish fifty shallow pages solely to increase URL count. Pages must help a reader accomplish a task or understand a tradeoff.

Use canonical URLs that match the actual deployment, a crawlable sitemap, robots rules, descriptive metadata, and appropriate structured data. The current preview’s component tabs are not separate document routes. Creating a sitemap cannot make those nonexistent routes real. The earlier static toolkit is crawlable after publication, but its default GitHub Pages address is a configuration assumption until deployed. Do not claim indexing or rankings from generated files alone.

Maintain a concise llms.txt summary and machine-readable catalog exports as conveniences, not guaranteed search mechanisms. Include definitions of shape preview, model judge, tool evidence, held release, and protocol identity. Frequently asked questions should answer actual misunderstandings: Does this diagnose ADHD? Does the Bench run models? Can it edit files? Why is the candidate held? Where is data stored? Answers should change when the implementation changes.

Keep provenance near numerical claims. Link a pinned published source for historical results and downloadable evidence for later runs. Explain rounded values rather than adjusting the old delta to fit displayed subtraction. A statement such as “best coding harness” needs a defensible scope and comparison; until there is suitable evidence, use concrete language about the features users can inspect.

## 14. Measure outcomes and decide what to postpone

Track onboarding completion, task completion with evidence, recovery after interruption, misunderstanding of score labels, and time spent resolving avoidable confusion. Separate product analytics from benchmark metrics. A user returning to finish a real task is more informative than a page-view spike. Use voluntary research and privacy-preserving measurement; do not turn the project into a surveillance system.

For engineering, track build reproducibility, failed qualification scenarios, release-blocking defects, protocol-validation failures, and time to reproduce a bug. For community health, track unanswered reproducible reports, first-contribution success, review turnaround, and documentation corrections. Report stars as a community signal, but never optimize them by sacrificing truthful status or stable releases.

Defer gamification, streaks, idle nudges, automatic social posting, broad marketplace features, and multi-agent orchestration until users demonstrate demand. A focus tool can become a source of pressure if it nags people or rewards activity rather than useful outcomes. Preferences should be reversible and optional. The default surface should support a task without asking the user to manage a second system.

The next concrete engineering priority is scorer separation and tests, followed by the first-run journey and a qualified local tool adapter. This order turns the existing preview into an understandable product before expanding its authority. The repository can earn attention by making both its capabilities and limitations unusually easy to verify. That is the strongest foundation for becoming a respected, user-friendly coding-agent harness.

## Source references

These references inform the proposal; they are not evidence that future features have shipped.

- GitHub community profiles: https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories
- GitHub repository topics: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/
- W3C understandable controls: https://www.w3.org/WAI/WCAG2/supplemental/objectives/o1-understandable/
- W3C clear content: https://www.w3.org/WAI/WCAG2/supplemental/objectives/o3-clear-content/
- Historical benchmark source: https://github.com/ayghri/i-have-adhd
