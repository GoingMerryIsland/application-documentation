# Browser documentation artifact

Read when producing or updating a documentation preview, HTML artifact, or PDF/PowerPoint/image exports. This reference belongs to the application-documentation skill; it is not another skill or an external dependency.

## Preflight and completion gates

Before investing in layout, inspect the available filesystem, browser/renderer, PDF generator, PowerPoint generator, and image exporter. Select concrete supported paths for each requested format. Check versions locally and run a small relevant smoke check before full generation; an importable automation package does not prove its browser executable is installed. Never assume an API or bundled library exists because this skill mentions it. Reuse installed tools. If needed, install an ordinary project-local dependency only when permitted; do not change global configuration, bypass restrictions, or upload content externally.

If a preferred tool fails, diagnose the actual error, attempt a relevant correction, then use a supported local alternative. Stop repeating an identical failed attempt. A missing tool is not permission to relabel another format. Preserve completed work and identify which outputs remain unavailable. Do not silently abandon exports merely because the first library is absent.

Treat these as separate gates: grounded content, structurally valid files, working browser interactions, readable rendered exports. Passing a structural check does not pass the other gates. Claim full completion only when requested outputs are produced and the applicable checks pass; otherwise identify the exact remaining gap.

## Output contract

Create an actual browser-viewable artifact from the task's grounded documentation. Default to a dedicated new folder such as docs-preview/<app-slug>/; follow the user's location and avoid overwriting unrelated files. For subsequent updates, modify the established artifact rather than creating competing copies.

Use index.html as the entrypoint. Prefer plain HTML/CSS/JavaScript for a portable, build-free document. Reuse an existing framework only when the user requests it or the established preview requires it. Do not build a SaaS shell, add authentication, or deploy a public site for a documentation preview.

Record the actual generator dependencies and a repeatable generation command when scripts are used; use paths relative to the artifact root, not machine-specific paths. Keep temporary conversion files and QA screenshots separate from delivered assets.

Maintain one canonical content model with stable section/diagram IDs and source/status information. This may be Markdown plus structured metadata or a document data file. Derive the HTML and exports from it; do not independently invent different facts in each format. Reuse existing project documentation as the source where possible.

A suitable folder contains:

| Path | Purpose |
| --- | --- |
| index.html | Browser entrypoint with navigation and export controls |
| assets/ | Local styles/scripts, rendered diagrams, images, fonts when needed |
| source/ | Canonical content/model and editable Mermaid sources if not already maintained elsewhere |
| exports/documentation.pdf | Complete print-oriented documentation |
| exports/documentation.pptx | Presentation with editable titles/text and readable diagrams |
| exports/png/ | Section or diagram PNGs, named with stable IDs |
| exports/jpg/ | Matching JPGs with an opaque background |

Create only real files needed for the requested scope. Keep lightweight documents in one HTML file where practical; do not multiply source files solely to match this example.

## Preview experience

Use a clean, responsive layout with readable typography, restrained color, adequate contrast, and a main content column. Include a contents sidebar/drawer, section anchors, active-section indication, and search for multi-section documentation. For a one-diagram artifact, use a simple canvas and export toolbar instead.

For full HTML documentation, include a prominent Full Workspace menu alongside Documentation. Follow [Full Workspace visual explorer](full-workspace.md) for its diagram canvas, page organization, navigation, shared content model, scoped exports, and interaction checks. A fullscreen button or a gallery of thumbnails alone does not satisfy this mode. Explicit narrower deliverables still control scope.

Give diagrams a zoom/reset or full-size view where their complexity warrants it. Preserve readable labels on narrow screens. Include keyboard access, visible focus, semantic headings, and useful button labels. Light/dark appearance is optional; export backgrounds must remain predictable. Display proposed/unknown status alongside affected content.

Use escaped text or trusted structured rendering for source code and external input. Set literal labels with textContent; escape HTML-sensitive characters and closing script delimiters when embedding source data in HTML. Validate imported SVG before inlining it; remove active content and remote references. Do not execute scripts embedded in imported documentation. Avoid trackers and remote uploads.

Target opening index.html directly in a browser. Embed required content instead of relying on file:// fetch of sibling JSON/Markdown. Pre-render Mermaid to SVG and retain its source, or bundle the necessary local renderer. Bundle dependencies locally when practical. Do not claim offline operation if fonts, scripts, images, or export libraries still require a network.

If a local server is genuinely necessary, give an exact launch command and state that direct opening is unsupported. Hosting requires a separate request. A Claude-like artifact means an interactive browser preview; do not claim integration into Claude's artifact UI.

## Functional exports

Provide actual PDF, PPTX, PNG, and JPG output for the default full browser-artifact workflow when tools permit, with working controls to obtain each. A button alone is not an export implementation. Respect narrower format requests.

Choose either a tested client-side generator or generation during authoring with downloads of the produced files. Prefer author-time generation when it avoids heavy browser libraries and gives reliable layout. Show the export scope and file type accurately. Static downloads are snapshots: label them accordingly if the preview supports editing. Regenerate affected exports whenever content changes so the preview and downloads agree. Never present an old export as current; track the source revision or digest, and replace final outputs only after successful generation. Retain the prior working artifact on failed rebuilds.

- **PDF:** Produce a real paginated PDF. Supply print CSS that hides navigation/toolbars, exposes content regardless of search/collapse state, handles tables/long code, and prevents diagram clipping. Wait for diagrams, images, and fonts before generation. A print button may call the browser's print dialog as a fallback, labeled Print / Save as PDF; it is not a verified generated PDF download.
- **PowerPoint:** Produce a genuine .pptx, the default modern PowerPoint format. Do not rename HTML, PDF, or images to .ppt/.pptx. Build coherent slides with editable headings/body text/tables where supported. Diagrams may be SVG/PNG if native shapes would compromise layout; disclose their editability. Split dense content across slides or appendices. Identify a summarized deck as a summary and retain source section IDs. Do not claim all text is editable if slides are screenshots.
- **PNG/JPG:** Default to a selected section or diagram and show that scope in the control. Exclude UI chrome and temporary zoom transforms. Use readable export dimensions, flatten the JPG background, and preserve PNG transparency only where intentional. Split a long document into named images rather than one unreadable or memory-heavy canvas. Wait for assets; handle cross-origin/canvas errors visibly instead of downloading blank images.
- **Controls:** Download only verified existing files or invoke implemented generators. For generation, show progress, prevent duplicate clicks, report failures, and restore the control afterward. Disable an unavailable format with a concise reason; never substitute a different format silently. Keep browser print available where practical.

Use available document, presentation, and rendering tools directly. Execute this bundled workflow without downloading or installing companion skills. Missing export tools must be handled through the preflight and local-tool fallback, not a skill installer. Do not require a particular library when a supported alternative is available. State a genuine capability limitation and deliver supported outputs; do not claim all exports work without creating/testing them. Never send private documentation to a conversion service without authorization.

For Full Workspace, also follow [Editable diagram exports](editable-diagram-exports.md) for .drawio and FigJam import packages. These require semantic nodes/edges and separate target-editor verification; the basic artifact validator's pdf/pptx/png/jpg checks do not verify them. Respect narrower user-selected formats.

## Verification

Run the bundled structural check from the resolved skill folder, using an absolute artifact path and the available Python interpreter (Python 3.9+):

```bash
python scripts/validate_artifact.py /absolute/path/to/artifact --offline
```

Default required formats are pdf, pptx, png, jpg. For an explicitly narrower request, pass e.g. `--required pdf png`; an empty `--required` checks the preview without requiring exports. Add `--report /path/to/qa-report.json` to retain results outside deliverables. The script uses standard-library checks, deepening PDF/image/slide checks when pypdf, Pillow, or python-pptx are installed. Missing optional validators produce warnings, not proof of successful decoding. Resolve reported errors and complete the remaining checks below.

Open the preview using an available browser and check navigation, search, responsive layout, diagrams, and every export control. For direct-file support, test file:// rather than inferring it from a working HTTP preview. Test offline behavior if advertised. Block outbound network requests and reload. Test at least a narrow phone viewport and desktop. Search for a match and for no results, clear search, navigate to a previously hidden section, and print while filtered/collapsed; printing must include all intended content. Keyboard-test the menu/export controls. Capture browser errors and missing resources.

When Full Workspace is included, also execute the interaction and export checks in full-workspace.md. The structural validator does not validate camera transforms, pointer behavior, workspace state, or export framing.

Download each required format through the actual control; confirm the resulting filename, format, nonempty content, and selected scope. A successful direct read of an export does not verify its button. Test literal source strings containing `<`, `>`, `&`, quotes, and closing script delimiters: display must remain intact and no code execute. Use the densest relevant document/diagram to exercise overflow; add a targeted regression case whenever a defect is fixed.

Open/parse the actual exported files. Inspect PDF pages, rendered slides, and representative images for clipping, overflow, missing glyphs, tiny labels, blank assets, and unwanted UI. Compare exported diagrams with their source: arrowheads, line styles, direction, cardinality, and labels must survive conversion. Some SVG renderers silently omit markers or CSS; switch to a renderer that preserves them rather than accepting a decodable but semantically wrong image. Check file signatures and the slide package rather than trusting extensions. Verify editable text if promised. Inspect at least the densest page/slide/diagram and every distinct export layout.

If browser/rendering tools are unavailable, perform possible structural checks and identify precisely what remains untested. Do not manufacture screenshots or claim visual verification.

Deliver the HTML entrypoint and exports or the portable folder package through the host's supported file mechanism. If only individual downloads are supported, embed resources or deliver a portable archive through a supported mechanism. Do not expect separate downloaded files to recreate nested paths automatically. Preserve the folder's relative paths; a lone index.html download is insufficient if dependencies are external to it. State how to open it, what exports are included, and any material limitations. Avoid pasting the entire artifact source into chat unless requested.

## Maintaining the checker

After changing the validator, run `python scripts/test_validate_artifact.py` from the skill folder. These regression cases cover structural failures; they do not replace actual export generation, browser interaction, or visual review.
