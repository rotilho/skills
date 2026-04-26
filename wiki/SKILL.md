---
name: "wiki"
description: "Organize and maintain a local wiki or repo knowledge base so durable knowledge stays clear, discoverable, linked, and easy to update over time. Use when agents need to decide where knowledge belongs, whether to update or create pages, how to name and scope pages, and how to keep notes, decisions, status, ownership, and sources consistent without heavy process."
license: "MIT"
compatibility: "opencode"
metadata:
  audience: "general"
  workflow: "knowledge-management"
  style: "concise"
---

# Wiki

Use this skill to keep repo-local knowledge organized like a maintainable wiki, not a pile of notes.

## When to use

Trigger for work like:
- organizing a local knowledge base, wiki, notes folder, or docs tree
- deciding where a new piece of knowledge should live
- choosing whether to update an existing page or create a new one
- naming, scoping, splitting, merging, or linking knowledge pages
- turning research, decisions, or repeated context into durable repo knowledge
- improving discoverability, summaries, ownership, or status on existing pages
- reducing duplication or drift across multiple knowledge artifacts

Do not use this skill to polish or expand temporary scratch work, raw research collection, or one-off prose unless the main problem is deciding where that knowledge should live or how it should be organized long term.

## Core promise

Produce wiki changes that:
- keep durable knowledge easy to find
- keep page scope clear and narrow enough to maintain
- keep related pages linked instead of duplicated
- keep temporary work separate from durable reference material
- capture context that helps future readers decide whether a page is current, authoritative, and still useful

## Hard constraints

- prefer updating a good existing page over creating a near-duplicate
- create new pages only when the topic, owner, lifecycle, or audience is meaningfully different
- keep durable knowledge in the repo's existing wiki or docs area when one is clear; keep drafts, working notes, and run-specific artifacts in `.workbench/wiki/`
- if no clear durable wiki location exists, ask the user instead of creating one implicitly
- do not promote temporary notes into durable pages without summarizing and de-duplicating them first
- keep page structure lightweight; use only the metadata and sections that help future maintenance
- favor navigable page names, short summaries, and explicit links over deep bureaucracy or rigid templates

## Workflow

### Step 1 - Classify the artifact before writing

Decide what kind of knowledge you are handling:
- durable reference: concepts, architecture, workflows, decisions, operating guidance, inventories
- time-bounded status: current state, rollout progress, migration tracking, ownership handoff
- temporary work: rough notes, raw captures, drafts, open questions, exploratory research

Default rule:
- durable knowledge belongs in the repo's existing wiki or knowledge base when one is clear; otherwise ask the user where it should live
- temporary work belongs in `.workbench/wiki/`

If the content is mostly unfinished or likely to expire soon, do not treat it as a durable page yet.

### Step 2 - Inventory before creating

Before adding a page, check what already exists:
- the durable wiki location the repo already uses, if any
- nearby pages on the same topic
- index or overview pages that should link to this topic
- decision logs, status pages, or reference pages that already own part of the content
- duplicate or stale pages that should be updated, merged, redirected, or retired

Prefer the smallest correct change that improves the knowledge base as a whole.

If multiple plausible durable locations exist or none exists, stop and ask instead of guessing.

### Step 3 - Decide update vs new page

Update an existing page when:
- the new information extends the same topic
- readers would reasonably expect to find it there
- splitting would create thin or overlapping pages

Create a new page when:
- the topic has distinct purpose or lifecycle
- the existing page is becoming hard to scan or maintain
- the content needs separate ownership, status, or decision history
- the new page can be linked from existing pages without ambiguity

When in doubt, update first and split later once the boundary is obvious.

### Step 4 - Name pages for retrieval, not cleverness

Prefer names that are:
- specific enough to predict content
- stable over time
- aligned with domain language readers will search for
- short enough to scan in a directory or link list

Prefer:
- concrete nouns or noun phrases
- consistent singular/plural choices within the same area
- names that distinguish overview pages from deep pages

Avoid:
- vague names like `notes`, `misc`, `thoughts`, or `stuff`
- names that only make sense to the current author
- date-based names for durable reference pages unless chronology is the point

### Step 5 - Keep one page, one job

Each page should have a primary job, such as:
- explain a concept
- describe a workflow
- record a decision
- track current status
- index a topic area

Keep supporting context, but do not mix multiple jobs so heavily that readers cannot tell whether the page is a reference, a decision log, or a status tracker.

If a page tries to do too much, split by purpose and cross-link the pieces.

### Step 6 - Use lightweight hierarchy and linking

Organize the wiki so readers can move:
- from overview to detail
- from stable reference to changing status
- from decisions to the pages they affect
- from a page to its related concepts, workflows, and owners

Prefer shallow, understandable hierarchies over deep folder trees.

Use links to connect:
- parent overview -> child detail pages
- detail page -> owning overview page
- workflow page -> related decisions, tools, and status pages
- status page -> source reference or canonical plan

Links should reduce searching, not create a web of redundant pages.

### Step 7 - Summarize early, detail below

Start durable pages with a short summary that answers:
- what this page is for
- when to use it
- what is most important right now

Then place deeper detail below the summary.

Default page shape, adapted as needed:
- summary
- main content
- related pages
- source or context notes when relevant

Useful optional fields or sections when they materially help:
- status
- owner
- last reviewed or as-of date
- decision
- source of truth

Only include them when readers need them to judge freshness, authority, or next action.

### Step 8 - Capture source, status, and ownership where they matter

For knowledge that may age or be disputed, record enough context to answer:
- where this came from
- who owns or maintains it
- whether it is current, proposed, deprecated, or historical
- what decision or event changed it

Do this lightly. A short line is often enough.

Examples:
- `Status: active`
- `Owner: platform team`
- `As of: 2026-04-22`
- `Source: incident review 2026-04-18`

### Step 9 - Remove duplication by linking and merging

If the same knowledge appears in multiple places:
- choose one canonical page for the durable version
- trim the duplicates to a brief summary or link
- merge overlapping pages when separate ownership is not justified

Small repetition for local readability is fine.
Do not copy whole sections across pages when a clear link would keep them aligned.

### Step 10 - Keep the wiki maintainable

Favor pages that future agents can safely update.

That usually means:
- concise summaries
- explicit scope
- obvious page names
- clear canonical location for each topic
- light metadata only where it changes decisions
- archived or removed stale pages instead of leaving misleading history in place

If a process would make the wiki harder to update than to ignore, simplify it.

### Step 11 - Keep overlap boundaries clear

If the main task is:
- evidence-backed external or multi-source research: use `deep-research`
- creating or improving agent skills: use `create-skill`
- general code quality or architecture advice: use `code-practice`
- rewriting for brevity or tighter wording: use `concise`

Use this skill when the main problem is where knowledge should live, how pages should relate, and how to keep the knowledge base useful over time.

## Verification checklist

Before finishing, confirm that you:
- classified durable knowledge vs temporary notes
- checked for an existing page before creating a new one
- checked whether the repo already has a clear durable wiki location
- chose a clear, searchable page name
- kept each page focused on one primary job
- added summaries and links that improve discovery
- captured status, owner, decision, or source only where they help
- reduced duplication instead of spreading it
- kept drafts or run-specific artifacts in `.workbench/wiki/`, not the durable wiki
- asked the user when the durable wiki location was missing or ambiguous
- kept the process practical rather than bureaucratic
