---
name: "kotlin-code-style"
version: "1.0.3"
description: "Apply Kotlin-specific code style and design guidance for Kotlin implementation and review: feature-owned file and type organization, helper and extension placement, constructors, validation shape, nullability, serialization, multiplatform expect/actual source sets, coroutines, Flow, mutable state ownership, Kotlin unit/integration test style, and Gradle formatting or focused verification outside Cucumber or BDD. Use when writing, formatting, testing, or changing Kotlin code unless Spring application architecture or Cucumber/BDD is the main concern. When this skill loads, also load `code-practice` as the shared engineering base layer."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "engineering"
---

# Kotlin Code Style

Use this skill for Kotlin-specific guidance.

## Required companion skill

Immediately load `code-practice` after loading this skill.

Use `code-practice` for shared naming, ownership, boundaries, state, error handling, testing, and abstraction defaults. Then use this skill to refine or override those defaults only where Kotlin-specific language behavior, idioms, or tooling changes the recommendation.

## When to use

Trigger for work like:
- Kotlin code style
- idiomatic Kotlin
- Kotlin backend conventions
- coroutine and Flow usage
- Kotlin file and type organization
- Kotlin unit or integration test style outside Cucumber / BDD
- Kotlin formatting or focused Gradle verification

Do not use this skill when the request is mainly about framework-neutral engineering defaults, Spring application structure, Spring-managed coroutine or Flow behavior, or Cucumber / BDD test structure.

## Hard constraints

- load and treat `code-practice` guidance as the base layer
- add Kotlin-specific refinements instead of restating generic rules
- do not expand into Spring Boot, controller, transaction, or bean-wiring guidance
- separate application and library Kotlin advice when the distinction changes the answer

## Workflow

### Step 1 - Identify the Kotlin-specific decision

Focus on the main Kotlin concern:
- file organization
- type design
- constructors or factories
- extensions or helper placement
- nullability and validation
- multiplatform source-set boundaries
- serialization
- coroutines or Flow
- Kotlin tests

### Step 2 - Apply Kotlin defaults

Prefer these defaults unless local code shows a better house style:
- one main public type per file
- name files after the main owned type, feature concept, or behavior; avoid broad names like `Models.kt`, `Extensions.kt`, `Utils.kt`, `Helpers.kt`, or `Support.kt`
- place files by feature or concept ownership before grouping by utility, DTO, enum, or extension type
- split multi-type files when types belong to different feature owners or change for different reasons
- keep small related value types together only when they form one concept and are usually read or changed together
- prefer compact immutable value types for domain values; use `data class` when structural equality and copying are part of the intended contract
- constructors for straightforward creation, factories when creation has rules
- keep factories close to the type when they enforce construction rules, parse external data, or hide platform-specific setup
- nearby extensions over broad utility files; place them next to the owned feature or type they support
- expression bodies only when the function stays obvious
- direct `if` / `when` and early returns when they make straightforward branches easier to scan
- local `if` / `when` over `?.let`, `also`, or `run` when there is no real scoping or receiver benefit
- scope functions when they improve locality or receiver clarity, not just to avoid writing a simple branch
- nullability as part of the contract
- use structured validation results when callers need error detail, rejected-field detail, or recovery choices
- keep `isValid()` as a convenience wrapper over structured validation when both detailed and boolean checks are useful
- use `expect` / `actual` declarations or platform source sets for platform behavior instead of runtime conditionals in common code
- `suspend` for one-shot async work and `Flow` for streams
- coroutine scopes, channels, mutexes, and background jobs owned by the lifecycle or workflow that starts and stops them
- make `Mutex`, coroutine scope, channel, and `Flow` collection ownership explicit in the owning type; do not hide it in a helper with no lifecycle
- mutable collections and `MutableStateFlow` hidden behind the narrow Kotlin type that owns their invariants
- sparse comments focused on the why

### Step 3 - Apply the right Kotlin mode

For applications:
- prefer feature-local Kotlin files and packages from the first implementation
- keep protocol DTOs, local models, and feature state under the workflow or feature that owns their behavior unless they are shared contracts
- keep core feature logic in ordinary Kotlin types and functions when no framework-managed lifecycle, wiring, or external boundary is involved
- prefer one lifecycle owner for each coroutine scope, channel, mutex, or background worker
- prefer explicit concurrency primitives around shared mutable runtime state
- prefer internal feature-owned models over root-level shared model files
- prefer boundary-specific serialization choices

For libraries:
- prefer tighter public API control
- prefer explicit wire-format and parsing behavior
- prefer predictable failure, structured validation, and round-trip testing for external contracts
- keep platform-specific implementations behind `expect` / `actual`, source sets, or injected platform adapters

### Step 4 - Avoid common Kotlin failure modes

Push back on:
- catch-all extension files
- root-level `Models.kt`, `Extensions.kt`, `Utils.kt`, `Helpers.kt`, or `Support.kt` files that mix feature concepts
- packages split only by type category instead of feature ownership
- common-source runtime conditionals that should be platform source-set implementations
- top-level functions that hide which feature owns the behavior
- `object` singletons used as dumping grounds for unrelated helpers
- `!!` outside tight invariant boundaries
- scope-function or operator chains that hide straightforward control flow
- Kotlin helper or extension extraction only to reshape one local value for one call site
- Kotlin-local normalization or reshaping chains around simple inputs unless nullability, parsing correctness, or the user request requires them
- nullable chains or expression-body cleverness when explicit branching would be clearer
- hidden background work with unclear scope ownership
- coroutine workers started without a clear owner, shutdown path, and failure boundary
- `Mutex` or `MutableStateFlow` ownership that cannot be traced to one workflow or lifecycle
- mutable maps, mutable lists, or `MutableStateFlow` exposed outside their owner

### Step 4a - Keep Flow collection with its lifecycle owner

Collect state in the lifecycle scope that owns the work:

```kotlin
fun start(scope: CoroutineScope) {
    scope.launch {
        printer.connectionState.collect { state ->
            if (state == PrinterState.CONNECTED) flushQueuedJobs()
        }
    }
}
```

### Step 5 - Keep overlap boundaries clear

If the issue is:
- direct calls, events, projections, or ownership across components: use `component-collaboration-architecture`
- generic naming, architecture, or testing defaults: use `code-practice`
- Kotlin Cucumber, feature files, step definitions, or BDD glue design: use `kotlin-cucumber-tests`
- Spring controllers, configuration, transactions, or integration testing: use `spring-application-code-style`

### Step 6 - Shape Kotlin tests around behavior

Prefer behavior-named tests that cover:
- positive examples that prove the intended path
- negative examples that prove expected rejection
- round-trip examples for serialization, parsing, and wire contracts
- boundary examples for minimum, maximum, empty, malformed, or platform-specific values

Use lower-level Kotlin tests for dense rule matrices, serializers, validators, and value types. Use broader integration or workflow tests only when the behavior depends on real wiring, external contracts, or coroutine scheduling.

### Step 7 - Format and verify Kotlin changes

When Kotlin code or tests change:
- inspect the repository's build tasks and local verification conventions first
- when the repository uses ktlint and exposes `ktlintFormat`, run it to apply formatting; `ktlintCheck` reports violations but does not replace the formatting step
- when the default Gradle home is not writable, use an existing writable Gradle home or set `GRADLE_USER_HOME` to a writable temporary directory
- format before verification, then run the most focused relevant test task or test filter
- expand to broader verification only when the change or repository contract requires it

## Canonical references

- Kotlin coding conventions: https://kotlinlang.org/docs/coding-conventions.html
- Kotlin coroutines: https://kotlinlang.org/docs/coroutines-overview.html
- Kotlin Flow: https://kotlinlang.org/docs/flow.html

## Verification checklist

Before finishing, confirm that you:
- added Kotlin-specific guidance rather than generic restatement
- kept helper placement and ownership clear
- treated nullability and async behavior explicitly
- kept coroutine and mutable-state ownership narrow
- kept platform differences out of common runtime conditionals when source sets fit
- used structured validation where callers need error detail
- selected test level and case shape for the Kotlin behavior being changed
- applied the repository's Kotlin formatter before running focused verification
- used a writable Gradle home when the execution environment required one
- preferred direct control flow over clever chaining where the branch was straightforward
- avoided adding normalization or reshaping code unless correctness or the request justified it
- separated application and library advice when it mattered
- avoided Spring-specific framework guidance
