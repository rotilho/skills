---
name: "orchestrated-kanban-subagents"
version: "1.3.0"
description: "Coordinate user-requested Kanban work through planner and executor subagents, persisted plans, and main-session review. Ordinary subagent use or local task tracking alone does not require this workflow."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "engineering"
  workflow: "coordination"
---

# Orchestrated Kanban Subagents

Keep project state in Kanban and task execution in subagents. The main session reviews plans and results, coordinates ownership, and closes accepted work.

## Prerequisites and scope

- Use the relevant `local-kanban-board` guidance for board operations; setup applies only to a new board. For read-only status inspection, read the existing Markdown without invoking the CLI, which sources shell config and may write files.
- Use when the user requests this coordination model; do not introduce it just because a task uses a subagent or needs a checklist.
- Honor the user's worker limit and runtime capacity. Parallelize only work with independent file ownership; one assignment covers one task unless the user requests a bundle.
- The main session coordinates rather than implementing task code. If it must perform a small unblocker because a worker lacks permissions or tooling, record that exception in the task.

## Workflow

### 1. Select ready work

Read `kanban/BOARD.md` and the relevant task files. Create missing tasks and dependencies through `kanban/scripts/kanban`. Select work whose dependencies are closed; do not silently bypass waiting tasks.

Keep task intent in the body and use the CLI for metadata and appended history. The CLI writes history at end of file; preserve custom sections and keep `## Notes` last in new templates so history lands there. Directly edit the body for description, plan, and acceptance criteria. Coordinate board mutations serially because workers share task files and generated board output.

### 2. Plan and review

Assign a planner one task ID and the relevant repo scope. It inspects the task and dependencies, then writes:

- `## Description`: problem, current state, scope, constraints, and dependency context.
- `## Plan`: implementation steps, executor file ownership, verification commands, and material risks or blockers.
- `## Acceptance Criteria`: concrete completion checkboxes.

The planner reports the task path and key decisions; it need not repeat the full plan in chat. A plan that exists only in chat or notes is incomplete.

The main session reads and reviews the persisted plan before dispatching an executor. This is the plan approval step; it does not require a new user confirmation for already-authorized work. Return concrete feedback to the planner when needed. Reuse an existing plan when it still fits the current task and code; revise it when scope, ownership, criteria, or verification changes.

### 3. Execute the approved task

Give the executor the task ID, approved ownership scope, and instruction to read the task body before editing. It must preserve unrelated work.

The executor moves the task to `in-progress`, implements the plan, runs its verification, and records actions and results in notes. It then moves the task to `review`, or to `blocked` with the exact obstacle and needed next action. Main review normally owns closure unless the user delegates it.

Use the persisted plan for implementation details and verification commands; do not maintain a second copy in a prompt template.

### 4. Review and continue

Review changed files and verification evidence against the plan and acceptance criteria. Use a separate reviewer when the task warrants another independent check.

- Accept: record the review, mark satisfied criteria, and move the task to `done`.
- Request changes: give focused feedback to the responsible worker; revise the task plan first if the request changes its scope or contract.
- Discover separate work: create a follow-up task with dependencies and criteria. Keep fixes required for the current acceptance criteria in the current task.

Continue through the requested scope until tasks are done, explicitly deferred by the user, or blocked with evidence and no meaningful next step. Do not stop while a required worker is still running.

## Verification

- Executed tasks have reviewed body plans and recorded implementation/verification results.
- Accepted tasks are closed by the designated reviewer; remaining work has explicit status and next actions.
- Run `kanban/scripts/kanban validate` after board metadata, dependency, config, or layout mutations, or when CLI validation is requested. It regenerates the snapshot; skip it for body-only edits and read-only inspection. Review dependency chains and body content separately because validation does not detect multi-task cycles or prove plan quality or completion.
- The final response states completed work, blockers, and verification, after required workers finish.
