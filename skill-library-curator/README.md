# Skill Library Curator

Review the purpose, overlap, and maintenance cost of user-owned skills. Keep good guidance, remove rules that do not improve behavior, and consolidate only where one skill can clearly own the workflow.

Every global or repo-local review applies the [OpenAI skills and prompts guide](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra). The checks are embedded in `SKILL.md`, including relevant agent instructions and completion boundaries.

`SKILL.md` contains the full review, merge, promotion, archive, and verification procedure. Local agent instructions supply source roots and any global refresh command. Installed and externally owned packages stay read-only unless explicitly authorized.

Examples:

- "Review every skill and remove unnecessary complexity."
- "Merge duplicate user-owned skills and archive the old packages."
- "Review this repo's local skills for global promotion."
- "Audit all global skills against the Astra skills and prompts guide."
- "Produce a curation report without changing vendor skills."
