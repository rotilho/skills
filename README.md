# Skills

Repo-local agent skills for OpenCode-compatible agents. They emphasize concise, procedural behavior: load the right skill, preserve trigger boundaries, make small safe edits, and verify the result.

## Compatibility

- Target runtime: OpenCode agent skills.
- Skill format: one folder per skill, each with `SKILL.md` YAML frontmatter.
- Canonical format docs: https://opencode.ai/docs/skills/

## Install / refresh

From this repo root:

```bash
npx skills add ~/IdeaProjects/skills/ -g -y --all
```

OpenCode can also discover skills from `.opencode/skills`, `.claude/skills`, `.agents/skills`, and global equivalents. This repo keeps the source of truth at the repo root as `<skill-name>/SKILL.md`.

## Skill matrix

| Skill | Use when | Avoid when |
|---|---|---|
| `code-practice` | Framework-neutral code quality, naming, boundaries, state, error handling, tests, refactoring. | Kotlin, Spring, or Cucumber-specific rules dominate. |
| `component-collaboration-architecture` | Choosing direct calls, orchestration, events, observers, projections, state ownership, and proxy removal across components. | The task is only local cleanup, language idioms, framework wiring, or test glue. |
| `concise` | Default concise communication, brief updates, tighter rewrites. | User asks for fuller, warmer, formal, legal, or safety-sensitive detail. |
| `create-skill` | Creating, rewriting, or evaluating agent skills and trigger boundaries. | The task is ordinary docs/code work rather than reusable skill behavior. |
| `deep-research` | Evidence-backed research, comparisons, audits, and gap-first source validation. | Routine local code or prompt review with no research need. |
| `design-extractor` | Create or audit `DESIGN.md` from screenshots, Figma, CSS, tokens, brand notes, or app references, including evidence counts and conflicts. | Ordinary frontend implementation when no durable `DESIGN.md` or design extraction is requested. |
| `kotlin-code-style` | Kotlin file/type organization, nullability, extensions, coroutines, Flow, tests. | Spring architecture or Cucumber/BDD is central. |
| `kotlin-cucumber-tests` | Kotlin Cucumber feature files, steps, hooks, fixtures, and executable specs. | Generic unit tests, plain Kotlin style, or Spring test architecture. |
| `spring-application-code-style` | Spring Boot application package structure, controllers, repositories, transactions, wiring, integration tests. | Plain Kotlin, framework-neutral code quality, or Spring internals/libraries. |
| `wiki` | Maintaining durable repo wiki/knowledge-base pages and deciding where knowledge belongs. | Temporary scratch notes or research collection that should stay in `.workbench/`. |

## Trigger evals

Use `evals/trigger-prompts.md` as a lightweight fixture set when changing descriptions, overlap boundaries, or skill instructions.

## Canonical sources

- OpenCode agent skills: https://opencode.ai/docs/skills/
- Kotlin coding conventions: https://kotlinlang.org/docs/coding-conventions.html
- Kotlin coroutines: https://kotlinlang.org/docs/coroutines-overview.html
- Spring Boot reference: https://docs.spring.io/spring-boot/index.html
- Cucumber documentation: https://cucumber.io/docs/
- Cucumber JVM: https://github.com/cucumber/cucumber-jvm
