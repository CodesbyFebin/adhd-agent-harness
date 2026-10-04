# Contributing

Start with the source audit and a proposed issue. Keep one change focused and include a reproducible example, appropriate validation, and limitations. Do not alter the historical board, remove failing cases, invent benchmark evidence, or describe heuristics as judges.

Run toolkit tests for toolkit changes. For app changes, first establish a compatible Node and package environment from `app/package.json`; validate type checking and relevant tests before build. Build currently invokes migrations, so isolate it until the portability milestone separates those actions.

Model evaluation changes must pin the full protocol and preserve raw rows. Accessibility contributions should describe observable behavior without requiring disclosure of diagnosis. Avoid posting secrets or private repository content in issues. New skills need triggers, examples, conflict behavior and evaluation status.

Suggested starter work: document storage reset behavior, add a scorer negative-control fixture, or check public documentation links. Discuss broad architecture changes before submitting a large patch. Maintainer review times are not yet an SLA.
