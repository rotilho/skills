---
name: "component-ownership"
version: "1.3.0"
description: "Design or refactor component collaboration and state ownership. Use for direct calls versus events, forwarding chains, dependency cycles, projections, or cross-component invariants; skip ordinary style and framework wiring."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "architecture"
---

# Component Ownership

Decide how the affected components should collaborate and where their behavior, data, and failure responsibility belong. Scope analysis and changes to the requested boundary; an architecture question can end with a reasoned recommendation without refactoring code.

Use `code-practice` for local readability and abstraction quality, and Kotlin, Spring, or Cucumber skills for their language or framework mechanics. Resolve the collaboration decision here, then continue the authorized task with any relevant specialist guidance.

## Identify owners and requirements

Trace the initiating request, timer, message, or input through the affected workflow. Identify who can accept or reject the action, who holds the deciding state, who protects its invariant, and who owns side effects and recovery. The current caller is not necessarily the owner.

For links that matter to the decision, establish whether they request work, query current state, or report a completed fact. Check the need for an immediate result, sequencing, transaction coupling, independent reactions, and freshness. Include downstream consumers only as far as these requirements or the proposed change affect them.

For affected data, make the source of truth, writer, readers, projection owners, and contract boundary clear. Keep mutation with one owner; multiple writers need an explicit coordination protocol. Define rebuild or reconciliation behavior when derived state or recovery is part of the task.

## Choose the collaboration shape

| Shape | Use when |
| --- | --- |
| Direct call | Validation, sequencing, return values, failure propagation, or transaction-coupled work must stay synchronous; the callee is a required participant. |
| Orchestrator | Several participants are required, no participant owns the whole process, and the workflow owns real ordering, progress, compensation, or retry state. |
| Event or observer reaction | An owner has completed a fact, consumers can react independently, and the consistency and failure contract permits the chosen delivery model. The publisher should not need to know each consumer. |
| Projection or event-fed cache | A downstream owner needs local reads of another owner's facts, can tolerate the resulting staleness, and has a suitable rebuild/update contract. |
| Query | A component needs current information from its owner without requesting mutation; stale derived state would be unsafe or misleading. |
| Adapter | A protocol, transport, storage, vendor, process, or authorization boundary needs translation or normalization. |

Keep requests as commands, calls, jobs, or workflow steps. Events describe completed facts such as `PrimaryDocumentChanged`; a name such as `CleanSearchIndexRequested` disguises a command. Do not split required synchronous work into events just because several collaborators are involved.

## Change only collaboration that causes the problem

When several forwarding paths, caller-specific branches, or workarounds reflect the same missing responsibility, evaluate one ownership or contract change that addresses them together. For a dependency cycle, identify the required behavior behind each edge; hiding an edge in global state, service lookup, or an event does not resolve its ownership or sequencing obligations.

- Collapse pass-through listener, handler, or proxy chains when they own no translation, protocol adaptation, authorization, retry, lifecycle, observability, or meaningful deduplication.
- Move decisions and state out of generic coordinators or registries into their behavior owner. Keep an orchestrator when the workflow itself has an independent responsibility.
- Replace micro-events for internal steps with private calls, and event-as-command flows with explicit requested work.
- When a source-of-truth owner depends on independent downstream cleanup, indexing, notification, or cache maintenance, consider completed-fact publication with a behavior-owned consumer. Apply the consistency and failure criteria above first; required synchronous or transaction-coupled work stays direct.
- Name remaining abstractions by their owned decision, state, or side effect. Do not introduce eventing or indirection merely for style.

Read [the examples](references/examples.md) only when a concrete comparison would help: required fan-out, independent downstream cleanup, pass-through listeners, or a validator-local cache. The sketches do not replace the real workflow's transaction and failure requirements.

## Preserve failure behavior and verify the result

For changed collaboration, assess the failures its actual contract allows: duplicates, reordering, partial completion, retries, and stale state. Preserve or define needed idempotency, transaction boundaries, compensation, abort, reconciliation, and observability. Expected rejection is a domain result; recovery, resync, and external-state adoption are explicit behaviors. Added eventing must make the failure model clear.

When implementing a behavior change, select tests that prove the affected ownership and consistency contract: rejection before side effects, required synchronous work, publication after the fact is true, an independent consumer's reaction, or projection updates/rebuilds. Exercise duplicate, stale, and recovery paths when reachable and relevant. Do not expand a review-only task into implementation or add tests for unrelated mechanisms.

Explain the chosen owner and collaboration shape, the material tradeoff, and any verification limit. For implementation requests, finish the requested change and relevant verification without treating skill routing or the first draft as a review gate.
