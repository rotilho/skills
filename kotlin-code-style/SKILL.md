---
name: "kotlin-code-style"
description: "Apply Kotlin-specific code style and design guidance for Kotlin implementation and review: feature-owned file and type organization, helper and extension placement, type design, constructors, nullability, serialization, coroutines, Flow, mutable state ownership, and Kotlin unit/integration test style outside Cucumber or BDD. Use when writing or changing Kotlin code unless Spring application architecture or Cucumber/BDD is the main concern. When this skill loads, also load `code-practice` as the shared engineering base layer."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "engineering"
  style: "concise"
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

Do not use this skill when the request is mainly about framework-neutral engineering defaults, Spring application structure, Spring-managed coroutine or Flow behavior, or Cucumber / BDD test structure.

## Core promise

Produce Kotlin guidance or edits that:
- feel idiomatic without being clever
- keep Kotlin features visible and intentional
- use nullability, coroutines, and serialization deliberately
- keep helper placement and ownership easy to follow
- keep helpers, extensions, models, and coroutine owners near the behavior they support

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
- serialization
- coroutines or Flow
- Kotlin tests

### Step 2 - Apply Kotlin defaults

Prefer these defaults unless local code shows a better house style:
- one main public type per file
- name files after the main owned type or behavior; avoid broad names like `Models.kt`, `Extensions.kt`, `Utils.kt`, `Helpers.kt`, or `Support.kt`
- split multi-type files when types belong to different feature owners or change for different reasons
- keep small related value types together only when they form one concept and are usually read or changed together
- `data class` for small immutable values
- constructors for straightforward creation, factories when creation has rules
- nearby extensions over broad utility files; place them next to the owned feature or type they support
- expression bodies only when the function stays obvious
- direct `if` / `when` and early returns when they make straightforward branches easier to scan
- local `if` / `when` over `?.let`, `also`, or `run` when there is no real scoping or receiver benefit
- scope functions when they improve locality or receiver clarity, not just to avoid writing a simple branch
- nullability as part of the contract
- `suspend` for one-shot async work and `Flow` for streams
- coroutine scopes, channels, mutexes, and background jobs owned by the lifecycle or workflow that starts and stops them
- mutable collections and `MutableStateFlow` hidden behind the narrow Kotlin type that owns their invariants
- local event-fed caches owned by the Kotlin type that makes the synchronous decision; extract shared state only after repetition is real
- sparse comments focused on the why

### Step 3 - Apply the right Kotlin mode

For applications:
- prefer feature-local Kotlin files and packages from the first implementation
- keep core feature logic in ordinary Kotlin types and functions when no framework-managed lifecycle, wiring, or external boundary is involved
- prefer one lifecycle owner for each coroutine scope, channel, mutex, or background worker
- prefer explicit concurrency primitives around shared mutable runtime state
- prefer internal feature-owned models over root-level shared model files
- prefer boundary-specific serialization choices

For libraries:
- prefer tighter public API control
- prefer explicit wire-format and parsing behavior
- prefer predictable failure and round-trip testing for external contracts

### Step 4 - Avoid common Kotlin failure modes

Push back on:
- catch-all extension files
- root-level `Models.kt`, `Extensions.kt`, `Utils.kt`, `Helpers.kt`, or `Support.kt` files that mix feature concepts
- packages split only by type category instead of feature ownership
- top-level functions that hide which feature owns the behavior
- `object` singletons used as dumping grounds for unrelated helpers
- `!!` outside tight invariant boundaries
- scope-function or operator chains that hide straightforward control flow
- Kotlin helper or extension extraction only to reshape one local value for one call site
- Kotlin-local normalization or reshaping chains around simple inputs unless nullability, parsing correctness, or the user request requires them
- nullable chains or expression-body cleverness when explicit branching would be clearer
- hidden background work with unclear scope ownership
- coroutine workers started without a clear owner, shutdown path, and failure boundary
- mutable maps, mutable lists, or `MutableStateFlow` exposed outside their owner

### Step 4a - Kotlin examples for event-owned state

Prefer small local caches when a component needs synchronous validation from events:

```kotlin
private val blockedCustomers = ConcurrentHashMap.newKeySet<CustomerId>()

@EventListener
fun onCustomerBlocked(event: CustomerBlocked) {
    blockedCustomers += event.customerId
}

fun canPlaceOrder(customerId: CustomerId): Boolean =
    customerId !in blockedCustomers
```

Keep execution-safety Flow collection inside the lifecycle owner rather than routing through an app event when directness matters:

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
- generic naming, architecture, or testing defaults: use `code-practice`
- Kotlin Cucumber, feature files, step definitions, or BDD glue design: use `kotlin-cucumber-tests`
- Spring controllers, configuration, transactions, or integration testing: use `spring-application-code-style`

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
- preferred direct control flow over clever chaining where the branch was straightforward
- avoided adding normalization or reshaping code unless correctness or the request justified it
- separated application and library advice when it mattered
- avoided Spring-specific framework guidance
