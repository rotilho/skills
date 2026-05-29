---
name: "skill-library-curator"
version: "1.1.0"
description: "Review, improve, merge, promote, embed, deduplicate, and archive global or repo-local Agent Skills. Use for periodic skill library curation in ~/IdeaProjects/skills or <repo>/.agents/skills, vague or outdated skill cleanup, duplicate consolidation, archive planning, and curation reports."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "skill-library-maintenance"
  scope: "global"
  style: "concise"
---

# Skill Library Curator

Use this skill to keep global and repo-local user-owned skill libraries coherent, current, and deduplicated.

## Reference files

- Read `references/curation-policy.md` before reviewing or patching skills.
- Read `references/merge-policy.md` before merging, promoting, embedding, or archiving skills.
- Use `templates/curation-report-template.md` for the final curation report.

## When to use

Trigger for work like:
- periodically review the user-owned skills library
- improve vague, stale, overlapping, or hard-to-trigger skills
- merge clear duplicates
- promote repo-local skills that have become globally reusable
- embed thin or overlapping skills into a better local or global owner
- archive unused or superseded skills
- produce a skill curation report

Do not use for creating one new skill from a fresh workflow unless the task also asks to review or curate the broader library.

## Hard constraints

- Treat `~/IdeaProjects/skills` as the global user-owned skills source.
- Treat `<target-repo>/.agents/skills` as the repo-local user-owned skills source.
- Inspect the requested source root before modifying anything.
- Do not modify vendor, bundled, third-party, registry-installed, package-managed, or git-submodule skills unless explicitly requested.
- Do not edit installed or generated copies under `~/.agents/skills`, `~/.codex/skills`, `~/.claude/skills`, `.codex/skills`, `.claude/skills`, or generated skill directories unless explicitly asked.
- Patch vague or outdated skills in place when their identity is still valid.
- Merge clear duplicates into the strongest target skill.
- Promote repo-local skills to global only when their reusable content is no longer repo-bound.
- Embed a skill into another skill when it is only a caveat, workflow variant, pitfall, or verification step for the target.
- Never delete a skill immediately; archive instead.
- Archive full global skill packages under `~/IdeaProjects/skills/.archive/YYYY-MM-DD/<skill-name>/`.
- Archive full repo-local skill packages under `<target-repo>/.agents/skills/.archive/YYYY-MM-DD/<skill-name>/`.
- Preserve `SKILL.md`, `README.md`, `references/`, `templates/`, `scripts/`, `assets/`, and any other support files when archiving.
- Produce a curation report after changes.
- After global changes, run `npx skills add ~/IdeaProjects/skills/ -g --all -y`.
- For repo-local-only changes, verify files and report that no global install was needed.

## Procedure

1. Choose curation mode.
   - `global`: inspect and change `~/IdeaProjects/skills`.
   - `repo-local`: inspect and change `<target-repo>/.agents/skills`.
   - `mixed`: inspect both roots when deciding whether a local skill should stay local, promote to global, or embed into another skill.

2. Inventory the library.
   - List root-level skill directories under the selected source root.
   - Exclude `.git`, `.archive`, package caches, generated install folders, and clearly external/vendor directories.
   - Note missing `SKILL.md`, invalid frontmatter, weak descriptions, duplicate names, and overlapping triggers.

3. Classify each candidate.
   - `keep`: clear, current, and non-overlapping.
   - `patch`: useful but vague, outdated, bloated, or missing verification.
   - `merge`: clear duplicate or near-duplicate with another user-owned skill.
   - `promote`: repo-local skill should become global or be merged into a global skill.
   - `embed`: skill should be folded into a better local or global target skill.
   - `archive`: superseded, empty, unsafe, or no longer useful.
   - `exclude`: vendor, package-managed, third-party, or submodule-owned.

4. Patch skills conservatively.
   - Keep `SKILL.md` compact and trigger-oriented.
   - Move long policy, examples, and templates into bundled files.
   - Preserve useful support files and existing skill identity.
   - Use ordinary file operations as a fallback if a skills CLI is unavailable.

5. Merge, promote, or embed carefully.
   - Choose the target skill with the clearest name, strongest trigger, and best support files.
   - Move unique reusable content into the target package.
   - Strip repo-specific facts before promoting content to global.
   - Prefer embedding over keeping a thin duplicate skill active.
   - Remove task logs, stale examples, and private details during the merge, promotion, or embedding.
   - Archive the superseded package instead of deleting it.

6. Archive instead of deleting.
   - Create the matching `.archive/YYYY-MM-DD/` under the source root.
   - Move the entire superseded skill directory under that date folder.
   - Preserve every support file unless the user explicitly asks for cleanup.
   - Add `ARCHIVE_NOTE.md` explaining the archive reason and target skill when applicable.

7. Verify and install.
   - Check frontmatter names match folder names for active skills.
   - Check no active duplicate names remain.
   - Check archived skills are complete packages.
   - Run `npx skills add ~/IdeaProjects/skills/ -g --all -y` only if global skills changed.

8. Report the outcome.
   - Use the curation report template.
   - Include scope, inspected skills, patches, merges, promotions, embeddings, archives, exclusions, install result, and residual risks.

## Pitfalls

- Do not treat installed/generated copies as source.
- Do not silently rewrite a specialized skill into a generic one.
- Do not archive a skill just because it is small.
- Do not merge skills with similar words but different trigger boundaries.
- Do not promote local product vocabulary, repo paths, secrets, or operational facts into global skills.
- Do not leave a superseded local skill active after successful promotion or embedding.
- Do not discard support files when moving a skill to the archive.

## Verification

- Source library was inspected before changes.
- Every active skill has one `SKILL.md` with valid frontmatter.
- Every modified skill remains triggerable and procedural.
- Promoted global content is free of repo-only assumptions.
- Archived packages include all original support files.
- The curation report names what changed and why.
- `npx skills add ~/IdeaProjects/skills/ -g --all -y` was run and recorded when global skills changed, or the report states that no global install was needed.
