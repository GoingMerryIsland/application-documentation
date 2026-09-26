# Full Workspace: visual documentation explorer

Read when creating/updating full browser documentation or its Full Workspace mode. This reference is part of application-documentation. The purpose is to let readers understand the system by directly exploring diagrams and flows without first reading long prose. It is a usable viewing mode inside the documentation artifact, not a separate SaaS product.

## Experience and scope

Provide clearly visible **Documentation** and **Full Workspace** navigation. Preserve the label Full Workspace unless the user requests another. Workspace mode fills the available application viewport, collapses the text-reading chrome, and offers a separate browser-fullscreen action where supported. If browser fullscreen is unavailable or denied, the full-width in-page workspace must still work.

Adapt the visual concept of the supplied whiteboard reference: a large light canvas with a subtle dot grid, floating compact controls, a page panel near the upper left, a bottom interaction toolbar, and zoom controls near the lower right. Give the document its actual title. Use an intentional initial arrangement of readable diagram frames; never open on an empty board when diagrams exist. Display a helpful empty state only when the source really contains no diagrams or filters match nothing.

Default to a read-only visual explorer. Include selection/focus and hand/pan controls because they support reading. Editing nodes, adding sticky notes, freehand drawing, collaboration, timers, billing, avatars, sharing, or user accounts are not required by the reference image. Add such controls only when explicitly requested and implemented; do not copy decorative or nonfunctional tools. Selecting a diagram must not accidentally move its nodes.

## Sidebar, spacing, and canvas geometry

Treat spacing as a coherent layout system. Reuse suitable established documentation design tokens; otherwise use the concrete defaults below as starting values, then verify actual content at target sizes. Do not add ad hoc margins to individual items to hide structural misalignment.

| Area | Default geometry and behavior |
| --- | --- |
| Spacing scale | Use 4, 8, 12, 16, 24, and 32 CSS px; choose one token per relationship and reuse it. |
| Desktop sidebar | Start at 280 px wide, normally within 256–320 px. Use 16 px internal padding and a consistent 16 px outer inset for floating panels. Long content must not silently widen the panel. |
| Sidebar hierarchy | Order title/mode navigation, search, filters, page list, then secondary actions. Use 24 px between major sections, 8 px between a label and its control, and 4–8 px between related list items. |
| Navigation row | At least 40 px high, 12 px horizontal/8 px vertical padding, 8 px icon-to-label gap. Align icons, titles, counts, and overflow actions to consistent columns. Allow height to grow when labels wrap. |
| Controls | Start at 40 px height with at least 44 px touch targets in touch layouts. Keep icons optically aligned at 16–20 px; reserve a fixed area for trailing actions. |
| Titles and labels | Use a readable type hierarchy: normally 14 px body/navigation, 12 px secondary metadata, 16 px panel headings. Wrap important text; if navigation is truncated, expose the full name through an accessible detail/tooltip. |
| Header and toolbar | Start with a 56 px header and 8 px toolbar padding/gaps. Keep floating controls at least 16 px from viewport edges and safe areas; prevent separate toolbars from colliding. |
| Diagram frames | Start with 24 px frame padding and 32–48 px between frames. Reserve separate space for title/legend; labels and lanes must not touch the frame border. |
| Details panel | Start around 320 px on wide screens; convert to a drawer when opening it would leave less than about 480 px of usable canvas. Do not squeeze two sidebars onto a narrow screen. |

Give the sidebar a bounded viewport-aware height. Keep its header/search stable and make the long page-list region independently scrollable using proper flexible sizing (including min-height: 0); avoid stacked nested scrollbars. Footer controls must remain reachable and not cover the last row. Active, hover, and focus states must use the same row geometry without shifting text. Use min-width: 0 where needed, and verify badges, translated labels, filters, and menus do not create horizontal overflow.

Choose one intentional panel strategy: a docked sidebar reserves layout width, while a floating panel overlays the canvas with an explicit exclusion region. Do not apply both width reservation and a duplicate margin. Fit Board and Focus Diagram must use the unobscured canvas rectangle after subtracting actual panels, header, toolbar, and padding; recompute it after collapse, resize, fullscreen changes, or details-panel changes. Keep important content out from underneath floating UI.

On narrow layouts, use a collapsible drawer instead of a permanent sidebar; start near 85vw with a sensible maximum and preserve visible close/return controls and safe-area padding. Compact filter controls and move secondary actions into a real menu. Inspect 360 px, tablet, and desktop widths plus browser zoom at 200%, long page titles, many pages, and empty/search states. These are design defaults to evaluate, not a claim of universal accessibility compliance.

## Content and pages

Expose all diagrams within the agreed documentation scope, including flowcharts, UML activities/swimlanes, use-case views, UC-to-AD mapping, sequences, context/architecture, ERD, states, deployment, and relevant conditional diagrams. Selection of which diagrams to create still follows diagram-standards.md; workspace mode must not cause invented diagrams or automatic generation of all 24 types. Permission matrices and traceability tables may appear as structured visual cards when useful.

Group related diagrams into named pages/boards, such as Overview, User Journeys, Activities, Architecture, Data, and Integrations, using only categories with content. For small documentation sets, one organized board is enough. Pages are navigation categories, not a requirement to split the artifact into multiple HTML files. Within a board, use labeled frames grouped by feature or role, with enough whitespace and a clear reading order. Do not connect unrelated diagram frames with invented flow arrows.

Each diagram frame shows its title, type, stable ID, and short purpose or outcome. Keep proposal/unknown status visible with a compact badge when relevant. Move long explanations into an optional details panel. Provide actions to focus the diagram, view its legend/details, open its exact documentation section, explore related diagrams, and export it. A diagram-only reader must still understand lane names, guards, legend, key outcomes, and uncertainty without reading the entire PRD.

For activity diagrams, preserve aligned swimlanes and initial/final notation. For flowcharts, preserve semantic shapes and labeled branches. Layout inside a diagram must not change when its outer frame is focused or panned. Provide related UC/AD links where applicable.

## Required interactions

| Interaction | Required behavior |
| --- | --- |
| Pages panel | Select an existing board; indicate the active page and offer collapse/expand. Restore a useful view when switching pages. |
| Search and filters | Search titles, stable IDs, relevant labels, and use-case names; filter by available type, feature, or role. Show result counts and a clear reset/no-results state. Selecting a result opens its board and focuses the actual diagram. |
| Pan | Drag the empty canvas using hand mode or a documented modifier, without triggering text selection or diagram links. Support pointer cancellation and release outside the canvas so the hand never becomes stuck. |
| Zoom | Provide plus, minus, a percentage/readout, and reset. Support a documented mouse/trackpad gesture within the canvas; keep the intended focal point stable. Do not intercept browser zoom or unrelated page scrolling globally. |
| Fit board | Fit the active board's visible content bounds with padding, accounting for panels/toolbars. If the overview makes labels tiny, provide immediate focus of a diagram for reading. |
| Focus selection | Center and fit the selected diagram, with a readable-size option and further zoom if the whole diagram cannot fit legibly. Empty selection gives an explicit prompt, never a broken transform. |
| Fullscreen | Enter/exit browser fullscreen if available, track external exit such as Escape, and retain camera/selection. In-page workspace works without browser fullscreen. |
| Details and return | Open an optional details/legend panel or the linked text section. Returning to Full Workspace preserves board, selection, filters, and camera during the session; cross-mode links use stable IDs. |
| Export | Identify the selected diagram or active board as the scope; expose only implemented formats/actions, with explicit unavailable reasons when needed. |

Provide accessible names, visible focus, keyboard-operable page/search/tool controls, and a diagram list or equivalent structured navigation so dragging is not the only way to reach content. Keyboard pan/zoom shortcuts must work only when the workspace has focus and must not hijack text inputs or browser shortcuts. Escape closes transient UI appropriately. On touch devices offer deliberate pan/pinch behavior and button alternatives; keep panels collapsible and prevent them from covering all content. Diagrams need useful accessible titles/descriptions; a bitmap-only unlabeled canvas is insufficient.

## Shared source, state, and performance

Use one canonical diagram registry for Documentation, Full Workspace, and exports. Reuse stable diagram/UC/AD IDs, titles, types, relevant tags, source status, rendered assets, text-section anchors, and export references. Board membership and frame bounds are presentation metadata, not a second copy of business logic. Preserve notation and lane geometry from the existing diagram source.

Render from the existing SVG/assets where possible instead of maintaining separate Mermaid/PlantUML content for each mode. Generate new source only when the diagram itself changes; changing focus, filter, pan, or zoom must not regenerate diagrams or exports. Escape/sanitize labels and imported SVG using browser-artifact.md.

When embedding the same SVG in multiple modes or frames, namespace DOM IDs per rendered instance and rewrite all internal marker, clip-path, mask, and other fragment references consistently. Preserve canonical diagram IDs separately in registry metadata; duplicate SVG IDs can bind arrowheads or effects to another hidden instance.

For editable handoff, retain the structured nodes, edges, semantic shapes, labels, lane/group membership, and geometry alongside rendered assets, as specified in editable-diagram-exports.md. An SVG reference alone does not guarantee editable graph reconstruction.

Keep camera state distinct from document coordinates and export bounds. Reuse the same coordinate conversion for pointer handling, fit, and selection. Clamp zoom to a practical tested range and reject invalid/zero-size bounds. Handle window resize and panel changes without losing the selected diagram. Use optional local persistence only for view preferences; failure or absence of local storage must not break navigation. Changing source revisions must invalidate stale diagram/export references and reconcile removed selections.

Load or mount content per active board or viewport where it materially improves responsiveness. Prefer lightweight previews for inactive diagrams while retaining search access to the entire registry. Avoid rendering every complex diagram again on each interaction. Choose a simple SVG/DOM implementation or an existing suitable library according to available tools and complexity; do not require a new framework or another agent skill. Retain the portable/direct-file behavior required by browser-artifact.md.

## Export contract

Keep whole-document exports available in Documentation. In Full Workspace, label diagram and board exports distinctly; selecting a diagram must never silently download an unrelated whole-document snapshot. Author-time exports with verified download links are acceptable. If a requested dynamic selection or filtered scope cannot be generated, state the supported snapshot scope accurately.

Export from canonical content and content bounds, not the user's current zoom/pan viewport. The default export contains the selected diagram or board, its useful title/legend, and needed status/attribution. Exclude floating menus, selection outlines, handles, and the dot-grid background unless the user requests a workspace screenshot. Export an actual screenshot only with an explicit screenshot label and scope.

Preserve arrowheads, flowchart symbols, UML final rings, swimlane headers/borders, and legible text in PDF, PowerPoint/PPTX, PNG, and JPG. A large board should become a clearly labeled overview plus readable detail pages/slides or separate images, not one giant unreadable canvas. Preserve IDs and reading order. Flatten JPG background; disclose diagram editability in PPTX and retain editable headings where applicable. Observe the genuine-file and capability checks in browser-artifact.md.

Also offer **draw.io (.drawio)** and **FigJam (import package)** for selected diagrams and boards. Follow [Editable diagram exports](editable-diagram-exports.md) for the native graph/export contract, FigJam importer, instructions, capability limits, and edit-and-reopen verification. Clearly identify any import step; never present a screenshot as a fully editable diagram. Existing PDF/PPTX/PNG/JPG output remains available according to the agreed scope.

## Verification gates

Verify the actual implementation before claiming a working workspace:

1. Open Full Workspace from Documentation: the active board is populated, controls are reachable, frames do not overlap, and diagram notation matches the source. Return to the same text section and then the same workspace view.
2. Switch boards, search across boards, apply combined filters, select a result, clear filters, and handle zero results/empty data. Ensure hidden selections do not leave export controls pointing at unintended content.
3. Test drag/release/cancel, repeated zoom, fit board, focus selection, and reset. Exercise resizing and opening/collapsing panels. Verify labels and arrows remain sharp enough to read and diagram links still activate correctly after transforms.
4. Enter/exit fullscreen, including Escape, and test an unavailable fullscreen path. Keyboard-navigate the controls and diagram list; test narrow/touch layouts with button alternatives.
5. Export a selected diagram after aggressive zoom/pan and export a dense board. Inspect actual content, scope, crop, labels, and supported formats. Confirm that screenshots, whole-board exports, diagram exports, and whole-document exports are not confused. A filesystem-valid PDF does not prove its workspace button or framing works.
6. Update a diagram source and confirm both modes and affected exports use the new revision. Check direct-file/offline support if promised and no duplicate rendering on ordinary camera movement. State renderer/browser limitations rather than calling untested interactions verified.

7. Inspect sidebar alignment and spacing with short/long labels, badges, many pages, scrollbar appearance, browser zoom, and each target viewport. Check no clipping, overlapping controls, horizontal overflow, unreachable footer, or doubled canvas gutter; verify fit/focus after every panel transition.
8. Follow editable-diagram-exports.md to validate draw.io and FigJam handoff. Confirm actual text/shape edits and attached connector movement in the target editor when accessible; structural checks alone do not prove target-editor compatibility.

Report content coverage, structural checks, actual browser interactions, and visual/export checks separately. The existing structural validator cannot prove correct pan/zoom, selection, fullscreen, or usability. An instruction-only skill update is not itself an implemented or tested workspace in a user's application.
