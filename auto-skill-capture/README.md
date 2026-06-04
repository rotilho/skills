# Auto Skill Capture

`auto-skill-capture` helps agents create or update reusable user-owned skills after work that revealed durable procedural knowledge.

Use it when a task was complex, repeated, correction-heavy, tricky to debug, or dependent on local environment conventions. It keeps task history out of skills and focuses on procedures future agents can reuse globally or inside one repo.

## Package Contents

- `SKILL.md` - compact activation and workflow instructions
- `references/skill-writing-criteria.md` - criteria for deciding what belongs in a skill
- `references/self-improve-example.md` - example agent-level self-improvement policy with local skill location bindings
- `templates/new-skill-template.md` - portable starting template for new skills

## Skill Locations

Reusable guidance uses placeholders for skill locations:

- `<global-skill-source>` - source checkout for reusable global/user-owned skills
- `<repo-local-skill-source>` - repo-local source, usually `<target-repo>/.agents/skills`
- `<installed-skill-root>` - generated installed skill locations
- `<global-refresh-command>` - local command that syncs global skills into installed copies

Each machine's local `SELF-IMPROVE.md` should define concrete `skill_locations` bindings. Agents should resolve those bindings at runtime instead of replacing placeholders in reusable skill source.

## Usage Examples

- "We just debugged this same deployment issue again. Capture the reusable procedure as a skill."
- "After this refactor, update any existing skill so future agents follow the same workflow."
- "Create a skill for this repeated local build diagnosis, but do not store branch names or logs."
- "Capture this repo-specific release workflow as a local skill."
- "This debugging pattern applies across repos; make it a global skill."
