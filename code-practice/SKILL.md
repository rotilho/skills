---
name: "code-practice"
version: "1.1.0"
description: "Apply framework-neutral code quality guidance for readability, refactoring, ownership, concurrency, trust boundaries, and behavior-focused tests. Use when these engineering decisions are the main task; use specialist skills for language or framework rules."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "engineering"
---

# Code Practice

Apply the guidance relevant to the requested review or change. Inspect the affected behavior and its callers; a small naming edit does not require a repository inventory or architecture review. Preserve useful local conventions when they fit the contract.

## Select the needed guidance

- For shared mutation, concurrent collections, or locking decisions, read [compound state](references/compound-state.md).
- Before adding retries, fallbacks, guards, recovery branches, or failure tests, read [defensive behavior](references/defensive-behavior.md).
- For direct calls versus events, forwarding chains, projections, or cross-component ownership, use `component-collaboration-architecture`.
- For Kotlin mechanics, Spring-managed boundaries, or Cucumber scenarios, use `kotlin-code-style`, `spring-application-code-style`, or `kotlin-cucumber-tests` as the primary skill. They can use the relevant shared policies here without turning a specialist task into a general code review.

Load only the guidance the task needs, then continue the authorized work.

## Diagnose within the changed boundary

For a defect or operational issue, establish a read-only baseline from the failing test, runtime trace, logs, public contract, or current caller behavior before changing production paths. Identify the owner that can accept or reject the action and the state transition or side effect that must stay correct. Verify the same signal after the fix.

For a design review or refactor, identify the concrete pressure in the affected code: unclear names, mixed decisions, duplicated policy, hidden side effects, or misplaced ownership. Do not manufacture a defect or expand the task to satisfy these categories.

## Ownership, readability, and abstraction

- Place behavior, its state, policies, adapters, and tests with the smallest feature, workflow, or concept that owns them. Shared contracts can live separately; avoid mixed-concern utility buckets and root-level behavior files when an owner exists.
- Name responsibilities and observable intent in domain language. Avoid placeholders such as `util`, `manager`, or `misc`; name booleans and predicates so both outcomes read naturally.
- Keep each unit responsible for one kind of decision and one level of abstraction. Split when mixed decisions, nesting, or section comments obscure the flow; prefer early exceptional branches when they clarify the main path.
- Keep operations and mandatory follow-up state transitions cohesive. Split them only for a valid independent lifecycle or policy boundary; extract a repeated compound transition at the smallest shared scope when that exposes its invariant.
- Group cohesive parameters without creating grab-bag objects. Separate commands from queries when combining them hides side effects, and avoid mode flags when distinct entry points clarify the contract.
- Remove duplication of behavior or policy, not merely repeated tokens. Do not extract helpers just to reshape one local value, satisfy symmetry, or anticipate speculative reuse.
- Keep a forwarding layer only when it owns a decision, invariant, boundary translation, or meaningful deduplication. Prefer direct data flow over indirection and implicit shared state.
- Keep comments for intent, invariants, and non-obvious tradeoffs. Explain a recommendation's local benefit and material cost; do not narrate every default.

## Contracts, trust, and errors

- Keep public APIs small and explicit. Preserve public contracts unless a breaking change is intentional; use migration, adapters, or compatibility coverage where the change requires them.
- Normalize and validate external, persisted, serialized, remote, generated, or user-controlled values at the boundary that accepts them when correctness, security, or compatibility relies on those values. Translate them into trusted domain values; do not repeatedly normalize values whose owner already enforces the invariant.
- Keep integration concerns at the edges. Distinguish expected rejection from system failure, translate errors at the boundary that changes context, and avoid duplicating recovery, translation, and logging in every layer.
- Keep mutable state and its guard with the owner. Make concurrency and retry behavior explicit; use the linked procedures when either changes.

For applications, favor feature-local ownership, thin external edges, and observable workflow behavior. For libraries, prioritize stable contracts, minimal surface area, predictable failure modes, and auditable wire or serialization behavior. Let that distinction determine relevant compatibility and verification needs.

## Verify the requested result

When behavior changes, choose checks at the level of the defect or contract: local rule tests, integration checks for boundary wiring, or end-to-end checks for workflow behavior. A build alone does not prove a failing behavior is fixed. Library contract changes may need compatibility, round-trip, and rejected-input cases.

Structure every new or changed code-based test with explicit Given, When, and Then sections using the host language's comment syntax. Do not rewrite untouched tests solely to add markers. Tests should explain the scenario, action, and observable outcome and exercise reachable behavior.

For advice-only or mechanical changes, verify the relevant reasoning or diff without adding tests solely to satisfy this skill. Complete the requested implementation and applicable verification, resolve failures caused by the change, and report material limits. Unrelated checklist topics do not expand the task.
