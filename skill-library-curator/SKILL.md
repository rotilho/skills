---
name: "skill-library-curator"
version: "1.4.0"
description: "Curate global or repo-local skill libraries: review skills, reduce unnecessary instructions, consolidate overlaps, and report improvements. Use for library reviews or maintenance."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "skill-library-maintenance"
---

# Skill Library Curator

Keep user-owned skill libraries useful and coherent. For authoring one skill without reviewing the library, use `create-skill`.

## 1. Establish scope and baseline

Resolve the requested source roots from the user and local agent context, including `SELF-IMPROVE.md` when present. Global sources hold reusable user-owned skills; repo-local sources usually live at `<target-repo>/.agents/skills`. Use concrete paths for operations and keep machine bindings out of reusable skill content. Ask only if a source needed for a write remains ambiguous.

Inspect the worktree before changing it and preserve unrelated edits. Inventory every candidate package in scope, including committed and untracked skills, nested packages, and bundled support files. Account for every discovered `SKILL.md`; distinguish active skills from examples and nested external packages. Exclude archives, scratch output, caches, and generated installs from the active library. Inspect/report externally owned packages when included in scope, but do not modify vendor, registry/package-managed, or submodule skills without explicit authorization. Installed copies are not source.

## 2. Judge purpose before wording

For each skill, determine the task it enables and the behavior its instructions improve. Challenge its assumptions, overlap, and procedural cost. Existing or lengthy content is not evidence that it is necessary.

Leave useful guidance alone. Delete duplicated, obsolete, or obvious instructions before reorganizing them; moving unnecessary policy into references does not make it useful. Add requirements only to address a demonstrated gap. A small skill can have a valid independent purpose.

For every global or repo-local curation, apply [OpenAI's guide to rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra):

- **Selection:** Keep descriptions short and specific to the task. Check competing triggers and unnecessary skill loading across the library.
- **Loading:** Route independent workflows to relevant supporting files; remove unnecessary content before splitting it. Avoid unconditional document or companion-skill reads.
- **Procedure:** Retain useful commands, domain constraints, and failure handling; challenge rigid recipes and repeated test mandates without a task-specific purpose.
- **Context:** Inspect applicable `AGENTS.md` and agent/task templates for conflicting or excessive requirements. Report issues outside the editable scope.
- **Autonomy:** Check whether approval gates respect existing authorization. Preserve real ownership, destructive-action, and user-requested review boundaries.
- **Completion:** Define the expected result, appropriate verification, repair of affected failures, and stopping point. Avoid ending authorized work at a first draft.
- **Portability:** Consider the models sharing the instructions; do not assume every agent is Astra or remove useful safeguards solely on that basis.

Use these checks directly; the article is their rationale, not an additional mandatory read for each run. Judge changes by behavior, not word-count targets. Record concrete evidence per skill and distinguish static findings from untested improvement hypotheses.

Record a judgement and reason for each inspected skill:

- `keep`: useful and current.
- `patch`: valid purpose with a concrete content or activation gap.
- `merge`: shared purpose and trigger boundary justify one owner.
- `promote`: repo-local content now works across repos.
- `embed`: a variant or caveat belongs inside an existing owner.
- `archive`: superseded or no longer useful as an active skill.
- `exclude`: outside the editable source boundary or ownership unclear.

Similar words do not establish duplication. Keep general base layers separate from domain-specific workflows when both improve behavior. Do not merge different tool/runtime instructions or purposes merely to reduce skill count. If ownership or a safe consolidation is unclear, keep the skills and report the unresolved decision.

## 3. Apply justified changes

Patch in place when the identity remains valid. For merges, promotion, or embedding:

1. Read the full source and target packages. Choose a target with a clear name, appropriate trigger boundary, and useful existing support.
2. Move only unique guidance and support files the target still needs. Resolve conflicting rules against current evidence and explicit user constraints.
3. Promote content only when it works outside the source repo after removing repo-specific assumptions. If removing those assumptions makes it vague, keep it local.
4. Update trigger boundaries and support links without broadening the target beyond its purpose.
5. Archive the superseded package under its source root at `.archive/YYYY-MM-DD/<skill-name>/`, with an `ARCHIVE_NOTE.md` naming the reason and target. Preserve the complete package and check for destination collisions before moving it.

Archive whole skills by default; permanent deletion requires explicit authorization. Obsolete or duplicated support files can be removed as part of an authorized package cleanup. Do not discard unrelated user work.

## 4. Verify and report

Bump versions for behavior changes. Check frontmatter, name/folder agreement, support links, and complete archives. Check positive and near-miss prompts when triggers change. Test changed behavior with realistic isolated scratch tasks using `create-skill`'s verification procedure when available; do not treat trigger selection alone as behavioral proof.

For reduced instructions or relaxed gates, compare the existing and proposed behavior on a representative task when feasible. Check that useful constraints survive and authorized work reaches completion. Reuse valid evidence; rerun affected cases after failures or changes, and disclose when no behavioral comparison was performed.

For global changes, run the configured refresh command with its exact agent scope unless the user requested source-only work. Do not substitute `--all` for a scoped install. A missing refresh command need not block source work: report refresh as incomplete. Repo-local-only changes do not need a global refresh.

Report inspected scope, each skill's judgement and guide-based findings, concrete changes and reasons, source/target/archive paths for moves, validation, refresh results, and unresolved decisions. Separate recommendations from applied changes and reconcile the report with the inventory. Use a compact table or the user's requested format; create a separate report file only when requested or useful for resuming a large review. Omit empty change categories. Complete authorized edits, affected verification, and refresh before reporting completion; for review-only requests, deliver findings and proposed changes.
