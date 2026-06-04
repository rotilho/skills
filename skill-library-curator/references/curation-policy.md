# Curation Policy

Use this policy when reviewing global or repo-local user-owned skills.

## Source Boundary

Curate only the selected source roots:

- Global skills: resolved `<global-skill-source>`
- Repo-local skills: resolved `<repo-local-skill-source>`

Use mixed curation when deciding whether a repo-local skill should stay local, promote to global, or embed into another skill.

Do not modify:

- installed or generated copies under home-level agent folders
- generated repo-local copies such as `<repo>/.codex/skills` or `<repo>/.claude/skills`
- vendor or bundled skills
- third-party registry installs
- package-managed directories such as `node_modules`
- git submodules or externally owned folders
- scratch output under `.workbench`

If ownership is unclear, classify the folder as `exclude` and report the uncertainty.

## Inventory Checklist

For each root-level candidate skill, inspect:

- directory name
- presence of `SKILL.md`
- frontmatter `name` and `description`
- support folders such as `references/`, `templates/`, `scripts/`, and `assets/`
- README or human-facing docs when present
- whether the trigger overlaps another skill
- whether the skill is global or repo-local
- whether a repo-local skill has become promotable to global
- whether the skill should be embedded in an existing skill instead of remaining standalone
- whether instructions are procedural or just descriptive
- whether examples are current, safe, and reusable

Use `rg` when available. Fall back to ordinary file listing and reading commands when it is not.

## Classification

Use these labels in the report:

- `keep`: clear trigger, useful body, no obvious drift
- `patch`: useful skill with weak trigger, vague procedure, stale examples, missing verification, or excessive body length
- `merge`: duplicate or near-duplicate that can be safely consolidated
- `promote`: repo-local skill whose reusable content belongs in global skills
- `embed`: thin or overlapping skill that should be folded into a better local or global target
- `archive`: superseded, unsafe, abandoned, empty, or no longer useful as an active skill
- `exclude`: outside the user-owned source boundary

## Promotion Rules

Promote a repo-local skill to global when:

- the trigger and procedure are useful outside the current repo
- repo-specific paths, product names, commands, ownership facts, and temporary context can be removed cleanly
- the content either deserves a standalone global skill or clearly belongs inside an existing global skill

Do not promote when:

- the skill depends on repo layout, scripts, fixtures, product vocabulary, deployment topology, or local ownership decisions
- the skill contains private, secret, customer, incident, branch, commit, PR, or issue details
- removing repo-specific context would make the guidance vague

When promotion succeeds, archive the repo-local source package under the resolved `<repo-local-skill-source>/.archive/YYYY-MM-DD/<skill-name>/` and add an `ARCHIVE_NOTE.md` naming the global target.

## Embedding Rules

Embed a skill into another skill when:

- it is a caveat, variant, pitfall, or verification step for a stronger existing skill
- keeping it standalone creates trigger noise or duplicate maintenance
- its support files can either move cleanly into the target or stay preserved in the archive

Embed into a global target only when the reusable content is not repo-bound. Otherwise, embed into a repo-local target in the resolved `<repo-local-skill-source>`.

## Patch Rules

Patch vague or outdated skills when the skill still has a valid purpose.

Good patches usually:

- strengthen the frontmatter description
- add clear when-to-use and when-not-to-use boundaries
- replace broad principles with concrete steps
- move long examples or policy into references
- add verification steps
- remove stale one-off details
- keep existing support files unless they are clearly obsolete and archived with the skill

Do not patch by adding filler. A shorter, more triggerable skill is usually better.

## Quality Signals

A healthy skill:

- has a lowercase kebab-case name that matches its folder
- has a trigger-oriented description
- declares or clearly implies global vs repo-local scope
- tells the agent when not to use it
- contains prerequisites when the workflow depends on tools, files, permissions, or environment state
- gives an ordered procedure
- names pitfalls or failure modes
- includes verification
- keeps private or time-sensitive data out of durable instructions

## Report Requirements

Every curation pass should report:

- scope inspected
- skills kept, patched, merged, promoted, embedded, archived, and excluded
- source and target paths for merges, promotions, and embeddings
- reasons for each non-trivial change
- archive paths
- install command result for global changes, or note that no global install was needed
- unresolved risks or follow-up recommendations
