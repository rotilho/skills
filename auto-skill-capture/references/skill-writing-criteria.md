# Skill Writing Criteria

Use this reference when deciding whether a recent task should become a reusable skill and how to shape the result.

## Global vs Repo-Local Placement

Resolve local `skill_locations` bindings before creating or updating skills:

- `<global-skill-source>` for global skills when the procedure is reusable across multiple repos, tools, agents, or workflows.
- `<repo-local-skill-source>` for repo-local skills when the procedure depends on one repo's structure, scripts, product language, deployment topology, test fixtures, or ownership boundaries.
- `<global-refresh-command>` for syncing global source skills into the configured installed skill targets after global changes.

Keep placeholders inside reusable skill source files. For actual file operations, archive paths, verification commands, and final reports, use the resolved local values from `SELF-IMPROVE.md` or equivalent local agent context. If a needed binding is missing, ask the user before touching files.

Run the resolved `<global-refresh-command>` exactly, preserving the intended universal-only target.

Treat global vs repo-local as a source-root placement decision. Keep skill content focused on the reusable procedure, and omit placement bookkeeping such as `metadata.scope` or a `## Scope` section.

Default to repo-local when a lesson was learned in one repo and might generalize later but still contains repo assumptions. A later curation pass can promote it after those assumptions are removed.

Examples of repo-local captures:

- this repo's Gradle task sequence or local build cache setup
- this service's Terraform ownership boundary
- this app's active UI evidence locations
- this repository's deployment or release workflow

Examples of global captures:

- generic Kotlin Cucumber structure
- general skill-writing workflow
- cross-repo debugging pattern
- reusable documentation or release-review process

## Capture When

Create or update a skill when the work produced procedural knowledge that is likely to recur:

- a repeated workflow with several ordered steps
- a tricky debugging path that future agents should follow
- environment-specific setup or verification that is easy to forget
- correction-heavy behavior where the user had to steer the agent repeatedly
- a durable repo convention that affects future implementation or review
- a reusable decision rule for choosing between valid approaches

The captured content should help a future agent act better, not just remember that a past task happened.

## Do Not Capture

Keep these out of skills:

- task progress and status updates
- PR numbers, issue numbers, branch names, and commit hashes
- temporary incident facts, rollout state, or one-off command output
- secrets, credentials, tokens, private customer data, or internal identifiers
- stale external facts that should be looked up fresh
- broad advice that a competent agent already knows
- details that only make sense for one completed task

When a fact might expire, convert it into a verification step instead of storing the fact.

## Update Versus Create

Update an existing skill when:

- the new behavior fits the same trigger boundary
- users would expect one skill to cover both workflows
- the new lesson is a caveat, pitfall, or verification step for an existing procedure
- the existing skill in the correct source root already owns the workflow

Create a new skill when:

- the procedure has a distinct purpose or audience
- adding it to an existing skill would make that skill vague or too broad
- the activation language would conflict with an existing skill
- the workflow needs its own references, templates, scripts, or assets

If unsure between update and create, update the closest existing skill first and split later if the boundary becomes clear. If unsure between repo-local and global, capture repo-local first and promote later when the content is clearly reusable outside that repo.

## Required Skill Shape

A portable skill package should normally include:

- `SKILL.md` with valid YAML frontmatter
- a trigger-oriented `description`
- clear "when to use" and "when not to use" boundaries
- prerequisites or assumptions
- a concrete procedure
- common pitfalls
- verification steps
- examples that show realistic activation

Keep `SKILL.md` short enough to load comfortably. Put long examples, policies, and reusable templates under `references/` or `templates/`.

## Trigger Quality

A good trigger description says:

- what the skill helps do
- when it should activate
- the nearby phrases users may use
- how it differs from adjacent skills

Prefer concrete verbs such as "debug", "curate", "capture", "migrate", "publish", "audit", or "generate" over generic labels.

## Verification

Before installing, check:

- folder name and frontmatter `name` match
- YAML parses as ordinary frontmatter
- string values are quoted
- support files are referenced from `SKILL.md`
- placeholders remain only where intentionally templated
- captured content excludes private and stale data
- trigger examples include should-use and should-not-use prompts
- global skills are free of repo-only assumptions
- repo-local skills name repo assumptions only when those assumptions affect the procedure
- the skill was written to the correct source root for the placement decision
- the resolved `<global-refresh-command>` was run after global changes, with its intended agent scope preserved

## Example Transformation

Poor capture:

> On PR 183, the branch failed because the service account was wrong. We fixed it with commit abc123.

Reusable skill content:

> For deployment-auth failures, first inspect the live runtime identity, then compare it with the deploy configuration and only then patch source configuration. Strip incident IDs, branch names, and commit hashes.

## Placement Examples

Repo-local placement:

> In this repo, diagnose release workflow failures by checking `.github/workflows/release-promote.yml`, bootstrap allow-lists, and `deploy/terraform/` static validation before changing pipeline inputs.

Global placement:

> When diagnosing deployment failures, establish the live runtime state first, compare it to source configuration, make the smallest targeted change, then verify against the same baseline.
