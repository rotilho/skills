# Skill Library Curator

`skill-library-curator` helps agents maintain global and repo-local user-owned Agent Skills.

Use it for periodic reviews, vague skill cleanup, duplicate consolidation, local-to-global promotion, embedding thin skills into stronger skills, archive moves, and curation reports. It is intentionally conservative: patch useful skills, merge clear duplicates, promote only sanitized reusable content, and archive instead of deleting.

## Package Contents

- `SKILL.md` - compact curation workflow
- `references/curation-policy.md` - inspection, classification, and patching policy
- `references/merge-policy.md` - duplicate merge and archive policy
- `templates/curation-report-template.md` - final report template

## Skill Locations

Reusable guidance uses placeholders for skill locations:

- `<global-skill-source>` - source checkout for reusable global/user-owned skills
- `<repo-local-skill-source>` - repo-local source, usually `<target-repo>/.agents/skills`
- `<installed-skill-root>` - generated installed skill locations
- `<global-refresh-command>` - local command that syncs global skills into installed copies

Each machine's local `SELF-IMPROVE.md` should define concrete `skill_locations` bindings. Agents should resolve those bindings at runtime instead of replacing placeholders in reusable skill source.

## Usage Examples

- "Review my skills library and patch vague skill descriptions."
- "Find duplicate user-owned skills, merge the clear duplicates, and archive the old folders."
- "Run a curation pass and produce a report, but do not touch vendor skills."
- "Review this repo's local skills and promote any that now belong globally."
- "Embed thin local skills into stronger existing skills when they do not need to stand alone."
