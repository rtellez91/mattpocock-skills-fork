## What it does

Answer a question with a focused experiment. Logic experiments stay small; interface exploration and interactive prototypes use the separately installed Product Design plugin.

## When to reach for it

The agent may reach for this when a question needs concrete evidence, or you can invoke `/prototype`. The question determines whether images or working interaction are needed.

## Prerequisites

Visual work requires the separate Product Design plugin and access to the product references being reused. Logic experiments use the existing local development tools and do not require that plugin.

## Common questions

**Does choosing a mock authorize production implementation?**

No. An exploration-only request ends with its decision. An already-requested interactive prototype can continue after selection, while production integration remains a separate scope.

## It's working if

The prototype answers its question, reuses product references, and reports exactly what was and was not verified.

## Where it fits

This is a standalone experiment or a detour within an interview. [UX discovery](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/ux-discovery.md) frames the uncertainty, while [to-spec](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/to-spec.md) carries accepted findings into implementation requirements. [Ask Matt](https://github.com/rtellez91/mattpocock-skills-fork/blob/main/docs/engineering/ask-matt.md) maps the full workflow.
