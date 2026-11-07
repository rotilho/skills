# Trigger Prompt Evals

Use these prompts after changing skill descriptions or overlap boundaries. Expected result means the named skill should be loaded first or clearly chosen as the active domain skill.

## Should trigger

| Prompt | Expected skill | Why |
|---|---|---|
| "Capture the reusable debugging procedure we learned and put it in the existing source skill." | `create-skill` | Retaining an uncovered procedural lesson. |
| "Review every skill's purpose and overlap; remove instructions that add no value." | `skill-library-curator` | Library-wide curation before wording changes. |
| "Curate my global skills using the OpenAI Astra skills and prompts guide." | `skill-library-curator` | Global library review with model-aware instruction assessment. |
| "Review every skill in this repo, including committed and nested packages, for unnecessary instructions." | `skill-library-curator` | Complete repo inventory and instruction review. |
| "Refactor this function for clearer naming and ownership without using framework-specific rules." | `code-practice` | Framework-neutral maintainability. |
| "Diagnose this failing workflow first, then make the smallest compatibility-preserving API change and test the contract directly." | `code-practice` | Evidence-first diagnosis, public-surface safety, and test-level choice without framework specifics. |
| "Reorganize this module's files around its existing workflows and improve generic names; keep component interactions and state ownership unchanged." | `code-practice` | File organization and naming without redesigning component collaboration. |
| "Update these Java unit tests and keep every changed test visibly split into Given, When, and Then sections." | `code-practice` | Given/When/Then is a language-agnostic code-test readability convention. |
| "This service uses two concurrent maps, mutable sets inside their values, and an aggregate limit counter. Two limit branches run the same drop callback; simplify them without breaking the guarded check-and-update invariant or moving event publication into the critical section." | `code-practice` | Framework-neutral compound-invariant and locking-strategy review. |
| "Class A calls five collaborators today. Should it keep direct calls or publish one event and let each owner react?" | `component-ownership` | Collaboration shape and ownership decision. |
| "Untangle this entire codebase: investigate structural problems, implement the justified refactors, and finish review and verification." | `untangle-codebase` | Complete repository-wide structural refactoring workflow. |
| "Untangle only the report-export subsystem end to end; preserve public contracts and complete the implementation." | `untangle-codebase` | Complete structural refactoring within a named boundary. |
| "This listener just forwards events to another service. Refactor the flow so behavior and state ownership are clearer." | `component-ownership` | Proxy/listener removal across components. |
| "AccountService owns the account state change, but it now imports vote cleanup to mark old votes stale. Break the dependency so the source-of-truth update can notify the downstream cleanup owner." | `component-ownership` | Source-of-truth to downstream cleanup boundary should be a collaboration-shape decision. |
| "Create a new skill for release-note generation and include trigger eval prompts plus a realistic behavior simulation." | `create-skill` | Skill authoring, trigger evaluation, and behavior simulation. |
| "Research current options for hosted vector databases and recommend one with sources." | `deep-research` | Multi-source evidence-backed research. |
| "Create a DESIGN.md from these screenshots, Tailwind config, and brand notes; count which references support each section and flag inconsistencies." | `design-extractor` | DESIGN.md extraction with evidence counts and conflicts. |
| "Audit only the primary button color in this DESIGN.md against the current CSS; report the discrepancy without rewriting the document." | `design-extractor` | Focused design audit with a read-only completion boundary. |
| "Use a temporary Podman image to install a RAW converter and write the converted files to /tmp without installing anything on the host." | `ephemeral-container-workbench` | One-off tool installation isolated in a disposable container. |
| "Build this project's GraalVM native binary in Podman using the same toolchain as CI." | `graalvm-native-build` | Native-image build and toolchain parity. |
| "Run this long local build in a background service with a log and desktop notification." | `long-running-jobs` | Durable local command execution with saved status. |
| "Diagnose this native-image build log against CI and give reproduction commands; do not edit application source." | `graalvm-native-build` | Native-build diagnosis with source changes outside scope. |
| "Clean up these Kotlin extensions, nullability checks, and coroutine scope ownership." | `kotlin-code-style` | Kotlin-specific implementation style. |
| "Fix only this Kotlin comment typo using the repository formatter." | `kotlin-code-style` | Mechanical Kotlin edit without a general engineering review. |
| "In this Kotlin multiplatform library, replace runtime platform branches with source-set-owned behavior and add validation tests with positive, negative, round-trip, and boundary cases." | `kotlin-code-style` | Kotlin library style, expect/actual boundaries, validation, and test shape. |
| "Format these Kotlin changes with the repository's ktlint task and run the focused Gradle test in a sandbox where the default Gradle home is read-only." | `kotlin-code-style` | Kotlin-specific formatting and focused Gradle verification workflow. |
| "Review these Kotlin Cucumber feature files and step definitions for BDD quality." | `kotlin-cucumber-tests` | Cucumber feature/step design. |
| "Turn this async workflow into Kotlin Cucumber scenarios where step glue hides protocol details and polls for observable outcomes." | `kotlin-cucumber-tests` | Workflow-level Cucumber with async outcome boundaries. |
| "Take a screenshot of my localhost app with Playwright now that browsermcp is gone." | `playwright-screenshots` | Headless browser screenshot capture without browsermcp. |
| "Verify Playwright can launch Chromium and save a screenshot before using it for UI checks." | `playwright-screenshots` | Browser launch plus screenshot smoke test. |
| "Capture mobile and full-page screenshots of this generated HTML page using a headless browser." | `playwright-screenshots` | Screenshot workflow with viewport/full-page options. |
| "Improve this Spring Boot controller/service/repository package structure and transaction boundary." | `spring-application-code-style` | Spring application architecture. |
| "Clean up this Spring Boot app so controllers stay thin, feature config validates at startup, and async event tests prove downstream observable state." | `spring-application-code-style` | Spring application edges, configuration, async events, and validation. |
| "Run these Spring Boot AOT-backed Gradle test tasks without colliding on processTestAot output." | `spring-application-code-style` | Spring AOT verification and generated-output ownership. |
| "Map transaction submission through account persistence and dependent work, following actual events, workers, and completion callbacks." | `runtime-flow-mapping` | Reconstructing an existing runtime scenario from source. |
| "Compare this sequence diagram with the current implementation; verify calls, event delivery, and after-commit semantics." | `runtime-flow-mapping` | Source-backed runtime map verification without redesign. |
| "A write committed but a consumer has not finished. Trace what publication, worker completion, and callbacks actually guarantee." | `runtime-flow-mapping` | Establishing completion and ordering semantics across existing boundaries. |
| "Decide where this architecture decision belongs in the repo wiki and link related pages." | `wiki` | Durable knowledge-base organization. |
| "Create a small wiki from these architecture notes and link it from README; the repo has no docs directory yet." | `wiki` | Authorized wiki creation includes choosing a conventional location. |
| "Create a local Markdown Kanban board with task dependencies for this repo." | `local-kanban-board` | Persistent repo-local task tracking. |
| "Read the existing Kanban files and report ready tasks without changing the board." | `local-kanban-board` | Read-only board inspection does not require CLI validation. |
| "Use Kanban with planner and executor subagents; keep the main session reviewing persisted plans and completed work." | `orchestrated-kanban-subagents` | Requested coordination model with plans and review. |
| "Resume the Kanban project as coordinator, reviewing task plans before dispatching workers." | `orchestrated-kanban-subagents` | Resumption of the same coordination model. |

## Near misses / should not trigger

| Prompt | Skill that should stay inactive | Better fit |
|---|---|---|
| "We read twelve files and ran the existing tests; nothing new was learned. Summarize the result." | `create-skill` | Normal task reporting. |
| "Write one new skill for inspecting archive contents." | `skill-library-curator` | `create-skill` |
| "Explain the OpenAI article about Astra skills and prompts." | `skill-library-curator` | Official documentation research; no library curation requested. |
| "Use a subagent to review this small patch." | `orchestrated-kanban-subagents` | Ordinary delegated review. |
| "Move TASK-003 to review on the local board." | `orchestrated-kanban-subagents` | `local-kanban-board` |
| "Make a quick checklist in the PR description." | `local-kanban-board` | Normal prose editing. |
| "Run the normal JVM unit tests with the existing Gradle wrapper." | `graalvm-native-build` | The repository's verification workflow. |
| "Run this one-second formatting check." | `long-running-jobs` | Ordinary foreground command execution. |
| "Rename this helper and simplify the nested conditionals." | `component-ownership` | `code-practice` |
| "Rename this helper and simplify the nested conditionals." | `untangle-codebase` | `code-practice` |
| "Should this operation call its collaborators directly or publish an event? Give advice only." | `untangle-codebase` | `component-ownership` |
| "Trace this existing event flow and document its commit boundaries without changing code." | `untangle-codebase` | `runtime-flow-mapping` |
| "Fix a Kotlin Cucumber step definition that leaks scenario state." | `kotlin-code-style` | `kotlin-cucumber-tests` |
| "Explain how to wire a Spring `@ConfigurationProperties` class." | `kotlin-code-style` | `spring-application-code-style` |
| "Make this plain Kotlin value object idiomatic." | `spring-application-code-style` | `kotlin-code-style` |
| "Write generic unit tests for a pure function." | `kotlin-cucumber-tests` | `code-practice` or language-specific test style |
| "Add Given, When, and Then sections to these Java tests." | `kotlin-code-style` | `code-practice` |
| "Show the Java `ConcurrentHashMap.computeIfAbsent` API for computing one independent value per key." | `code-practice` | Java/JDK API documentation |
| "Add boundary and malformed-input tests for this Kotlin serializer." | `kotlin-cucumber-tests` | `kotlin-code-style` |
| "Review whether this event listener should be direct call or event projection across three components." | `spring-application-code-style` | `component-ownership` |
| "Explain how to declare a Spring `@EventListener` method for an existing event." | `component-ownership` | `spring-application-code-style` |
| "Fix this Spring-free coroutine mutex race in a plain Kotlin library." | `spring-application-code-style` | `kotlin-code-style` |
| "Format this plain Kotlin module and run one focused unit test." | `spring-application-code-style` | `kotlin-code-style` |
| "Summarize this provided note more briefly." | `deep-research` | Normal prose editing; follow AGENTS.md writing guidance. |
| "Make this dashboard visually cleaner without producing a DESIGN.md." | `design-extractor` | Frontend design or implementation guidance |
| "Add this CLI to the project Dockerfile so CI can use it." | `ephemeral-container-workbench` | Project container/toolchain maintenance |
| "Use my current Chrome tab and logged-in cookies to inspect this dashboard." | `playwright-screenshots` | Browser bridge or exported auth state |
| "Scrape the latest pricing table from this public website." | `playwright-screenshots` | `firecrawl` or web research tooling |
| "Install a browser extension into my personal Chrome profile." | `playwright-screenshots` | Manual browser setup or browser bridge |
| "Redesign these collaborating services: choose direct calls, domain events, or a projection and assign state ownership." | `runtime-flow-mapping` | `component-ownership` |
| "Move these architecture decision records into the existing wiki and repair their index links." | `runtime-flow-mapping` | `wiki` |
| "Fix spelling in this event-flow document without changing its technical content." | `runtime-flow-mapping` | Normal prose editing |
| "Show how to declare a Spring listener method for this existing event." | `runtime-flow-mapping` | `spring-application-code-style` |
| "Create a reusable skill that maps existing runtime flows." | `runtime-flow-mapping` | `create-skill` |
| "Organize temporary raw scrape outputs from a research run." | `wiki` | `deep-research` working artifacts |

## Realistic workflow prompts

- "Given this mixed `service` package, identify the owning workflows, move behavior to feature-owned homes, and explain the tradeoffs."
- "Given this coordinator that forwards commands and events through handlers, decide which interactions should be direct calls, events, projections, or owned workflows."
- "Given a source-of-truth service that directly calls downstream stale cleanup after a state change, refactor the boundary so required validation stays direct and downstream cleanup is owned by its domain."
- "Extract a DESIGN.md from the existing app screens and CSS, then list conflicting color and spacing evidence."
- "Add a Kotlin Flow endpoint in a Spring WebFlux app; keep coroutine ownership and Spring boundaries clear."
- "Turn these product acceptance notes into Cucumber scenarios and Kotlin step glue without coupling to DTO field names."
- "Using the current code in node and commons only as evidence, extract reusable engineering style guidance without creating a product-specific skill."
- "Update a mixed Java and Kotlin test fixture so all changed code-based tests have Given/When/Then sections, Kotlin is formatted before focused verification, and independent Spring AOT invocations do not write the same generated output concurrently."
- "Audit this local docs folder, merge duplicate knowledge, and create only the durable wiki pages that have clear owners."

## Pass criteria

- Should-trigger prompts choose the expected skill.
- Near-miss prompts choose the adjacent better skill or no skill.
- Realistic workflow prompts load the primary skill and hand off when the dominant concern changes.
