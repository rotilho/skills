---
name: "code-practice"
version: "1.0.7"
description: "Improve or apply language-agnostic, framework-neutral code practices for clean code, maintainability, refactoring, naming, readability, behavior ownership, evidence-backed diagnosis, trust boundaries, compatibility, state, concurrent collections, compound invariants, locking strategy, error handling, testing, Given/When/Then test structure, and reusable engineering defaults. Use when the user wants broad code quality guidance rather than Kotlin-, Spring-, or framework-specific conventions."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "engineering"
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
- shared state, mutation, concurrent collections, locking strategy, compound invariants, error handling, or testability concerns
- test readability or Given/When/Then structure in code-based tests
- code review focused on reusable engineering defaults rather than language or framework rules
- application vs library tradeoffs without language-specific rules

Do not use this skill when the main question is about component collaboration shape, Kotlin idioms, Spring architecture, Cucumber / BDD structure, or any framework-managed pattern.

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
- the direct evidence for the defect or design pressure, such as a failing test, runtime trace, log line, public contract, or current caller behavior
- whether names expose intent and domain language or hide behind generic placeholders
- which functions or methods mix multiple decisions, levels of abstraction, or deep nesting
- whether duplication is at the token level or the behavior / policy level
- who owns each mutable state change, side effect, and concurrency guard
- which boundaries are public, internal, or external
- which external inputs, generated outputs, remote responses, or persisted values cross a trust boundary
- whether a proposed file, module, or package would become a mixed-concern bucket
- whether a new abstraction owns a real decision or only forwards calls
- where errors are created, translated, logged, or retried
- which production caller, lifecycle, input, or dependency can actually trigger each proposed failure path
- whether tests cover the defect or contract at the same level where it failed

Keep the diagnosis gap-first: strengthen the weakest high-impact area first instead of rewriting everything.

### Step 3 - Apply the base defaults

Prefer these defaults unless local evidence strongly disagrees:
- place new code with the smallest behavior owner instead of a generic technical bucket
- choose feature-, workflow-, or concept-owned homes before technical layer homes
- name things by responsibility and observable intent
- prefer domain words over vague helpers like `util`, `manager`, `processor`, or `misc`
- choose names that describe owned behavior, not implementation type
- name booleans and predicates so true and false read naturally
- keep commands and queries distinct when mixing them would hide side effects
- keep public APIs small and explicit
- preserve public contracts by default; when changing one, add migration, adapter, or compatibility coverage unless a breaking change is intentional
- keep functions small enough to hold in one pass; split when a unit mixes multiple decisions or needs section comments to stay readable
- keep an operation and the state transition that must always follow it in one cohesive method; split them only when either has a valid independent use or the separation exposes a real policy boundary
- keep a repeated compound state transition together at the smallest shared scope; extract a helper when it makes the invariant clearer
- prefer flat control flow; handle exceptional branches early when that makes the main path clearer
- keep parameter lists short; group cohesive data, but do not hide unrelated inputs in grab-bag objects
- keep each unit responsible for one kind of decision
- keep integration concerns at the edges
- keep mutable state local to the workflow that mutates it
- guard shared mutable state explicitly, close to its owner, and make the guard visible in tests when concurrency matters
- keep related policies, state owners, adapters, and tests near the owning behavior unless they are shared contracts
- avoid root-level behavior files when a feature- or workflow-owned home exists
- make concurrency and retries explicit
- verify external outputs locally when correctness, security, or compatibility depends on them
- translate untrusted or remote data into trusted domain values at the boundary
- distinguish expected rejection from system failure
- keep error translation near the boundary that changes context
- remove duplication at the level of behavior or policy, not just repeated tokens
- favor simple data flow over implicit shared state
- use already-available values directly when cleanup, reshaping, or normalization has no correctness or readability payoff
- normalize external input at the boundary that accepts it; do not normalize domain values in the middle of behavior owners
- test behavior and boundaries, not only construction
- test at the same level as the defect or contract: unit for local rules, integration for boundary wiring, end-to-end for workflow behavior
- structure every new or changed code-based test with explicit Given, When, and Then sections, using the host language's ordinary comment syntax; do not rewrite untouched tests solely to add the markers
- avoid proof-by-build when a focused test or assertion can prove the changed contract directly
- make tests readable enough to explain the scenario, action, and expected outcome without extra narration

### Step 3a - Protect compound state as one invariant

Before choosing a lock, mutex, actor, or concurrent container:
- define the whole invariant and every collection, nested mutable value, counter, limit, and check-and-act transition it couples
- rely on concurrent collections alone only when correctness consists of independent per-entry atomic operations
- use one invariant-owned guard for transitions spanning collections, nested mutable values, counters, or check-and-act limits
- prefer plain collections when every access shares that guard; combining a concurrent collection with a broad lock needs a documented independent access path that benefits from per-entry concurrency
- name the guard for the state or invariant it owns, and comment its complete ownership when the boundary is not obvious
- decide and mutate under the guard; move avoidable logging, events, callbacks, and I/O outside it only when required ordering and failure behavior are preserved
- preserve required fairness and reentrancy behavior when changing concurrency mechanisms
- test the relevant invariant under contention and propagate worker failures to the test

### Step 3b - Require evidence before defensive behavior

Before adding a retry, fallback, guard, recovery branch, or failure test:
- identify the exact production caller, input, dependency, scheduler, or lifecycle event that can trigger it
- establish reachability from production callers or the boundary and lifecycle contract; a test-created state alone does not justify new recovery behavior
- distinguish untrusted boundaries from closed-world internals; validate public, persisted, serialized, remote, and user-controlled values, but trust internal values whose owners already enforce the invariant
- check whether an existing owner already provides recovery through restart, expiration, reconciliation, idempotency, or rediscovery
- weigh the actual consequence and frequency against the permanent branch, state, API, and test complexity
- do not let a test manufacture an otherwise unreachable failure and then use that test as the reason production code must handle it

If the trigger cannot be named or demonstrated, omit the behavior. Record the assumption only when it is important and inexpensive to revisit.

### Step 4 - Apply the right mode

For applications:
- prefer feature- or workflow-local organization
- prefer thin external edges and clear orchestration ownership
- prefer operationally useful logging and integration coverage at real boundaries
- prove fixes through the observable workflow, not just through the helper that was edited

For libraries:
- prefer stable, explicit contracts
- prefer wire and serialization behavior that is easy to audit
- prefer minimal surface area and predictable failure modes
- treat compatibility, round trips, and rejected inputs as first-class tests

### Step 5 - Use actionable review heuristics

Push toward changes that:
- reduce the number of places a behavior must be understood or edited
- move behavior to the owner that can see the state transition or side effect directly
- make control flow, side effects, and failure paths easier to trace
- make the happy path and edge cases visually easy to separate
- replace placeholder names with names that tell the reader what decision, data, or side effect matters
- extract units at natural seams, but stop before the code becomes a maze of trivial forwarding helpers
- avoid extracting helpers only to reshape one local value for one call site
- move policy decisions closer to their owner and incidental mechanics closer to the edge
- replace broad indirection with direct code when the abstraction adds no leverage
- keep comments for intent, invariants, or non-obvious tradeoffs, not narration
- replace theories with direct checks before mutating production paths
- keep a read-only baseline for debugging or operational work, then verify the same signal after the change

### Step 6 - Guard against bad abstraction

Push back on:
- generic names that hide real intent or domain meaning
- boolean flags or mode parameters when separate entry points would make the caller clearer
- deep nesting when guard clauses, extraction, or data reshaping would flatten the flow
- duplicated branches that should share one policy, while avoiding abstraction over coincidence
- methods that only forward arguments and return the same result without owning a decision, invariant, translation, or meaningful deduplication
- utility buckets with mixed concerns
- local normalization or reshaping logic for simple inputs unless correctness, an external contract, or the request requires it
- abstractions added only for symmetry, testing ceremony, or speculative reuse
- method pairs such as `run()` then `record()` when every caller must invoke both and neither has a valid independent lifecycle
- shared mutable state without a clear owner
- state mutated in one workflow but guarded, refreshed, or invalidated by unrelated callers
- accepting generated, serialized, remote, or user-provided data without a boundary check when the next step relies on it
- error handling that mixes recovery, translation, and logging in every layer
- wide interfaces that bundle unrelated capabilities
- tests that only prove the project builds while the failing behavior or public contract remains untested

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
- diagnosed with direct evidence before fixing when the request was a defect or operational issue
- tied every new retry, fallback, guard, and failure test to a reachable production trigger or external trust boundary
- kept public surface and compatibility impact explicit
- tested at the level of the changed behavior or contract
- kept new or changed code-based tests visibly separated into Given, When, and Then sections
- protected compound state at the invariant boundary and kept avoidable side effects outside its guard
- avoided speculative abstraction
- did not duplicate Kotlin or Spring-specific guidance
