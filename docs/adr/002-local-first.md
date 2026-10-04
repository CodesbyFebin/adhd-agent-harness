# Start with local-first execution

Status: proposed for maintainer adoption.

## Decision

Deliver one scoped local workspace before hosted multi-user execution. UI requests pass through policy and tool gateways; model output cannot execute shell commands directly.

## Consequences

More explicit metadata and validation are required. Existing previews remain usable but cannot claim qualified execution or benchmark equivalence. Acceptance evidence must accompany implementation.
