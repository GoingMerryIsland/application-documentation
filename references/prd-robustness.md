# Complete PRD and robustness standard

Read when creating/reviewing a PRD, full application documentation, or robustness requirements. This is an internal reference of application-documentation, not a dependency on another skill. Use the user's language and scope. A full PRD must support product, design, engineering, QA, and operations decisions; length alone does not establish completeness.

## Coverage and evidence

Cover every applicable area below, merging related sections and linking existing specifications instead of duplicating them. A narrow feature PRD may limit coverage to that feature and its dependencies. Do not omit important requirements to save tokens: keep chat short, use structured detail in the deliverable, and read sources selectively.

For each area distinguish documented evidence, explicitly requested behavior, proposals/Assumption, unresolved TBD/Requires Confirmation, and not applicable with reason. Missing evidence is not a reason to mark an area irrelevant. Do not invent stakeholder approval, research, market size, budgets, release dates, legal obligations, architecture, service tiers, metrics, or implemented controls. Ask only about decisions that materially block correctness; complete useful work and retain visible gaps.

| Area | Required detail when applicable |
| --- | --- |
| Document baseline | Product/version, purpose, audience, document status, source baseline, glossary, existing owners/reviewers and decision history. Do not invent people or approval. |
| Problem and opportunity | Current situation, concrete user problems, evidence, affected segments, existing workarounds, and why solving this matters. Label unvalidated discovery hypotheses. |
| Goals and success | Business/user outcomes, non-goals, measurable success metrics, baseline or unknown baseline, proposed/agreed target, measurement method, and evaluation window. |
| Users and stakeholders | Actors, roles, needs/jobs, context of use, supported platforms, accessibility needs, and operating responsibilities supported by sources. |
| Scope and priorities | In/out of scope, MVP versus later phases, priority rationale, dependencies, constraints, assumptions, and explicit tradeoffs. Do not turn future ideas into MVP commitments. |
| Functional requirements | Feature-by-feature behavior using the requirement contract below; include admin/support operations that are necessary for the stated product. |
| Business rules | Validation and decision tables, calculations, limits, eligibility, ownership, lifecycle transitions, approvals, cancellation/deletion, and cross-feature invariants. Specify rounding, currency, dates/time zones, and effective periods when relevant. |
| UX and information architecture | Sitemap, navigation, screen inventory, role-specific journeys, key interactions, form fields, user feedback, loading/empty/success/error states, responsive behavior, keyboard/accessibility requirements, localization, and recovery from interrupted work. Link existing final designs and preserve them. |
| Identity and permissions | Authentication, registration/recovery, verification, sessions, role/resource/action matrix, ownership or tenant restrictions, and permission changes during an operation. Distinguish visibility from server enforcement; identify denied and unknown separately. |
| Data and lifecycle | Entities, identifiers, field dictionary, types/formats, required/default/unique rules, relationships, ownership, source of truth, retention/deletion/export, backup/restore, and migration/versioning needs. Separate conceptual proposals from existing schema. |
| API, events, and integrations | Contracts and dependencies, caller permissions, request/response/error schemas, side effects, external-service boundaries, versioning, timeouts, quotas, retries, idempotency, webhooks, and integration failure behavior where relevant. Link exact technical specifications. |
| Architecture and platforms | Relevant context, logical components, deployment/environment boundaries, web/mobile/desktop responsibilities, compatibility, and documented technology constraints. Leave solution alternatives as proposals until decided. |
| Nonfunctional requirements | Measurable performance, capacity, availability, reliability, data integrity, accessibility, security/privacy, compatibility, maintainability, and resource/cost constraints appropriate to the product. Use the quality contract below. |
| Robustness and recovery | Failure analysis for critical journeys, prevention, detection, user/system behavior, safe retry/recovery, data reconciliation, and acceptance tests. Use the failure matrix below. |
| Analytics and audit | Product events and properties tied to success metrics, operational signals, audit actions and actor/time/outcome, privacy constraints, and retention. Do not collect sensitive payloads merely for debugging. |
| Operations and support | Environment/configuration needs, relevant monitoring/alerts, operational ownership or TBD, runbooks/escalation, manual recovery, backup restoration, and third-party outage handling. |
| Delivery and release | Dependencies, migration/backfill, rollout and feature flags when needed, compatibility during transition, release gates, rollback/recovery including data changes, and justified phases. Distinguish estimated from committed dates/effort. |
| Verification and acceptance | Testable acceptance criteria, risk-based test scenarios, suitable unit/integration/contract/end-to-end/UX/security/performance/recovery testing, test data/environment needs, UAT criteria, and real execution status. Do not mandate every test type for every feature. |
| Risks and open decisions | Risk, likelihood/impact when grounded or labeled estimates, mitigation, residual risk, decision/owner or TBD, and consequence of leaving it unresolved. |
| Traceability and readiness | Coverage table linking requirements, rules, UI/flows, entities/contracts, tests, and release gates. Explicitly state what is ready and which unresolved decisions block implementation or release. |

## Feature requirement contract

Reuse project identifiers or assign stable REQ IDs. For each significant requirement provide:

- ID, title, actor, goal/value, priority and rationale, evidence/status, and dependencies.
- Preconditions, permissions, trigger, inputs/validation, normal sequence, outputs, postconditions, and side effects.
- Business rules, allowed state changes, affected screens/data/APIs/events, and notifications where present.
- Alternative, denied, cancelled, interrupted, and failed outcomes that apply; define what the user sees and what persists after each.
- Observable acceptance criteria, linked tests, and unresolved decisions. Use Given/When/Then or equally precise conditions and outcomes.

Keep each criterion independently verifiable. Avoid vague requirements such as "fast", "secure", "user friendly", or "handles all errors" without a measurable rule or explicit open decision. Preserve numerical limits and exception rules. Include important negative and boundary cases rather than only happy paths. Record shared rules once and cross-link them from affected features.

## Quality requirement contract

For each important nonfunctional requirement specify ID, scope/scenario, metric and units, threshold, workload/environment, measurement method, verification criterion, and evidence status. Distinguish a proposed/agreed target from an observed result. Define latency percentiles and payload/concurrency assumptions when discussing performance; availability windows and exclusions when discussing uptime; recovery time (RTO) and recoverable data-loss window (RPO) when relevant. If a target cannot be grounded, leave it TBD or explicitly proposed rather than inventing an SLA.

Describe required outcomes before prescribing infrastructure. Do not impose queues, distributed services, replication, circuit breakers, or new vendors solely to look robust. Explain the risk addressed by a proposed mechanism and its operational tradeoff. Verify current external constraints or normative requirements from authoritative sources when needed; do not assert legal or standards compliance from a checklist.

## Robustness analysis

For each critical journey, state the invariant that must hold, such as one authorized side effect per logical operation or no cross-tenant disclosure, only when relevant. Select applicable failure cases below; do not manufacture product capabilities to fill the list. Existing behavior and recommended improvements must remain separate.

| Failure family | Questions to resolve when relevant |
| --- | --- |
| Invalid or hostile input | Required/empty/malformed/oversized values, boundary limits, encoding, uploads, permission bypass, and safe error messages; validation location and persisted-state outcome. |
| Duplicate or concurrent actions | Double-click, repeated requests, concurrent edits, stale versions, duplicate jobs/events, and race conditions; idempotency scope/lifetime or unresolved policy, conflict handling, and invariant preservation. |
| Network or dependency failure | Offline/disconnect, high latency, timeout, rate limits, service outage, malformed responses, and ambiguous success; visible status, timeout boundary, bounded retry/backoff, fallback or escalation. Never blindly retry a non-idempotent side effect. |
| Partial completion and integrity | Failure between linked writes or services, rollback/compensation, reconciliation, interrupted import/migration, and recoverable progress. Do not promise exactly-once delivery without evidence. |
| Identity and isolation | Expired/revoked sessions, changed roles, unauthorized ownership/tenant access, and secrets/PII exposure; define denied behavior and audit needs. |
| State and time | Invalid/out-of-order transitions, stale callbacks, expiry, scheduling/time-zone issues, and cancellation arriving during processing; define precedence and final state. |
| File and background processing | Unsupported/corrupt/large files, interrupted uploads, storage exhaustion, worker crash, lost/duplicate/out-of-order events, poison jobs, and stuck work; supported resumption, retry limits, quarantine/manual handling or TBD. |
| Capacity and degradation | Load spikes, resource limits, overload and third-party quotas; graceful degradation, backpressure or explicit refusal, observability, and recovery where applicable. |
| Data loss and recovery | Accidental deletion, corruption, backup failure and restoration; recovery ownership, integrity checks, applicable RPO/RTO, and evidence of restore testing or an unexecuted test plan. |
| Release and compatibility | Old/new clients or schema coexistence, failed rollout, configuration errors, migration compatibility, and rollback limits after irreversible changes. |
| Domain-specific critical paths | For payments: duplicate/ambiguous charges, refunds and reconciliation. For AI: timeout, invalid/unsupported output, unsafe source instructions, quality validation and user correction. For multi-device/offline apps: conflict and synchronization policy. Include only domains actually in scope. |

Maintain a failure matrix for the selected critical cases:

| Requirement / flow | Failure or trigger | Invariant / data impact | Detection / signal | User-visible behavior | System handling / retry bounds | Recovery / responsible role | Acceptance test | Evidence / open decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Fill rows with concrete supported or clearly proposed behavior. Do not emit the empty template as completed work. Identify nonrecoverable states and required manual decisions. Test plans must distinguish expected outcomes from tests actually executed. A robustness specification does not prove the application is robust.

## Diagrams, delivery, and completion

Apply references/diagram-standards.md from the skill root for full documentation and diagram work: ten applicable required views, plus conditional views that add distinct information. Cross-link their stable IDs from the relevant PRD sections and acceptance tests. A standalone narrow feature PRD does not require unrelated whole-system diagrams.

Apply references/browser-artifact.md for requested/default HTML and PDF, PPTX, PNG, JPG outputs. Keep one canonical requirements baseline across the preview and exports; regenerate affected exports after revisions. Respect explicit Markdown-only or other narrower format requests. These references are resources of this same skill.

Before declaring the PRD complete:

1. Check every applicable coverage area, every in-scope critical journey, and the diagram coverage. A heading without decision-useful content is not coverage.
2. Trace each critical requirement to a testable acceptance criterion, relevant flow/UI/data/API links, and a test scenario. Resolve dangling or contradictory references without inventing facts.
3. Check normal, negative, boundary, concurrency, interruption, and recovery cases where applicable. Confirm proposed mitigations are not mislabeled as implementation.
4. Cross-check permissions, entity/field names, state transitions, calculations, error outcomes, quality targets, and release scope across all sections.
5. Report document coverage, unresolved decisions, implementation readiness, and actual validation status separately. A comprehensive draft may still have blocking decisions; never label it approved, production-ready, fully tested, or failure-proof without supporting evidence.

For updates, revise affected requirements and linked rules/diagrams/contracts/tests together. Preserve unrelated decisions and identifiers. Do not overwrite previous accepted requirements with new assumptions; show the conflict and the decision needed.
