---
name: "kotlin-code-style"
description: "Apply Kotlin-specific code style and design guidance for file organization, type design, constructors, extensions, nullability, serialization, coroutines, Flow, and Kotlin unit/integration test style outside Cucumber or BDD. Use when the user wants idiomatic Kotlin conventions or Kotlin-language-specific code review guidance, excluding Spring application architecture, Spring-managed wiring concerns, and Cucumber/BDD-specific test design."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "engineering"
  style: "concise"
---

# Kotlin Code Style

Use this skill for Kotlin-specific guidance.

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

## Hard constraints

- treat generic code-practice guidance as the base layer
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
- `data class` for small immutable values
- constructors for straightforward creation, factories when creation has rules
- nearby extensions over broad utility files
- expression bodies only when the function stays obvious
- nullability as part of the contract
- `suspend` for one-shot async work and `Flow` for streams
- sparse comments focused on the why

### Step 3 - Apply the right Kotlin mode

For applications:
- prefer feature-local organization
- prefer explicit concurrency primitives around shared mutable runtime state
- prefer boundary-specific serialization choices

For libraries:
- prefer tighter public API control
- prefer explicit wire-format and parsing behavior
- prefer predictable failure and round-trip testing for external contracts

### Step 4 - Avoid common Kotlin failure modes

Push back on:
- catch-all extension files
- `!!` outside tight invariant boundaries
- deep scope-function or operator chains that hide control flow
- interfaces added only for symmetry or testing ceremony
- hidden background work with unclear scope ownership

### Step 5 - Keep overlap boundaries clear

If the issue is:
- generic naming, architecture, or testing defaults: use `code-practice`
- Kotlin Cucumber, feature files, step definitions, or BDD glue design: use `kotlin-cucumber-tests`
- Spring controllers, configuration, transactions, or integration testing: use `spring-application-code-style`

## Verification checklist

Before finishing, confirm that you:
- added Kotlin-specific guidance rather than generic restatement
- kept helper placement and ownership clear
- treated nullability and async behavior explicitly
- separated application and library advice when it mattered
- avoided Spring-specific framework guidance
