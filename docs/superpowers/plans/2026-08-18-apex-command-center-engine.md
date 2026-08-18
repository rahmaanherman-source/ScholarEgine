# APEX Command Center Engine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an additive APEX TERMINAL / REAL-TIME ENGINE command-center layer over ScholarEgine, preserving Slab-Zero while adding the exact requested elevated UI, runtime/provider surfaces, and truth-memory tracking.

**Architecture:** Create a TypeScript/React application shell around the existing ScholarEgine verification foundation. Keep UI state and orchestration separate from the Slab-Zero Python verifier, expose local/runtime/provider capabilities through adapters, and make every status evidence-driven.

**Tech Stack:** TypeScript, React, Vite, existing ScholarEgine Python Slab-Zero/Gatekeeper, browser-local UI state, adapter interfaces for local/cloud providers.

**Spec:** `docs/superpowers/specs/2026-08-18-apex-command-center-engine.md`

## Global Constraints

- Upgrade, do not destructively replace the existing ScholarEgine verification foundation.
- Preserve Slab-Zero/Gatekeeper and provenance validation.
- Never expose or commit credentials, private keys, API keys, or tokens.
- Never show VERIFIED without evidence.
- UI controls are additive and reversible where applicable.
- Local/runtime features must report actual execution state; no fake green.
- Use the exact supplied APEX Terminal visual language as the UX direction.
- Record PRESENT / ADDED / TESTED / VERIFIED / BLOCKED / MISSING state in the memory/truth record.

---

### Task 1: TypeScript Application Foundation

**Files:**
- Create: `package.json`
- Create: `tsconfig.json`
- Create: `vite.config.ts`
- Create: `index.html`
- Create: `src/main.tsx`
- Create: `src/app/App.tsx`
- Test: `src/app/App.test.tsx`

**Interfaces:**
- Produces a bootable React application that later tasks render into.

- [ ] **Step 1: Write the failing test**

Create an app smoke test that imports `App` and asserts the APEX Terminal shell label is rendered.

- [ ] **Step 2: Run test to verify it fails**

Run: `npm test -- --run src/app/App.test.tsx`
Expected: FAIL because the app scaffold does not yet exist.

- [ ] **Step 3: Write minimal implementation**

Create the Vite/React TypeScript scaffold and a minimal `App` that renders `APEX TERMINAL` and `REAL-TIME ENGINE`.

- [ ] **Step 4: Run test to verify it passes**

Run: `npm test -- --run src/app/App.test.tsx`
Expected: PASS.

- [ ] **Step 5: Run typecheck**

Run: `npm run typecheck`.
Expected: exit 0.

- [ ] **Step 6: Commit**

```bash
git add package.json tsconfig.json vite.config.ts index.html src/main.tsx src/app/App.tsx src/app/App.test.tsx
git commit -m "feat: scaffold apex command center app"
```

---

### Task 2: Core Bootstrap and Ollama Adapter Boundary

**Files:**
- Create: `src/core/bootstrap.ts`
- Create: `src/adapters/OllamaAdapter.ts`
- Create: `src/adapters/types.ts`
- Test: `src/core/bootstrap.test.ts`
- Test: `src/adapters/OllamaAdapter.test.ts`

**Interfaces:**
- `bootstrapApp(): AppRuntime`
- `OllamaAdapter.isAvailable(): Promise<boolean>`
- `OllamaAdapter.chat(input: ChatRequest): Promise<ChatResponse>`

- [ ] **Step 1: Write failing tests**

Test that bootstrap returns an application runtime and the Ollama adapter reports unavailable rather than falsely connected when no local Ollama endpoint exists.

- [ ] **Step 2: Run tests to verify red**

Run: `npm test -- --run src/core/bootstrap.test.ts src/adapters/OllamaAdapter.test.ts`
Expected: FAIL with missing modules/functions.

- [ ] **Step 3: Implement minimal interfaces**

Implement `bootstrapApp()` and a fetch-based Ollama adapter with timeout/error handling and explicit unavailable state.

- [ ] **Step 4: Run tests**

Run the same command; expected PASS.

- [ ] **Step 5: Run typecheck**

Run: `npm run typecheck`.
Expected: exit 0.

- [ ] **Step 6: Commit**

```bash
git add src/core/bootstrap.ts src/adapters/types.ts src/adapters/OllamaAdapter.ts src/core/bootstrap.test.ts src/adapters/OllamaAdapter.test.ts
git commit -m "feat: add runtime bootstrap and ollama adapter"
```

---

### Task 3: APEX Shell, Navigation, and Layer Model

**Files:**
- Create: `src/ui/layout/ApexShell.tsx`
- Create: `src/ui/layout/WorkspaceRail.tsx`
- Create: `src/ui/layout/ConnectedAppsRail.tsx`
- Create: `src/ui/layout/TopCommandBar.tsx`
- Create: `src/ui/layout/BottomLifecycleBar.tsx`
- Create: `src/ui/state/layoutStore.ts`
- Test: `src/ui/layout/ApexShell.test.tsx`

**Interfaces:**
- `LayoutLayerId` union for workspace, connected-apps, main-stage, gabby, project, system, audit, sketchpad.
- `LayoutState` with sidebar/panel/focus state.

- [ ] **Step 1: Write failing tests**

Test that the shell renders all canonical top-level surfaces and that `BUILD`, `RUN`, `TEST`, `VERIFY`, `DEPLOY`, and `PUBLISH` controls exist.

- [ ] **Step 2: Verify red**

Run: `npm test -- --run src/ui/layout/ApexShell.test.tsx`
Expected: FAIL.

- [ ] **Step 3: Implement shell**

Build the dark APEX Terminal shell with responsive regions matching the reference board. Use semantic buttons and data-driven layer definitions.

- [ ] **Step 4: Verify green**

Run the test command; expected PASS.

- [ ] **Step 5: Commit**

```bash
git add src/ui/layout src/ui/state/layoutStore.ts
 git commit -m "feat: add apex terminal shell and layer model"
```

---

### Task 4: Workspace Manager and Focus Mode

**Files:**
- Create: `src/ui/workspace/WorkspaceManager.tsx`
- Create: `src/ui/workspace/workspaceStore.ts`
- Create: `src/ui/focus/FocusMode.tsx`
- Test: `src/ui/workspace/WorkspaceManager.test.tsx`
- Test: `src/ui/focus/FocusMode.test.tsx`

**Interfaces:**
- `WorkspaceManager.open(id)` / `close(id)` / `select(id)`
- `FocusMode.enter()` / `exit()` / `isActive`

- [ ] **Step 1: Write failing tests**

Cover non-destructive workspace close, active-workspace preservation, Focus Mode entry/exit, and restoration of prior layout state.

- [ ] **Step 2: Verify red**

Run both test files; expected FAIL.

- [ ] **Step 3: Implement**

Add the Workspace Manager and reversible Focus Mode. Use local persistence only for non-sensitive layout state.

- [ ] **Step 4: Verify green**

Run tests; expected PASS.

- [ ] **Step 5: Commit**

```bash
git add src/ui/workspace src/ui/focus
 git commit -m "feat: add workspace manager and focus mode"
```

---

### Task 5: Collapsible Sidebars and Panel Controls

**Files:**
- Create: `src/ui/layout/CollapseButton.tsx`
- Create: `src/ui/panels/Panel.tsx`
- Create: `src/ui/panels/PanelRegistry.ts`
- Test: `src/ui/layout/CollapseButton.test.tsx`
- Test: `src/ui/panels/Panel.test.tsx`

**Interfaces:**
- `PanelProps { id, title, collapsed, onToggle, children }`
- `setSidebarCollapsed(id, value)`

- [ ] **Step 1: Write failing tests**

Test accessible collapse/expand behavior, preserved panel children, and independent sidebar state.

- [ ] **Step 2: Verify red**

Run the tests; expected FAIL.

- [ ] **Step 3: Implement**

Add sidebar and panel collapse controls with responsive behavior and persisted non-sensitive layout state.

- [ ] **Step 4: Verify green**

Run tests; expected PASS.

- [ ] **Step 5: Commit**

```bash
git add src/ui/layout/CollapseButton.tsx src/ui/panels
 git commit -m "feat: add collapsible sidebars and panels"
```

---

### Task 6: Gabby Concierge and Engine/Capability Surfaces

**Files:**
- Create: `src/ui/gabby/ConciergeGabby.tsx`
- Create: `src/ui/engines/EngineGrid.tsx`
- Create: `src/ui/engines/engineRegistry.ts`
- Create: `src/ui/engines/CapabilityStatus.tsx`
- Test: `src/ui/engines/CapabilityStatus.test.tsx`

**Interfaces:**
- `CapabilityStatus = 'CONNECTED_VERIFIED' | 'CONNECTED_NOT_VERIFIED' | 'AVAILABLE_NOT_CONNECTED' | 'MISSING_CONNECTOR' | 'NOT_NEEDED'`
- `EngineCapability { id, label, status, evidenceRef? }`

- [ ] **Step 1: Write failing tests**

Verify that `CONNECTED_VERIFIED` requires an evidence reference while non-connected states do not display false-green treatment.

- [ ] **Step 2: Verify red**

Run: `npm test -- --run src/ui/engines/CapabilityStatus.test.tsx`
Expected: FAIL.

- [ ] **Step 3: Implement**

Build the Concierge: Gabby panel and engine grid. Wire commands to existing adapters where available; otherwise expose truthful unavailable states.

- [ ] **Step 4: Verify green**

Run the test; expected PASS.

- [ ] **Step 5: Commit**

```bash
git add src/ui/gabby src/ui/engines
 git commit -m "feat: add gabby concierge and engine capability surfaces"
```

---

### Task 7: Sketchpad Backplane and Local Environment Manager

**Files:**
- Create: `src/ui/sketchpad/Sketchpad.tsx`
- Create: `src/runtime/EnvironmentManager.ts`
- Create: `src/runtime/types.ts`
- Test: `src/runtime/EnvironmentManager.test.ts`

**Interfaces:**
- `EnvironmentManager.list(): Promise<EnvironmentInfo[]>`
- `EnvironmentManager.start(id): Promise<ExecutionResult>`
- `EnvironmentManager.stop(id): Promise<ExecutionResult>`
- `EnvironmentManager.inspect(id): Promise<EnvironmentInfo>`

- [ ] **Step 1: Write failing tests**

Test that environments without an available adapter return explicit `UNAVAILABLE` rather than `RUNNING`, and that successful operations return evidence data.

- [ ] **Step 2: Verify red**

Run: `npm test -- --run src/runtime/EnvironmentManager.test.ts`
Expected: FAIL.

- [ ] **Step 3: Implement environment contract**

Implement an adapter-neutral manager and Sketchpad UI as the persistent project/backplane surface. Do not pretend local execution exists until an adapter returns a real result.

- [ ] **Step 4: Verify green**

Run tests; expected PASS.

- [ ] **Step 5: Commit**

```bash
git add src/ui/sketchpad src/runtime
 git commit -m "feat: add sketchpad and truthful runtime environment manager"
```

---

### Task 8: Creation Studio and Command-Center Modules

**Files:**
- Create: `src/ui/studio/CreationStudio.tsx`
- Create: `src/ui/studio/CharacterSurface.tsx`
- Create: `src/ui/studio/StudioTabs.tsx`
- Create: `src/ui/system/SystemStatusPanel.tsx`
- Create: `src/ui/audio/FoleySoundPanel.tsx`
- Create: `src/ui/dialogue/DialogueAdakPanel.tsx`
- Create: `src/ui/timeline/TimelinePanel.tsx`
- Create: `src/ui/audit/AuditFeed.tsx`
- Test: `src/ui/studio/CreationStudio.test.tsx`

**Interfaces:**
- `StudioTab = 'CREATE' | 'CHARACTERS' | 'WORLDS' | 'ANIMATION' | 'RENDER'`
- Panels consume the shared `PanelProps` contract.

- [ ] **Step 1: Write failing tests**

Verify tab switching and required reference-board section labels.

- [ ] **Step 2: Verify red**

Run the studio test; expected FAIL.

- [ ] **Step 3: Implement panels**

Add the creation/studio and lower command-center surfaces with modular panels. Keep initially non-integrated creative tools explicit as UI surfaces, not fake operational engines.

- [ ] **Step 4: Verify green**

Run tests; expected PASS.

- [ ] **Step 5: Commit**

```bash
git add src/ui/studio src/ui/system src/ui/audio src/ui/dialogue src/ui/timeline src/ui/audit
 git commit -m "feat: add apex creation and operations surfaces"
```

---

### Task 9: Truth Memory / Verification Register

**Files:**
- Create: `docs/memory/APEX_COMMAND_CENTER_TRUTH.md`
- Create: `docs/memory/apex-command-center-status.json`
- Test: `docs/memory/apex-command-center-status.schema.json`

- [ ] **Step 1: Define truth states**

Create machine-readable status with PRESENT, ADDED, TESTED, VERIFIED, BLOCKED, and MISSING states.

- [ ] **Step 2: Verify schema**

Validate the JSON against its schema.

- [ ] **Step 3: Write human-readable memory**

Record the exact reference-board architecture, implemented files, test commands, evidence references, and remaining blockers. Do not mark untested functionality VERIFIED.

- [ ] **Step 4: Commit**

```bash
git add docs/memory
 git commit -m "docs: add apex command center truth memory"
```

---

### Task 10: Integration, Typecheck, Build, and Regression Verification

**Files:**
- Modify: `src/app/App.tsx`
- Modify: `src/main.tsx`
- Modify: `docs/memory/APEX_COMMAND_CENTER_TRUTH.md`
- Test: all existing project tests plus newly added tests

- [ ] **Step 1: Wire the shell**

Mount the APEX shell and all completed panels without removing the existing Slab-Zero tooling.

- [ ] **Step 2: Run full test suite**

Run: `npm test -- --run`
Expected: all tests pass or documented blockers with exact failures.

- [ ] **Step 3: Run typecheck**

Run: `npm run typecheck`
Expected: exit 0.

- [ ] **Step 4: Run production build**

Run: `npm run build`
Expected: exit 0.

- [ ] **Step 5: Verify application entrypoint**

Run: `npm run dev -- --host 127.0.0.1` and confirm the app serves successfully on localhost.

- [ ] **Step 6: Update truth memory**

Record fresh results, including actual command outputs, and use VERIFIED only where evidence exists.

- [ ] **Step 7: Commit integration**

```bash
git add src docs/memory package.json tsconfig.json vite.config.ts index.html
git commit -m "feat: integrate apex command center engine"
```

## Final Verification Checklist

- [ ] APEX Terminal shell renders.
- [ ] Workspace Manager is functional and non-destructive.
- [ ] Focus Mode enters/exits correctly.
- [ ] Sidebars collapse/expand.
- [ ] Panels collapse/expand.
- [ ] Gabby Concierge is present.
- [ ] Engine capability statuses are truthful.
- [ ] Sketchpad exists as a shared backplane.
- [ ] Runtime environments report real state.
- [ ] Creation Studio and lower command-center surfaces render.
- [ ] Build/run/test/verify/deploy/publish controls exist and do not fabricate outcomes.
- [ ] Slab-Zero/Gatekeeper remains intact.
- [ ] No secrets were added.
- [ ] Tests pass.
- [ ] Typecheck passes.
- [ ] Production build passes.
- [ ] Truth memory reflects actual evidence.
