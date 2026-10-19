## What it does

Synthesize established discussion into a team-readable spec, preserving technical contracts and experience evidence. It does not restart the interview or invent missing design decisions.

## When to reach for it

You invoke this with `/to-spec`; the agent does not start it automatically. Reach for it after enough discussion to capture the agreed scope. A spec may explicitly name design work that still prevents implementation.

## Prerequisites

Use the existing project discussion and repository context. Configure the issue tracker and readiness vocabulary with `/setup-matt-pocock-skills` before publication.

## Common questions

**Does a finished spec automatically become ready for an autonomous agent?**

No. Readiness is assessed per deliverable, and a parent spec is not automatically an executable work ticket. Pending design remains explicit.

## It's working if

Product and engineering readers can find the outcome and acceptance scenarios; technical detail follows; unresolved decisions are visible.

## Where it fits

This is the synthesis step after [grill-with-docs](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/grill-with-docs.md) or Wayfinder. [To tickets](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/to-tickets.md) decomposes the resulting scope and retains its decision dependencies. [Ask Matt](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/ask-matt.md) maps the full workflow.
