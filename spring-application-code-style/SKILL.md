---
name: "spring-application-code-style"
version: "1.1.0"
description: "Apply Spring Boot application conventions for controller/service boundaries, wiring, validation, transactions, events, and integration tests. Use also for Spring AOT verification; skip plain Kotlin style and framework internals."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "engineering"
---

# Spring Application Code Style

Apply the sections relevant to the Spring-managed boundary being changed or reviewed. Follow local conventions; do not invent mandatory Bean Validation, global exception advice, or slice-test rules without repository evidence.

For AOT output collisions or build-only verification, go directly to [Verification and Spring AOT](#verification-and-spring-aot). A narrow configuration or build repair does not require an application-wide architecture review.

## Related guidance

Load another skill only when its decisions are part of the task and its guidance is not already available:

- `code-practice`: framework-neutral ownership, state invariants, trust boundaries, error handling, or test design. New or changed code-based tests retain its explicit `Given`, `When`, and `Then` comment sections.
- `component-collaboration-architecture`: deciding between direct calls and events, forwarding chains, projections, or cross-component ownership.
- `kotlin-code-style`: Kotlin types, extensions, nullability, coroutine mechanics, and Kotlin formatting.

## Application boundaries and wiring

- Organize by feature or workflow rather than technical packages such as `service`, `handler`, `config`, `dto`, or `event`. Keep root application packages for bootstrap, composition, entrypoints, and shared public API.
- Controllers translate protocol and framework concerns. Keep business sequencing, transactions, and background coordination with the owning feature workflow.
- Keep repositories and persistence adapters near the feature they persist unless they are shared infrastructure. Other services and listeners call the feature owner rather than accessing its repository directly.
- Prefer `@Component` for application-owned collaborators with simple constructor wiring. Use `@Bean` for external objects, factories, properties, lifecycle scopes, or non-trivial wiring.
- Keep configuration with the feature it wires. Root or shared configuration fits bootstrap, external clients, infrastructure factories, lifecycle scopes, and cross-feature composition; avoid classes added only for symmetry.
- Use `suspend` controller methods for one-shot endpoints and `Flow` only for real streams. Keep Spring-managed background work in its owning lifecycle; do not push ordinary business logic into framework abstractions without a need.
- Use scheduled processors for bounded maintenance or draining work, with operational logs and metrics where the workflow needs them.

## Configuration and validation

Use dedicated, simple `@ConfigurationProperties` classes per namespace instead of scattered raw property lookups. Validate critical configuration at startup with checks close to the property, bean, or external-client wiring that needs the invariant.

Keep validation at the right boundary:

- Controllers and message adapters handle protocol shape, binding, and authentication context.
- Feature workflows own semantic business rules, including when multiple entrypoints call the same workflow.
- Startup checks enforce configuration and wiring invariants.

DTO annotations, persistence constraints, and framework binding errors must not be the only enforcement of a business rule that other callers can bypass.

## Events and asynchronous behavior

Once event-based collaboration fits the consistency and failure contract, put `@EventListener` on the owner of the resulting state transition, projection, side effect, or lifecycle action. Avoid broad listeners mixing unrelated workflows and listener classes that only forward a call without owning behavior.

Publish after commit when consumers require durable state. Publishing a fact before the related write commits needs an explicit consistency tradeoff.

For asynchronous event behavior, trigger the upstream command and assert downstream observable state with bounded waiting. Calling or mocking the listener directly does not prove that delivery and wiring work:

```kotlin
// Given
val order = anOrder()

// When
orders.place(order)

// Then
await().untilAsserted {
    assertThat(inventory.reservationFor(order.id)).isEqualTo(ReservationStatus.RESERVED)
}
```

## Verification and Spring AOT

Select checks for the changed contract. Use `@SpringBootTest` and real infrastructure when framework wiring or persistence is part of that contract. For asynchronous changes, verify the relevant downstream result; for configuration changes, check binding and startup validation as applicable. Formatting or comment-only work needs formatting checks, with tests only when a repository rule requires them.

For Kotlin edits, follow the repository formatter convention, including `ktlintFormat` when available; use `kotlin-code-style` for its execution details when needed.

When Spring AOT generation is involved:

- Identify the Gradle tasks and generated-output paths involved in the requested check.
- Do not overlap independent Gradle invocations that write the same AOT output, such as concurrent `processTestAot` invocations. Run those writers serially; independent checkouts or output directories can be used when isolation is established.
- If a writer collision caused a failure, wait for the active writer to finish or stop a redundant writer started for this task before rerunning the affected check. Do not add unrelated test runs merely because AOT is present.

Complete the requested work and fix failures caused by it. Review the touched boundaries, configuration, events, or AOT writers; mechanisms absent from the change do not create extra checks or refactors.

## Canonical references

- Spring Boot reference: https://docs.spring.io/spring-boot/index.html
- Spring Framework reference: https://docs.spring.io/spring-framework/reference/
- Spring Guides: https://spring.io/guides
