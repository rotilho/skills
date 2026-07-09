# Trigger Prompt Evals

Use these prompts after changing skill descriptions or overlap boundaries. Expected result means the named skill should be loaded first or clearly chosen as the active domain skill.

## Should trigger

| Prompt | Expected skill | Why |
|---|---|---|
| "Refactor this function for clearer naming and ownership without using framework-specific rules." | `code-practice` | Framework-neutral maintainability. |
| "Diagnose this failing workflow first, then make the smallest compatibility-preserving API change and test the contract directly." | `code-practice` | Evidence-first diagnosis, public-surface safety, and test-level choice without framework specifics. |
| "This module is organized by services and utils; move behavior toward the workflow that owns the state and side effects." | `code-practice` | Behavior ownership and state boundaries in a language-neutral design prompt. |
| "Class A calls five collaborators today. Should it keep direct calls or publish one event and let each owner react?" | `component-collaboration-architecture` | Collaboration shape and ownership decision. |
| "This listener just forwards events to another service. Refactor the flow so behavior and state ownership are clearer." | `component-collaboration-architecture` | Proxy/listener removal across components. |
| "AccountService owns the account state change, but it now imports vote cleanup to mark old votes stale. Break the dependency so the source-of-truth update can notify the downstream cleanup owner." | `component-collaboration-architecture` | Source-of-truth to downstream cleanup boundary should be a collaboration-shape decision. |
| "Rewrite this update in concise mode but keep the warning clear." | `concise` | Communication style and brevity. |
| "Create a new skill for release-note generation and include trigger eval prompts plus a realistic behavior simulation." | `create-skill` | Skill authoring, trigger evaluation, and behavior simulation. |
| "Research current options for hosted vector databases and recommend one with sources." | `deep-research` | Multi-source evidence-backed research. |
| "Create a DESIGN.md from these screenshots, Tailwind config, and brand notes; count which references support each section and flag inconsistencies." | `design-extractor` | DESIGN.md extraction with evidence counts and conflicts. |
| "Use a temporary Podman image to install a RAW converter and write the converted files to /tmp without installing anything on the host." | `ephemeral-container-workbench` | One-off tool installation isolated in a disposable container. |
| "Clean up these Kotlin extensions, nullability checks, and coroutine scope ownership." | `kotlin-code-style` | Kotlin-specific implementation style. |
| "In this Kotlin multiplatform library, replace runtime platform branches with source-set-owned behavior and add validation tests with positive, negative, round-trip, and boundary cases." | `kotlin-code-style` | Kotlin library style, expect/actual boundaries, validation, and test shape. |
| "Review these Kotlin Cucumber feature files and step definitions for BDD quality." | `kotlin-cucumber-tests` | Cucumber feature/step design. |
| "Turn this async workflow into Kotlin Cucumber scenarios where step glue hides protocol details and polls for observable outcomes." | `kotlin-cucumber-tests` | Workflow-level Cucumber with async outcome boundaries. |
| "Take a screenshot of my localhost app with Playwright now that browsermcp is gone." | `playwright-screenshots` | Headless browser screenshot capture without browsermcp. |
| "Verify Playwright can launch Chromium and save a screenshot before using it for UI checks." | `playwright-screenshots` | Browser launch plus screenshot smoke test. |
| "Capture mobile and full-page screenshots of this generated HTML page using a headless browser." | `playwright-screenshots` | Screenshot workflow with viewport/full-page options. |
| "Improve this Spring Boot controller/service/repository package structure and transaction boundary." | `spring-application-code-style` | Spring application architecture. |
| "Clean up this Spring Boot app so controllers stay thin, feature config validates at startup, and async event tests prove downstream observable state." | `spring-application-code-style` | Spring application edges, configuration, async events, and validation. |
| "Decide where this architecture decision belongs in the repo wiki and link related pages." | `wiki` | Durable knowledge-base organization. |

## Near misses / should not trigger

| Prompt | Skill that should stay inactive | Better fit |
|---|---|---|
| "Rename this helper and simplify the nested conditionals." | `component-collaboration-architecture` | `code-practice` |
| "Fix a Kotlin Cucumber step definition that leaks scenario state." | `kotlin-code-style` | `kotlin-cucumber-tests` |
| "Explain how to wire a Spring `@ConfigurationProperties` class." | `kotlin-code-style` | `spring-application-code-style` |
| "Make this plain Kotlin value object idiomatic." | `spring-application-code-style` | `kotlin-code-style` |
| "Write generic unit tests for a pure function." | `kotlin-cucumber-tests` | `code-practice` or language-specific test style |
| "Add boundary and malformed-input tests for this Kotlin serializer." | `kotlin-cucumber-tests` | `kotlin-code-style` |
| "Review whether this event listener should be direct call or event projection across three components." | `spring-application-code-style` | `component-collaboration-architecture` |
| "Explain how to declare a Spring `@EventListener` method for an existing event." | `component-collaboration-architecture` | `spring-application-code-style` |
| "Fix this Spring-free coroutine mutex race in a plain Kotlin library." | `spring-application-code-style` | `kotlin-code-style` |
| "Summarize this provided note more briefly." | `deep-research` | `concise` |
| "Make this dashboard visually cleaner without producing a DESIGN.md." | `design-extractor` | Frontend design or implementation guidance |
| "Add this CLI to the project Dockerfile so CI can use it." | `ephemeral-container-workbench` | Project container/toolchain maintenance |
| "Use my current Chrome tab and logged-in cookies to inspect this dashboard." | `playwright-screenshots` | Browser bridge or exported auth state |
| "Scrape the latest pricing table from this public website." | `playwright-screenshots` | `firecrawl` or web research tooling |
| "Install a browser extension into my personal Chrome profile." | `playwright-screenshots` | Manual browser setup or browser bridge |
| "Organize temporary raw scrape outputs from a research run." | `wiki` | `deep-research` working artifacts |

## Realistic workflow prompts

- "Given this mixed `service` package, identify the owning workflows, move behavior to feature-owned homes, and explain the tradeoffs."
- "Given this coordinator that forwards commands and events through handlers, decide which interactions should be direct calls, events, projections, or owned workflows."
- "Given a source-of-truth service that directly calls downstream stale cleanup after a state change, refactor the boundary so required validation stays direct and downstream cleanup is owned by its domain."
- "Extract a DESIGN.md from the existing app screens and CSS, then list conflicting color and spacing evidence."
- "Add a Kotlin Flow endpoint in a Spring WebFlux app; keep coroutine ownership and Spring boundaries clear."
- "Turn these product acceptance notes into Cucumber scenarios and Kotlin step glue without coupling to DTO field names."
- "Using the current code in node and commons only as evidence, extract reusable engineering style guidance without creating a product-specific skill."
- "Audit this local docs folder, merge duplicate knowledge, and create only the durable wiki pages that have clear owners."

## Pass criteria

- Should-trigger prompts choose the expected skill.
- Near-miss prompts choose the adjacent better skill or no skill.
- Realistic workflow prompts load the primary skill and hand off when the dominant concern changes.
