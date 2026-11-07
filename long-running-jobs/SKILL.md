---
name: 'long-running-jobs'
version: "1.0.1"
description: 'Use when a requested local build or command may outlast the current Codex turn and should continue in a Linux systemd user service with a saved log and completion notification.'
license: 'MIT'
compatibility: 'Linux with Python 3, a running systemd user manager, and notify-send for desktop notifications.'
metadata:
  scope: 'global'
---

# Long-running local jobs

Run lengthy, authorized local commands in a systemd user service with saved logs and status. The command can continue after a Codex turn ends. Desktop notifications do not resume Codex or invoke a model.

Use this for local builds and similar commands that do not need ongoing model decisions. Do not use it for work that needs continuous review, credentials that should not be inherited, remote deployment, or commands the user has not authorized. Keep command arguments explicit; never build a shell command string or add retries, sandbox bypasses, or model callbacks. Before starting, ensure the exact underlying command and working directory are authorized under the active sandbox. A detached systemd service must not bypass tool permissions; if approval is required, obtain it for the exact command before launch.

Start a command with an explicit working directory:

```bash
python3 /path/to/long-running-jobs/scripts/job.py start --cwd /path/to/repo -- ./gradlew build
```

The command after `--` is an argv list and supports spaces and shell metacharacters literally. The helper disables systemd environment expansion. It passes `PATH` and desktop routing variables to the service; supply any other required per-command environment explicitly as argv, for example `-- env NAME=value ./build`. `start` prints the job ID, job directory, and systemd unit. The helper stores `output.log` and atomic `status.json` files under the default state directory (`$XDG_STATE_HOME/codex-long-running-jobs`, or `~/.local/state/codex-long-running-jobs`). Use `--state-dir PATH` to choose another location.

Inspect or cancel a job using the printed directory:

```bash
python3 /path/to/long-running-jobs/scripts/job.py status /path/to/job-dir
python3 /path/to/long-running-jobs/scripts/job.py cancel /path/to/job-dir
```

After verifying launch, report the job ID, directory, unit, and how to read its log/status. During ongoing implementation or orchestration, continue independent work or wait for an available completion event, then inspect the saved result and finish the requested verification. End after launch when the user requested a standalone detached job, wants to return after notification, or no useful independent work or completion event is available and remaining active would only poll or wait for a scheduled time. Honor explicit instructions to remain active. When ending after launch, explain that the notification does not resume Codex and the user must return to continue analysis.

On completion, notify-send reports success or failure and gives the status path; it excludes the command and its arguments. Notification failure does not affect the job result.
