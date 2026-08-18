# Elevated ScholarEgine Design

**Date:** 2026-08-18  
**Status:** Approved for implementation

## Goal

Turn the existing ScholarEgine Slab-Zero foundation into a verifiable TypeScript application foundation with an additive elevated workspace UI, without weakening or replacing the existing verification/provenance layer.

## Non-Destructive Rule

**REMEMBER → REBUILD → REBOOT → VERIFY → UPGRADE.**

Existing Slab-Zero/Gatekeeper behavior remains intact. New application code is additive. No secrets are introduced. No existing verification policy is weakened. UI close/collapse actions affect presentation state only and never delete user data.

## Current Verified Repository State

At the start of this work the repository is public and its visible top-level structure is `.github/`, `docs/`, `slab-zero/`, and `README.md`. The repository is Python-centered and did not contain `package.json`, `tsconfig.json`, `OllamaAdapter.ts`, or `core/bootstrap.ts`.

The existing Slab-Zero layer includes Gatekeeper, manifest, policy, schema, audit/evidence/proof directories, probes, and tests.

## Target Architecture

```text
ScholarEgine
├── slab-zero/                 existing verification/provenance foundation
├── core/
│   └── bootstrap.ts           application bootstrap and composition root
├── adapters/
│   └── OllamaAdapter.ts       Ollama HTTP adapter with typed interface
├── ui/
│   ├── WorkspaceManager.tsx
│   ├── FocusMode.tsx
│   ├── Sidebar.tsx
│   ├── CollapsiblePanel.tsx
│   └── App.tsx
├── styles/
│   └── app.css
├── tests/
│   └── ui.test.tsx
├── package.json
└── tsconfig.json
```

## UI Capabilities

### Workspace Manager

Provide an additive manager for named workspaces with open/close behavior. Closing a workspace changes UI state only and never deletes workspace data.

### Focus Mode

Provide an explicit reversible mode that hides/minimizes secondary navigation and panels while retaining the active workspace and task.

### Collapsible Sidebars

Provide keyboard-accessible collapse/expand controls and preserve navigation state.

### Collapsible Panels

Provide accessible collapse/expand controls for content panels without destroying their contents.

### Elevated Visual Treatment

Use restrained spacing, typography, borders, depth, active/hover/focus states, and responsive layout. Preserve ScholarEgine/GODSPEED identity.

## Ollama Boundary

`OllamaAdapter.ts` is an isolated provider adapter. It receives configuration from the application boundary rather than embedding secrets. The adapter exposes typed model listing and chat-generation methods and uses standard `fetch`.

## Bootstrap Boundary

`core/bootstrap.ts` creates the application model and adapter from environment/configuration. It does not contain credentials, private keys, or provider secrets.

## Verification

The TypeScript layer must have a deterministic typecheck. UI behavior must have automated tests for workspace close, Focus Mode, sidebar collapse, and panel collapse. The repository memory/truth file records actual evidence and distinguishes PRESENT, ADDED, TESTED, FAILED, and BLOCKED.

## Security Boundary

Do not modify authentication, authorization, Slab-Zero verification, provenance validation, GitHub credentials, private keys, API keys, or secrets handling. No credentials may be committed to source.
