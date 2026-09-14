# Agent Instructions

Use the installed `local-kanban-board` skill for work managed by this repo's `kanban/` board.

Read `kanban/BOARD.md` and relevant task files; task files are authoritative. Use `kanban/scripts/kanban` for metadata and notes; edit descriptions, plans, and acceptance criteria directly while preserving metadata and history. Keep existing config, scripts, and templates when resuming.

Serialize board mutations. Run `kanban/scripts/kanban validate` after metadata, dependency, config, or layout changes, then inspect the affected task and snapshot. Validation checks structure, not multi-task dependency cycles or work completion.

For read-only status or review, inspect files directly. Every nonempty CLI invocation sources shell config and creates missing directories; `board` and successful `validate` rewrite the snapshot.
