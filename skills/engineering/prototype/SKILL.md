---
name: prototype
description: Build a throwaway prototype to answer a design question. Use when the user wants to sanity-check whether a state model or logic feels right, or explore what a UI should look like.
---

# Prototype

A prototype is **a focused experiment that answers a question**. The question decides the shape, fidelity, and whether code is needed. Producing an artifact is distinct from resolving the question.

## Pick a branch

Identify which question is being answered, using the user's prompt, the surrounding code, or by asking if the user is around:

- **"Does this logic / state model feel right?"** → [LOGIC.md](LOGIC.md). Build a single shareable HTML file (free-play buttons plus tabbed guided walkthroughs) that pushes the state machine through cases that are hard to reason about on paper, and that a non-developer can drive.
- **"How should this interface look or work?"** → [UI.md](UI.md). Use the separately installed Product Design plugin, grounded in current product patterns and resources, for visual exploration and any authorized interactive prototype.

If the distinction is unclear, call the Skill tool with "ux-discovery" to identify the uncertainty and useful fidelity. Clarify only when the missing choice materially changes the scope. A map or wireframe can be enough; a UI image does not prove interaction behavior.

## Rules that apply to both

1. **Throwaway from day one, and clearly marked as such.** Keep artifacts in the project's prototype/workspace conventions. For UI, let Product Design select its supported prototype setup within the authorized scope; preserve the real product and its reusable resources. Do not silently modify production routes or invent a new design system.
2. **Trivial to run.** A UI prototype starts from one command in the project's task runner: `pnpm <name>`, `python <path>`, `bun <path>`, etc. A logic demo is a single HTML file the user double-clicks. Either way, no thinking required to start it.
3. **No persistence by default.** State lives in memory. Persistence is the thing the prototype is _checking_, not something it should depend on. If the question explicitly involves a database, hit a scratch DB or a local file with a clear "PROTOTYPE, wipe me" name.
4. **Match the fidelity to the question.** Avoid production infrastructure and abstractions. Logic experiments stay minimal; UI work follows Product Design's required visual and browser QA. This rule never waives those checks.
5. **Make behavior observable.** Logic demos expose readable state; UI prototypes demonstrate the task and relevant transitions through the interface, without adding engineering debug panels to the product experience.
6. **Capture the answer and evidence.** Record what the experiment established, the human's decision, and remaining uncertainty in the caller's canonical record. Preserve the exact artifact/reference using project conventions. Reuse current branch scope; a new archive branch, publication, production integration, or deployment requires authorization for that action. A selected mock is not automatic approval to implement production code.
