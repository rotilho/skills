---
name: "code-practice"
description: "Improve or apply language-agnostic, framework-neutral code practices for clean code, maintainability, refactoring, naming, readability, ownership, boundaries, state, error handling, testing, and reusable engineering defaults. Use when the user wants broad code quality guidance rather than Kotlin-, Spring-, or framework-specific conventions."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "engineering"
  style: "concise"
---

# Code Practice

Use this skill for cross-language engineering defaults in guidance, review, and implementation.

## When to use

Trigger for work like:
- clean code or maintainability guidance
- refactoring for readability, ownership, or cohesion
- general code style or coding conventions
- naming, function shape, duplication, or complexity reduction
- API shape, module boundaries, and responsibility splits
- state, mutation, concurrency, error handling, or testability concerns
- code review focused on reusable engineering defaults rather than language or framework rules
- application vs library tradeoffs without language-specific rules

Do not use this skill when the main question is about component collaboration shape, Kotlin idioms, Spring architecture, Cucumber / BDD structure, or any framework-managed pattern.

## Core promise

Produce guidance or edits that:
- keep behavior explicit
- keep ownership clear
- place new code at the smallest behavior owner from the first edit
- keep mutation narrow
- make boundaries visible
- keep tradeoffs visible
- avoid abstraction without payoff
- prevent blob files, dumping-ground modules, and generic layers before they appear
- place code files by feature or workflow ownership from the first edit

## Hard constraints

- treat this as the base layer
- keep advice language-agnostic and framework-neutral unless the user only needs generic principles applied to a specific snippet
- do not prescribe Kotlin, Spring, ORM, HTTP-framework, or build-tool-specific rules
- do not drift into architecture-by-template; stay at the level of reusable engineering defaults
- if the user clearly needs Kotlin, Spring, or Cucumber conventions, hand off to the more specific skill
- separate application and library advice when that changes the recommendation

## Workflow

### Step 1 - Classify the request and boundary

Decide whether the request is mainly about:
- naming and readability
- function shape and local complexity
- duplication and extraction
- API shape and boundaries
- state, mutation, or concurrency
- error handling or logging
- tests or change safety
- abstraction, cohesion, or ownership

Also classify the target as:
- application
- library
- mixed or unclear

If the main answer depends on language, framework, or platform rules, hand off instead of stretching this skill.

### Step 2 - Inventory the current shape first

Before prescribing changes, identify what already exists:
- where behavior starts and ends
- which feature, workflow, or concept owns the behavior being added or changed
- whether names expose intent and domain language or hide behind generic placeholders
- which functions or methods mix multiple decisions, levels of abstraction, or deep nesting
- whether duplication is at the token level or the behavior / policy level
- who owns each mutable state change or side effect
- which boundaries are public, internal, or external
- whether a proposed file, module, or package would become a mixed-concern bucket
- whether a new abstraction owns a real decision or only forwards calls
- where errors are created, translated, logged, or retried
- whether tests cover behavior, boundaries, and failure modes

Keep the diagnosis gap-first: strengthen the weakest high-impact area first instead of rewriting everything.

### Step 3 - Apply the base defaults

Prefer these defaults unless local evidence strongly disagrees:
- place new code with the smallest behavior owner instead of a generic technical bucket
- name things by responsibility and observable intent
- prefer domain words over vague helpers like `util`, `manager`, `processor`, or `misc`
- choose names that describe owned behavior, not implementation type
- name booleans and predicates so true and false read naturally
- keep commands and queries distinct when mixing them would hide side effects
- keep public APIs small and explicit
- keep functions small enough to hold in one pass; split when a unit mixes multiple decisions or needs section comments to stay readable
- prefer flat control flow; handle exceptional branches early when that makes the main path clearer
- keep parameter lists short; group cohesive data, but do not hide unrelated inputs in grab-bag objects
- keep each unit responsible for one kind of decision
- keep integration concerns at the edges
- keep mutable state local to its owner
- keep related policies, state owners, adapters, and tests near the owning behavior unless they are shared contracts
- avoid root-level behavior files when a feature- or workflow-owned home exists
- make concurrency and retries explicit
- distinguish expected rejection from system failure
- keep error translation near the boundary that changes context
- remove duplication at the level of behavior or policy, not just repeated tokens
- favor simple data flow over implicit shared state
- use already-available values directly when cleanup, reshaping, or normalization has no correctness or readability payoff
- normalize external input at the boundary that accepts it; do not normalize domain values in the middle of behavior owners
- test behavior and boundaries, not only construction
- make tests readable enough to explain the scenario, action, and expected outcome without extra narration

### Step 4 - Apply the right mode

For applications:
- prefer feature- or workflow-local organization
- prefer thin external edges and clear orchestration ownership
- prefer operationally useful logging and integration coverage at real boundaries

For libraries:
- prefer stable, explicit contracts
- prefer wire and serialization behavior that is easy to audit
- prefer minimal surface area and predictable failure modes

### Step 5 - Use actionable review heuristics

Push toward changes that:
- reduce the number of places a behavior must be understood or edited
- make control flow, side effects, and failure paths easier to trace
- make the happy path and edge cases visually easy to separate
- replace placeholder names with names that tell the reader what decision, data, or side effect matters
- extract units at natural seams, but stop before the code becomes a maze of trivial forwarding helpers
- avoid extracting helpers only to reshape one local value for one call site
- move policy decisions closer to their owner and incidental mechanics closer to the edge
- replace broad indirection with direct code when the abstraction adds no leverage
- keep comments for intent, invariants, or non-obvious tradeoffs, not narration

### Step 6 - Guard against bad abstraction

Push back on:
- generic names that hide real intent or domain meaning
- boolean flags or mode parameters when separate entry points would make the caller clearer
- deep nesting when guard clauses, extraction, or data reshaping would flatten the flow
- duplicated branches that should share one policy, while avoiding abstraction over coincidence
- service layers that only forward calls
- proxy methods added only to preserve layering symmetry
- methods that only forward arguments and return the same result without owning a decision, invariant, translation, or meaningful deduplication
- utility buckets with mixed concerns
- local normalization or reshaping logic for simple inputs unless correctness, an external contract, or the request requires it
- abstractions added only for symmetry, testing ceremony, or speculative reuse
- shared mutable state without a clear owner
- error handling that mixes recovery, translation, and logging in every layer
- wide interfaces that bundle unrelated capabilities

### Step 6a - Apply event-owned refactoring when current code is coupled

When refactoring event- or command-heavy application code, prefer these moves:

- find the owner from the state transition or side effect, not from the current caller
- delete forwarding layers instead of renaming or polishing them
- publish facts that real consumers need; avoid micro-events for internal steps
- let consumers keep local event-fed caches for synchronous decisions
- keep execution-safety side effects close to the execution boundary
- replace registries with facts when one validator is the real consumer
- make expected rejection a domain outcome, not an exception caught by a generic wrapper

If the main decision is whether components should use direct calls, orchestration, events, projections, observers, or local state ownership, use `component-collaboration-architecture` instead of stretching this base skill.

Examples:

```kotlin
// Bad: forwarding layer owns no decision.
fun onRefund(command: RefundOrder) = billing.refund(command.orderId)

// Better: real owner consumes the fact/command and publishes a domain fact.
fun onRefund(command: RefundOrder) {
    refunds[command.orderId] = RefundStatus.APPROVED
    publish(OrderRefunded(command.orderId))
}
```

```kotlin
// Bad: shared registry only feeds one validator.
validator.validate(order, customerRegistry.customers())

// Better: validator keeps the local cache it needs.
fun onCustomerBlocked(event: CustomerBlocked) {
    blockedCustomers += event.customerId
}
```

### Step 7 - Explain tradeoffs briefly

When recommending a pattern, state:
- why it helps here
- what it costs
- what would justify breaking the default

### Step 8 - Keep overlap boundaries clear

If the issue is:
- direct calls vs events, listener/proxy chains, projections, or cross-component state ownership: use `component-collaboration-architecture`
- Kotlin file layout, type design, nullability, or coroutine idioms: use `kotlin-code-style`
- Spring controllers, transactions, bean wiring, or application structure: use `spring-application-code-style`
- Cucumber features, step definitions, hooks, or BDD test structure: use `kotlin-cucumber-tests`

## Canonical references

- OpenCode agent skill format: https://opencode.ai/docs/skills/
- Clean Code principles are contextual; prefer this skill's ownership and boundary rules over language-specific style-guide details when no more specific skill applies.

## Verification checklist

Before finishing, confirm that you:
- kept the guidance framework-agnostic
- kept the guidance language-agnostic
- separated application and library advice when needed
- improved naming, local readability, or complexity when those were part of the problem
- made ownership and boundaries clearer
- improved change safety, state boundaries, or error handling where relevant
- avoided speculative abstraction
- did not duplicate Kotlin or Spring-specific guidance
