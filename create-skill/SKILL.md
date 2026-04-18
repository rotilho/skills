---
name: create-skill
description: Create or improve an agent skill. Use when the user wants to add a new SKILL.md, refactor an existing skill, improve trigger accuracy, tighten instructions, or turn a repeated workflow into a reusable skill.
license: MIT
compatibility: opencode
metadata:
  audience: general
  workflow: authoring
  style: concise
---

# Create Skill

Use this skill when the user wants to create, rewrite, or optimize a reusable agent skill.

Activate it for tasks like:
- create a new skill from an idea, prompt, or workflow
- improve an existing `SKILL.md`
- make a skill trigger more reliably
- turn repeated instructions into a reusable skill
- split an overgrown skill into cleaner sections or bundled resources

## Core promise

Produce a skill that is:
- valid for the target runtime
- easy for an agent to trigger correctly
- procedural instead of vague
- as short as possible while still useful
- verified enough to hand off with confidence

Do not stop at a draft unless the user asked for planning only.

## Hard constraints

Treat these as hard requirements unless the local runtime clearly documents different rules:

- create one folder per skill and put `SKILL.md` inside it
- use YAML frontmatter at the top of `SKILL.md`
- recognized frontmatter fields are `name`, `description`, `license`, `compatibility`, and `metadata`
- `name` must be lowercase kebab-case, 1-64 chars, and match the folder name
- `description` is the main trigger mechanism, so make it specific about when to use the skill
- keep the body lean; if the skill grows large, move detail into `references/`, `scripts/`, or `assets/`

If local repo conventions conflict with generic examples, prefer the runtime's documented constraints over stylistic habits.

## Working rule

Write the `description` first, not last.

The description is what the agent sees before loading the skill. A weak description causes under-triggering even if the body is excellent. Include:
- what the skill helps do
- when it should trigger
- nearby phrasings or contexts that should also trigger it

Be a little pushy when needed. It is usually better for a good skill to trigger slightly more often than to be invisible.

## Workflow

### Step 1 - Frame the job

Infer or confirm:
- skill name
- whether this is `new-skill` or `update-skill`
- target runtime or repo
- user goal
- expected outputs
- whether trigger optimization matters

If the user did not give a name, infer a short kebab-case name.

### Step 2 - Inspect before writing

Read local examples first.

Check:
- existing skills in the repo
- local tone and section patterns
- any runtime docs for skill discovery or frontmatter rules

Use local examples for style. Use documented runtime rules for validity.

### Step 3 - Scaffold

For a new skill, scaffold with:

```bash
npx skills init <skill-name>
```

Then replace placeholders completely.

If the scaffold command behaves oddly, clean up only what you created and continue with the intended folder.

### Step 4 - Write the skill

At minimum include:
- a strong `description`
- a clear title
- activation guidance
- step-by-step instructions
- any constraints or caveats
- a verification checklist

Prefer imperative guidance. Tell the agent what to do.

Avoid:
- generic mission-statement filler
- repeating the same idea in multiple sections
- giant walls of prose when a short checklist works
- unsupported frontmatter fields

### Step 5 - Use resources when warranted

If the skill needs large or reusable material, organize it instead of bloating `SKILL.md`.

Typical layout:

```text
skill-name/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

Use:
- `references/` for long docs or domain guides
- `scripts/` for deterministic repeated work
- `assets/` for templates or files consumed by outputs

### Step 6 - Verify triggering

Create a small eval set before finishing:
- 3 should-trigger prompts
- 3 near-miss should-not-trigger prompts

Check whether the description would help the agent choose this skill over adjacent ones.

Focus on realistic prompts, not toy keywords.

### Step 7 - Verify the final artifact

Check:
- folder exists in the expected location
- `SKILL.md` exists and is not scaffold boilerplate
- `name` matches folder name
- frontmatter fields are valid and intentional
- instructions are actionable
- skill is not needlessly long

If there is a repo-specific check for skills, run the smallest relevant one.

## Default structure

Use this shape unless local conventions strongly suggest another one:

```md
---
name: <skill-name>
description: <what it does and when to use it>
license: <license>
compatibility: <agent>
metadata:
  audience: <audience>
  workflow: <workflow>
---

# <Title>

## When to use

## Core promise

## Hard constraints

## Workflow

## Verification checklist
```

## Verification checklist

Before finishing, confirm that you have:
- inspected local examples
- matched the folder name and skill name
- written a triggerable description, not just a topic label
- removed scaffold placeholders
- kept the skill concise
- added supporting files only when they earn their keep
- verified the final layout

## Final answer style

When reporting back, include:
- what skill was created or updated
- which files changed
- what you improved about triggering or structure
- any limitations or open risks
- what you verified
