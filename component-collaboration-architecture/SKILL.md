---
name: "component-collaboration-architecture"
description: "Design or refactor how components, classes, modules, or services collaborate by choosing direct calls, orchestration, events, observers, projections, shared state, or local ownership. Use when a class calls many collaborators, handlers/listeners/proxies only forward, ownership of behavior/data/state is unclear, or the user asks whether to emit an event and consume it in N places. Avoid for ordinary cleanup, Kotlin idioms, Spring wiring, or Cucumber structure unless collaboration boundaries are the main issue."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "architecture"
  style: "concise"
---

# Component Collaboration Architecture

Use this skill to decide how application parts should talk to each other and where behavior, data, state, and side effects should live.

## When to use

Trigger for work like:
- deciding whether one class should call several collaborators directly
- deciding whether to emit one event and let multiple consumers react
- removing proxy, listener, handler, manager, or service chains that only forward
- finding who owns state, validation, lifecycle, retries, side effects, or recovery
- replacing shared registries, broad mutable state, or god coordinators with clearer owners
- designing local projections, read models, event-fed caches, or explicit query boundaries
- reviewing event-heavy, command-heavy, observer-heavy, or callback-heavy code for ownership

Do not use this skill for ordinary naming, small-function cleanup, Kotlin idioms, Spring wiring, or Cucumber structure unless the main issue is collaboration shape or ownership boundaries.

## Core promise

Choose the simplest collaboration shape that keeps:
- ownership clear
- behavior traceable
- state controlled by one owner
- side effects close to the component responsible for their outcome
- failure, ordering, idempotency, and recovery visible
- direct coupling intentional instead of accidental

## Hard constraints

- Pick owners from invariants, state transitions, side effects, and failure responsibility, not from the current caller.
- Prefer direct calls when the caller intentionally needs sequencing, a return value, one transaction, or immediate failure handling.
- Prefer events when an owner has completed a fact and independent consumers may react without the owner knowing them.
- Do not use events as disguised commands. If something is being requested, model it as a command, method call, job, or workflow step.
- Keep mutable state local to one writer. Other components can keep projections or caches fed by owner-published facts.
- Keep proxies only when they own translation, protocol adaptation, authorization, retry, lifecycle, observability, or real deduplication.
- Delete pass-through layers that exist only for symmetry or because "everything needs a handler."
- Treat expected rejection as a domain result, not as an exception hidden behind a generic wrapper.
- Treat recovery, resync, and external-state adoption as explicit behavior, not as normal request handling.

## Workflow

### Step 1 - Map the current collaboration

Before changing code, identify:
- the initiating actor, request, timer, message, or external input
- the component that can accept or reject the action
- the component that owns each affected state change
- every downstream side effect
- every consumer that needs to know about the outcome
- whether each consumer needs ordering, a return value, retry, idempotency, or transaction coupling
- which classes only forward calls, events, or DTOs

Classify each link as:
- direct call
- query
- command or request
- domain fact or event
- observer callback
- projection or read model update
- external adapter call
- recovery or reconciliation flow

### Step 2 - Find the real owner

Ask these questions:
- Who can say no?
- Who has the state needed to decide?
- Who must keep the invariant true?
- Who owns the external side effect or irreversible operation?
- Who pays the cost when this fails halfway?
- Who needs to recover, retry, deduplicate, or reconcile?

The owner is usually the component that changes durable state, protects the invariant, or owns the side effect. It is not necessarily the component that currently receives the call.

### Step 3 - Choose the collaboration shape

Use direct calls when:
- the caller needs an immediate answer
- the operation is one synchronous workflow
- failure must stop the current operation
- the callee is a required collaborator, not an optional reaction
- the coupling is part of the domain or transaction

Use an orchestrator when:
- the workflow itself owns ordering, progress, compensation, or retry
- several participants are required but none owns the whole process
- the orchestration state is real and observable

Use events when:
- a component has completed something factual
- multiple consumers can react independently
- the publisher should not know every consumer
- consumers can tolerate eventual consistency
- adding a consumer should not change the publisher

Use projections or local event-fed caches when:
- a component needs fast local reads for its own decision
- the source of truth is owned elsewhere
- rebuilding from facts is acceptable or useful
- direct shared reads would couple schemas or internals

Use queries when:
- a component needs current information from the owner
- no state change is requested
- staleness would be unsafe or misleading

Use adapters when:
- the code crosses a protocol, transport, storage, vendor, process, or authorization boundary
- translation and normalization are the real responsibility

### Step 4 - Remove false collaboration

Push these refactors:
- collapse listeners or handlers that only call another component
- move behavior from a generic coordinator into the owner of the decision or state
- split god classes by owned workflow or invariant
- replace broad registries with local projections owned by the validator or decision maker
- replace micro-events for internal steps with direct private methods
- replace event-as-command flows with explicit commands, jobs, or workflow steps
- rename remaining abstractions by the decision, state, or side effect they own

### Step 5 - Make data ownership explicit

For each important data set, state:
- source of truth
- only writer
- allowed readers
- projection or cache owners
- rebuild or reconciliation path
- schema or contract boundary

If several components write the same data, redesign until there is one writer or an explicit coordination protocol.

### Step 6 - Guard failure and recovery

For collaboration that crosses owners, check:
- duplicate requests or events
- out-of-order delivery
- partial failure
- retry behavior
- idempotency keys or natural idempotency
- transactional boundary
- compensating action, pause, abort, or reconciliation
- observability needed to debug the workflow

Do not add eventing or indirection unless the failure model is clearer afterward.

### Step 7 - Test the boundary, not the plumbing

Prefer tests that show:
- the owner accepts or rejects the action
- required direct collaborators are called only after validation passes
- events are published only after the fact is true
- independent consumers react to facts without changing the publisher
- projections can be rebuilt or updated from facts
- duplicate, stale, rejected, and recovery paths are explicit

## Examples

### Direct fan-out vs event fan-out

If class `A` calls five collaborators and those calls are required steps of one operation, keep the directness but rename and shape `A` as the workflow owner:

```kotlin
class CheckoutWorkflow(
    private val payments: Payments,
    private val inventory: Inventory,
    private val orders: Orders,
) {
    fun checkout(cart: Cart): CheckoutResult {
        val reservation = inventory.reserve(cart)
        val charge = payments.charge(cart.total)
        return orders.confirm(cart, reservation, charge)
    }
}
```

If the main owner only needs to record a fact and the other work is independent, publish the fact and let owners react:

```kotlin
class Orders(private val events: DomainEvents) {
    fun markPaid(orderId: OrderId) {
        paidOrders += orderId
        events.publish(OrderPaid(orderId))
    }
}

class ReceiptEmails {
    fun onOrderPaid(event: OrderPaid) = sendReceipt(event.orderId)
}
```

### Pass-through listener

Avoid listeners that only forward:

```kotlin
class OrderPlacedListener(private val inventory: InventoryService) {
    fun onOrderPlaced(event: OrderPlaced) = inventory.reserve(event.orderId)
}
```

Prefer the behavior owner consuming the fact:

```kotlin
class InventoryReservations(private val events: DomainEvents) {
    fun onOrderPlaced(event: OrderPlaced) {
        reserved += event.orderId
        events.publish(InventoryReserved(event.orderId))
    }
}
```

### Shared registry used by one decision

Avoid shared state that exists only to feed one validator:

```kotlin
fraudCheck.validate(order, customerRegistry.blockedCustomers())
```

Prefer local projected state owned by the decision maker:

```kotlin
class FraudCheck {
    private val blockedCustomers = mutableSetOf<CustomerId>()

    fun onCustomerBlocked(event: CustomerBlocked) {
        blockedCustomers += event.customerId
    }

    fun validate(order: Order): FraudDecision =
        if (order.customerId in blockedCustomers) FraudDecision.Rejected else FraudDecision.Accepted
}
```

## Overlap boundaries

If the issue is:
- local naming, readability, duplication, or generic abstraction quality: use `code-practice`
- Kotlin file layout, nullability, Flow, coroutine ownership, or type design: use `kotlin-code-style`
- Spring controller/service/repository wiring, transactions, bean config, or Spring events: use `spring-application-code-style`
- Cucumber feature files, step definitions, hooks, or scenario state: use `kotlin-cucumber-tests`

Use this skill first when the main decision is how components should collaborate. Hand off to language or framework skills after the ownership shape is clear.

## Canonical references

- Martin Fowler, event-driven pattern distinctions: https://martinfowler.com/articles/201701-event-driven.html
- Martin Fowler, bounded contexts: https://martinfowler.com/bliki/BoundedContext.html
- Martin Fowler, anemic domain model: https://martinfowler.com/bliki/AnemicDomainModel.html
- Microsoft domain events guidance: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation
- Microservices.io database per service: https://microservices.io/patterns/data/database-per-service.html
- Confluent data ownership: https://developer.confluent.io/courses/microservices/data-ownership/

## Verification checklist

Before finishing, confirm that you:
- identified the real owner for each important decision, state change, or side effect
- chose direct calls, orchestration, events, projections, queries, or adapters deliberately
- removed or justified forwarding layers
- kept mutable state with one owner
- separated requests from facts
- made failure, retry, ordering, and recovery visible where they matter
- avoided adding eventing or indirection for style alone
- handed off to language or framework skills only after the collaboration shape was clear
