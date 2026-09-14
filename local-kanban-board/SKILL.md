---
name: "local-kanban-board"
version: "1.1.0"
description: "Create or maintain a repository-local Markdown Kanban board under `kanban/`. Use for board setup, task updates, dependencies, archiving, or resuming work from an existing board."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "project-tracking"
---

# Local Kanban Board

Use this skill for durable local task tracking. Skip external trackers, one-off checklists, and repositories whose existing task system the user wants to keep. Updating a task record does not itself authorize implementing the task.

## Prerequisites

- A writable target repository for board changes; existing Markdown can be inspected read-only.
- Bash, `awk`, `sed`, `find`, and `date` for CLI operations.
- A project-specific task prefix, such as `MKT`, when initializing a board.

## Inspect or resume an existing board

Read `kanban/BOARD.md` and the task files relevant to the request. Task files are authoritative if the snapshot is stale. Preserve existing config, scripts, templates, and repo instructions; resuming or updating a task does not require reinstalling board assets. For a partial setup, restore only what the requested operation needs without overwriting custom files.

For a read-only status or audit request, inspect Markdown and config as text. Every nonempty CLI invocation, including `show`, `list`, and `--help`, sources `config.env` as shell code and creates missing layout directories. `board` and successful `validate` also rewrite `BOARD.md`. Use the CLI when operating the board within the requested scope.

## Initialize a new board

When the requested work requires a new board and none exists:

1. Create this layout:

   ```text
   kanban/
   ├── config.env
   ├── BOARD.md
   ├── archive/
   ├── scripts/kanban
   ├── tasks/
   └── templates/task.md
   ```

2. Copy [config.env](templates/config.env), [task.md](templates/task.md), and the [CLI](scripts/kanban) to their corresponding paths. Mark `kanban/scripts/kanban` executable.
3. Set `KANBAN_PROJECT_NAME`, `KANBAN_TASK_PREFIX`, and optional ID width, statuses, and priorities in `kanban/config.env`; preserve the semantic status names described below.
4. Add discovery guidance from [templates/AGENTS.md](templates/AGENTS.md) only where missing, merging it into existing repo instructions.
5. Run `kanban/scripts/kanban validate` to check the layout and generate `kanban/BOARD.md`.

## Operate the board

Invoke `kanban/scripts/kanban` with the needed command. Inspect the CLI's usage text for additional options when relevant.

| Operation | Command arguments |
| --- | --- |
| Create a task | `create "Title"` |
| Inspect tasks | `list`, `show ID`, `ready`, `waiting`, `next` |
| Move or annotate | `move ID status`, `note ID "text"` |
| Change dependencies | `depend ID DEPENDS_ON_ID`, `undepend ID DEPENDS_ON_ID` |
| Archive completed work | `archive ID`, `archive --done` |
| Regenerate the snapshot | `board` |
| Check structure and regenerate | `validate` |

## Task Rules

- Treat `kanban/tasks/*.md` and `kanban/archive/**/*.md` as the source of truth.
- Keep `kanban/BOARD.md` tracked as a generated human-readable snapshot.
- Change metadata and append notes through `kanban/scripts/kanban`; edit descriptions, plans, and acceptance criteria directly in task bodies, preserving metadata and history.
- The CLI appends history at the end of the task file. Keep `## Notes` last in new templates; in existing customized tasks, preserve later sections and identify where appended history actually landed rather than assuming it is under `## Notes`.
- Serialize board mutations when multiple agents share the repo; the CLI does not lock task IDs or generated board writes.
- Store active tasks in `kanban/tasks/`; store archived tasks under `kanban/archive/YYYY/`.
- Keep task metadata flat: `id`, `title`, `status`, `priority`, `type`, `assignee`, `depends_on`, `created`, `updated`, `archived`.
- Generate IDs by scanning active and archived tasks for the configured prefix; do not use a separate counter file.
- The CLI's `ready` and `next` consider only `todo`, `in-progress`, and `review`, with no dependencies or all dependencies closed. Closure means literal `done` status or an archived task; ordinary archive and `archive --done` also require literal `done`. Additional configured statuses appear on the board but do not gain these semantics. Preserve these names when configuring the workflow.
- Treat a task as waiting when any dependency is still open or missing. Multiple dependencies are comma-separated.

## Pitfalls

- Do not hand-edit generated board output and expect it to persist; edit task files or use the script.
- Do not archive unfinished tasks unless the user explicitly wants a forced archive.
- Do not create task IDs manually unless repairing a broken board.
- Do not pick waiting tasks for implementation until their dependencies are closed, unless the user explicitly overrides the dependency.
- Keep project-specific task prefixes in `kanban/config.env`, not in this skill.

## Verify the requested change

After a batch of related metadata, dependency, config, or layout changes, run `kanban/scripts/kanban validate` and inspect the affected task and generated snapshot. Body-only edits need content review; read-only inspection needs no CLI invocation or snapshot rewrite.

Validation checks required metadata, status/priority membership, filename/ID agreement, duplicate IDs, and self or missing dependencies. It does not detect cycles spanning multiple tasks or prove acceptance criteria are satisfied. Inspect dependency chains when changing scheduling and review task content before declaring work complete.

Exercise CLI behavior on a disposable scratch board when an installation, CLI change, or suspected command defect warrants it. Routine task updates do not require a lifecycle regression run, and test tasks must not be added to the user's board.
