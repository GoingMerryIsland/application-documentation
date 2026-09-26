# Activity diagrams for use cases and use-case mapping

Read for Activity Diagram for Use Case, Mapping Use Cases to Activity Diagrams, or activity/swimlane creation and corrections. This is an internal application-documentation resource. Keep work scoped to the requested features; load no companion skills.

## Reference concept and output

Use the user's reference concept: a bordered canvas divided into clearly labeled responsibility lanes, with actions owned by the actor or system and arrows crossing lanes for handoffs. Favor clean monochrome lines and light backgrounds with restrained optional accents. Preserve the user's terminology and language; screenshots guide visual structure, not application facts.

- **Activity Diagram for Use Case:** Default to one detailed diagram per significant in-scope user goal. Put actor and system in adjacent vertical columns with headers on one horizontal line and time generally progressing downward, like the Customer/System example. Use additional admin or external-service lanes only when they do work in the documented scenario. Identify the use case and activity IDs in the title.
- **Mapping Use Cases to Activity Diagrams:** Provide the traceability table below plus the related activity diagrams. When a connected overview is requested in the reference style, use horizontal actor/system bands with a readable overall left-to-right flow, like the User/System example. Show actual transitions between related use cases with explicit guards and labeled call/reference actions to their detailed diagrams. This overview supplements, rather than replaces, detailed behavior and traceability. Do not draw fictitious execution arrows merely because two use cases are listed together.

The second reference is conceptually a connected activity workflow across responsibility bands; a lane by itself does not map a use case to its detailed steps. Supply explicit UC/AD references to make that mapping useful. If the user asks only for a mapping table or one diagram, honor that narrower output instead of adding all views. Unrelated use cases remain separate; use table references instead of forcing a single graph.

In a composite overview, retain enough representative actor actions and system responses to show the actual handoffs; do not reduce every use case to one actor-lane box that hides all system work. Do not add empty decorative lanes. Place a call action in the lane responsible for invoking it and identify delegated participants in the referenced detail. A data prerequisite between use cases is not proof of an automatic control-flow transition; mark an unknown trigger instead of inventing an arrow.

Adapt the presentation, not incidental defects in the screenshots: do not copy ambiguous decisions, missing failure paths, actor icons used as flow nodes, or potentially unsafe sequencing such as committing an account before a required validation. Resolve behavior against sources and flag any conflict; do not silently change implemented behavior to match a preferred workflow.

## UML activity notation

| Element | Representation | Rule |
| --- | --- | --- |
| Initial node | Filled black circle | Show where this activity starts; it is not a role icon. |
| Action | Rounded rectangle | Use a concise verb/object label and place it fully inside the responsible lane. Human typing, manual review, and system validation are all actions here. |
| Control flow | Directed arrow | Express execution order or a handoff, with a visible arrowhead. A lane crossing does not automatically imply an API call. |
| Decision | Diamond | Branch on a supported condition with outgoing guards such as [valid] and [invalid]. Make alternatives distinct and collectively cover the documented possibilities. |
| Merge | Diamond | Recombine alternative paths; a merge does not wait for simultaneous branches. Separate decision and merge roles where combining would obscure behavior. |
| Fork / join | Thick bar | Use only for evidenced concurrent work and required synchronization. Do not use a join for mutually exclusive Yes/No branches. |
| Activity final | Filled circle within an outer ring | Ends the whole activity. Label the associated outcome where success, rejection, and cancellation differ. |
| Flow final | Circle containing an X | Ends only that flow when others continue; never substitute it for activity final without considering concurrent paths. |
| Activity partition / swimlane | Labeled column or row | Identifies responsibility; it is not a processing step or a use-case boundary. |
| Call to another activity | Labeled call action with referenced AD ID | Resolve it to a defined activity and show the expected return/outcome. Use supported call-behavior notation when available; otherwise explain the reference explicitly. |

Do not substitute parallelograms for user input, manual-operation trapezoids for review actions, or pill terminators for UML initial/final nodes. Those belong to the separate conventional flowchart palette. Use-case actors and goal ovals belong to the use-case view; optional actor icons in lane headers are decorative identifiers, never substitutes for execution nodes. Do not style every action as a use-case ellipse.

## From a use case to executable behavior

For each use case, reuse its ID or assign UC-001, then record goal, initiating/supporting actors, trigger, preconditions, main scenario, supported alternatives/exceptions, and postconditions. Mark missing decisions as TBD or Requires Confirmation and proposals as Assumption/proposed.

1. Reuse the requirement's step identifiers or assign stable local identifiers. Map each relevant scenario step to its responsible action, decision, guard, or referenced subactivity; keep these links in metadata/table detail without overcrowding labels.
2. Split actor requests from system responses: opening a form versus displaying it, submitting values versus validating them. Add internal steps only when they are needed to explain the use case and are supported by evidence.
3. Place each action in the lane of the party doing the work. Keep the system as a coarse responsibility lane unless the scope requires frontend/backend/provider decomposition; do not turn this view into a sequence diagram or deployment architecture.
4. Represent alternative and exception paths with explicit guards, recovery/return points, and terminal outcomes where supported. Include relevant invalid-input, denied-access, cancellation, and integration-failure cases; do not invent retries or omitted product policies.
5. Mark the goal's postcondition at completion. Completing a referenced registration activity need not terminate a larger login journey: its caller resumes at the appropriate return point. Never use an activity final as a connector to a later step in the same activity.

Separate independent goals into their own detailed diagrams. Use a shared referenced activity for genuine reused behavior. Translate include relationships into required included behavior, and extend relationships into guarded behavior at the specified extension point; neither relation automatically implies temporal order between whole use cases. Do not infer include/extend merely because login and registration appear in the same overview.

## Mapping and coverage

For Full documentation, deliver three linked outputs without waiting for the user to ask: populated activity scenario/step tables, the related UML activity diagrams, and the UC→AD mapping table. Include a populated use-case catalog as their baseline. Keep these outputs distinct; mapping alone does not describe activity steps. For selected scope, honor the requested subset.

For each in-scope use case, provide its scenario/step table (a shared table may cover genuinely identical behavior using exact references and explicit differences):

| UC / scenario / step ID | Actor or responsible lane | Actor action | System response | Guard / rule | Next step / alternate or exception path | Outcome / state | AD node/path and requirement/test links |
| --- | --- | --- | --- | --- | --- | --- | --- |

Fill concrete rows for the main scenario and applicable alternatives/exceptions. Keep supported actor actions and system responses separate; use not applicable for a side with no action, and TBD for unavailable behavior. Do not invent steps just to fill cells. Link scenario IDs to identifiable diagram paths; record missing evidence or deliberately shared activities explicitly. The table must remain readable in the chosen format; split by scenario/use case or repeat identifying columns when necessary.

Use stable UC-001 and AD-001 identifiers or preserve project IDs. Map all use cases in the agreed documentation scope; for a focused request, map only its selected scope and relevant dependencies. A diagram may cover several tightly connected use cases and a use case may link to several diagrams when decomposed; describe those scopes instead of claiming an artificial one-to-one match.

| Use case ID and goal | Actors | Activity ID / link | Scenario / step coverage | Linked requirements / tests | Evidence and coverage gaps |
| --- | --- | --- | --- | --- | --- |

Populate actual rows; do not deliver an empty template. Distinguish covered, partially covered, blocked by missing information, and intentionally excluded with reason. A file existing or a diagram sharing a title does not prove that its scenarios are covered. Each AD must link back to its UC(s); verify both directions and links in HTML/exports. Link main and alternative/exception scenarios to identifiable paths, not only to the diagram as a whole. Do not claim 100% coverage while relevant gaps remain.

## Layout and rendering

Use real aligned lane boundaries spanning the diagram with consistent headers, spacing, and action sizes. For vertical lanes, keep headers at the top; for horizontal lanes, put role labels at the left. Preserve requested orientation rather than silently rotating to suit a tool. Route handoff arrows across boundaries without passing through unrelated actions or covering guard labels. Loops may return against the main reading direction; make the return target unambiguous. Avoid excessive width by splitting the journey and retaining AD references.

For native lane rendering, use an available local tool such as PlantUML, editable draw.io, or precise SVG. PlantUML documents lane assignment and branching in its [activity-diagram guide](https://plantuml.com/activity-diagram-beta); verify actual installed support and output geometry before choosing it. No additional agent skill is required. Do not send private content to public rendering services.

Mermaid flowchart subgraphs can approximate responsibility groups, but automatic layout may rearrange them when edges cross groups. Do not promise aligned columns/rows solely from subgraph or direction directives. For the reference-style output, use a renderer/vector layout that preserves real lane geometry; if constrained to Mermaid-only, label the approximation and disclose the layout limitation. Never invent a Mermaid activityDiagram keyword.

Preserve editable source and embed the rendered diagram in HTML. Follow browser-artifact.md for PDF/PPTX/PNG/JPG exports. Lane headers, separator lines, control arrowheads, guards, and the activity-final outer ring must remain readable. Repeat role headers and identify continuation targets if a diagram must span pages; do not crop a lane or split a decision from its outcomes without navigation.

## Acceptance checks

- Trace each main/alternate/exception scenario from its trigger through correct responsibility lanes to its postcondition or supported ongoing state. Verify merges versus joins and called-activity returns.
- Check every action's owner, guards, loop return, initial/final semantics, and cross-lane handoff against the use case and PRD. Record unknown behavior instead of making the diagram look complete by invention.
- Check UC-to-AD and AD-to-UC links, scenario/step coverage, shared activity references, and linked tests. Report unresolved or unmapped items.
- Render and inspect actual lane alignment, node placement, guard labels, edge routing, and legibility in the requested orientations and export formats. Syntax checks do not prove swimlane geometry or semantic accuracy. Report unavailable render/export checks honestly.
