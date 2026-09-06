# Self-Improving Skills

Use this example only when asked to install or configure an agent-level self-improvement policy. Copy it to the requested instruction file, commonly `~/.agents/SELF-IMPROVE.md`, and adapt the bindings below to the machine. Resolve known values from local context; ask only for a value needed for setup that remains unknown. Preserve unrelated existing instructions.

## Local bindings

```yaml
skill_locations:
  global-skill-source: "~/IdeaProjects/skills"
  repo-local-skill-source: "<target-repo>/.agents/skills"
  installed-skill-roots:
    - "~/.agents/skills"
  global-refresh-command: "npx skills add ~/IdeaProjects/skills/ -g --agent universal --skill '*' -y"
```

These are example machine settings. Use resolved paths for file operations and reports; keep location placeholders in reusable skill source. Preserve the configured install scope. `--all` installs to every supported agent and is not a substitute for `--agent universal`.

## Capture policy

At the end of substantial work, consider whether it revealed a durable procedural gap. A long task or a user correction is a reason to look, not a reason by itself to create a skill.

Use `auto-skill-capture` to decide what to retain and where it belongs. Search existing source skills first and prefer a focused patch. Use `create-skill` for authoring and realistic behavioral verification; use `skill-library-curator` for broader reviews, merges, and archiving.

Skills store reusable procedures, decision rules, prerequisites, pitfalls, and verification. Exclude progress, one-off outcomes, PR/issue numbers, branches, commit hashes, incident logs, secrets, private data, and facts that should be checked fresh.

Write global procedures to the configured global source. Keep repo-dependent instructions in the repo-local source. Installed/generated copies and third-party packages are read-only unless explicitly authorized. Keep reusable source free of machine-specific location bindings.

Apply focused changes within the user's authorized scope. Do not create a skill when the lesson is obvious, already covered, transient, or inseparable from private context. Do not turn capture into unrelated library rewrites. Ask for additional authorization only when a necessary action falls outside the existing request.

After global source changes, use the configured refresh command unless source-only work was requested. Repo-local changes need no global refresh. Report validation and any incomplete refresh accurately.
