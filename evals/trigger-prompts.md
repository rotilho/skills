# Trigger Prompt Evals

Use these prompts after changing skill descriptions or overlap boundaries. Expected result means the named skill should be loaded first or clearly chosen as the active domain skill.

## Should trigger

| Prompt | Expected skill | Why |
|---|---|---|
| "Refactor this function for clearer naming and ownership without using framework-specific rules." | `code-practice` | Framework-neutral maintainability. |
| "Rewrite this update in concise mode but keep the warning clear." | `concise` | Communication style and brevity. |
| "Create a new skill for release-note generation and include trigger eval prompts." | `create-skill` | Skill authoring and trigger evaluation. |
| "Research current options for hosted vector databases and recommend one with sources." | `deep-research` | Multi-source evidence-backed research. |
| "Clean up these Kotlin extensions, nullability checks, and coroutine scope ownership." | `kotlin-code-style` | Kotlin-specific implementation style. |
| "Review these Kotlin Cucumber feature files and step definitions for BDD quality." | `kotlin-cucumber-tests` | Cucumber feature/step design. |
| "Improve this Spring Boot controller/service/repository package structure and transaction boundary." | `spring-application-code-style` | Spring application architecture. |
| "Decide where this architecture decision belongs in the repo wiki and link related pages." | `wiki` | Durable knowledge-base organization. |

## Near misses / should not trigger

| Prompt | Skill that should stay inactive | Better fit |
|---|---|---|
| "Fix a Kotlin Cucumber step definition that leaks scenario state." | `kotlin-code-style` | `kotlin-cucumber-tests` |
| "Explain how to wire a Spring `@ConfigurationProperties` class." | `kotlin-code-style` | `spring-application-code-style` |
| "Make this plain Kotlin value object idiomatic." | `spring-application-code-style` | `kotlin-code-style` |
| "Write generic unit tests for a pure function." | `kotlin-cucumber-tests` | `code-practice` or language-specific test style |
| "Summarize this provided note more briefly." | `deep-research` | `concise` |
| "Organize temporary raw scrape outputs from a research run." | `wiki` | `deep-research` working artifacts |

## Realistic workflow prompts

- "Given this mixed `service` package, identify the owning workflows, move behavior to feature-owned homes, and explain the tradeoffs."
- "Add a Kotlin Flow endpoint in a Spring WebFlux app; keep coroutine ownership and Spring boundaries clear."
- "Turn these product acceptance notes into Cucumber scenarios and Kotlin step glue without coupling to DTO field names."
- "Audit this local docs folder, merge duplicate knowledge, and create only the durable wiki pages that have clear owners."

## Pass criteria

- Should-trigger prompts choose the expected skill.
- Near-miss prompts choose the adjacent better skill or no skill.
- Realistic workflow prompts load the primary skill and hand off when the dominant concern changes.
