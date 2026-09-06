---
name: "create-skill"
version: "1.1.0"
description: "Create or improve an agent skill. Use when the user wants a new `SKILL.md`, a rewrite of an existing skill, better trigger coverage, behavior simulation, trigger/overlap evaluation, tighter instructions, or a repeated workflow turned into a reusable skill."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "authoring"
---

# Create Skill

Create, rewrite, or evaluate reusable agent instructions. Use `auto-skill-capture` to decide what to retain from completed work, and `skill-library-curator` for library-wide ownership and overlap decisions.

## 1. Establish the purpose and source

Infer the intended task, expected work product, runtime, and skill name from the request. Inspect existing skills and local instructions before writing. Edit the canonical user-owned source, preserving unrelated changes; installed/generated or third-party copies need explicit authorization.

Choose an existing owner when the behavior fits its trigger boundary. Create a separate skill only for a distinct workflow. Do not expand an adjacent skill just because its name is similar.

Write the description first: what the skill does, when it should activate, and the boundary with nearby skills. Aim for correct selection, including realistic near misses.

## 2. Write only the guidance that changes behavior

Use one folder containing `SKILL.md`. Create files directly unless the repo provides a useful scaffold; an installer is not needed to author instructions.

Follow the target runtime's frontmatter rules. For this library:

- Match a lowercase kebab-case `name` to the folder name, within the runtime's length limit.
- Include `version`, `description`, `license`, `compatibility`, and `metadata`; quote string values.
- Use a quoted semantic version and bump it when behavior changes.
- Set license and compatibility from the actual package, not assumed defaults.

Give the agent concrete actions, relevant prerequisites and failure handling, and a way to verify the result. Include examples or exclusion boundaries where they resolve a real ambiguity. Do not require a section for every category.

Delete instructions that repeat existing guidance, state the obvious, or add ceremony without affecting the outcome. Keep useful guidance intact. Add support files only for material worth retaining: long domain references, reusable assets, or scripts that make repeated work reliable. Link them from `SKILL.md` with when-to-read guidance.

## 3. Verify selection and behavior

When creating a skill or changing its trigger, check realistic should-trigger prompts and near misses against adjacent skills. Choose cases around the actual ambiguity; a fixed prompt count does not prove coverage.

For a new skill or a behavior-changing update, run a realistic isolated task simulation:

- Give a subagent only the skill path, task, and raw input artifacts or target repo. Do not supply expected answers or intended fixes.
- Have it produce the actual kind of work product the skill governs.
- Put outputs under `.workbench/` or another scratch location outside the target repo. Target edits require explicit user authorization; use a disposable fixture for editing tests.
- Inspect the result for the intended behavior and reusable gaps. Patch gaps and rerun only affected cases.

Trigger checks do not replace behavior simulation. If isolated agents are unavailable, use the closest realistic scratch exercise and report the limitation. Skip behavioral verification only for unchanged behavior, a trigger-only review, or an unavailable environment that a realistic fixture cannot replace; state the reason.

Check final frontmatter, name/folder agreement, support links, and absence of unintended placeholders. Run the smallest relevant repo validation. Follow the configured refresh process for global source changes, preserving its agent scope, unless the user requested source-only work.

Report the skill changed, the behavior improved, verification performed, and any unresolved limitation. Complete the artifact unless the user asked only for a plan or review.
