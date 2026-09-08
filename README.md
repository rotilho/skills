# Skills

Global user-owned agent skills for OpenCode-compatible agents. They emphasize concise, procedural behavior: load the right skill, preserve trigger boundaries, make small safe edits, and verify the result.

## Compatibility

- Target runtime: OpenCode agent skills.
- Skill format: one folder per skill, each with `SKILL.md` YAML frontmatter.
- Canonical format docs: https://opencode.ai/docs/skills/

## Install / refresh

From this repo root:

```bash
npx skills add https://github.com/rotilho/skills -g --agent universal --skill '*' -y
```

This intentionally targets only the universal agent. Do not use `--all` for routine refreshes; in the `skills` CLI it expands to all skills for all supported agents.

OpenCode can also discover skills from `.opencode/skills`, `.claude/skills`, `.agents/skills`, and global equivalents. This repo keeps the user-owned source of truth at the repo root as `<skill-name>/SKILL.md`.

## Skill matrix

User-owned active skills:

| Skill | Use when | Avoid when |
|---|---|---|
| `auto-skill-capture` | Capturing a reusable procedural gap revealed by work, corrections, diagnosis, or environment setup. | The lesson is already covered, routine, private, temporary, or only a task outcome. |
| `code-practice` | Framework-neutral code quality, behavior ownership, evidence-first debugging, trust boundaries, state ownership, compatibility, tests, refactoring. | Kotlin, Spring, or Cucumber-specific rules dominate. |
| `component-collaboration-architecture` | Choosing direct calls, orchestration, domain events, observers, projections, state ownership, proxy removal, and source-of-truth to downstream dependency boundaries. | The task is only local cleanup, language idioms, framework wiring, or test glue. |
| `create-skill` | Creating, rewriting, or evaluating agent skills, trigger boundaries, and realistic behavior simulations. | The task is ordinary docs/code work rather than reusable skill behavior. |
| `deep-research` | Evidence-backed research, comparisons, audits, and gap-first source validation. | Routine local code or prompt review with no research need. |
| `design-extractor` | Create or audit `DESIGN.md` from screenshots, Figma, CSS, tokens, brand notes, or app references, including evidence counts and conflicts. | Ordinary frontend implementation when no durable `DESIGN.md` or design extraction is requested. |
| `ephemeral-container-workbench` | Running one-off tools, converters, SDKs, or package installs in a temporary Podman/Docker container instead of mutating the host. | The repo already owns the toolchain, a long-lived service is needed, or the user wants the dependency installed locally. |
| `graalvm-native-build` | Building or diagnosing GraalVM native images in disposable containers with the project's toolchain and CI settings. | Ordinary JVM builds or unrelated temporary tooling. |
| `kotlin-code-style` | Kotlin file/type organization, concept-owned helpers, validation shape, multiplatform source sets, nullability, coroutines, Flow, tests. | Spring architecture or Cucumber/BDD is central. |
| `kotlin-cucumber-tests` | Kotlin Cucumber workflow scenarios, feature files, steps, hooks, fixtures, async outcomes, and executable specs. | Generic unit tests, dense validator/serializer cases, plain Kotlin style, or Spring test architecture. |
| `local-kanban-board` | Creating or maintaining repo-local Markdown task tracking, dependencies, and resumable board state. | One-off checklists or external project trackers. |
| `orchestrated-kanban-subagents` | Coordinating requested Kanban work through task-scoped planners, executors, and review, with persisted plans and results. | Ordinary subagent use or task tracking without this coordination model. |
| `playwright-screenshots` | Browser screenshots, visual verification, page smoke tests, or headless browser capture without browsermcp. | The task needs the user's already-open browser session, extensions, active tabs, or existing cookies. |
| `skill-library-curator` | Periodic curation of global or repo-local skills, duplicate merges, promotions, embeddings, archive moves, vague skill cleanup, and curation reports. | Creating one new skill without reviewing the broader library. |
| `spring-application-code-style` | Spring Boot application package structure, thin controllers, feature-owned config, events, validation boundaries, transactions, wiring, integration tests. | Plain Kotlin, framework-neutral code quality, or Spring internals/libraries. |
| `wiki` | Maintaining durable repo wiki/knowledge-base pages and deciding where knowledge belongs. | Temporary scratch notes or research collection that should stay in `.workbench/`. |

## External skills

| Skill | Source | Curation rule |
|---|---|---|
| `humanizer` | Git submodule at `humanizer/` | Treat as externally owned. Inspect or report it during curation, but do not edit, merge, or archive it unless explicitly requested. |

## Trigger evals

Use `evals/trigger-prompts.md` as a lightweight fixture set when changing descriptions, overlap boundaries, or skill instructions.

## Canonical sources

- OpenCode agent skills: https://opencode.ai/docs/skills/
- Kotlin coding conventions: https://kotlinlang.org/docs/coding-conventions.html
- Kotlin coroutines: https://kotlinlang.org/docs/coroutines-overview.html
- Spring Boot reference: https://docs.spring.io/spring-boot/index.html
- Cucumber documentation: https://cucumber.io/docs/
- Cucumber JVM: https://github.com/cucumber/cucumber-jvm
