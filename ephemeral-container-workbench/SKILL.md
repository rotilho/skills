---
name: "ephemeral-container-workbench"
version: "1.0.0"
description: "Use when a task needs installing rarely used CLI tools, converters, SDKs, package managers, or system dependencies and the work can be isolated in a temporary Podman or Docker container instead of mutating the host. Trigger for phrases like throwaway container, temporary image, use podman/docker for this install, one-off dependency, or run a conversion/tooling job without installing locally."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "tooling"
  style: "concise"
---

# Ephemeral Container Workbench

Use this skill to run one-off tooling in a disposable container while keeping the host clean.

## When to use

Trigger for work like:
- installing a converter, SDK, package manager, or system tool that is unlikely to be reused soon
- running a batch operation where inputs and outputs can be bind-mounted
- using a temporary Podman or Docker image to avoid host package changes
- reproducing a command in a clean Linux environment

Do not use when:
- the project already has a committed dev container, toolchain wrapper, or repo-native script that should be used
- the task needs long-lived services, persistent databases, or daemon state
- the operation must integrate deeply with the host desktop, kernel modules, hardware devices, or credentials
- installing the dependency in the repo or user environment is the actual requested outcome

## Prerequisites

- A container runtime is available: prefer `podman` when present, otherwise use `docker`.
- The input path and output path are known.
- The output path is writable by the host user, usually under `/tmp` for scratch work or the workspace for durable artifacts.
- Network/package installation inside the container is acceptable, or the needed image/tool is already local.

## Procedure

1. Establish the host-side baseline.
   - Confirm the input path exists and count the expected inputs.
   - Create the output directory before running the container.
   - Decide whether outputs should be temporary (`/tmp/...`) or durable (workspace path).

2. Pick the runtime and image.
   - Use `command -v podman docker` to choose the available runtime.
   - Prefer a small, familiar base image already present locally when possible.
   - Use `--pull=never` only when the local image is known to be sufficient; otherwise allow a pull with approval when network is restricted.

3. Build a safe container command.
   - Use `--rm` for disposable runs.
   - Mount inputs read-only with `-v "$input:/in:ro"`.
   - Mount outputs read-write with `-v "$output:/out"`.
   - Add `--security-opt label=disable` for Podman bind mounts on SELinux hosts when the container cannot read or write mounted paths.
   - Pass secrets through environment variables only when required, and do not persist them in scripts, skills, logs, or final summaries.

4. Test one representative item first.
   - Install the required tools inside the container.
   - Convert or process one small input.
   - Verify the output from the host using native inspection tools.
   - Only then run the full batch.

5. Run the batch with progress and failure accounting.
   - Use strict shell mode inside the container when practical: `set -euo pipefail`.
   - Track `count` and `fail` counters for batch jobs.
   - Emit periodic progress rather than noisy per-file logs.
   - Preserve source timestamps or ownership only when useful and safe.

6. Verify from the host.
   - Count outputs and compare against expected inputs.
   - Check total size and inspect a few sample outputs.
   - Confirm permissions and ownership are usable by the host user.
   - If the task uploaded or copied data externally, inspect the tool's final report and saved log.

## Pitfalls

- Do not install packages on the host just because a command is missing; first consider a disposable container.
- Do not mount broad host paths read-write when the task only needs a specific input directory.
- Do not assume a file extension is supported; test one representative file before the batch.
- Do not treat a successful package install as proof the actual tool can process the input.
- Do not leave secrets embedded in command history, generated scripts, skill files, or final reports.
- Do not hide partial failures. Report converted/uploaded/processed counts and failed counts separately.

## Verification

- Runtime chosen: `podman` or `docker`.
- Input count was measured before the run.
- Output directory exists and contains the expected artifacts.
- Sample outputs were inspected from the host.
- Final report includes counts, failures, output path, and any logs.
- No host package installation was performed unless the user explicitly requested it.

## Examples

Should trigger:
- "Use a temporary Podman image to convert these RAW files."
- "Can you run this one-off tool without installing it on my machine?"
- "Use docker or podman, whatever is available, to install the converter and write outputs to /tmp."

Should not trigger:
- "Add this dependency to the project Dockerfile."
- "Install this CLI globally so I can use it every day."
- "Debug why the existing devcontainer fails to start."
