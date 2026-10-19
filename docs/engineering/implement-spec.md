## What it does

Implement a spec across eligible tickets using the existing task graph. The execution frontier excludes pending design and human decisions.

## When to reach for it

You invoke this with `/implement-spec`; the agent does not start it automatically. Reach for it when you want the existing multi-agent implementation workflow. Its authorization and branch/worktree rules still apply.

## Prerequisites

Provide the canonical spec, configured tracker, and linked tickets with blocking relationships. This workflow needs permitted agent delegation and Git worktrees, plus the original `tdd` and `code-review` skills.

## Common questions

**What if only design decisions remain?**

The agent reports completed work and the exact pending decisions and returns control. It does not assign an implementer to invent them or declare the spec complete.

## It's working if

Independent work proceeds, design-dependent work waits on evidence, and prototype QA is not presented as production verification.

## Where it fits

This orchestrates the tickets produced by [to-tickets](https://github.com/rtellez91/mattpocock-skills-fork/blob/product-ux/docs/engineering/to-tickets.md). [Implement](https://github.com/rtellez91/mattpocock-skills-fork/blob/product-ux/docs/engineering/implement.md) is the alternative when driving one ticket at a time. [Ask Matt](https://github.com/rtellez91/mattpocock-skills-fork/blob/product-ux/docs/engineering/ask-matt.md) maps the full workflow.
