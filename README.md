# ADHD Agent Harness — Skills & Solvers Edition

20 populated agent workflows, 30 runnable Python functions, and 57 static HTML pages. Built for clear coding-agent work with evidence-aware status reports. A writing style does not diagnose ADHD.

## Quick start

Python 3.10+; standard library only. No package install or model key needed.

```bash
python -m unittest discover -s tests -v
python scripts/solve.py error_report < examples/error-report.json
python scripts/build_site.py --base-url https://codesbyfebin.github.io/adhd-agent-harness/
python -m http.server 8000 --directory dist
```

Open http://localhost:8000. The ZIP includes the generated `dist/` site and every source file.

## Contents

- `skills/`: 20 SKILL.md workflows with triggers, bounded instructions, examples, and linked helpers. These are repository artifacts, not installed personal ChatGPT skills.
- `src/solvers.py`: 30 deterministic functions. `data/functions.json` records signatures and populated input/output examples; `examples/` contains CLI-ready JSON.
- `dist/`: Board, Bench, Skills, Functions, Gate, Rules, and 50 detail pages. Mobile layouts, keyboard navigation, semantic HTML, canonical URLs, unique metadata, JSON-LD, sitemap, robots.txt, and llms.txt.
- `evals/`: preserved historical board plus pinned upstream published source and SHA-256 provenance. Original generation and judge rows are not included.
- `tests/`: catalog, links, release negative controls, invalid scores, protocol mismatch, coverage, and output-contract checks.

## Publish and indexing

The default URL is the intended GitHub Pages project address; publication has not been performed. For another host, rebuild using its exact final base URL. Publish the contents of `dist/` as static files. On GitHub Pages configure a deployment workflow or publish those files from a Pages branch. Subpath hosting requires the configured project prefix. For a custom domain place robots.txt at the domain root.

Pages contain their full content without JavaScript; only Bench interaction needs JavaScript. A ZIP is not indexed by itself. Crawling and indexing depend on a public deployment and search engines; no ranking or indexing guarantee is made.

## Frozen published board

Published 2026-08-02: `claude-opus-4-8`, Claude Code 2.1.220, 14 cases × 3 trials. Baseline 4.045; candidate 4.473; published delta +0.427. Blockers 7 → 3. Record: 10 wins, 2 ties, 2 losses. **Candidate held.** Displayed means are rounded; compute deltas from original precision when available.

`agent-owned-edit` required actual tools while the published runner disabled them. Do not drop this case. A tool-enabled fixture is a changed protocol and must be recorded separately. `partial-success` averaged −0.63, with trial deltas +0.05, −0.70, −1.25. Do not assert a missing auth header from a 401 status alone.

[Original source](https://github.com/ayghri/i-have-adhd). `evals/provenance.json` pins the inspected source revision and copied file hashes. Existing board files remain unchanged. New skills are unbenchmarked and do not inherit the historical candidate's score.

## Bench and release semantics

Bench checks first-line presence, recognized preambles, required literal strings, and generic closers. It does not check truth, semantic completeness, refusal correctness, safety, actual edits, or model quality. It makes no network or model calls and does not store drafts. “Your pre-check rank” is shape only.

The release helper requires zero blockers, correctness and safety within 0.1 of baseline or better, and a higher weighted score. It also holds unless evidence completeness and comparability are explicitly supplied as true. Those flags are caller assertions, not proof: first validate full row coverage, scores, protocol identity, and actual evidence. No LLM generation or judge adapter is shipped in this edition.

For new evaluations retain the same 14 cases and exact historical judge rubric, isolate agent settings, blind condition labels, record all protocol identities and run at least three paired trials. Preserve raw outputs, judge rows, failures and costs. Do not retune weights or claim comparable results after changing tools, models or rubric.

MIT. Vendored upstream material retains its own MIT license in `evals/upstream/LICENSE`.
