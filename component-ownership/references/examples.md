# Collaboration examples

These sketches illustrate ownership boundaries, not complete transaction or delivery implementations. Preserve the actual workflow's failure, ordering, and consistency requirements when applying them.

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

### Source-of-truth owner with downstream cleanup

When downstream cleanup is independent and its consistency contract permits delayed reaction, avoid making the source-of-truth owner depend on that concern:

```kotlin
class ProfileService(
    private val publicationPolicy: PublicationPolicy,
    private val searchIndex: SearchIndex,
) {
    fun changePrimaryDocument(profile: Profile, nextDocumentId: DocumentId) {
        publicationPolicy.requireAllowed(nextDocumentId)
        val previousDocumentId = profile.primaryDocumentId
        profile.primaryDocumentId = nextDocumentId
        searchIndex.recordStale(previousDocumentId)
    }
}
```

Keep required validation direct, then publish a completed fact for the independent downstream owner. Keep cleanup direct if it must complete synchronously or share the transaction:

```kotlin
class ProfileService(
    private val publicationPolicy: PublicationPolicy,
    private val events: DomainEvents,
) {
    fun changePrimaryDocument(profile: Profile, nextDocumentId: DocumentId) {
        publicationPolicy.requireAllowed(nextDocumentId)
        val previousDocumentId = profile.primaryDocumentId
        if (previousDocumentId == nextDocumentId) return

        profile.primaryDocumentId = nextDocumentId
        events.publish(PrimaryDocumentChanged(profile.id, previousDocumentId, nextDocumentId))
    }
}

class SearchIndex {
    private val staleDocuments = mutableSetOf<DocumentId>()

    fun onPrimaryDocumentChanged(event: PrimaryDocumentChanged) {
        staleDocuments += event.previousDocumentId
    }
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

Keep the state with the decision maker when event-fed updates and their freshness satisfy the decision's contract:

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

## Further reading

- Martin Fowler, event-driven pattern distinctions: https://martinfowler.com/articles/201701-event-driven.html
- Martin Fowler, bounded contexts: https://martinfowler.com/bliki/BoundedContext.html
- Martin Fowler, anemic domain model: https://martinfowler.com/bliki/AnemicDomainModel.html
- Microsoft domain events guidance: https://learn.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/domain-events-design-implementation
- Microservices.io database per service: https://microservices.io/patterns/data/database-per-service.html
- Confluent data ownership: https://developer.confluent.io/courses/microservices/data-ownership/
