# Compound state and concurrency

Use this procedure when changing shared mutation, a concurrent container, or its locking strategy.

Before choosing a lock, mutex, actor, or concurrent container:

- Define the whole invariant and every collection, nested mutable value, counter, limit, and check-and-act transition it couples.
- Rely on concurrent collections alone only when correctness consists of independent per-entry atomic operations.
- Use one invariant-owned guard for transitions spanning collections, nested mutable values, counters, or check-and-act limits.
- Prefer plain collections when every access shares that guard. Combining a concurrent collection with a broad lock needs a documented independent access path that benefits from per-entry concurrency.
- Name the guard for the state or invariant it owns, and comment its complete ownership when the boundary is not obvious.
- Decide and mutate under the guard. Move avoidable logging, events, callbacks, and I/O outside it only when required ordering and failure behavior are preserved.
- Preserve required fairness and reentrancy behavior when changing concurrency mechanisms.

Test the changed invariant under contention and propagate worker failures to the test. Follow the root skill's Given/When/Then convention for new or changed code-based tests.
