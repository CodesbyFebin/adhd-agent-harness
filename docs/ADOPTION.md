# What was adopted from the planning package

Source: ADHD Agent Harness Master Blueprint, planning edition 1.0, 4 October 2026.

Adopted: `docs/MASTER_BLUEPRINT.md` (and the HTML copy), the source audit, evidence contract, growth plan, release checklist, three architecture notes, `ROADMAP.md`, `planning/`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, and the issue and pull-request templates.

Not copied:

- `app/` — the live preview is already this product. The archive also bundled platform caches and a production build. Those are not source.
- `toolkit/` — this repository is that toolkit at the root. Replacing it would drop the evidence-row work on `evidence-row-split`.
- `tools/validate_package.py` — it checks a manifest of the whole archive, including files this repo does not contain.

The thirty issues in `planning/ISSUES.md` are drafts. They have not been opened on GitHub. No milestone clears the historical hold: weighted 4.473, three blockers, evidence still incomplete.

Private vulnerability reporting is not enabled yet. Do not describe the security file as a working disclosure program until the Security tab is turned on.
