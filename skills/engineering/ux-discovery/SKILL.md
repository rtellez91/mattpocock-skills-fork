---
name: ux-discovery
description: Choose UX methods and fidelity for an unresolved product-experience question, ground visual work in existing product resources, or assess whether an experience is ready for implementation. Use during product interviews, wayfinding, prototyping, specification, ticketing, or implementation readiness checks; internal changes with no experience impact need only a brief applicability check.
---

# UX Discovery

Help the current workflow resolve experience uncertainty. Keep its interview, decision ownership, scope, and canonical record. This is a shared guide, not a second interview or a mandatory design phase.

## Choose the operation

- **Discovery:** identify the question that prevents a product decision, then choose a proportionate method using [methods](references/methods.md). Continue the caller's interview with what was learned.
- **Assessment:** when synthesizing a spec, decomposing tickets, or checking implementation readiness, inspect existing evidence using [readiness](references/readiness.md). Report gaps without starting research, visual generation, or another interview.
- **Visual work:** when authorized to explore or prototype an interface, use [the Product Design bridge](references/product-design.md). It owns the integration with the separately installed Product Design plugin. A readiness check never implies permission to start this work.

When a caller needs several operations, perform only those its current task authorizes. For a behavior-preserving internal change, record why experience design is not applicable and return to the caller.

## Frame the uncertainty

Establish the actor, goal, situation, decision still open, available evidence, and consequence of getting it wrong. Reuse settled answers. Distinguish observed behavior, stakeholder decisions, expert inspection, and hypotheses. A generated persona, journey, or simulation is not user research.

Select the method yourself and explain it briefly: the question, why this method helps, the material needed, and the evidence that would let the next decision proceed. Ask the human about product tradeoffs or missing facts only when they cannot be obtained from available sources. Do not ask them to select a UX methodology.

Choose fidelity independently for content, interaction, and appearance. Use enough detail to examine the question; high visual finish is not evidence of usability. Reuse an established pattern when it already resolves the question.

Keep the complete experience in view, including entry, completion, interruption, recovery, and transitions to other people or hosted services where relevant. Map ownership before slicing by technical layer. One experience may span several implementation tickets.

## Decide when design belongs

The agent chooses the order and states its reason:

- Design before decomposition when the open decisions could change the outcome, scope, flow, or independently deliverable boundaries. Keep implementation slices provisional until those decisions settle.
- Create bounded design work with dependencies when delivery boundaries are stable and the missing design outcome can be stated precisely.
- Proceed through existing contracts when current design evidence covers the experience.

Only block work that needs the unresolved decision to be completely implemented or verified. Backend work is not automatically independent, and UI work is not automatically blocked. Scope or product changes still require the human's decision. Tracker mutations follow the caller's authorization and review process.

## Return to the caller

Record only what this task earned in its existing spec, decision ticket, or discussion:

- question and method, with the reason for using it;
- findings with evidence and limitations;
- human decisions and exact design references selected;
- unresolved assumptions and the work they affect;
- readiness disposition and next action, when assessment was requested.

Link evidence rather than duplicating editable requirements. A question is resolved when the evidence supports its agreed decision criterion or the human explicitly chooses a course with the remaining uncertainty recorded. If evidence is insufficient, state the gap instead of substituting invented observations.

Finish when the caller can make its next decision or has a concrete named blocker. Do not turn every possible UX concern into a deliverable.
