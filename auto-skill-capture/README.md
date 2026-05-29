# Auto Skill Capture

`auto-skill-capture` helps agents create or update reusable user-owned skills after work that revealed durable procedural knowledge.

Use it when a task was complex, repeated, correction-heavy, tricky to debug, or dependent on local environment conventions. It keeps task history out of skills and focuses on procedures future agents can reuse globally or inside one repo.

## Package Contents

- `SKILL.md` - compact activation and workflow instructions
- `references/skill-writing-criteria.md` - criteria for deciding what belongs in a skill
- `templates/new-skill-template.md` - portable starting template for new skills

## Skill Locations

Global user-owned skills live in:

```bash
~/IdeaProjects/skills
```

Repo-local skills live in:

```bash
<target-repo>/.agents/skills
```

After global changes, refresh installed skills with:

```bash
npx skills add ~/IdeaProjects/skills/ -g --all -y
```

## Usage Examples

- "We just debugged this same deployment issue again. Capture the reusable procedure as a skill."
- "After this refactor, update any existing skill so future agents follow the same workflow."
- "Create a skill for this repeated local build diagnosis, but do not store branch names or logs."
- "Capture this repo-specific release workflow as a local skill."
- "This debugging pattern applies across repos; make it a global skill."
