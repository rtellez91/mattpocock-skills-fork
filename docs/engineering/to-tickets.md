## What it does

Split established scope into verifiable implementation slices and bounded design work when needed. Dependencies describe what actually gates each complete deliverable.

## When to reach for it

You invoke this with `/to-tickets`; the agent does not start it automatically. Reach for it when the scope is ready to decompose. If design can still change delivery boundaries, the agent identifies that decision before pretending the slices are final.

## Prerequisites

Configure the issue tracker and readiness vocabulary with `/setup-matt-pocock-skills`. Supply the established scope and accessible decision references; publication follows review of the breakdown.

## Common questions

**Must one design ticket block all engineering work?**

No. Only work that needs its answer is blocked. Existing design may already cover UI work, and a backend task can still depend on an unresolved experience decision.

## It's working if

Tickets lead with purpose, result, and observable acceptance; design work is distinguished from implementation; blockers have reasons.

## Where it fits

This follows [to-spec](https://github.com/rtellez91/mattpocock-skills-fork/blob/product-ux/docs/engineering/to-spec.md) or another sufficiently established plan. [Implement](https://github.com/rtellez91/mattpocock-skills-fork/blob/product-ux/docs/engineering/implement.md) executes eligible slices while design work follows its human decision workflow. [Ask Matt](https://github.com/rtellez91/mattpocock-skills-fork/blob/product-ux/docs/engineering/ask-matt.md) maps the full workflow.
