# Source audit — uploaded preview

Inspected source, not a runtime or dependency-security audit.

| Area | Observed implementation | Next action |
|---|---|---|
| Views | Board, Bench, Gate, Rules, Backlog selected inside `src/components/harness/app.tsx` | Create addressable document routes |
| Historical protocol | Fourteen cases and frozen aggregates in `src/lib/harness/protocol.ts` | Pin provenance and exact rubric |
| Local score | Regex heuristics produce five scores and weighted result in `score.ts` | Rename as heuristic measures and prevent release use |
| Agent-owned edit | Text patterns such as edited/fixed receive favorable autonomy treatment | Require real diff evidence in a separate tool-enabled protocol |
| Safety | Refusal and destructive-command regex matching | Keep advisory; add actual tool policies |
| Persistence | Zustand localStorage key `adhd-agent-harness-v1`, at most eighty filings | Disclose persistence and expose reset/export |
| Presets | Fixture drafts scored using the same local scorer | Label as authored demonstrations |
| Tests | Package test script lists scaffold/auth/app-data tests; no harness-specific test file observed | Add protocol, scorer, store, and UI scenario tests |
| Deployment | Build invokes migration command and platform-specific plugins exist | Separate build from migrations; portability spike |
| Authentication | Scaffold exists; app-env marks auth disabled | Do not describe an authenticated runtime as delivered |
| Python toolkit | Separate source package included under `toolkit/` | Add integration and parity fixtures deliberately |

Important risks: text can claim work without proving it; the word “preview” can affect a destructive-command heuristic; unknown causes require semantic handling beyond a narrow phrase list. Heuristic and judge values must not share a release authority. Pasted data persists locally in the React app, unlike the prior static Bench.

The uploaded archive is preserved under `app/`, including platform scaffolding needed to understand its original environment. It is not a clean portable production template. Do not activate database/auth features merely because helper code exists. No live provider calls, npm install, application build, or browser qualification were run for this planning task.
