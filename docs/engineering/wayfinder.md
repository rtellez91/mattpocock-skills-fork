## What it does

Organize a large uncertain effort as a shared map of decision tickets. The destination determines whether detailed design must be resolved or can be explicitly deferred.

## When to reach for it

You invoke this with `/wayfinder`; the agent does not start it automatically. Reach for it for work whose related decisions do not fit a single focused conversation. UX discovery supports product questions inside the existing ticket types.

## Prerequisites

Configure the issue tracker with `/setup-matt-pocock-skills` and identify the project workspace. The map needs a persistent home for its decisions; Product Design is required only for visual prototype work.

## Common questions

**Does finishing the map mean every screen is ready to build?**

Only if that was the destination. A requirements destination can leave named design work pending; an implementation-ready destination cannot hide it.

## It's working if

The map exposes decisions and dependencies, prototype tickets record conclusions rather than just assets, and pending design remains visible.

## Where it fits

This is a planning entry point for large uncertain efforts. Its settled decisions feed [to-spec](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/to-spec.md); [prototype](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/prototype.md) supplies concrete evidence when conversation alone cannot settle a question. [Ask Matt](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/ask-matt.md) maps the full workflow.
