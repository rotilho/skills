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
| `auto-skill-capture` | Creating or updating global or repo-local reusable skills after complex, repeated, correction-heavy, tricky-debugging, or environment-specific work. | The work is routine, one-off, private, temporary, or should remain a task log. |
| `code-practice` | Framework-neutral code quality, naming, boundaries, state, error handling, tests, refactoring. | Kotlin, Spring, or Cucumber-specific rules dominate. |
| `component-collaboration-architecture` | Choosing direct calls, orchestration, events, observers, projections, state ownership, and proxy removal across components. | The task is only local cleanup, language idioms, framework wiring, or test glue. |
| `concise` | Default concise communication, brief updates, tighter rewrites. | User asks for fuller, warmer, formal, legal, or safety-sensitive detail. |
| `create-skill` | Creating, rewriting, or evaluating agent skills and trigger boundaries. | The task is ordinary docs/code work rather than reusable skill behavior. |
| `deep-research` | Evidence-backed research, comparisons, audits, and gap-first source validation. | Routine local code or prompt review with no research need. |
| `design-extractor` | Create or audit `DESIGN.md` from screenshots, Figma, CSS, tokens, brand notes, or app references, including evidence counts and conflicts. | Ordinary frontend implementation when no durable `DESIGN.md` or design extraction is requested. |
| `ephemeral-container-workbench` | Running one-off tools, converters, SDKs, or package installs in a temporary Podman/Docker container instead of mutating the host. | The repo already owns the toolchain, a long-lived service is needed, or the user wants the dependency installed locally. |
| `kotlin-code-style` | Kotlin file/type organization, nullability, extensions, coroutines, Flow, tests. | Spring architecture or Cucumber/BDD is central. |
| `kotlin-cucumber-tests` | Kotlin Cucumber feature files, steps, hooks, fixtures, and executable specs. | Generic unit tests, plain Kotlin style, or Spring test architecture. |
| `skill-library-curator` | Periodic curation of global or repo-local skills, duplicate merges, promotions, embeddings, archive moves, vague skill cleanup, and curation reports. | Creating one new skill without reviewing the broader library. |
| `spring-application-code-style` | Spring Boot application package structure, controllers, repositories, transactions, wiring, integration tests. | Plain Kotlin, framework-neutral code quality, or Spring internals/libraries. |
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
