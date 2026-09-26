# Scope selection and completeness gates

Read after scope is selected, and on coverage corrections. This reference belongs to the same skill. The first-interaction question is in SKILL.md; do not ask it again after a clear answer.

## Freeze the requested outcome

Record mode (Full / Selected sections), application/module boundary, named features/roles, output language and formats, source baseline, and explicit exclusions. Keep this small record in the document baseline or working notes, not a second questionnaire. Reuse supplied details. Ask additional questions only for consequential unresolved decisions; otherwise preserve visible TBD or proposal labels.

Accept arbitrary selected-scope text, for example "tabel activity untuk checkout, mapping UC ke AD, dan ERD". Resolve its meaning and dependencies without forcing a predefined checklist. If the selection is only "bagian tertentu", ask which parts. If the user later adds sections, extend the same coverage record. Preserve agreed content during corrections.

Full means every applicable content family below and every in-scope feature, not a maximal number of files, all possible conditional diagrams, or invented application behavior. Selected sections uses the same depth and checking within the named boundary. Output constraints such as Markdown-only change delivery formats, not content completeness.

## Build a coverage ledger before drafting

Inventory known features, actors, goals/use cases, screens, entities, integrations, and critical processes from the actual brief/code. Build the ledger from this inventory and the agreed scope before writing, not retrospectively from whatever was produced. Assign stable identifiers and planned anchors/files. This prevents forgotten requirements from disappearing from the denominator.

| Coverage item / ID | Applies and why | Required detail | Actual section / artifact link | Status | Evidence, gap, or justified combination |
| --- | --- | --- | --- | --- | --- |

Use Planned during work, then Complete, Partial, Blocked, Not applicable, or explicitly Excluded by user. Complete means substantive content is present and linked, not that an application behavior is implemented or a test executed. A combined section must map each covered obligation to identifiable content. Missing information is Partial/Blocked, never Not applicable. A TBD-only heading is not Complete. Count unique obligations even when a diagram is shared.

For Full mode, seed these obligations:

| Content family | Minimum completion evidence |
| --- | --- |
| PRD and requirements | All applicable areas in prd-robustness.md, with per-feature behavior, business rules, testable acceptance criteria, UX states, quality targets/status, failure matrix, operations, release, risks, and open decisions. |
| Use cases | Populated catalog covering every known in-scope goal: UC ID, actor, goal, trigger, preconditions, scenarios and postconditions. Record unavailable decisions rather than inventing them. |
| Activity tables | Scenario/step tables for the in-scope use cases, with actor action, system response, conditions, alternatives/failures, and outcomes. A flowchart or UC→AD mapping is not a substitute. |
| Activity diagrams and mapping | Aligned UML activities for significant goals, justified shared/referenced activities, and a populated UC→AD table with identifiable main/alternate/exception path coverage. Inspect every UC row; none silently disappears. |
| Required diagram views | Explicit ledger rows for all ten views in diagram-standards.md. Produce applicable context, sitemap, use case, user flow, activity, architecture, ERD, sequence, permission matrix, and deployment views. Explain actual non-applicability. |
| Conditional views and process flowcharts | Evaluate the fourteen conditional triggers. Create only those adding relevant information; preserve a compact reason for nonselection or links to coverage in another view. Include requested flowcharts with their own semantic notation. |
| Data and technical contracts | Applicable field dictionary, keys/cardinality, data lifecycle, APIs/events/integrations, permissions, setup/configuration, environments, and deployment/recovery details; distinguish proposals from existing facts. |
| Traceability and tests | Link requirements ↔ use cases/scenarios ↔ activity paths ↔ relevant UI/data/contracts ↔ acceptance tests. Cover evidenced negative/boundary/recovery cases and state real execution status. |
| Delivery and exports | Agreed formats and usable navigation. Full HTML includes Documentation and Full Workspace, their shared registry and applicable visual/editable exports. Check format-specific capability separately from content coverage. |

For Selected sections, create ledger rows for each user-named output and its necessary supporting context. Do not seed unrelated full-document obligations. A request for an activity table must yield a populated activity table, not only a diagram; a mapping-only request stays mapping-only.

## Produce the complete agreed scope

Load the relevant internal standards before drafting their sections. In Full mode, always load prd-robustness.md, diagram-standards.md, and use-case-activities.md. Load browser/workspace/export references for those formats, and flowchart-symbols.md when drawing flowcharts. No companion skills are required.

Write real content into deliverables progressively; keep conversation updates brief. For many use cases, split files/pages/boards by feature or role with an index. Reuse genuine shared activities by ID and document each use case's distinct scenario differences. Do not cover only the first one to three use cases because sequence diagrams prioritize one to three critical processes; that sequence-specific prioritization does not limit the activity catalog or tables.

Do not replace requested details with "etc.", "same as above" without a precise reference, empty tables, generic boilerplate, or an offer to expand later. Token efficiency applies to repetition, source reading, and chat length, not to removing acceptance criteria, tables, alternate paths, or in-scope features. If context is tight, retain the ledger and continue in bounded batches without requiring the user to request the complete version again. If a hard tool/session limit truly blocks completion, label the result partial and list exact outstanding IDs.

## Reconcile before final delivery

1. Compare the initial scope and feature inventory against actual content, not merely filenames or headings. Every promised output must have substantive content or an explicit unresolved status.
2. In Full mode, inspect the use-case catalog, per-use-case activity scenario tables, UC→AD mapping, all ten required-view decisions, PRD coverage, robustness matrix, permissions, and acceptance tests. Check actual populated rows; ensure main and applicable alternate/exception paths are represented.
3. Verify links both ways where traceability requires it. Check every referenced UC, AD, requirement, section and test exists, and every in-scope use case is accounted for. Fix omissions within authorization immediately; do not ask whether to add an already-required table.
4. For combined diagrams/sections, verify each obligation remains understandable and linked. A matrix cannot replace a diagram's behavioral explanation; an activity diagram cannot replace its scenario table. A table or diagram type with zero applicable evidence needs a specific explanation, not silent removal.
5. Check that HTML navigation, Documentation, Full Workspace, and agreed exports reflect the same content revision. Keep content coverage, rendering, interaction tests, and export compatibility as separate statuses. Static artifact validation alone cannot certify completeness.
6. Remove Planned statuses before final handoff. Deliver a compact coverage summary with actual links and exact Partial/Blocked items. Do not report 100% or complete when mandatory content remains absent. An explicit unresolved policy can coexist with a useful draft but is not an implemented or approved decision.

When the user reports "tabel activity mana?", treat it as a missed requirement if already in scope: repair it and audit neighboring obligations against the ledger. Do not merely append one table and ignore other missing sections. Do not ask them to reselect Full or repeat requirements already provided.
