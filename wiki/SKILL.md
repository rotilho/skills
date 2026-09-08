---
name: "wiki"
version: "1.1.1"
description: "Organize a local wiki or repo knowledge base: decide where durable knowledge belongs, update or merge existing pages, create distinct pages when needed, and maintain useful names, links, sources, and freshness context. Use for knowledge organization, not temporary notes or prose polishing."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "knowledge-management"
---

# Wiki

Keep durable knowledge easy to find, verify, and update. Prefer one clear home for a topic over repeated explanations across pages.

## When to use

Use when organizing docs or a knowledge base, deciding where new knowledge belongs, merging overlapping pages, or improving their scope and discoverability.

Use `deep-research` for gathering evidence and `create-skill` for agent procedures. Handle prose-only edits directly, following AGENTS.md writing guidance. Raw research and temporary progress are not durable wiki pages.

## Workflow

### 1. Find the existing home

Inspect the repo's wiki/docs area, nearby pages, indexes, decision logs, and relevant source material. Separate durable reference, changing status, and temporary working notes.

Use the established location or one the user named. Keep drafts and run-specific artifacts in `.workbench/wiki/`. If the durable location is missing or ambiguous, prepare the content in scratch and clarify the destination before publishing it into the repo.

### 2. Choose the smallest useful change

- Update an existing page when it owns the same topic and audience.
- Create or split a page when purpose, lifecycle, audience, or ownership is meaningfully different, or the existing page has become hard to use.
- Merge overlapping pages into a canonical owner. Replace duplicate explanations with short links or summaries, repairing inbound links when retiring a page.
- Leave a useful page alone when a rewrite would only rearrange it.

Do not promote rough notes by copying them wholesale. Summarize the durable facts, decisions, and operating guidance first.

### 3. Write for retrieval and maintenance

- Use stable, concrete names in the repo's vocabulary. Avoid `misc`, author-only shorthand, and date-based names unless chronology is the page's purpose.
- Give each page one primary job: reference, workflow, decision, status, or index. Link related jobs instead of blending them into one long page.
- Start with a short explanation of the page's purpose and key information, then add needed detail.
- Use shallow structure and links from an existing overview so readers can find the page. Link related references, decisions, workflows, and status where useful.
- Include source, owner, status, or as-of date only when readers need it to judge authority, freshness, or next action. Do not invent owners or review dates.

Use only the sections and metadata the content needs. A small update does not need a new hierarchy or template.

## Verification

- Durable content has a clear canonical home; scratch and transient status remain distinguishable.
- Names, summaries, and overview links make the content discoverable.
- Merges preserve useful information and leave working links.
- Sources and freshness context support claims that may age or be disputed.
- The change reduces duplication without adding unnecessary pages or process.
