# Thirty proposed implementation issues

These drafts have not been posted to GitHub.

## AH-001: Separate heuristic and judge types

Priority: P0. Milestone: M1. Status: proposed.

Acceptance: Heuristic records cannot enter release evaluation; UI labels identify their origin.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-002: Freeze provenance identities

Priority: P0. Milestone: M1. Status: proposed.

Acceptance: Cases, rubric, runner, model, tools and skill hashes recorded; mutations invalidate comparison.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-003: Add scorer adversarial tests

Priority: P0. Milestone: M1. Status: proposed.

Acceptance: Fabricated edit and unsafe text containing preview do not produce a safety clearance.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-004: Add protocol arithmetic tests

Priority: P0. Milestone: M1. Status: proposed.

Acceptance: Fourteen unique IDs, historical aggregates and rounded deltas stay consistent.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-005: Audit build portability

Priority: P0. Milestone: M1. Status: proposed.

Acceptance: Build and migration are separate; required platform environment documented.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-006: Document browser persistence

Priority: P1. Milestone: M1. Status: proposed.

Acceptance: Filings notice, export and reset behavior match actual storage.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-007: Add route-addressable docs

Priority: P1. Milestone: M2. Status: proposed.

Acceptance: Each public view has a real route and server-readable content.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-008: Create first-run example

Priority: P1. Milestone: M2. Status: proposed.

Acceptance: New user distinguishes shape preview from judged benchmark.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-009: Add keyboard journey tests

Priority: P1. Milestone: M2. Status: proposed.

Acceptance: Example, editing, filing, export and reset work without pointer input.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-010: Validate imports

Priority: P1. Milestone: M2. Status: proposed.

Acceptance: Malformed, oversized and incompatible input is rejected without data loss.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-011: Create skill registry

Priority: P1. Milestone: M2. Status: proposed.

Acceptance: Twenty entries have version, source, trigger and explicit evaluation status.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-012: Create function parity fixtures

Priority: P1. Milestone: M2. Status: proposed.

Acceptance: Thirty helper examples retain behavior across chosen language implementations.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-013: Implement workspace path boundary

Priority: P0. Milestone: M3. Status: proposed.

Acceptance: Traversal, symlinks and external roots are rejected in hostile fixtures.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-014: Implement command gateway

Priority: P0. Milestone: M3. Status: proposed.

Acceptance: Arguments, timeout, output cap, environment and cancellation are controlled.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-015: Bind approvals to operations

Priority: P0. Milestone: M3. Status: proposed.

Acceptance: Changed command or target cannot reuse an approval.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-016: Build real-edit fixture

Priority: P0. Milestone: M3. Status: proposed.

Acceptance: Exact README typo changed; diff and verification captured with actual tools.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-017: Implement task state machine

Priority: P1. Milestone: M3. Status: proposed.

Acceptance: Illegal transitions rejected; textual completion alone cannot finish a task.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-018: Write event journal

Priority: P1. Milestone: M3. Status: proposed.

Acceptance: Ordered events survive restart; evidence gaps remain explicit.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-019: Capture verification evidence

Priority: P1. Milestone: M3. Status: proposed.

Acceptance: Command and exit code recorded; unknown checks never become passes.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-020: Validate complete evaluation coverage

Priority: P0. Milestone: M4. Status: proposed.

Acceptance: Missing conditions, duplicates and invalid trial keys prevent ranking.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-021: Implement resumable generation

Priority: P1. Milestone: M4. Status: proposed.

Acceptance: Retries preserve failures and cannot silently replace recorded outputs.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-022: Implement blind judge mapping

Priority: P1. Milestone: M4. Status: proposed.

Acceptance: Condition names hidden; label mapping reproducible and kept out of judge prompt.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-023: Publish cost and coverage report

Priority: P1. Milestone: M4. Status: proposed.

Acceptance: Unknown costs remain null; protocol scope stated with every report.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-024: Export reproducible evidence bundle

Priority: P1. Milestone: M4. Status: proposed.

Acceptance: Independent verifier recomputes aggregate from original rows.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-025: Add second qualified runner

Priority: P2. Milestone: M5. Status: proposed.

Acceptance: Same contract fixtures pass; unsupported capabilities shown.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-026: Prototype editor integration

Priority: P2. Milestone: M5. Status: proposed.

Acceptance: Scoped task and diff flow works without granting unrestricted authority.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-027: Test interruption recovery

Priority: P1. Milestone: M5. Status: proposed.

Acceptance: Resume reconstructs recorded state and requires revalidation before mutation.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-028: Run accessibility review

Priority: P1. Milestone: M5. Status: proposed.

Acceptance: Keyboard, zoom, contrast and screen-reader results documented with limitations.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-029: Publish contribution journey

Priority: P1. Milestone: M5. Status: proposed.

Acceptance: Starter tasks have owner, acceptance criteria and reproducible setup.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.

## AH-030: Publish honest release demo

Priority: P2. Milestone: M5. Status: proposed.

Acceptance: Actual diff, failure, recovery and evidence shown; no unsupported best-in-class claim.

Evidence: attach reproducible commands, fixtures or user-test observations appropriate to this change. Preserve failures and identify limitations.