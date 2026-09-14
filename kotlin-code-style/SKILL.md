---
name: "kotlin-code-style"
version: "1.1.0"
description: "Apply Kotlin style, type, coroutine, multiplatform, and test conventions when changing or reviewing Kotlin, including formatting. Use Spring or Cucumber guidance when framework behavior or BDD is the main concern."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "engineering"
---

# Kotlin Code Style

Use the sections relevant to the Kotlin decision being made. Follow local conventions where they differ, and distinguish application internals from public library contracts when that affects the answer.

For formatting or comment-only work, go directly to [Format and verify](#format-and-verify). Apply ownership, concurrency, and API guidance only to the requested change.

## Related guidance

Load another skill only when the task needs its policies and they are not already available:

- `code-practice`: shared ownership, compound state, trust boundaries, error handling, or test design. New or changed code-based tests retain its explicit `Given`, `When`, and `Then` comment sections.
- `component-collaboration-architecture`: direct calls versus events, projections, or ownership across components.
- `spring-application-code-style`: controllers, transactions, bean wiring, or Spring-managed lifecycle behavior.
- `kotlin-cucumber-tests`: feature files, step definitions, hooks, and BDD scenarios.

## Files and types

- Prefer one main public type per file. Name files after the owned type, feature, or behavior; avoid catch-all `Models.kt`, `Extensions.kt`, `Utils.kt`, `Helpers.kt`, and `Support.kt` files.
- Organize by feature or concept before technical type. Split types with different owners or reasons to change; keep small related value types together when they form one concept and are usually changed together.
- Keep protocol DTOs, local models, and feature state with their owner unless they are shared contracts. Ordinary Kotlin types and functions suit feature logic with no framework-managed lifecycle or boundary.
- Prefer compact immutable domain values. Use `data class` when structural equality and copying are part of the contract.
- Use constructors for straightforward creation and nearby factories for construction rules, parsing, or platform-specific setup.
- Put extensions near the feature or type they support. Avoid top-level helpers or `object` collections that obscure ownership, and avoid extraction merely to reshape one value at one call site.

## Control flow and validation

- Use expression bodies and scope functions when they make intent clearer. Prefer direct `if` / `when` and early returns over nullable or operator chains that hide a simple branch.
- Treat nullability as a contract. Reserve `!!` for tight invariant boundaries.
- Use structured validation results when callers need rejected-field detail or recovery choices. Keep `isValid()` as a convenience wrapper when both detailed and boolean checks are useful.
- Normalize or reshape inputs when parsing correctness, nullability, or the requested behavior requires it; avoid incidental transformation chains around simple values.
- Keep comments focused on why the code is shaped this way.

## Coroutines and mutable state

Use `suspend` for one-shot asynchronous work and `Flow` for streams. Each scope, channel, mutex, background worker, and collection must have a traceable workflow or lifecycle owner, including startup, shutdown, and failure handling. Keep mutable collections and `MutableStateFlow` behind the narrow type that owns their invariants.

Collect state in the owning lifecycle scope; a helper must not hide who starts or cancels the work:

```kotlin
fun start(scope: CoroutineScope) {
    scope.launch {
        printer.connectionState.collect { state ->
            if (state == PrinterState.CONNECTED) flushQueuedJobs()
        }
    }
}
```

Choose explicit concurrency primitives for shared mutable runtime state. When correctness spans multiple values or transitions, use the compound-state guidance in `code-practice` to define the whole invariant before choosing a guard.

## Libraries, multiplatform, and serialization

Keep public library APIs narrow, with explicit parsing, wire-format, failure, and validation contracts. Application serialization can remain boundary-specific.

Use `expect` / `actual`, platform source sets, or injected platform adapters for platform behavior. Avoid common-source runtime conditionals when platform implementations fit.

For changed serializers, parsers, validators, or value contracts, choose relevant positive, rejection, round-trip, and boundary cases. Include platform-specific cases when platforms can differ. Dense rule matrices belong in lower-level Kotlin tests; integration tests fit contracts that depend on wiring, external boundaries, or coroutine scheduling.

## Format and verify

- Inspect the relevant build tasks and repository verification conventions.
- When Kotlin code or tests change and the repo provides `ktlintFormat`, run it to apply formatting; `ktlintCheck` does not replace it. Prefer a supported module or file scope, inspect the resulting diff, and keep unrelated files unchanged.
- If the default Gradle home is not writable, use an existing writable home or set `GRADLE_USER_HOME` to a writable temporary directory.
- Format before verification. For formatting or comment-only changes, use formatting verification; run tests only for changed behavior or an explicit repository requirement.
- For behavior changes, use the most focused relevant task or test filter. Broaden verification only when the changed contract, a failure, or the repository requires it.

Finish the requested change and its applicable checks. Review only the touched ownership, lifecycle, nullability, or platform contracts; these sections do not require unrelated refactoring.

## Canonical references

- Kotlin coding conventions: https://kotlinlang.org/docs/coding-conventions.html
- Kotlin coroutines: https://kotlinlang.org/docs/coroutines-overview.html
- Kotlin Flow: https://kotlinlang.org/docs/flow.html
