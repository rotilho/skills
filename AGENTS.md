# Skills Repo Agent Guide

## Scope

These instructions apply to this skills repository.

## Source of truth

- Treat each root-level `<skill-name>/SKILL.md` as the source of truth for that skill.
- Treat git submodule skills as externally owned even when they live at the repo root; inspect/report them during curation, but do not edit, merge, or archive them unless explicitly requested.
- Keep bundled references under the owning skill folder.
- Refresh installed universal skills with `npx skills add ~/IdeaProjects/skills/ -g --agent universal --skill '*' -y` after changing a global skill.
- Do not use `--all` for refreshes; it installs to every supported agent.

## Testing Skills

- Test skill behavior in an isolated subagent whenever the environment supports subagents and active tool policy permits delegation.
- Give the subagent only the skill path, the realistic task, and the raw artifacts or target repo it should inspect.
- Do not pass the expected answer, prior conclusions, or known intended fixes to the subagent.
- Ask the subagent to write any test outputs under `.workbench/<skill-name>-<target>/` or another scratch path outside the target repo.
- Do not let skill tests modify the target repo unless the user explicitly asks for that.
- After the subagent returns, review its artifact and update the skill only for reusable behavior gaps.

## Worktree Safety

- The worktree may contain unrelated user changes.
- Do not revert, overwrite, or clean up files you did not create unless the user explicitly asks.
- Keep scratch test artifacts under `.workbench/`.
