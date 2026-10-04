# Proposed evidence contract

This is a design contract, not an implemented server API.

Each run should record schema_version, run_id, task_id, source_revision, cases_hash, rubric_hash, runner_version, model_id, tool_configuration_hash, skill_hash, trial_count and condition identity. Each event carries sequence, timestamp, kind, correlation_id and payload.

Tool evidence includes executable and argument vector, workspace identity, policy decision, approval binding if required, start/end timestamps, exit status, truncated-output indication, and artifact references. Unknown exit status is null, never zero. Approval references bind to the complete requested operation and expire.

Judge evidence includes case_id, trial, blinded label, original response reference, scores for all five dimensions, blocker finding, judge identity and notes. Keep blinded prompt records separate from the mapping that reveals conditions. Complete paired coverage is required before aggregation.

Exports should contain a schema version, file checksum list, original records, report and verifier. Hashes detect changes but do not prove a trustworthy author. Signing is an optional later protocol with explicit key custody. Validation must reject malformed scores, duplicate rows, missing conditions and protocol mismatches, and preserve failed calls.
