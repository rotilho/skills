---
name: "create-skill"
description: "Create or improve an agent skill. Use when the user wants a new `SKILL.md`, a rewrite of an existing skill, better trigger coverage or trigger/overlap evaluation, tighter instructions, or a repeated workflow turned into a reusable skill."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "authoring"
  style: "concise"
---

# Create Skill

Use this skill to create, rewrite, or tighten reusable agent skills.

Trigger for work like:
- create a new skill from an idea, prompt, or workflow
- improve an existing `SKILL.md`
- make a skill trigger more reliably
- review a skill's trigger coverage or overlap without necessarily editing it
- tighten vague or repetitive instructions
- split an oversized skill into cleaner sections or support files

## Core promise

Produce a skill that is:
- valid for the target runtime
- easy to trigger correctly
- procedural, not vague
- short enough to stay usable
- verified enough to hand off

Do not stop at a draft unless the user asked for planning only.

## Hard constraints

Unless local runtime docs say otherwise:
- create one folder per skill with `SKILL.md` inside it
- use YAML frontmatter at the top of `SKILL.md`
- only use recognized frontmatter fields: `name`, `description`, `license`, `compatibility`, `metadata`
- keep `name` lowercase kebab-case, 1-64 chars, and matched to the folder name
- write `description` for triggering, not as a topic label
- always quote string-valued YAML frontmatter fields; do not leave them unquoted
- keep the body lean; move bulky detail into `references/`, `scripts/`, or `assets/` when needed

If repo conventions and runtime rules conflict, follow the runtime rules.

## Working rule

Write the `description` first.

It is the main trigger surface. A good body cannot fix a weak description.

Make it say:
- what the skill helps do
- when it should trigger
- nearby phrasings that should also trigger it

Bias slightly toward over-triggering rather than invisibility.

## Workflow

### Step 1 - Frame the job

Infer or confirm:
- skill name
- `new-skill` or `update-skill`
- target runtime or repo
- user goal
- expected outputs
- whether trigger optimization matters

If the user did not give a name, infer a short kebab-case one.

### Step 2 - Inspect before writing

Read local examples first.

Check:
- existing skills in the repo
- local tone and section patterns
- runtime docs for discovery or frontmatter rules

Use local examples for style and runtime docs for validity.

### Step 3 - Scaffold

For a new skill, scaffold with:

```bash
npx skills init <skill-name>
```

Then replace every placeholder.

If scaffolding misbehaves, clean up only what you created and continue.

### Step 4 - Write the skill

At minimum include:
- a strong `description`
- a clear title
- activation guidance
- step-by-step instructions
- constraints or caveats
- a verification checklist

Prefer imperative guidance.

Avoid:
- mission-statement filler
- repeated guidance across sections
- long prose where a checklist works
- unsupported frontmatter fields

Frontmatter rule:
- always write string-valued frontmatter fields as quoted YAML strings
- this includes at least: `name`, `description`, `license`, `compatibility`, and string values inside `metadata`

### Step 5 - Use support files only when they help

If the skill needs large or reusable material, move it out of `SKILL.md`.

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
- `scripts/` for repeatable deterministic work
- `assets/` for templates or bundled files

### Step 6 - Verify triggering

Create a small eval set:
- 3 should-trigger prompts
- 3 near-miss should-not-trigger prompts

Check that the description helps the agent choose this skill over adjacent ones.

Use realistic prompts.

### Step 7 - Verify the artifact

Check:
- the folder exists where expected
- `SKILL.md` is not scaffold boilerplate
- `name` matches the folder name
- frontmatter is valid and intentional
- instructions are actionable
- the skill is not longer than it needs to be

If the repo has a skill check, run the smallest relevant one.

## Default structure

Use this shape unless local conventions clearly differ:

```md
---
name: "<skill-name>"
description: "<what it does and when to use it>"
license: "<license>"
compatibility: "<agent>"
metadata:
  audience: "<audience>"
  workflow: "<workflow>"
---

# <Title>

## When to use

## Core promise

## Hard constraints

## Workflow

## Verification checklist
```

## Verification checklist

Before finishing, confirm that you:
- inspected local examples
- matched the folder name and skill name
- wrote a triggerable description
- quoted string-valued YAML frontmatter fields
- removed scaffold placeholders
- kept the skill concise
- added support files only when needed
- verified the final layout

## Final answer style

Report back with:
- what skill was created or updated
- which files changed
- what improved in triggering or structure
- any limitations or open risks
- what you verified
