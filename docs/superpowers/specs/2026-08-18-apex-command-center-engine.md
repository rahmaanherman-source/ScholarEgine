# APEX Command Center Engine — Design Specification

## Purpose

ScholarEgine is to serve as the operational foundation for the APEX Terminal / Real-Time Engine: a developer command center where the user can see, connect, create, run, test, verify, deploy, publish, and operate their software and creative systems from one visual environment.

The supplied visual references are the authoritative UX direction. The engine should preserve the existing ScholarEgine identity and verification foundation while adding an elevated command-center shell and modular layers.

## Visual Source of Truth

The primary visual reference is the supplied APEX TERMINAL / REAL-TIME ENGINE board:

- dark, high-contrast command-center UI
- APEX TERMINAL header
- global Gabby command/search bar
- verified status indicator
- GODSPEED owner identity
- left Workspace navigation
- Connected Apps rail
- central creation/workspace surface
- right Concierge: Gabby surface
- Project status and engine cards
- lower system/status/audio/dialogue/timeline/audit surfaces
- bottom operational lifecycle: BUILD / RUN / TEST / VERIFY / DEPLOY / PUBLISH
- central APEX REAL-TIME ENGINE identity
- Truth: Verified and Gabby Online indicators

A second visual reference defines the broader APEX ecosystem and provider/connectivity layer. It informs the engine's concept of providers, connectors, capability contracts, verification states, and revenue/operations surfaces.

A third reference shows a developer-facing connection flow for Vercel. It informs the local-first developer landing/connection UX, but credentials must never be exposed in frontend source or persistent UI state.

## Architectural Principle

This is an additive upgrade, not a destructive replacement.

Existing ScholarEgine Slab-Zero/Gatekeeper functionality remains intact. The UI shell sits above the existing verification layer and communicates with application adapters/services through explicit interfaces.

The engine is layered rather than flattened:

1. Identity / shell layer
2. Workspace and navigation layer
3. Command / Gabby layer
4. Creation and tooling layer
5. Provider/connector layer
6. Runtime/environment layer
7. Verification / audit layer
8. Memory / truth layer
9. Bottom lifecycle controls

## Functional Layers

### Workspace

- Dashboard
- Projects
- Tools
- Engines
- Connections
- Marketplace
- Audit Log
- Memory Slabs
- Settings
- Workspace Manager

### Command / Gabby

- global command/search input
- concierge panel
- context-aware prompts
- action routing to active workspace/tool
- no direct exposure of credentials

### Creation Studio

- Create
- Characters
- Worlds
- Animation
- Render
- asset/tool controls such as Sculpt, Model, Texture, Rig, Animate, Light, Render

### Engine Grid

- APEX Engine
- APEX Render
- Physics
- Audio Engine
- AI Generation
- World Builder

These are capability surfaces. They may begin as adapters/stubs with explicit unavailable states rather than fake connected states.

### System Surfaces

- CPU
- GPU
- RAM
- VRAM
- Network
- Foley & Sound Design
- AI Dialogue & ADAK
- Timeline / Sequence
- Audit Feed

### Provider / Connector Layer

Provider statuses must use explicit states such as:

- CONNECTED + VERIFIED
- CONNECTED NOT VERIFIED
- AVAILABLE NOT CONNECTED
- MISSING CONNECTOR
- NOT NEEDED

The UI must never display VERIFIED without evidence from the verification layer.

### Runtime / Environment Layer

Provide an environment manager capable of showing and operating approved local/dev environments. The interface may start, stop, inspect, and route to configured environments through adapters, but must never imply successful execution without a real result.

### Sketchpad / Backplane

Sketchpad is a persistent backplane behind the visible command-center board. It is not a replacement for the main UI. It stores or links working artifacts, diagrams, notes, layout intent, and project context so each visible engine layer can reference the same underlying project state.

## Required UX Features

### Workspace Manager

- open/view/manage workspaces
- close workspace surface without deleting workspace data
- preserve active workspace state

### Focus Mode

- collapse/minimize secondary chrome
- preserve active task and state
- explicit enter/exit controls
- reversible

### Collapsible Sidebars

- left workspace rail collapsible
- connected-app rail collapsible
- clear icons and accessible labels
- preserve navigation state

### Collapsible Panels

- all appropriate lower/right/secondary panels may collapse
- collapse icons use consistent affordances
- contents remain intact
- state may persist locally when safe

## Developer Landing Page Direction

The developer-facing landing page should communicate:

APEX TERMINAL — REAL-TIME ENGINE

It should be visually faithful to the supplied board while making clear which capabilities are operational, which are available, and which require connection. The developer view should emphasize the command center and real work rather than marketing-only content.

## Local-first Direction

The intended architecture is local-first where practical:

- run development environments locally
- run approved local engines/adapters locally
- use cloud providers for services that require cloud infrastructure
- use secure secret references rather than sending raw credentials through the UI
- maintain a single command center that orchestrates both local and connected resources

The UI must not claim that all resources can run locally until adapters and environment contracts actually provide that capability.

## Security / Verification

Do not weaken:

- authentication
- authorization
- Slab-Zero
- Gatekeeper
- provenance validation
- audit records
- secret handling

Do not commit credentials, PEM keys, API keys, or tokens.

## Evidence Rules

The memory/truth record must distinguish:

- PRESENT — observed in repository
- ADDED — implementation committed
- TESTED — automated/local test executed
- VERIFIED — evidence-based verification completed
- BLOCKED — dependency or environment prevents verification
- MISSING — required component not present

No fake green. A green status must have a corresponding evidence source.

## Acceptance Criteria

1. APEX Terminal command-center shell exists as an additive layer over ScholarEgine.
2. Workspace Manager exists and is non-destructive.
3. Focus Mode exists and is reversible.
4. Sidebars are collapsible and preserve state.
5. Panels have collapse/expand controls.
6. Gabby command surface routes to real application actions where implemented.
7. Engine capability cards show real status rather than fabricated verification.
8. Provider/connector states use explicit truthful status vocabulary.
9. Sketchpad exists as the persistent backplane/context layer.
10. Local/dev environment surfaces can expose real environment state without false claims.
11. Build/run/test/verify/deploy/publish lifecycle actions exist with truthful outcomes.
12. Slab-Zero/Gatekeeper remains intact.
13. A memory/truth file records implementation and verification status.
14. Typecheck/build/tests run where supported, and blockers are recorded rather than hidden.
