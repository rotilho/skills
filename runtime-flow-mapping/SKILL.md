---
name: "runtime-flow-mapping"
version: "1.0.0"
description: "Trace existing runtime flows across calls, events, queues, callbacks, and persistence. Use to explain, map, or verify an end-to-end code path; skip collaboration redesign and routine edits."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "runtime-analysis"
---

# Runtime Flow Mapping

Reconstruct how a bounded scenario actually runs and produce a source-backed explanation or map. Use it for understanding an existing workflow, investigating ordering, or maintaining runtime documentation. Choosing a new collaboration architecture is a separate task.

## Establish the scenario and evidence

Start from the requested input, visible outcome, or invariant. Identify the relevant entry points and shared state; include alternate entry points only when they affect that scenario. Read local instructions and existing maps for context, then verify their claims against current implementation and configuration.

Inspect the publisher, dispatcher, worker, and transaction implementation that the code actually uses. If a consequential boundary depends on unavailable library, service, or configuration evidence, mark its semantics unresolved. Names and framework defaults are insufficient evidence.

Keep source inspection, observed runtime behavior, inferred behavior, and intended invariants distinct. A diagram alone does not establish production timing or race reachability; support those claims with relevant implementation or runtime evidence.

## Reconstruct the relevant edges

Search definitions and uses with repository tools such as `rg`. Follow exact event/message types, concrete payloads, wrappers, base-type subscriptions, helper methods, and values passed through variables. Find production publishers and matching consumers, then read their bodies and direct callers. Searching only listener annotations misses important paths.

Record the edges that explain the scenario:

| Caller/producer → callee/consumer | Boundary and completion point | Guards, state owner, failure/cleanup | Evidence |
| --- | --- | --- | --- |
| Actual symbols from the implementation | Direct/awaited call, event delivery, queue handoff, callback, or transaction phase | Relevant validation, synchronization, retention, retry, or terminal action | Source path and named method; precise location when useful |

For queued work, trace enqueue, wakeup, drain, retention, and removal separately. For promises, futures, deferreds, or callback registrations, identify who creates, completes, and observes them and what success, failure, and cancellation mean. A lifecycle completion can mean expiry or discarded work rather than successful persistence.

Follow guards and predecessor checks before assuming that an event order can occur. Identify the owner of each state transition and the source of truth for snapshots, caches, and projections. Include feedback from recovery, cleanup, and user-visible completion when it changes the outcome.

## Establish execution and failure guarantees

Derive guarantees from the actual boundary, including:

- Dispatch and waiting: synchronous or asynchronous delivery, awaited work, coroutine/task ownership, locks, ordering, and scheduling. Publisher return, timestamps, registration order, and listener priority do not by themselves establish consumer completion order.
- Transaction phases: when writes occur, when publication/callbacks are registered, when commit becomes known, and which reactions run later. Distinguish local commit from downstream completion and inspect rollback or unknown-completion handling.
- Delivery and recovery: in-process versus durable transport, acknowledgement, redelivery, retry ownership, duplicates, stale snapshots, cancellation, and retained work. A logged listener failure is not automatically retried.

Check only the failure orders relevant to the scenario and supported by the upstream guards. Include alternate ingestion or recovery paths that reach the same state owner, even when they bypass the normal event chain. Stop when the requested invariant, completion, and recovery path are explained; list consequential unresolved edges rather than inventing guarantees.

## Present a map that can be maintained

Choose a small number of representative scenarios. Use a diagram when it clarifies the interaction, with a title/scope, a legend, and labeled arrows that distinguish calls, events, queue/worker handoffs, and callbacks or commit phases. When a worker publishes an event, show or label both the queue/worker handoff and listener dispatch; combining them must not imply a shared execution context. Show branches and loops without implying a global timeline or parallel execution that the source does not establish. Split an unreadable diagram into smaller views.

Pair the diagram with the relevant edge/event index and ownership/failure notes; omit sections that add no information. Link claims to source files and named methods. State the map's scope and omissions, especially if metrics or other listeners are excluded from an index. Distinguish a producer with no current consumer from an omitted consumer.

For durable documentation, update the existing reference that owns the flow and link it from the repository overview. Keep detailed topology in that reference; agent instructions need only the scoped tracing rule and a local link. Keep investigation scratch outside durable docs unless the user requests it. Follow the requested review/edit boundary.

## Verify and deliver

- Cross-check the relevant producers, consumers, direct calls, completion signals, state owners, and failure/cleanup paths against source. Recheck affected files before finalizing when concurrent edits may have changed them.
- Validate source links, section anchors, code fences, and diagram syntax. Render and inspect diagrams when layout matters; syntax success alone does not catch overlaps or unreadable labels.
- Use existing tests or a reachable input/event sequence to check disputed behavior when needed. Run application tests when behavior verification requires them; documentation edits alone do not justify a full build. Report the actual verification scope.
- If implementation changes are also requested, update affected map entries with those changes and verify the changed behavior. Otherwise, deliver the requested explanation, findings, or documentation without expanding into a refactor.

Report the artifact or concise trace, its evidence scope, and any material unknowns. Keep repository-specific names and topology in the resulting map rather than copying them into this reusable skill.
