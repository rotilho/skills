---
name: "spring-application-code-style"
version: "1.0.1"
description: "Apply Spring Boot application-layer conventions for package structure, thin controllers, services, repositories, transactions, feature-owned configuration properties, bean wiring, semantic validation boundaries, events, async observable-state tests, observability, and integration testing. Use when the user wants Spring application structure or Spring application architecture and wiring guidance, including coroutine or Flow usage inside Spring-managed code, especially for WebFlux or coroutine-first services, not shared libraries or framework internals. When this skill loads, also load `code-practice` as the shared engineering base layer."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "engineering"
---

# Spring Application Code Style

Use this skill for Spring application conventions.

## Required companion skill

Immediately load `code-practice` after loading this skill.

Use `code-practice` for shared naming, ownership, boundaries, state, error handling, testing, and abstraction defaults. Then use this skill to refine or override those defaults only where Spring application lifecycle, framework boundaries, or infrastructure concerns change the recommendation.

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
- keep feature-owned configuration close to the feature that consumes it
- treat async Spring event delivery as real behavior that must be proved through observable downstream state

## Hard constraints

- this skill is application-only, not a generic Spring or library skill
- load and use `code-practice` for framework-neutral defaults
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
- use `@EventListener` in a behavior owner when it owns the resulting state change, side effect, projection, or lifecycle transition; avoid listener classes that only forward
- keep repositories behind the owning service or workflow; event listeners and other services should call that owner instead of reaching into another feature's repository directly
- use Spring events to keep lower-level source-of-truth services from depending on downstream cleanup, projection, notification, or feedback concerns
- keep repositories and persistence adapters near the feature they persist unless persistence is shared infrastructure
- keep configuration feature-owned when it wires one feature
- use root or shared configuration only for app bootstrap, external clients, infrastructure factories, lifecycle scopes, or cross-feature composition
- prefer `@Component` for application-owned collaborators with simple constructor wiring
- use `@Bean` for external objects, factories, properties, lifecycle scopes, or non-trivial wiring
- keep transactional boundaries out of controllers
- validate critical configuration at startup with simple checks close to the property or bean that needs the invariant
- separate protocol and framework validation from semantic validation owned by the feature workflow
- use operational logging and metrics where workflows need them

### Step 3 - Use the right Spring patterns

Prefer:
- `suspend` controller methods for one-shot endpoints
- `Flow` endpoints only for real streams
- dedicated `@ConfigurationProperties` classes per config namespace
- constructor-bound or otherwise simple configuration properties whose usage validates quickly at startup
- after-commit event publication when consumers need durable state
- tests that trigger the upstream command and assert the downstream observable state when event delivery is asynchronous
- scheduled processors for bounded maintenance or draining work
- `@SpringBootTest` and real infrastructure when framework wiring or persistence is part of the contract

### Step 4 - Avoid framework misuse

Push back on:
- controllers owning write orchestration or background coordination
- `service`, `manager`, `processor`, `handler`, `config`, `dto`, `model`, or `event` packages created only by technical type
- feature logic placed in root application packages
- configuration classes added only for symmetry
- shared configuration for one feature's private settings
- property values used deep in a workflow without startup validation when invalid values would break later behavior
- broad event or listener classes that mix unrelated feature workflows
- `@EventListener` methods that only call another component without owning validation, state, lifecycle, retry, translation, or a side effect
- tests that mock the listener directly when the real contract is that an upstream action eventually changes downstream state
- raw property lookups spread through the codebase
- publishing downstream facts before the related write commits without an explicit tradeoff
- pushing simple business logic into framework abstractions for no gain
- using Bean Validation, HTTP binding errors, or DTO constraints as a substitute for semantic validation that belongs to the feature

### Step 4a - Spring event listener examples

Prefer behavior-owned event listeners:

```kotlin
@Component
class InventoryReservations(private val events: DomainEvents) {
    @EventListener
    fun onOrderPlaced(event: OrderPlaced) {
        reserved[event.sku] = (reserved[event.sku] ?: 0) + event.quantity
        events.publish(InventoryReserved(event.orderId, event.sku, event.quantity))
    }
}
```

Avoid pass-through listener classes:

```kotlin
@Component
class OrderListener(private val service: OrderService) {
    @EventListener
    fun onOrderPlaced(event: OrderPlaced) = service.reserveInventory(event)
}
```

For async event flows, test the externally visible result instead of the listener method:

```kotlin
orders.place(order)

await().untilAsserted {
    assertThat(inventory.reservationFor(order.id)).isEqualTo(ReservationStatus.RESERVED)
}
```

### Step 5 - Keep ownership boundaries clear

If the issue is:
- direct calls vs events, proxy/listener chains, projections, or ownership across components: use `component-collaboration-architecture`
- general API design, mutation, logging, or testing defaults: use `code-practice`
- Kotlin file layout, extensions, nullability, or coroutine mechanics outside Spring boundaries: use `kotlin-code-style`

### Step 6 - Keep validation layers distinct

Prefer:
- protocol validation at controllers and message adapters for shape, binding, and authentication context
- semantic validation in the feature workflow that owns the business rule
- startup validation for configuration invariants and external-client wiring

Do not let DTO annotations, persistence constraints, or framework binding errors become the only place a business rule is enforced when other callers can reach the same workflow.

## Canonical references

- Spring Boot reference: https://docs.spring.io/spring-boot/index.html
- Spring Framework reference: https://docs.spring.io/spring-framework/reference/
- Spring Guides: https://spring.io/guides

## Verification checklist

Before finishing, confirm that you:
- kept the guidance Spring-application-specific
- kept controllers thin and orchestration elsewhere
- kept Spring annotations, lifecycle, and infrastructure concerns at application boundaries
- kept configuration feature-owned unless it is shared infrastructure
- treated event listeners as owners of side effects or state transitions, not forwarding glue
- tested async event behavior through downstream observable state
- separated semantic validation from protocol/framework validation
- avoided inventing unsupported framework house rules
- did not drift into generic or Kotlin-only guidance
