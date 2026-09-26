# Application diagram standard

Read for full application documentation or when creating/reviewing diagrams. This reference belongs to application-documentation; no companion skill is required. Use the user's language for deliverables.

## Selection and creation order

For full documentation, create all applicable required views below in numbered order, then the relevant conditional views. A focused diagram or feature request limits coverage to that scope. Do not automatically create every diagram.

Maintain a compact coverage table: view, purpose/scope, source or evidence status, output link, and reason if omitted or combined. Review all ten required views; omit only when irrelevant to the application type. Missing deployment/schema/UI evidence does not make a view irrelevant: retain the coverage gap as TBD or Requires Confirmation. Produce the supported part without inventing details; label deliberate provisional choices Assumption and proposals as proposed.

Select conditional views only when their trigger is present and they add information. Cross-link an existing sufficient view instead of repeating it. Combine simple diagrams only if each required purpose remains explicit and readable; record the covered views. Keep different abstraction levels separate where combining would confuse readers. Split large diagrams by feature, module, or role. Prioritize core business processes, high-risk paths, and difficult relationships.

## Required views when applicable

The numbering is the recommended creation order. The permission matrix is a table, not a node diagram.

| # | View | Purpose and required content |
| --- | --- | --- |
| 1 | System Context Diagram | Show the application as the focal system, its boundary, users, administrators, external systems, and third-party services that exist in the sources. Explain the big picture without internal implementation detail. |
| 2 | Sitemap / Information Architecture | Show the hierarchy of pages, menus, submenus, and navigation. Separate role-specific structures when roles have different pages; do not invent screens for API-only systems. |
| 3 | Use Case Diagram | Relate actors/roles to the capabilities they can use within the system boundary. Include include/extend relations only when needed and supported by the behavior. |
| 4 | User Flow Diagram | Show how a user reaches a main goal through entry points, screens/actions, decisions, and outcomes. Select the actual core processes, such as registration, login, search, transaction, publishing, or data management. |
| 5 | Activity Diagram | Explain use-case behavior using UML actions, initial/final nodes, decisions/merges, guards, loops, and parallel work when present. Use aligned actor/system swimlanes and trace use cases to activity diagrams using use-case-activities.md. Distinguish process logic and responsibility from screen navigation in a user flow. |
| 6 | System Architecture Diagram | Show frontend, backend, databases, storage, authentication, APIs, and external services that apply. Label communication direction, component responsibility, and known technologies. Distinguish logical structure from deployment placement. |
| 7 | Entity Relationship Diagram (ERD) | Show supported entities/tables, main attributes, primary/foreign keys, relationships, cardinality (one-to-one, one-to-many, many-to-many), and optionality. Distinguish conceptual entities from physical tables; match constraints and ownership/tenant relationships to the schema. Do not invent relational keys for a conceptual model. |
| 8 | Sequence Diagram | Show ordered interactions among relevant user, frontend, backend, database, and external-service participants. Prioritize authentication when present and one to three most important business processes. Preserve asynchronous behavior, authorization, and transaction boundaries. |
| 9 | Role and Permission Matrix | Use a table of roles versus resources/actions. Include View, Create, Edit, Delete, Approve, Publish, and Export where relevant; specify ownership/tenant/condition limits. Distinguish UI visibility from server enforcement and distinguish denied from unknown permissions. |
| 10 | Deployment Diagram | Show actual environments and runtime placement: servers, databases, CDN, storage, domains, and third-party services when applicable. Distinguish development, staging, and production if they exist. For desktop/mobile/local apps, show their relevant installation/runtime boundaries; never invent cloud hosting. |

## Conditional views

| # | View | Trigger and additional information to show |
| --- | --- | --- |
| 11 | State Diagram | Entities change status. Show supported states and allowed transitions, actors, triggers, guards, and side effects; for example Draft to Review to Published to Archived only if supported. |
| 12 | Data Flow Diagram (DFD) | Significant data processing, movement, or transformation. Show sources, processes, stores, destinations, and labeled data flows; distinguish data movement from control flow. |
| 13 | API Integration Diagram | External APIs such as payment, AI, maps, analytics, email, or WhatsApp are present. Show integration boundaries, callers, purposes, and exchange direction beyond the architecture overview. |
| 14 | Authentication and Authorization Flow | Login, registration, verification, OAuth, multiple roles, sessions, tokens, or two-factor authentication exist. Show identity verification, access decisions, and relevant session/token lifecycle. Reuse sequences where they already cover the same behavior. |
| 15 | Component Diagram | Modular or large applications need internal decomposition. Show frontend/backend modules, shared services, key packages, interfaces, and dependencies. |
| 16 | Notification Flow | In-app, email, push, SMS, or WhatsApp notifications exist. Show event/trigger, recipient selection, channel, dispatch, and supported outcomes. |
| 17 | Error Handling Flow | Critical processes involve validation, API failure, disconnection, retry, timeout, or fallback. Show detection, decision, recovery, and terminal outcomes; label proposed recovery rather than inventing implemented behavior. |
| 18 | File Upload and Processing Flow | Images, videos, or documents are uploaded or processed. Show applicable upload, validation, compression, conversion, processing, and storage steps and rejection paths. |
| 19 | Background Job / Queue Flow | Asynchronous work, scheduled jobs, workers, webhooks, retries, or long-running processing exist. Show the actual trigger, dispatch, processing, result, and failure path. A webhook alone does not prove a queue exists. |
| 20 | CI/CD Pipeline Diagram | Scope includes build, test, deployment, release, rollback, and environments. Show configured stages, gates, artifacts, and target environments; mark unavailable stages or recovery information. |
| 21 | Security Architecture Diagram | Payments, personal/sensitive data, or high security requirements apply. Show relevant trust boundaries, data paths, authentication/authorization, and evidenced protections or gaps. Do not imply compliance or implemented controls without evidence. |
| 22 | Customer Journey Map | UX analysis needs user goals, touchpoints, pain points, emotions, and improvement opportunities. Label inferred emotions or pain points as hypotheses unless grounded in research. |
| 23 | Service Blueprint | Service delivery crosses users, admins, support, operations, and backend systems. Connect frontstage actions, backstage work, support processes, and handoffs. |
| 24 | Wireframe / Screen Flow | UI designs are absent or screen relationships need clarification. Use low-fidelity wireframes or linked existing screens as appropriate; preserve existing final UI designs rather than replacing them. |

## Representation and semantic precision

For process flowchart symbols, apply [Flowchart symbols and semantics](flowchart-symbols.md). Classify the meaning of each node before styling. This applies to process flowcharts, not automatically to every diagram drawn using Mermaid's flowchart engine (for example, a sitemap or C4-style architecture).

For activity diagrams and use-case/activity mapping, apply [Use-case activity diagrams and swimlanes](use-case-activities.md). Prefer true aligned lane geometry for the requested reference style. Generic flowchart subgraphs alone are not evidence that a swimlane layout has been achieved.

Use Mermaid where it clearly represents the relationship and the available renderer supports the syntax. Prefer flowchart for navigation, process, integration, architecture, or pipeline views; sequenceDiagram for ordered interactions; erDiagram for entity relations; stateDiagram-v2 for lifecycles; journey for suitable journey maps. Use tables for permissions, field mapping, status rules, comparisons, and blueprint/journey dimensions when clearer. Use a class diagram only when an actual class model adds needed detail or is requested.

Use C4-style context/container views where appropriate. A C4 container means an application or data store, not necessarily a Docker container. Use labeled flowchart subgraphs when specialized syntax is unsupported. Do not invent Mermaid keywords such as useCaseDiagram or activityDiagram. Represent use cases with clearly labeled flowchart boundaries or a compatible vector renderer; for activity swimlanes follow the dedicated lane-layout guidance above. Label an approximation honestly; if formal UML/BPMN notation is required, preserve its semantics with a supported renderer rather than silently substituting generic boxes.

For include, point from the including use case to its required included behavior; for extend, point from the optional extension to its base and show the condition. Do not add either relation merely to decorate the diagram. For activity lanes, identify responsibility without implying synchronization that does not exist. User flows explain goal completion; activities explain process logic; sequences explain message order. Their content must justify separate views.

Use stable node and diagram IDs, concise labels, valid quoting, and explicit branch conditions. Keep feature, role, state, technology, and entity names consistent with sources and throughout the documentation. Use directional arrows for flows/messages/dependencies; use appropriate association and cardinality notation where direction is not the meaning. Never add fake edges solely to make a picture connected. Remove accidental orphan nodes/dangling relations; intentionally isolated items need an explanation or a separate view.

## Quality and export checks

For every delivered diagram or matrix:

- Give a title, explicit purpose/scope, and a short explanation immediately after it; add a legend where notation is not obvious.
- Ground nodes, relationships, technologies, integrations, and paths in sources. Mark gaps as TBD, Assumption, or Requires Confirmation, preserving the distinction between unknown and proposed behavior.
- Cross-check names, permissions, states, entities, API interactions, and screen paths against the PRD, requirements, database, APIs, UI, and related diagrams. Resolve contradictions or record the unresolved question.
- Check that the diagram answers a distinct question, has no accidental disconnected nodes/relations, and clearly expresses direction or relationship semantics. Preserve alternate/failure/retry/cancel paths when relevant and supported.
- Validate with an available compatible parser/renderer and review the result. Report unavailable rendering checks honestly; syntax validity alone does not prove semantic correctness.
- Keep labels readable on desktop and in PDF, PowerPoint/PPTX, PNG, and JPG. Split oversized views instead of shrinking labels to illegibility. Avoid color-only meaning and AI-generated raster art for precise diagrams; preserve editable source and provide editable SVG/draw.io when requested and supported.
- Follow references/browser-artifact.md (relative to the skill root) when creating previews/exports. Inspect actual converted output for clipping, glyphs, labels, direction, arrowheads, line styles, and cardinality; regenerating exports after a change is part of completion. Do not claim browser/export validation from a text-only review.
