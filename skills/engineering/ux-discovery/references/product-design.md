# Product Design bridge

Product Design means the separately installed `product-design` plugin. It owns visual exploration and prototype construction when this workflow needs them. This file owns the integration contract; do not copy the plugin's prompts or implementation procedures into other skills.

## Ground the request

Before visual generation, inspect the relevant current product sources:

- accepted requirements, decisions, and product design guidance;
- similar screens and complete flows, including return and recovery;
- the usable component catalog or Storybook, variants, states, and contracts;
- design tokens, typography, icon and image assets, content conventions, and accessibility rules;
- relevant hosted/provider surfaces and their customization limits.

Use applicable repository discovery skills when code structure must be explored. A folder name, logo, generated stylesheet, or old screenshot is not by itself evidence of the usable design system. Inspect real references. Honor current accepted product decisions; do not silently reuse a superseded experiment. If current sources contradict one another, surface the conflict before choosing an authority.

Prepare a compact brief: question, actor and task, target surface, fixed behavior, resources to reuse, permitted variation, relevant sizes and states, requested fidelity, and decision criterion. Attach the actual relevant screenshots or images to visual-generation calls; text-only descriptions of available images are not equivalent. State the referenced component and token constraints. If a named source cannot be accessed, follow the plugin's access-gap procedure and continue only independent work.

Existing product foundations stay fixed unless a new direction was explicitly requested. Compare structure, hierarchy, and interaction before changing brand style. Identify genuinely missing resources and propose additions without silently expanding the design system.

## Select the plugin workflow

Load the installed Product Design index and the focused skill it routes to. Resolve installed capabilities by name or plugin metadata, not a hard-coded cache version. Follow the plugin's current context, reference, selection, browser, and verification requirements.

| Need | Product Design capability |
| --- | --- |
| Inspect an existing experience | `audit` |
| Resolve a minimal brief | `get-context`, through the plugin router |
| Explore visual alternatives without a selected target | `ideate` |
| Build an interactive prototype from a selected target | `image-to-code` |
| Faithfully reproduce an explicitly requested live reference | `url-to-code` |

Availability is discovered, not assumed. If the plugin or a required capability is unavailable, name the missing dependency and offer to resolve it or continue nonvisual work. Do not substitute a coding-only UI design workflow without the user's explicit choice.

Set the authorized output boundary before starting: visual exploration only, focused interactive prototype, or another explicitly requested scope. The plugin's default selection and build flow is subordinate to that boundary. If images answer the question, stop after the decision; selecting an image during exploration-only work is not authorization to build. If a prototype was already requested, an unambiguous selection permits continuing that prototype without repeating approval. Production implementation and publication remain separate scopes.

The plugin's normal ideation flow currently uses three images before selection; do not promise a lower-fidelity output or different count that its active instructions do not support. Honor an explicit user override. A workflow choice that materially affects time, output, or fidelity should be explained before proceeding.

## Receive the result

Record the exact selected reference, the human's decision, covered viewport/state combinations, reused resources, any approved departures, and unresolved behavior. Generated images are visual evidence, not replacements for token definitions or component contracts. Reconcile conflicts against canonical sources before declaring readiness.

For a runnable prototype, require the plugin's browser and design QA evidence and report which interactions were exercised. A build or screenshot alone does not establish working behavior. Follow the plugin's handoff procedure, then return the finding to the original question without treating a passing visual comparison as user research.

Preserve the result under the project's existing artifact conventions with usable references. Apply [readiness](readiness.md) only to the deliverables actually covered. Do not infer implementation approval, update tracker state, or close design work beyond the caller's authorized scope.
