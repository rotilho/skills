Assessment: rotilho/skills

I cloned https://github.com/rotilho/skills at commit 05fd5c1.

Repo snapshot:
- 8 skills
- Valid YAML frontmatter
- Skill names match folders
- No README
- GitHub metadata: 0 stars / 0 forks
- Main compatibility target: opencode

Overall: good private/operator skill repo. Strong at trigger boundaries, concise procedural guidance, and avoiding overlap. Weak at examples, runnable assets, external references, and discoverability for public reuse.

Skill quality table

| Skill | Score | 3 popular similar references used for comparison | Assessment |
|---|---:|---|---|
| `code-practice` | **8.1/10** | `donnemartin/system-design-primer` ★344k, `ryanmcdermott/clean-code-javascript` ★94k, `zedr/clean-code-python` ★4.8k | Strong agent-facing clean-code workflow. Better than popular guides at *decision discipline* and avoiding generic abstractions. Weaker because it has almost no concrete before/after examples, no language-specific examples, and no references. Good as an internal base layer, less strong as public learning material. |
| `concise` | **8.5/10** | `f/awesome-chatgpt-prompts` ★160k, `dair-ai/Prompt-Engineering-Guide` ★74k, `danielmiessler/Fabric` ★41k | Very good behavioral skill. Clear modes, clear trigger, practical examples. More usable as an agent style-control skill than huge prompt collections. Weakness: no measurable quality test, no “bad/good rewrite” set beyond a few examples, and “default mode after domain skill selection” may over-trigger if installed broadly. |
| `create-skill` | **8.4/10** | `anthropics/skills` ★124k, `ComposioHQ/awesome-claude-skills` ★56k, `travisvn/awesome-claude-skills` ★12k | Strong. It knows skill anatomy, trigger optimization, support files, and verification. Good internal authoring standard. Main risk: `npx skills init` and allowed frontmatter fields are runtime-specific; if reused outside this repo, it may be wrong. Needs official-runtime links and maybe an eval template file. |
| `deep-research` | **8.8/10** | `stanford-oval/storm` ★28k, `assafelovic/gpt-researcher` ★27k, `microsoft/AI-For-Beginners` ★47k | Best skill in repo. Very mature workflow: knowledge inventory, gap map, source governance, contradiction pass, evidence registry, deliverable modes. Stronger than many research-agent prompts because it controls research waste. Weakness: very long for a skill body; should move templates/register formats into `references/`. Also lacks runnable citation tooling. |
| `kotlin-code-style` | **7.7/10** | `JetBrains/kotlin` ★53k, `pinterest/ktlint` ★6.7k, `android/nowinandroid` ★21k | Good opinionated Kotlin guidance. Nice overlap boundaries with Spring/Cucumber. Strong on ownership, extensions, nullability, coroutine ownership. Weak compared with canonical refs because it has no code examples, no ktlint/Detekt config notes, no official style links, and no concrete “prefer this over that” snippets. |
| `kotlin-cucumber-tests` | **8.2/10** | `cucumber/cucumber-jvm` ★2.8k, `cucumber/cucumber-java-skeleton` ★498, `cucumber/cucumber-expressions` ★196 | Strong specialized skill. Clear on when Cucumber fits, feature-file quality, step-definition scope, hooks, fixtures, and Kotlin glue. Better than starter repos for agent review behavior. Weakness: lacks runnable Gradle/Maven setup, package examples, sample feature + step files, and version-specific Cucumber JVM notes. |
| `spring-application-code-style` | **7.6/10** | `spring-projects/spring-boot` ★80k, `spring-projects/spring-petclinic` ★9.1k, `spring-guides/gs-spring-boot` ★980 | Good Spring application architecture heuristic. Strong on thin controllers, feature ownership, Spring boundaries, bean wiring distinction, and transactions. Weak compared with Spring examples because it has no code snippets, no package tree example, no test slice guidance, and intentionally avoids some house rules. Good review skill, less complete implementation skill. |
| `wiki` | **8.5/10** | `logseq/logseq` ★42k, `foambubble/foam` ★17k, `dendronhq/dendron` ★7.4k | Very good knowledge-management skill. Strong at update-vs-create decisions, durable vs temporary knowledge, page scope, linking, duplication control. More practical for repo-local wiki hygiene than big PKM tools. Weakness: lacks templates for page types, index conventions, and examples of good/bad page splits. |


Overall repo grade

8.2/10

This is a high-quality agent behavior skill pack, not a public tutorial/reference pack.

Strong points

- Clear trigger descriptions.
- Good overlap boundaries between adjacent skills.
- Strong “when not to use” discipline.
- Good verification checklists.
- Consistent style across skills.
- Strong internal operating model: concise, procedural, low fluff.
- Skills are short enough except deep-research.

Main weaknesses

1. No README
    - Public users won’t know purpose, install path, compatibility, or skill list.

2. Few concrete examples
    - Kotlin/Spring/code-practice especially need before/after snippets.

3. No official source links
    - Kotlin, Spring, Cucumber, Claude/OpenCode skill formats should link to canonical docs.

4. No test/eval harness
    - create-skill mentions eval prompts, but repo does not include shared trigger-eval fixtures.

5. No reusable templates except deep-research reference
    - wiki, create-skill, kotlin-cucumber-tests, and spring-application-code-style would benefit from templates/.

6. Some skills are more review-guidance than implementation-ready
    - Spring/Kotlin are good for steering an agent, but weaker for generating concrete project changes.

Priority improvements

| Priority | Change | Why |
|---:|---|---|
| 1 | Add `README.md` with install/use instructions and skill matrix | Biggest repo-quality gap |
| 2 | Add examples to Kotlin, Spring, Cucumber, Code Practice | Raises usefulness fastest |
| 3 | Move long `deep-research` templates into `references/` | Keeps skill lightweight |
| 4 | Add `evals/trigger-prompts.md` per skill or repo-wide | Makes trigger quality testable |
| 5 | Add canonical source links | Improves trust and correctness |
| 6 | Add page/template files for `wiki` and `create-skill` | Makes repeatable outputs stronger |


Bottom line

rotilho/skills is well-designed for personal/agent use. It beats many popular repos in agent-operational clarity. It does not beat popular repos as a public reference library because it lacks examples, docs, citations, and runnable scaffolding.

Best skills: deep-research, wiki, concise, create-skill.  
Most improvement needed: spring-application-code-style, kotlin-code-style, code-practice. (2/2)