# Application Documentation Skill

An Agent Skill for creating, reviewing, and updating application documentation from a brief or codebase. Covers comprehensive PRDs, requirements, user flows, Mermaid diagrams, architecture, ERD, APIs, robustness, and tests.

## Features

- **End-to-End Application Documentation**: Full PRD, use cases, activity tables, data schemas, API contracts, and testing specifications.
- **Visual Diagrams**: Architecture diagrams, Mermaid flowcharts, ERD, and sequence diagrams.
- **Export Capabilities**: Browser-previewable HTML documentation with export support (PDF, PowerPoint, PNG, JPG).
- **Self-Contained & Portable**: Compatible with Agent Skills-compatible assistants (Antigravity, OpenCode, Claude Code, etc.).

## Repository Structure

```text
├── SKILL.md                  # Main skill definition and instructions
├── agents/                   # Agent configuration
│   └── openai.yaml
├── assets/                   # Skill assets (icon, etc.)
│   └── icon.svg
├── references/               # Standards, guidelines, and reference documentation
│   ├── browser-artifact.md
│   ├── diagram-standards.md
│   ├── editable-diagram-exports.md
│   ├── flowchart-symbols.md
│   ├── full-workspace.md
│   ├── prd-robustness.md
│   ├── scope-completeness.md
│   └── use-case-activities.md
└── scripts/                  # Helper scripts for validation and testing
    ├── test_validate_artifact.py
    └── validate_artifact.py
```

## Usage

This skill can be installed into any Agent Skills compatible environment (such as `~/.gemini/antigravity-cli/skills/` or `.opencode/skills/`).
