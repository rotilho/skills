---
name: "auto-skill-capture"
version: "1.3.2"
description: "Create or update global or repo-local Agent Skills after complex, repeated, correction-heavy, tricky-debugging, or environment-specific work. Use near the end of substantial tasks when procedural knowledge was learned, when a user asks to capture a workflow as a skill, or when repeated corrections show that future agents need durable instructions."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "skill-authoring"
  style: "concise"
---

# Auto Skill Capture

Use this skill to turn reusable procedural knowledge into a global or repo-local Agent Skill.

## Reference files

- Read `references/skill-writing-criteria.md` when deciding whether to create, update, or skip a skill.
- Read `references/self-improve-example.md` as a concrete example of agent-level self-improvement policy when aligning local skill location bindings, capture criteria, curation rules, or third-party skill safety.
- Use `templates/new-skill-template.md` when creating a new skill from scratch.

## Local skill location bindings

Before creating, updating, or installing skills, resolve these placeholders from local `skill_locations` in `SELF-IMPROVE.md` or equivalent local agent context:

- `<global-skill-source>`: source checkout for reusable global/user-owned skills
- `<repo-local-skill-source>`: repo-local source, usually `<target-repo>/.agents/skills`
- `<installed-skill-root>`: configured generated installed skill locations
- `<global-refresh-command>`: local command that syncs `<global-skill-source>` into the configured installed skill targets

Keep these placeholders inside reusable skill source files. Use the resolved local values only for actual filesystem operations, archive paths, reports, and refresh commands. If a needed binding is missing or still ambiguous, ask the user before touching files.

## When to use

Trigger after substantial work when:
- the task required repeated corrections, tricky diagnosis, or environment-specific setup
- the same workflow is likely to recur
- the user asks to capture, remember, codify, or convert a workflow into a skill
- existing skills failed to cover a reusable procedure
- the reusable lesson may belong either globally or only inside the current repo

Skip routine one-off work, transient project status, PR bookkeeping, and facts that will quickly go stale.

## Hard constraints

- Use `<global-skill-source>` for global user-owned skills after resolving it from local bindings.
- Use `<repo-local-skill-source>` for repo-local skills after resolving it from local bindings.
- Search repo-local and global source roots before creating a new skill.
- Prefer updating an existing relevant skill in the correct source root over creating a duplicate.
- Treat installed or generated copies under `~/.agents/skills`, `~/.codex/skills`, `~/.claude/skills`, `.codex/skills`, `.claude/skills`, or generated skill directories as read-only unless explicitly asked.
- Keep repo-local facts, private details, and product-only assumptions out of global skills.
- Exclude task progress, PR numbers, issue numbers, branch names, commit hashes, secrets, private data, temporary facts, and stale one-off details.
- Skills are procedural memory, not completed-work logs.
- Keep `SKILL.md` compact; move longer criteria, examples, and templates into bundled files.
- Use valid YAML frontmatter and quote string values.
- After changing global source skills, run the resolved `<global-refresh-command>`.
- Use the resolved refresh command exactly; `--all` broadens installation beyond the universal target.
- For repo-local-only changes, verify the files in the resolved `<repo-local-skill-source>`; run `<global-refresh-command>` only when a global skill also changed.

## Procedure

1. Identify the reusable lesson.
   - Extract the procedure, decision rule, or environment constraint that would help a future agent.
   - Strip away run-specific details and task history.

2. Choose the skill placement.
   - Choose `global` when the procedure applies across multiple repos, tools, or workflows.
   - Choose `repo-local` when the procedure depends on one repo's structure, scripts, product language, deployment shape, tests, or ownership boundaries.
   - If the lesson may generalize later but was first learned in one repo, capture it repo-local first and let curation promote it later.
   - Treat placement as a source-root decision. Keep skill content focused on the reusable procedure.

3. Inventory existing skills.
   - For repo-local placement, inspect the resolved `<repo-local-skill-source>` first.
   - Inspect the resolved `<global-skill-source>` for global owners or broader duplicates.
   - Search names, descriptions, and `SKILL.md` bodies for overlapping triggers in both source roots.
   - If a good owner exists, update it instead of adding a new folder.

4. Decide the change type.
   - Update an existing skill when the new behavior fits its trigger boundary.
   - Create a new skill only when the procedure has a distinct workflow, audience, or activation condition.
   - Skip capture when the lesson lacks reusable value or cannot be made safe without private context.

5. Write the skill package.
   - Include trigger conditions, when not to use, prerequisites, procedure, pitfalls, verification, and examples.
   - Put detailed writing rules or examples in `references/`.
   - Put reusable starting points in `templates/`.
   - Omit placement bookkeeping such as `metadata.scope` or a `## Scope` section.
   - Include repo assumptions only when they affect how the procedure should run.
   - Use ordinary file operations as a fallback if a skills CLI is unavailable.

6. Verify the package.
   - Confirm the folder name matches the `name` frontmatter.
   - Check that the description is trigger-oriented.
   - Check that captured content excludes temporary facts, secrets, IDs, branch names, commit hashes, and logs.
   - Check that repo-local details stayed in the repo-local source root and global source skills remain portable.
   - Run a lightweight trigger check with realistic should-trigger and should-not-trigger examples.
   - If global skills changed, run the resolved `<global-refresh-command>` and record whether it succeeded.

## Pitfalls

- Write reusable procedure, not a diary of what just happened.
- Create a new skill for reusable lessons, not task difficulty alone.
- Keep private logs, credentials, endpoints, customer data, and repository-specific secrets out of skills.
- Keep repo-specific paths, scripts, and product assumptions in repo-local skills.
- Put clearly cross-repo procedures in the global source root.
- Preserve exact commands only when the command itself is the durable procedure.
- Keep examples free of stale project details that will mislead future agents.

## End-of-task self-improvement checklist

Before the final reply on substantial work, ask:
- Did this task teach a reusable procedure or environment rule?
- Should it be written under the global source root or a repo-local source root?
- Is there already a skill in the resolved `<repo-local-skill-source>` or `<global-skill-source>` that should own it?
- Would saving it improve future agent behavior without preserving task history?
- Did I remove private, stale, and one-off details?
- Did I verify the skill package and run the global install command only if global skills changed?

## Final response

Report:
- placement: `global` or `repo-local`
- created or updated source skill paths
- whether the resolved `<global-refresh-command>` ran and whether it succeeded
- one or two usage examples that should trigger the captured skill
