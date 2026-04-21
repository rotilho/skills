---
name: "kotlin-cucumber-tests"
description: "Plan, review, or improve Kotlin Cucumber / BDD tests: decide when Cucumber fits, structure feature files, step definitions, hooks, fixtures, and Kotlin helpers, and keep domain language readable without coupling steps to implementation details. Use when the request explicitly centers on Kotlin Cucumber, Kotlin BDD, feature files, step definitions, hooks, or executable-specification tests and reviews."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "testing"
  style: "concise"
---

# Kotlin Cucumber Tests

Use this skill for Kotlin projects that automate Cucumber scenarios.

## When to use

Trigger for work like:
- create or clean up Kotlin Cucumber tests
- review feature files or step definitions for BDD quality
- organize hooks, shared fixtures, or scenario state in Cucumber JVM
- decide whether a behavior should live in Cucumber, integration tests, or unit tests
- fix Kotlin-specific Cucumber glue design

Do not use this skill for generic unit tests, framework-neutral test advice, broad Kotlin style work without Cucumber, or Spring test architecture that is not specifically about Cucumber glue and scenarios.

## Core promise

Produce Cucumber guidance or edits that:
- keep scenarios readable to non-implementers
- keep step definitions thin and behavior-focused
- keep shared state scenario-scoped and explicit
- use Kotlin-specific structure only where it improves the test code
- keep overlap boundaries with unit and lower-level integration tests clear

## Hard constraints

- treat BDD guidance as the base layer and add Kotlin specifics only where they change the answer
- use Cucumber for externally visible behavior, workflow rules, and acceptance-level examples; do not force it into unit-level logic
- keep feature files in business language, not UI locator, HTTP client, SQL, or object-construction detail
- prefer Cucumber Expressions and shared helper methods over many near-duplicate step definitions
- avoid sharing state across scenarios; keep fixtures and mutable context per scenario
- use hooks for low-level setup and teardown; prefer `Background` when the setup should stay visible to readers
- keep step-definition files grouped by domain concept or behavior area, not tightly coupled one-file-per-feature
- when global hooks are needed in Kotlin, prefer package-level functions over companion objects or named objects
- if the request becomes mainly about generic test design, use `code-practice`; if it becomes mainly about Kotlin idioms outside Cucumber, use `kotlin-code-style`

## Workflow

### Step 1 - Decide whether Cucumber fits

Use Cucumber when the test needs shared language across product, QA, and engineering, or when an end-to-end behavior is clearer as examples.

Prefer lower-level tests when the request is mainly about:
- pure domain logic
- algorithm branches
- mapper or serializer edge cases
- narrow repository or client behavior
- fast feedback on many permutations

If useful, say this explicitly: Cucumber covers the behavior contract; unit and integration tests cover implementation detail and edge density.

### Step 2 - Shape the feature file first

Prefer:
- one feature per user-visible capability or rule set
- short scenarios, usually about 3-5 steps
- `Rule` when one feature has multiple business rules
- `Scenario Outline` only when the examples truly share the same behavior shape
- `Background` only for brief context readers should remember
- observable outcomes in `Then` steps

Push back on:
- scenarios that read like Selenium scripts or API call logs
- database-state assertions when the outcome should be verified through a visible effect
- large backgrounds that hide the real scenario intent
- feature files full of technical setup detail

### Step 3 - Design step definitions as glue, not as the test body

Prefer these defaults:
- map each step to a thin Kotlin step definition that delegates to helpers, drivers, or domain-specific test services
- group step-definition files by domain concept or workflow area
- reuse steps when the phrasing represents the same behavior, but do not over-parameterize unrelated actions into one vague mega-step
- use data tables or doc strings when they make the example clearer than many scalar parameters
- keep assertions in `Then` steps focused on observable outcomes

Avoid:
- feature-coupled step files that duplicate nearly identical glue
- steps that directly expose internal method names, DTO fields, CSS selectors, or transport details unless those are part of the behavior contract
- long imperative logic inside step definitions
- ambiguous expressions that can match multiple steps

### Step 4 - Apply Kotlin-specific glue design

In Kotlin step code:
- prefer small constructor-injected collaborators or focused helper objects when using DI
- keep scenario state in small explicit context objects rather than scattered mutable vars
- use package-local helper functions or focused support types for repeated setup and assertions
- prefer clear block bodies over clever chaining when a step performs several actions
- use Kotlin collections, nullability, and data classes to make fixtures explicit and safe
- keep backticked function names only when they help readability more than standard names

For Cucumber JVM specifics:
- Cucumber creates new glue instances per scenario, so lean on scenario-local state rather than statics
- if sharing state across step classes, use the project's DI approach or a small scenario-scoped context object
- for JUnit Platform execution, keep Cucumber configuration visible and avoid accidental duplicate discovery setup

### Step 5 - Keep hooks and fixtures disciplined

Prefer:
- `Before` and `After` hooks for low-level environment setup, cleanup, screenshots, or database reset
- conditional hooks via tags for special environments
- shared fixture builders and helper APIs below the glue layer
- tags for selecting scenario subsets and for operational metadata that the team actually uses

Avoid:
- heavy business setup hidden in hooks when readers need to understand it
- cross-scenario caches or globals
- hooks that silently mutate too much test state
- giant fixture objects passed everywhere when a smaller scenario context would do

### Step 6 - Guard common failure modes

Watch for:
- ambiguous or overlapping step expressions
- brittle step wording tied to implementation details
- too many parameters in one step instead of a table or helper abstraction
- duplicated step text with slightly different regexes
- leaked state between scenarios
- slow suites caused by pushing too many narrow cases into Cucumber instead of lower-level tests
- Kotlin hook mistakes around companion objects, named objects, or static expectations

### Step 7 - Explain boundaries briefly

When giving advice, separate:
- generic BDD guidance
- Kotlin/Cucumber-JVM specifics
- framework-specific advice only if the user's stack requires it

If you recommend moving a test, say why:
- Cucumber for business-facing workflows and acceptance contracts
- integration tests for boundary wiring and infrastructure behavior
- unit tests for local logic and dense edge cases

## Verification checklist

Before finishing, confirm that you:
- kept feature-file advice readable to non-implementers
- kept step definitions thin and not tightly coupled to implementation detail
- treated hooks, background, and shared state with clear boundaries
- separated generic BDD advice from Kotlin-specific refinements
- called out when Cucumber is the wrong level for the requested test
- avoided over-triggering on generic unit-test requests
