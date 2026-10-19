## What it does

Build an authorized spec or ticket using accepted contracts and relevant validation. It checks design readiness and actual dependencies before implementing an affected experience.

## When to reach for it

You invoke this with `/implement`; the agent does not start it automatically. Reach for it for a sufficiently specified piece of implementation work. A design or decision ticket belongs in its human decision workflow.

## Prerequisites

Provide an authorized scope and access to its canonical requirements. Keep the original `tdd` and `code-review` skills installed, and use the project's required build and verification tools.

## Common questions

**What happens when the visual direction is still undecided?**

The agent names the missing decision and continues only independent authorized work. It does not silently select a design on your behalf.

## It's working if

The implementation reuses accepted resources, verifies relevant browser behavior, and reports unavailable checks without claiming they passed.

## Where it fits

This is the per-ticket execution step after [to-tickets](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/to-tickets.md). Use [implement-spec](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/implement-spec.md) when you want orchestration across the whole eligible task graph. [Ask Matt](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/ask-matt.md) maps the full workflow.
