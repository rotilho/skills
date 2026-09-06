---
name: "auto-skill-capture"
version: "1.4.0"
description: "Create or update global or repo-local Agent Skills after work reveals a reusable procedural gap, such as repeated corrections, tricky diagnosis, or environment-specific setup. Use when a user asks to capture a workflow or near the end of substantial work that taught future agents a better procedure."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "skill-authoring"
---

# Auto Skill Capture

Turn a reusable lesson into instructions that improve future work. Task difficulty or length alone does not justify capture.

## 1. Decide whether anything should be saved

Identify the procedure, decision rule, or stable environment constraint learned. State what a future agent should do differently and why existing guidance is insufficient.

Skip capture when the lesson is already covered, obvious, a one-off outcome, or cannot be separated from private context. Exclude task progress, PR/issue numbers, branch names, commit hashes, incident logs, secrets, and private data. Convert facts likely to expire into instructions for checking them afresh.

## 2. Find the owner

Resolve source locations from the user's request, local agent context, or `SELF-IMPROVE.md`. `<global-skill-source>` is the user-owned reusable source checkout; `<repo-local-skill-source>` is usually `<target-repo>/.agents/skills`. Resolve only the locations needed for this task; a missing install command does not block source work. Ask only if the source needed for a write remains ambiguous.

Search names, descriptions, and bodies in both available source roots before adding a skill. Patch an existing skill when the lesson fits its trigger boundary. Create one only for a distinct workflow, audience, or activation condition.

Use global placement for procedures that work across repos. Keep repo-dependent paths, scripts, product language, tests, deployment topology, and ownership assumptions repo-local. If removing those assumptions makes the procedure vague, keep it local.

Treat placement as a source-root decision; omit placement bookkeeping from the skill body. Installed/generated and externally owned skills are read-only unless explicitly authorized. Do not replace location placeholders in reusable guidance with machine-specific values.

## 3. Capture and verify

Write the smallest useful change. Preserve exact commands when they are the durable procedure, and include prerequisites, pitfalls, or examples only when they affect execution. Use `create-skill` for authoring and behavioral verification when available.

Check that the description selects the intended workflow, the frontmatter is valid, the version is bumped for behavior changes, and the folder name and support links are correct. Test changed behavior against a realistic scratch task; use an isolated subagent when available. Check positive and near-miss trigger examples when activation changes.

Review the result for temporary/private data and misplaced repo assumptions. Source-only work stays source-only. Otherwise, after global changes run the configured `<global-refresh-command>` with its exact agent scope; do not broaden a universal-only install with `--all`. Repo-local-only changes do not need a global refresh. If refresh is unavailable, report that limitation without treating source work as undone.

Report the source skill changed, the reusable behavior captured, and verification/refresh results. If no durable gap was found, finish without creating an artifact.

## Self-improvement setup

When asked to install or configure an agent-level capture policy, use [the portable policy example](references/self-improve-example.md). This setup is separate from capturing a lesson; ordinary capture does not require creating a policy file.
