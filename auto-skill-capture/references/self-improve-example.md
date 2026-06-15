# Self-Improving Skills

This is a portable example for a local agent-level self-improvement policy.

Use it as the starting point for a machine-local file such as:

```text
~/.agents/SELF-IMPROVE.md
```

The reusable skill source should keep placeholders such as `<global-skill-source>`.
The local `SELF-IMPROVE.md` should define concrete `skill_locations` bindings so
agents can resolve those placeholders at runtime.

## Installing This Policy Locally

When the user asks to install, enable, or set up self-improving skills:

1. Copy this file to the local agent instruction location, usually `~/.agents/SELF-IMPROVE.md`, unless the user names another location.
2. Fill `skill_locations` with concrete paths and commands for the current machine.
3. If any required value is unknown, ask the user before continuing.
4. Do not replace placeholders inside reusable skill source files.
5. Use the local bindings at runtime when a skill says `<global-skill-source>`, `<repo-local-skill-source>`, `<installed-skill-root>`, or `<global-refresh-command>`.

Useful setup prompt:

```text
Install the self-improvement policy from auto-skill-capture/references/self-improve-example.md.
Copy it to the right local instruction file and fill the skill_locations bindings for this machine.
```

## Local Skill Location Bindings

Each machine should define these bindings in its local `SELF-IMPROVE.md`.

Home-machine example:

```yaml
skill_locations:
  global-skill-source: "~/IdeaProjects/skills"
  repo-local-skill-source: "<target-repo>/.agents/skills"
  installed-skill-roots:
    - "~/.agents/skills"
  global-refresh-command: "npx skills add ~/IdeaProjects/skills/ -g --agent universal --skill '*' -y"
```

This example intentionally refreshes only the universal agent. Do not replace it with `--all` unless the user explicitly wants every supported agent updated.

Work-machine example:

```yaml
skill_locations:
  global-skill-source: "<work-skills-source>"
  repo-local-skill-source: "<target-repo>/.agents/skills"
  installed-skill-roots:
    - "<work-installed-skills-root>"
  global-refresh-command: "<work-refresh-command>"
```

Resolution rules:

- Treat `global-skill-source`, `repo-local-skill-source`, `installed-skill-roots`, and `global-refresh-command` as local bindings, not text-replacement instructions.
- Keep placeholders in reusable skill source files so the skills remain portable across machines.
- Before creating, updating, curating, archiving, or installing skills, resolve placeholders from the local bindings.
- Use resolved values for actual filesystem operations, archive paths, reports, and commands.
- Run the resolved command exactly; do not broaden a universal-only refresh into an all-agent install.
- If a binding is missing or still points at an unresolved placeholder when a concrete operation is needed, ask the user.

## Skill Source Roots

Use `<global-skill-source>` for global user-owned skills.

Use `<repo-local-skill-source>` for repo-local user-owned skills.

Use global skills for reusable procedures that apply across repos, tools, or workflows. Use repo-local skills for procedures that depend on one repo's structure, scripts, product language, deployment topology, test fixtures, or ownership boundaries.

Do not directly edit installed/generated skill copies under `<installed-skill-root>` unless the user explicitly asks.

Instead:

1. Make global skill source changes under the resolved `<global-skill-source>`.
2. Make repo-local skill source changes under the resolved `<repo-local-skill-source>`.
3. After creating, updating, merging, promoting, embedding, or archiving global skills, run the resolved `<global-refresh-command>`.

Repo-local-only changes do not require the global refresh command.

## Skill Source Editing Rules

When asked to create a new skill:

- Choose global scope when the skill is reusable across repos.
- Choose repo-local scope when the skill is tied to the current repo.
- Create global skills under the resolved `<global-skill-source>`.
- Create repo-local skills under the resolved `<repo-local-skill-source>`.
- Run the resolved `<global-refresh-command>` only when global skills changed.

When asked to update, rewrite, merge, or curate an existing skill:

- First check whether that skill exists under the resolved `<repo-local-skill-source>`.
- Then check whether it exists under the resolved `<global-skill-source>`.
- Edit the source copy in the correct scope.
- Run the resolved `<global-refresh-command>` only when global skills changed.

If a skill exists only in an installed/generated location but does not exist under the correct repo-local or global source root:

- Do not modify the installed/generated copy.
- Treat it as non-canonical.
- If a change is needed, create or import a source version under the correct repo-local or global root first.
- Run the resolved `<global-refresh-command>` only when global skills changed.

If the resolved `<global-skill-source>` or `<repo-local-skill-source>` does not exist and is the selected source root, create it before creating new skills.

## End-of-Task Self-Improvement

At the end of every substantial task, perform a brief self-improvement check.

Create or update a skill when any of these are true:

- The task required 5 or more meaningful steps.
- A tricky or non-obvious error was solved.
- The user corrected the agent's approach.
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

Before creating a new skill, search existing skills by name and content in both the resolved `<repo-local-skill-source>` and `<global-skill-source>`. Prefer patching an existing skill in the correct scope over creating a duplicate.

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

- Modify global skills under the resolved `<global-skill-source>`.
- Modify repo-local skills under the resolved `<repo-local-skill-source>`.
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
<global-skill-source>/.archive/YYYY-MM-DD/<skill-name>/
<repo-local-skill-source>/.archive/YYYY-MM-DD/<skill-name>/
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

After curation, run the resolved `<global-refresh-command>` only when global skills changed.

## Third-Party Skill Safety

Do not modify bundled, vendor, third-party, registry-installed, package-managed, or git-submodule skills unless explicitly asked.

Treat a skill as third-party or vendor-owned if:

- It is inside a git submodule.
- It has a remote upstream not controlled by the user.
- It is installed from a public skill registry.
- Its README or metadata says it is externally maintained.
- It is managed by a package manager or installer.

For third-party skills, prefer creating a local wrapper or companion skill under the correct repo-local or global source root instead of editing the original.

## Automatic Behavior

Act proactively. If a task clearly produced reusable procedural knowledge, create or update the relevant skill before finishing.

If the change is low-risk and local to user-owned skills under the resolved `<global-skill-source>` or `<repo-local-skill-source>`, apply it directly. Run the resolved `<global-refresh-command>` only when global skills changed.

Ask before making broad or destructive changes, including:

- archiving many skills
- modifying third-party skills
- rewriting a large skill library
- changing executable scripts
- deleting anything permanently

Prefer patching existing skills over creating new skills. Prefer creating reusable procedural knowledge over saving task-specific logs.
