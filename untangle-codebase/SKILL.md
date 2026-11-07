---
name: "untangle-codebase"
version: "1.0.0"
description: "Complete a structural refactor of an entire repository or named subsystem. Use when asked to untangle a codebase through investigation, implementation, independent review, and verification; skip isolated fixes and architecture advice."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "structural-refactoring"
---

# Untangle Codebase

Carry a broad structural refactor through to implemented and verified changes. With no narrower target, cover the repository's owned source and relevant tests and configuration. A named subsystem limits the work to that boundary and its affected contracts. Respect explicit review-only instructions.

Example requests: `$untangle-codebase` or `$untangle-codebase the transaction-processing subsystem`.

## Establish scope and evidence

Read local instructions, inspect worktree changes, and identify the existing checks and public entry points. Establish a read-only baseline before changing production paths. Preserve unrelated work; a dirty worktree does not require cleanup. Record existing failures separately from failures introduced by the refactor.

Use available specialist guidance when its decisions arise:

- `code-practice` for structural diagnosis, abstraction quality, and implementation.
- `component-ownership` for collaboration and state ownership changes.
- `runtime-flow-mapping` when execution, sequencing, or failure guarantees need tracing.
- Relevant language, framework, and test skills for their implementation mechanics.

Load only what the task needs. When a specialist is unavailable, continue with the evidence and applicable local conventions; identify consequential gaps.

## Investigate and group the work

Inspect the whole requested boundary sufficiently to identify concrete structural pressures. Record source evidence, affected requirements, and verification for each finding. Group related symptoms under a shared ownership or contract change before planning individual edits.

Keep a compact working plan for the refactor. Prioritize coherent batches without silently reducing a repository-wide request to one convenient module. Planning supports execution and is not an approval gate. Evaluate proposed simplifications against the real contracts, including necessary domain exceptions, compatibility, and recovery.

## Implement and independently review

Implement justified changes through the actual production paths. Preserve intended behavior, public and persisted contracts, transaction boundaries, ordering, cancellation, retry, and recovery guarantees unless the task authorizes changes. Update affected tests and documentation with the implementation.

Use subagents for independent investigation or isolated implementation when useful; give implementation workers distinct file ownership. Obtain an independent review of the resulting diff and affected callers, tests, and failure paths when subagents are available. Ask reviewers to find concrete problems without supplying expected conclusions. Otherwise, review the result explicitly and disclose that review was not independent.

Resolve substantiated findings and rerun affected checks. Continue through the justified work within scope; a findings list, first batch, or launched job alone does not complete an implementation request. Account for remaining findings with concrete evidence of the requirement or external limitation preventing resolution.

## Verify and deliver

Finish when the supported structural causes within scope have been addressed, relevant review findings resolved or accounted for, and applicable verification completed. Use behavior and contract checks; compilation alone does not establish preserved runtime guarantees. Verify disputed boundaries with reachable scenarios and distinguish baseline failures from regressions.

Report the structural changes and why they help, verification actually performed, and material remaining limits. State what remains unverified when dependencies or external systems prevent proof. Keep the completion summary concise; retain detailed working evidence in the repository's scratch location when useful.
