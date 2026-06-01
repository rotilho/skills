# Self-Improving Skills

This agent should maintain reusable procedural knowledge over time. When it completes substantial work, solves a non-obvious problem, learns a stable workflow, or receives a user correction, it should consider creating or updating an Agent Skill.

Skills are procedural memory. They are reusable workflows, commands, pitfalls, verification steps, and stable environment or project conventions.

Skills are not task logs. Do not save temporary progress, PR numbers, issue numbers, commit hashes, branch names, one-off outcomes, secrets, credentials, private user data, or facts likely to become stale within a week.

## Skill Source Roots

The global source of user-owned skills is:

```text
~/IdeaProjects/skills
```

The repo-local source of user-owned skills is:

```text
<target-repo>/.agents/skills
```

Use global skills for reusable procedures that apply across repos, tools, or workflows. Use repo-local skills for procedures that depend on one repo's structure, scripts, product language, deployment topology, test fixtures, or ownership boundaries.

Do not directly edit installed/generated skill copies under:

- `~/.agents/skills/`
- `~/.codex/skills/`
- `~/.claude/skills/`
- `.codex/skills/`
- `.claude/skills/`
- generated skill directories

unless the user explicitly asks.

Instead:

1. Make global skill source changes under `~/IdeaProjects/skills`.
2. Make repo-local skill source changes under `<target-repo>/.agents/skills`.
3. After creating, updating, merging, promoting, embedding, or archiving global skills, run the canonical refresh command:

```bash
npx skills add ~/IdeaProjects/skills/ -g --all -y
```

This installs/syncs the global skill source into the agent-specific skill locations. Later sections refer to this as the canonical refresh command.

## Skill Source Editing Rules

When asked to create a new skill:

- Choose global scope when the skill is reusable across repos.
- Choose repo-local scope when the skill is tied to the current repo.
- Create global skills under `~/IdeaProjects/skills`.
- Create repo-local skills under `<target-repo>/.agents/skills`.
- Run the canonical refresh command only when global skills changed.

When asked to update, rewrite, merge, or curate an existing skill:

- First check whether that skill exists under the current repo's `.agents/skills`.
- Then check whether it exists under `~/IdeaProjects/skills`.
- Edit the source copy in the correct scope.
- Run the canonical refresh command only when global skills changed.

If a skill exists only in an installed/generated location but does not exist under the correct repo-local or global source root:

- Do not modify the installed/generated copy.
- Treat it as non-canonical.
- If a change is needed, create or import a source version under the correct repo-local or global root first.
- Run the canonical refresh command only when global skills changed.

If `~/IdeaProjects/skills` or `<target-repo>/.agents/skills` does not exist and is the selected source root, create it before creating new skills.

## Skill Roots

For global user-owned skills, the source root is:

```text
~/IdeaProjects/skills
```

For repo-local user-owned skills, the source root is:

```text
<target-repo>/.agents/skills
```

Installed skill directories are deployment targets, not source-of-truth locations.

The agent may inspect installed skill directories to understand what is currently available, but should not modify them directly unless explicitly asked.

After changing global skills under `~/IdeaProjects/skills`, run the canonical refresh command. Repo-local-only changes do not require the global refresh command.

A skill is a directory containing `SKILL.md`.

Skill support files may live under:

- `references/`
- `templates/`
- `scripts/`
- `assets/`

## End-of-Task Self-Improvement

At the end of every substantial task, perform a brief self-improvement check.

Create or update a skill when any of these are true:

- The task required 5 or more meaningful steps.
- A tricky or non-obvious error was solved.
- The user corrected the agent’s approach.
- A reusable workflow was discovered.
- A stable project, tool, API, or environment convention was learned.
- The same kind of task is likely to recur.
- A reusable verification or debugging procedure was discovered.

Do not create or update a skill when:

- The task was trivial.
- The information is temporary task progress.
- The information is a PR number, issue number, branch name, commit hash, or release artifact.
- The information is secret or private.
- The fact will probably be stale within a week.
- The knowledge is generic and already obvious.
- The skill would duplicate an existing skill.

Before creating a new skill, search existing skills by name and content in both the current repo's `.agents/skills` and `~/IdeaProjects/skills`. Prefer patching an existing skill in the correct scope over creating a duplicate.

## Skill Creation

When creating a skill, create a complete skill package, not just a note.

Every `SKILL.md` should include:

- YAML frontmatter with `name`, `version`, `description`, `license`, `compatibility`, and `metadata`.
- A quoted semantic `version` string, bumped when the skill behavior changes.
- Scope metadata or clear scope guidance when global vs repo-local matters.
- Clear trigger conditions.
- When not to use.
- Prerequisites.
- Step-by-step procedure.
- Pitfalls and failure modes.
- Verification steps.
- Examples when useful.

The `description` field is the primary activation signal. It must be specific, concrete, and written in language the user is likely to use.

Good descriptions start with phrases like:

- `Use when...`
- `Review when...`
- `Run when...`
- `Apply when...`

Avoid vague descriptions like:

- `Helps with development.`
- `Useful utilities.`
- `General workflow.`

Do not include TODO placeholders in skills.

## Skill Updates

When a relevant skill already exists and the current task reveals missing or outdated guidance, patch the existing skill immediately.

Patch a skill when:

- A documented command is wrong.
- A prerequisite is missing.
- A failure mode was discovered.
- Verification steps are incomplete.
- The skill activates too broadly or too narrowly.
- The user corrected behavior that the skill should prevent in the future.

Prefer small, incremental patches over large rewrites.

## Skill Curation

Periodically, or when asked to clean up skills, curate the skill library.

Curation scope:

- Modify global skills under `~/IdeaProjects/skills`.
- Modify repo-local skills under `<target-repo>/.agents/skills`.
- Do not curate, rewrite, merge, archive, or delete skills from installed/generated locations unless explicitly requested.

Curation goals:

- Remove duplication.
- Improve vague descriptions.
- Merge overlapping skills.
- Promote repo-local skills that have become globally reusable.
- Embed thin or overlapping skills into stronger local or global skills.
- Archive stale or low-value skills.
- Fix broken links.
- Move long details into `references/`.
- Ensure skills have prerequisites, pitfalls, and verification steps.
- Preserve useful support files.

Classify each skill as one of:

- keep
- patch
- merge
- promote
- embed
- archive
- needs-human-review

Never permanently delete a skill during curation. Archive it instead.

Archive path format:

```text
~/IdeaProjects/skills/.archive/YYYY-MM-DD/<skill-name>/
<target-repo>/.agents/skills/.archive/YYYY-MM-DD/<skill-name>/
```

When archiving, preserve the complete skill package:

- `SKILL.md`
- `README.md`
- `references/`
- `templates/`
- `scripts/`
- `assets/`
- any other support files

Add `ARCHIVE_NOTE.md` explaining why the skill was archived, when it was archived, and where it was merged if applicable.

After curation, run the canonical refresh command only when global skills changed.

## Merge Policy

When two skills overlap:

1. Choose the broader, clearer, better-maintained skill as the merge target.
2. Move useful procedures, pitfalls, examples, and verification steps into the target.
3. Preserve and re-home needed support files.
4. Rewrite relative links after moving files.
5. Archive the absorbed skill rather than deleting it.
6. Add a note to the archived skill explaining the merge target.
7. Run the canonical refresh command after the merge only when global skills changed.

Do not flatten a skill package by copying only `SKILL.md` while losing its references, templates, scripts, or assets.

## Promotion And Embedding

During curation, a repo-local skill may be promoted to global when its procedure applies across repos after removing repo-specific paths, product language, commands, ownership facts, and temporary context.

A skill may be embedded into another skill when it is only a caveat, workflow variant, pitfall, or verification step for the target skill.

Do not promote private, repo-bound, or product-specific details into global skills. If promotion or embedding is not clearly safe, keep both skills active and report `needs-human-review`.

## Third-Party Skill Safety

Do not modify bundled, vendor, third-party, registry-installed, package-managed, or git-submodule skills unless explicitly asked.

Treat a skill as third-party or vendor-owned if:

- It is inside a git submodule.
- It has a remote upstream not controlled by the user.
- It is installed from a public skill registry.
- Its README or metadata says it is externally maintained.
- It is managed by a package manager or installer.

For third-party skills, prefer creating a local wrapper or companion skill under the correct repo-local or global source root instead of editing the original.

## Scheduled Skill Maintenance

When running periodic skill maintenance, use this workflow:

1. Locate the global skills root at `~/IdeaProjects/skills`.
2. Locate repo-local skills at `<target-repo>/.agents/skills` when curating a specific repo.
3. Inventory every skill directory containing `SKILL.md` in the selected roots.
4. Detect third-party/vendor/package-managed skills and mark them read-only unless explicitly requested.
5. Classify each user-owned skill as keep, patch, merge, promote, embed, archive, or needs-human-review.
6. Apply low-risk patches first.
7. Merge, promote, or embed only when the target is obvious and safe.
8. Archive instead of deleting.
9. Preserve full skill packages when moving, merging, promoting, or embedding.
10. Validate frontmatter, links, and referenced support files.
11. Run the canonical refresh command after global changes.
12. Write a curation report.

The curation report should include:

- Summary
- Skills inspected
- Skills kept
- Skills patched
- Skills merged
- Skills promoted
- Skills embedded
- Skills archived
- Skills skipped
- Human review needed
- Validation results
- Follow-up recommendations

Before making broad changes affecting more than 5 skills, stop and produce a proposed plan instead of applying changes.

## Automatic Behavior

Act proactively. If a task clearly produced reusable procedural knowledge, create or update the relevant skill before finishing.

If the change is low-risk and local to user-owned skills under `~/IdeaProjects/skills` or `<target-repo>/.agents/skills`, apply it directly. Run the canonical refresh command only when global skills changed.

Ask before making broad or destructive changes, including:

- archiving many skills,
- modifying third-party skills,
- rewriting a large skill library,
- changing executable scripts,
- deleting anything permanently.

Prefer patching existing skills over creating new skills. Prefer creating reusable procedural knowledge over saving task-specific logs.
