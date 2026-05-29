# Merge Policy

Use this policy before merging, promoting, embedding, or archiving skills.

## What Counts As A Duplicate

Treat skills as clear duplicates only when they share the same durable purpose and would reasonably trigger for the same user prompts.

Strong duplicate signals:

- same workflow with different names
- one skill is a thin rewrite of another
- overlapping descriptions and procedures with no meaningful boundary
- one skill is an outdated version of another user-owned skill

Do not merge when:

- one skill is a general base layer and the other is domain-specific
- similar words hide different procedures
- different tools, runtimes, or owners require separate instructions
- the user explicitly wants both skills to remain active

Use `promote` instead of ordinary merge when a repo-local skill should become global. Use `embed` when the useful content is only a caveat, variant, pitfall, or verification step for a stronger skill.

## Choosing The Target Skill

Prefer the target skill with:

- clearer and more stable name
- stronger trigger description
- more complete procedure
- better maintained support files
- broader correct usage without becoming vague
- active references from current docs or README files

If two skills are equally strong, keep the more specific name when the workflow is specialized; keep the broader name only when it can cleanly own both workflows.

## Merge Procedure

1. Read both complete skill packages.
2. Choose one target package.
3. Copy only reusable procedural content from the superseded package.
4. Preserve unique references, templates, scripts, or assets when they still support the target skill.
5. Remove duplicated wording, stale examples, task logs, private data, and time-bound facts.
6. Update the target skill's trigger boundaries so it owns the merged workflow.
7. Archive the superseded package instead of deleting it.
8. Record the merge in the curation report.

## Promotion Procedure

Promote repo-local content to global only when the reusable procedure works outside the source repo.

1. Read the full repo-local package and candidate global targets.
2. Remove repo-specific paths, product-only language, secrets, temporary facts, branch names, commit hashes, PR numbers, and issue numbers.
3. Choose one target:
   - create `~/IdeaProjects/skills/<skill-name>/` when the workflow deserves a standalone global skill
   - update an existing global skill when the content is a natural extension of that skill
4. Move or adapt only reusable references, templates, scripts, and assets that still make sense globally.
5. Update global trigger boundaries so the promoted content is discoverable without becoming vague.
6. Archive the repo-local source package under `<target-repo>/.agents/skills/.archive/YYYY-MM-DD/<skill-name>/`.
7. Add `ARCHIVE_NOTE.md` in the archived package explaining the global target and promotion reason.
8. Run `npx skills add ~/IdeaProjects/skills/ -g --all -y`.
9. Record the promotion in the curation report.

## Embedding Procedure

Embed a skill when its reusable content is too small or overlapping to justify a standalone package.

1. Read the source skill and candidate target skill.
2. Choose a same-scope target by default.
3. Choose a global target only when the embedded content is genuinely cross-repo.
4. Move useful procedure, pitfalls, examples, and verification steps into the target.
5. Move support files only when they still support the target; otherwise preserve them in the archive.
6. Update target trigger boundaries only if needed.
7. Archive the superseded package and add `ARCHIVE_NOTE.md` naming the target.
8. Run the global install command only if a global skill changed.
9. Record the embedding in the curation report.

## Archive Procedure

Archive full global packages under:

```text
~/IdeaProjects/skills/.archive/YYYY-MM-DD/<skill-name>/
```

Archive full repo-local packages under:

```text
<target-repo>/.agents/skills/.archive/YYYY-MM-DD/<skill-name>/
```

Preserve all files from the original package:

- `SKILL.md`
- `README.md`
- `references/`
- `templates/`
- `scripts/`
- `assets/`
- agent metadata
- any other support files

Use ordinary file moves. Do not reconstruct archived packages by hand unless the original package is already incomplete.

## Conflict Handling

If two duplicate skills disagree:

- prefer current user-owned source over installed/generated copies
- prefer same-scope embedding before cross-scope movement
- prefer reusable procedure over completed-task history
- prefer explicit user constraints over inferred behavior
- convert stale facts into verification steps
- keep both active and report `needs-human-review` if a safe merge, promotion, or embedding is not obvious

## Post-Change Verification

After merging, promoting, embedding, or archiving:

- the active target skill still has valid frontmatter
- the target description covers the merged trigger without becoming too broad
- support file links still resolve
- archived package is complete
- no active duplicate remains for the same workflow
- promoted global content has no repo-only assumptions
- `npx skills add ~/IdeaProjects/skills/ -g --all -y` has been run when global skills changed
