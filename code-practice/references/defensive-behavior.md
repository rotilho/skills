# Evidence before defensive behavior

Read before adding a retry, fallback, guard, recovery branch, or failure test.

- Identify the exact production caller, input, dependency, scheduler, or lifecycle event that can trigger it.
- Establish reachability from production callers or the boundary and lifecycle contract. A test-created state alone does not justify new recovery behavior.
- Distinguish untrusted boundaries from closed-world internals: validate public, persisted, serialized, remote, and user-controlled values, but trust internal values whose owners already enforce the invariant.
- Check whether an existing owner already provides recovery through restart, expiration, reconciliation, idempotency, or rediscovery.
- Weigh the actual consequence and frequency against the permanent branch, state, API, and test complexity.
- Do not manufacture an otherwise unreachable failure in a test and then use that test to justify production recovery behavior.

If the trigger cannot be named or demonstrated, omit the behavior. Record the assumption only when it is important and inexpensive to revisit. When adding a justified failure test, use the root skill's Given/When/Then convention.
