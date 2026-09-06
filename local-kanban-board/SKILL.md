---
name: "local-kanban-board"
version: "1.0.1"
description: "Create, resume, and maintain a repository-local Kanban board stored as readable Markdown under `kanban/`. Use when the user wants local task tracking, a resumable board, task prefixes, task dependencies, board scripts, templates, archives, or agent-readable project work state without relying on external project tools."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "project-tracking"
---

# Local Kanban Board

Use this skill to create and operate a repo-local Kanban board backed by readable Markdown files and a small script.

## Reference files

- Use `templates/config.env` when initializing a board.
- Use `templates/task.md` as the default task template.
- Use `templates/AGENTS.md` when adding repo-level discovery instructions.
- Use `scripts/kanban` as the board CLI.

## When to use

Trigger for work like:
- creating a local Kanban board in a repository
- resuming work from `kanban/BOARD.md` or `kanban/tasks/`
- adding, moving, annotating, or archiving project tasks
- configuring a project name, task prefix, statuses, priorities, dependencies, or ID width

Do not use when:
- the user wants GitHub Projects, Jira, Plane, or another external tracker
- the task is a one-off todo that does not need durable project state
- the repository already has a different task system the user wants to keep

## Prerequisites

- A writable target repository.
- Bash, `awk`, `sed`, `find`, and `date`.
- A project-specific task prefix, such as `MKT`, when initializing a board.

## Procedure

1. Inspect the current repository for `kanban/config.env`, `kanban/BOARD.md`, and `kanban/tasks/`.
2. If the board is missing, create this layout:

   ```text
   kanban/
   ├── config.env
   ├── BOARD.md
   ├── archive/
   ├── scripts/kanban
   ├── tasks/
   └── templates/task.md
   ```

3. Copy `templates/config.env`, `templates/task.md`, and `scripts/kanban` into the board. Mark `kanban/scripts/kanban` executable.
4. Set `KANBAN_PROJECT_NAME`, `KANBAN_TASK_PREFIX`, and optional statuses/priorities in `kanban/config.env`.
5. Add short repo instructions from `templates/AGENTS.md` if the repo lacks clear agent guidance.
6. Run `kanban/scripts/kanban validate` to generate `kanban/BOARD.md`.
7. For normal operation, use:
   - `kanban/scripts/kanban create "Title"`
   - `kanban/scripts/kanban list`
   - `kanban/scripts/kanban board`
   - `kanban/scripts/kanban show ID`
   - `kanban/scripts/kanban move ID status`
   - `kanban/scripts/kanban note ID "text"`
   - `kanban/scripts/kanban depend ID DEPENDS_ON_ID`
   - `kanban/scripts/kanban undepend ID DEPENDS_ON_ID`
   - `kanban/scripts/kanban ready`
   - `kanban/scripts/kanban waiting`
   - `kanban/scripts/kanban next`
   - `kanban/scripts/kanban archive ID`
   - `kanban/scripts/kanban archive --done`
   - `kanban/scripts/kanban validate`

## Task Rules

- Treat `kanban/tasks/*.md` and `kanban/archive/**/*.md` as the source of truth.
- Keep `kanban/BOARD.md` tracked as a generated human-readable snapshot.
- Change metadata and append notes through `kanban/scripts/kanban`; edit descriptions, plans, and acceptance criteria directly in task bodies, preserving metadata and history.
- Serialize board mutations when multiple agents share the repo; the CLI does not lock task IDs or generated board writes.
- Store active tasks in `kanban/tasks/`; store archived tasks under `kanban/archive/YYYY/`.
- Keep task metadata flat: `id`, `title`, `status`, `priority`, `type`, `assignee`, `depends_on`, `created`, `updated`, `archived`.
- Generate IDs by scanning active and archived tasks for the configured prefix; do not use a separate counter file.
- Treat a task as ready when `depends_on` is empty or every dependency is closed by `done` status or archive.
- Treat a task as waiting when any dependency is still open or missing. Multiple dependencies are comma-separated.

## Pitfalls

- Do not hand-edit generated board output and expect it to persist; edit task files or use the script.
- Do not archive unfinished tasks unless the user explicitly wants a forced archive.
- Do not create task IDs manually unless repairing a broken board.
- Do not pick waiting tasks for implementation until their dependencies are closed, unless the user explicitly overrides the dependency.
- Keep project-specific task prefixes in `kanban/config.env`, not in this skill.

## Verification

- `kanban/scripts/kanban validate` succeeds.
- `kanban/scripts/kanban board` shows every configured status.
- Creating, moving, noting, depending, ready/waiting listing, and archiving scratch tasks updates metadata and `kanban/BOARD.md`.
- Task files remain readable without running the script.

## Examples

Should trigger:
- "Create a local kanban board for this repo."
- "Resume the kanban and pick the next task."
- "Add this work as a blocked Kanban task."
- "Make this task depend on TASK-001 and TASK-002."

Should not trigger:
- "Add this to GitHub Projects."
- "Make a quick checklist in the PR description."
