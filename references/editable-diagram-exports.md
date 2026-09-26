# Editable draw.io and FigJam handoff

Read when delivering Full Workspace or requested editable diagram exports. This is part of application-documentation; do not install another agent skill. Preserve the selected diagram/board scope, canonical revision, meaningful labels, symbols, topology, and layout. A diagram being visible in an editor does not prove its elements are editable.

## Output and capability contract

| Target | Deliverable | What editable means |
| --- | --- | --- |
| draw.io | A genuine .drawio XML diagram, with one named page per selected board/diagram as appropriate | Individual shapes and labels can be edited, nodes moved/resized, and connectors remain bound to their endpoints. |
| FigJam | A supported verified native handoff, or a self-contained local import package containing graph data and a working FigJam development plugin | Import creates separate FigJam shapes/text and connected edges, not a single placed image. The import step and any unsupported symbols are disclosed. |
| SVG/PDF/PNG/JPG fallback | Clearly labeled visual reference, with semantic source when available | Never claim this fallback provides native graph editability or satisfies an editable-export requirement. |

Use explicit controls such as Export draw.io and Export FigJam Import Package. Explain scope and the import step briefly. If no native .jam writer/import path has been verified, do not synthesize a .jam extension, claim JSON can be imported directly, or invent a universal native clipboard format. Do not assume draw.io imports directly into FigJam. Keep supported local outputs even when a target editor is unavailable, but report the exact unverified or blocked capability.

## Shared semantic graph

Generate both targets from the same graph as the documentation diagrams. Retain a versioned payload with document/source revision, board and diagram IDs, node IDs, labels, semantic types, coordinates/dimensions, styles, parent/lane IDs, and edges with source/target IDs, labels/guards, endpoint anchors, line/arrow styles, and useful waypoints. Include titles, legends, and UC/AD references. Resolve all edge references and parent hierarchy; use finite geometry and stable coordinate conventions.

Reuse authored graph data or a supported parser for the exact source notation. When only rendered SVG or an image remains, recover structure against the editable source/evidence, disclose uncertainty, and do not silently infer logical relations from line proximity. For new diagrams, retain semantic data during authoring so export does not require reverse engineering pixels.

Preserve each diagram's internal geometry and translate whole diagrams into board space. Do not bake viewer pan/zoom or hidden UI into exported coordinates. A board export includes only its intended content with all internal connectors intact; a single-diagram export excludes unrelated frames. Handle Unicode, multiline labels, XML/JSON-sensitive characters, and long text without executing label content.

## draw.io implementation

Use the genuine graph XML structure, such as mxfile containing named diagram pages with mxGraphModel/root, valid layer/root cells, vertex cells with mxGeometry, and edge cells with source/target references and relative geometry. Keep IDs unique within each graph and parent references valid. XML-escape values; use a proper serializer. Prefer readable uncompressed XML unless a tested existing writer requires compression. draw.io documents [XML diagram source](https://www.drawio.com/docs/manual/advanced/diagram-source-edit/) and [file import](https://www.drawio.com/docs/manual/import/).

Map semantic shapes to verified draw.io styles or supported editable custom stencils: process, decision, input/output, manual-input/manual-operation, document, database, connectors, and UML activity initial/final states. Use real editable lane/group structures with labels and correct child-coordinate transforms. Preserve arrowheads and guard labels. Do not place a whole SVG/PNG inside one cell and call it an editable export. If a symbol needs an editable composite, preserve the semantic meaning and explain the composition.

Supply short local open/import instructions with the file. Keep external-editor changes as a separate source revision unless a tested reverse-import path exists; re-exporting documentation must not silently erase edits made in draw.io.

## FigJam implementation

Prefer an existing verified target-native route if available. Otherwise generate a local import package alongside the artifact: a versioned graph.json plus a small complete FigJam plugin (manifest, runnable JavaScript, import UI where used) and concise setup/import instructions. This is an export adapter included with the deliverable, not a prerequisite companion agent skill or a third-party plugin download. Users may need to create/import a local development plugin in their supported Figma desktop environment; verify current manifest/setup requirements and disclose editor/organization restrictions. Do not claim a raw JSON file alone is an import solution.

The [Figma Plugin API](https://developers.figma.com/docs/plugins/api/figma/) provides FigJam shape and connector creation. Use the supported editor type and actual APIs; load required fonts before assigning text. Build all nodes first, map source IDs to editor IDs, then bind native connectors to node endpoints. Preserve source IDs/revision in supported metadata for traceability.

Verify shape mappings against [ShapeWithTextNode](https://developers.figma.com/docs/plugins/api/ShapeWithTextNode/). Examples include ROUNDED_RECTANGLE, DIAMOND, PARALLELOGRAM_RIGHT, MANUAL_INPUT, TRAPEZOID, ENG_DATABASE, and DOCUMENT_SINGLE. Check orientation and actual silhouettes; an enum name alone does not establish correspondence with every flowchart symbol. Preserve UML final rings, lane structure, and unsupported notation through suitable editable primitives/composites when the target permits it, and report remaining fidelity limits instead of replacing everything with squares.

Use [ConnectorNode](https://developers.figma.com/docs/plugins/api/ConnectorNode/) for bound endpoints, labels, routing, and arrow caps. Free-standing drawn lines do not satisfy attached-connector editability. Where a composite cannot accept native endpoint binding, document and handle that limitation explicitly. Translate board pages to named sections/groups or supported pages according to actual target capability, without assuming draw.io page semantics are identical.

Validate the payload before creating objects: schema version, duplicate IDs, unresolved edges, parent cycles, dimensions, supported symbols, and practical size limits. Do not eval payloads or fetch remote data. Import into a new named section/group without replacing unrelated canvas content. Handle cancellation/partial failure visibly; roll back only objects created by that import or identify remaining partial content. Repeated import should create a clearly named new copy or use an explicit supported update policy, never silently overwrite edits. Report skipped/converted elements with counts and reasons.

The generated package must include real working import code, not an instruction to find an unspecified plugin. Distinguish generating this local package from running it against a user's live FigJam board; perform external writes only when authorized for the concrete target. If local plugin execution is blocked by the user's environment, provide the remaining usable exports and explain that native FigJam import is still blocked. After import, the user edits in FigJam; automatic two-way synchronization is not implied.

## Verification and delivery

Check these separately and state exactly what ran:

1. **Structure:** Parse .drawio XML and graph JSON; validate graph/parent references, geometry, page scope, escaped labels, and preservation of source revision. Check importer JavaScript and manifest against actual supported APIs. The existing HTML/PDF artifact validator does not perform these tests.
2. **Topology:** Compare semantic node/edge counts and relationships with the canonical model, accounting explicitly for groups/composite shapes. Confirm input/output, manual shapes, decision guards, arrow direction, lane membership, and UC/AD labels survived export.
3. **Target editing:** Open/import into the actual target when available. Change a label, move and resize a connected node, and confirm its connectors stay attached. Check the densest activity diagram's lanes and a flowchart's special symbols. A preview screenshot or mocked API test does not pass this gate.
4. **Persistence:** Save and reopen the draw.io file or FigJam board; verify edits, relationships, and named sections survive. Do not claim a working .jam export unless that native file path was actually tested.
5. **Import failure:** Test invalid data, unsupported shapes, Unicode/multiline text, missing fonts, cancellation, and repeat import proportional to the adapter's behavior. Report partial conversion and preserve existing user work.

Deliver the actual files/package and short instructions, alongside requested visual exports. Report full, partial, or unverified editability per target, listing affected element types where needed. Never claim all exports were tested because instruction files were validated. For a skill-only update, state that these are authoring/verification requirements; no target app or import adapter has been executed merely by updating this reference.
