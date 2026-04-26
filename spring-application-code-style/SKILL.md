---
name: "spring-application-code-style"
description: "Apply Spring Boot application-layer conventions for package structure, controllers, services, repositories, transactions, configuration properties, bean wiring, observability, and integration testing. Use when the user wants Spring application structure or Spring application architecture and wiring guidance, including coroutine or Flow usage inside Spring-managed code, especially for WebFlux or coroutine-first services, not shared libraries or framework internals."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "engineering"
  style: "concise"
---

# Spring Application Code Style

Use this skill for Spring application conventions.

## When to use

Trigger for work like:
- Spring Boot code style
- Spring application conventions
- controller, service, and repository boundaries
- WebFlux or coroutine-first Spring structure
- `@ConfigurationProperties` and bean wiring
- Spring transactions, events, scheduling, or integration tests

Do not use this skill for plain Kotlin style or language-agnostic coding guidance when the question is not tied to Spring-managed boundaries.

## Core promise

Produce Spring application guidance or edits that:
- keep HTTP and framework edges thin
- keep business sequencing out of controllers
- use Spring for lifecycle and infrastructure concerns
- keep Spring annotations and framework abstractions at real application boundaries

## Hard constraints

- this skill is application-only, not a generic Spring or library skill
- use `code-practice` for framework-neutral defaults
- use `kotlin-code-style` for pure Kotlin concerns unless they are directly tied to Spring usage
- do not infer unsupported house rules such as mandatory Bean Validation, global exception advice, or slice-test defaults unless the local codebase shows them

## Workflow

### Step 1 - Find the Spring boundary in question

Classify the request around one or more of:
- package or feature organization
- controller design
- request and response DTO boundaries
- service orchestration
- repository and persistence boundaries
- transaction scope
- configuration properties and bean wiring
- scheduling, events, or observability
- Spring integration tests

### Step 2 - Apply Spring application defaults

Prefer these defaults unless local evidence says otherwise:
- organize by feature or workflow first, not by technical layer
- keep root application packages for bootstrap, composition, entrypoints, and shared public API only
- keep controllers and listeners focused on protocol or framework translation
- keep business sequencing in the owning feature package
- keep repositories and persistence adapters near the feature they persist unless persistence is shared infrastructure
- keep configuration feature-owned when it wires one feature
- use root or shared configuration only for app bootstrap, external clients, infrastructure factories, lifecycle scopes, or cross-feature composition
- prefer `@Component` for application-owned collaborators with simple constructor wiring
- use `@Bean` for external objects, factories, properties, lifecycle scopes, or non-trivial wiring
- keep transactional boundaries out of controllers
- validate critical configuration at startup
- use operational logging and metrics where workflows need them

### Step 3 - Use the right Spring patterns

Prefer:
- `suspend` controller methods for one-shot endpoints
- `Flow` endpoints only for real streams
- dedicated `@ConfigurationProperties` classes per config namespace
- after-commit event publication when consumers need durable state
- scheduled processors for bounded maintenance or draining work
- `@SpringBootTest` and real infrastructure when framework wiring or persistence is part of the contract

### Step 4 - Avoid framework misuse

Push back on:
- controllers owning write orchestration or background coordination
- `service`, `manager`, `processor`, `handler`, `config`, `dto`, `model`, or `event` packages created only by technical type
- feature logic placed in root application packages
- configuration classes added only for symmetry
- broad event or listener classes that mix unrelated feature workflows
- raw property lookups spread through the codebase
- publishing downstream facts before the related write commits without an explicit tradeoff
- pushing simple business logic into framework abstractions for no gain

### Step 5 - Keep ownership boundaries clear

If the issue is:
- general API design, mutation, logging, or testing defaults: use `code-practice`
- Kotlin file layout, extensions, nullability, or coroutine mechanics outside Spring boundaries: use `kotlin-code-style`

## Verification checklist

Before finishing, confirm that you:
- kept the guidance Spring-application-specific
- kept controllers thin and orchestration elsewhere
- kept Spring annotations, lifecycle, and infrastructure concerns at application boundaries
- avoided inventing unsupported framework house rules
- did not drift into generic or Kotlin-only guidance
