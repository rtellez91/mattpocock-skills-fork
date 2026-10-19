## What it does

`to-spec` turns the conversation you have just had into a **[spec](https://www.aihero.dev/ai-coding-dictionary/spec)**, and publishes it to your issue tracker as a single issue.

It does not interview you. When you reach for it, the agreed scope is ready to record, even if some detailed design decisions are explicitly deferred. So it synthesises what is known (from the thread, the codebase, your `GLOSSARY.md` and ADRs) and does not start a new round of questions. The spec records decisions you already made. It is not a place to make new ones.

## When to reach for it

You invoke this by typing `/to-spec`; the [agent](https://www.aihero.dev/ai-coding-dictionary/agent) won't reach for it on its own.

Reach for it when the build is too big for one agent [session](https://www.aihero.dev/ai-coding-dictionary/session) and must be split across several. That is the whole trigger:

| Where you are | What to run |
| --- | --- |
| You haven't decided anything yet | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) first |
| Decided, and the work fits one [context window](https://www.aihero.dev/ai-coding-dictionary/context-window) | [implement](https://aihero.dev/skills-implement): skip the spec |
| Decided, and the work spans several sessions | `/to-spec`, then [to-tickets](https://aihero.dev/skills-to-tickets) |
| A [wayfinder](https://aihero.dev/skills-wayfinder) map has cleared | `/to-spec #<map_issue>` |

## Prerequisites

`to-spec` publishes the spec as an issue, so [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) must first configure a tracker and the triage-label vocabulary for this repo. Either kind of tracker works: a real tracker like GitHub, or local markdown files under `.scratch/`, which work with no extra setup.

## The spec is a decision record

The spec exists because context windows end. You settled many things while [grilling](https://www.aihero.dev/ai-coding-dictionary/grilling): the shape of the solution, the choices you argued through, and what you deliberately refused. All of that is in one conversation that you are about to clear. The spec keeps it.

The spec does not invent product decisions. It records what you decided and assesses the existing evidence, in your project's own vocabulary, so a fresh session can pick up the work without you explaining it again. If the spec states something you never said, that is a defect.

For experience-bearing work, [UX discovery](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/ux-discovery.md) assesses current evidence without starting research or design. The spec leads with outcomes, functional requirements, and observable acceptance scenarios for the whole team, then technical contracts. It records readiness per deliverable, exact references, and pending decisions with their effects.

## Seams before prose

Before it writes anything, `to-spec` sketches the **seams** where the feature will be tested, and checks them with you. It prefers existing seams to new ones, and picks the highest seam it can. The ideal number of seams for a change is one.

Other skills use those agreed seams later. [tdd](https://aihero.dev/skills-tdd) works only at seams you agreed in advance. [code-review](https://aihero.dev/skills-code-review) reviews the diff against the spec, so a seam nobody agreed to shows up as a review finding. Both connections go through this document. That is why you should take the seam conversation seriously here, and not leave it for implementation.

## Common questions

**Where did `/to-prd` go?**
It is this skill, renamed in v1.1. "Spec" is now the one term used throughout, and the old `to-prd` slug no longer works, so reinstall under the new name. The old vocabulary is replaced by the pair *spec* and *tickets*. The spec is the destination and the decisions that fix it. The [tickets](https://www.aihero.dev/ai-coding-dictionary/ticket) are the steps that get there. If you change direction, delete the unfinished tickets and keep the spec.

**Does the spec automatically get the `ready-for-agent` label?**
No. This fork uses the configured tracker roles according to actual readiness. A parent spec is not automatically an executable ticket, and pending design must remain visible. A complete requirements record does not make every deliverable ready for autonomous implementation.

**Why not go straight from grilling to `/to-tickets` and skip the spec?**
Often you should. The spec is worth its step only on multi-session work. Its value is that the tickets are disposable and the spec is not. Each ticket is sized for one fresh context window and then gets deleted or closed, while the spec stays as the one place that records the reasoning behind them. On a single-session change, that gives you nothing, and you pay for an extra synthesis step where the [model](https://www.aihero.dev/ai-coding-dictionary/model) can drift. Go from grilling to `/implement`.

**I just finished a wayfinder map. What do I feed it?**
Give it the main map issue, `/to-spec #<map_issue>`, not the individual decision tickets. [wayfinder](https://aihero.dev/skills-wayfinder) produces decisions spread across a map, not deliverables. `to-spec` collapses them into one document you can build from. If you loop the map straight into `/implement`, you lose that step.

**Is the spec for me to review, or is it just for the agent?**
Both the team and the agent should be able to review it. Outcomes, requirements, and observable acceptance scenarios come before implementation detail. Read the seams, design readiness, and out-of-scope section carefully: a wrong decision there is cheaper to catch now than during implementation.

**Do I keep the spec frozen once tickets start, or let the agent rewrite it?**
When design changes an agreed requirement, obtain the product decision before revising its canonical record and affected ticket references. This is not automatic synchronization. Keep lasting domain terminology in `GLOSSARY.md` and architectural decisions in ADRs, and link those sources rather than duplicating their editable content.

**My work is a refactor or a module boundary, not a feature. Does the template fit?**
Yes. Use only applicable sections. Internal work without a meaningful actor can omit user stories and state its purpose and observable guarantees instead. Record lasting architectural decisions as ADRs through [grill-with-docs](https://aihero.dev/skills-grill-with-docs), and reference them from the spec.

**Will it check the tracker for related work, or cite the ADRs it's respecting?**
The fork links canonical decisions and design evidence rather than duplicating them. It does not automatically search the tracker for overlapping work, so a spec can still duplicate an existing issue. If the area is busy, inspect related work before publication.

**`/to-tickets` couldn't read my spec: it kept truncating.**
A tracker issue may not return a very large spec in full, and there is no local copy to use instead. To fix this, do not [clear](https://www.aihero.dev/ai-coding-dictionary/clearing) or [compact](https://www.aihero.dev/ai-coding-dictionary/compaction) between `/to-spec` and `/to-tickets`. Run them in the same window, and `/to-tickets` never has to fetch the spec again.

## It's working if

- It starts writing instead of asking you a new round of questions.
- It shows you the seams before it writes, and proposes as few as it can.
- It uses your project's nouns, not generic product-management boilerplate.
- You remember making every decision in it. It invented nothing to fill a section.
- The out-of-scope section lists real things. The things you refused are usually the most useful lines on the page.

## Where it fits

`to-spec` is a step in the main build chain, but only on the multi-session branch of it:

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
```

Upstream, [grill-with-docs](https://aihero.dev/skills-grill-with-docs) makes the decisions that this skill only records, and a finished [wayfinder](https://aihero.dev/skills-wayfinder) map joins the chain here. Downstream, [to-tickets](https://aihero.dev/skills-to-tickets) cuts the spec into tracer-bullet tickets for [implement](https://aihero.dev/skills-implement) to build. When you're unsure which skill or flow fits, [ask-matt](https://aihero.dev/skills-ask-matt) routes you.
