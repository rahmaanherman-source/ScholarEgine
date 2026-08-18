# Elevated ScholarEgine Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a typed TypeScript application foundation and an elevated ScholarEgine UI with Workspace Manager, Focus Mode, collapsible sidebars, and collapsible panels while preserving Slab-Zero.

**Architecture:** Keep `slab-zero/` untouched as the verification/provenance boundary. Add a small TypeScript/React presentation layer with a typed Ollama adapter and a composition-root bootstrap. UI state is local to the application and presentation-only; it never deletes workspace data or secrets.

**Tech Stack:** TypeScript, React, Vite, Vitest, React Testing Library, CSS.

**Spec:** `docs/superpowers/specs/2026-08-18-elevated-scholaregine-design.md`

## Global Constraints

- Preserve existing `slab-zero/` verification and provenance behavior.
- Do not commit credentials, private keys, tokens, or API keys.
- UI close/collapse actions are non-destructive.
- Keep ScholarEgine/GODSPEED identity.
- Typecheck must run with `tsc --noEmit`.
- Tests must cover each new interaction.
- Memory/truth must record evidence rather than infer green status.

---

### Task 1: TypeScript application foundation

**Files:**
- Create: `package.json`
- Create: `tsconfig.json`
- Create: `vite.config.ts`
- Create: `index.html`
- Create: `src/main.tsx`

**Interfaces:**
- Produces a runnable React/Vite application and deterministic `typecheck`/`test` scripts.

- [ ] **Step 1: Add package metadata and scripts**

Use scripts:

```json
{
  "scripts": {
    "dev": "vite",
    "build": "tsc --noEmit && vite build",
    "typecheck": "tsc --noEmit",
    "test": "vitest run"
  }
}
```

Dependencies should be limited to React, React DOM, Vite, TypeScript, Vitest, jsdom, and React Testing Library packages needed by tests.

- [ ] **Step 2: Add strict TypeScript configuration**

Enable strict checking, JSX, ES module interoperability, DOM libraries, and a Vite-compatible module resolution strategy.

- [ ] **Step 3: Add Vite entry files**

Mount `src/main.tsx` into `#root` and render the application returned by `core/bootstrap.ts`.

- [ ] **Step 4: Run typecheck**

Run:

```bash
npm install
npm run typecheck
```

Expected: PASS with zero TypeScript errors.

- [ ] **Step 5: Commit**

```bash
git add package.json tsconfig.json vite.config.ts index.html src/main.tsx
git commit -m "feat: add TypeScript application foundation"
```

---

### Task 2: Ollama adapter and application bootstrap

**Files:**
- Create: `src/adapters/OllamaAdapter.ts`
- Create: `src/core/bootstrap.ts`
- Create: `src/core/types.ts`
- Create: `tests/ollama-adapter.test.ts`

**Interfaces:**
- `OllamaAdapter.listModels(): Promise<ModelInfo[]>`
- `OllamaAdapter.chat(request: ChatRequest): Promise<ChatResponse>`
- `bootstrap(): AppDependencies`

- [ ] **Step 1: Write failing adapter tests**

Test that `listModels()` calls `/api/tags`, maps returned model names, and surfaces non-OK responses. Test that `chat()` posts a model/messages payload and returns the generated message.

- [ ] **Step 2: Run the adapter tests and verify failure**

Run:

```bash
npm test -- tests/ollama-adapter.test.ts
```

Expected: FAIL because the adapter does not yet exist.

- [ ] **Step 3: Implement the minimal typed adapter**

Use an injected `fetch` and base URL. Default the base URL to `/api/ollama` so the browser does not require direct cross-origin Ollama access. Do not include credentials in source.

- [ ] **Step 4: Implement bootstrap**

Return the adapter and initial application configuration. Keep the composition root free of secrets.

- [ ] **Step 5: Run tests and typecheck**

```bash
npm test -- tests/ollama-adapter.test.ts
npm run typecheck
```

Expected: both PASS.

- [ ] **Step 6: Commit**

```bash
git add src/adapters src/core tests/ollama-adapter.test.ts
git commit -m "feat: add Ollama adapter and application bootstrap"
```

---

### Task 3: Workspace Manager and Focus Mode

**Files:**
- Create: `src/ui/WorkspaceManager.tsx`
- Create: `src/ui/FocusMode.tsx`
- Create: `tests/workspace-focus.test.tsx`

**Interfaces:**
- Workspace model: `{ id: string; name: string; active: boolean }`
- Workspace Manager receives workspace state and non-destructive `onClose`/`onSelect` callbacks.
- Focus Mode receives `enabled` and `onToggle`.

- [ ] **Step 1: Write failing UI tests**

Test that Workspace Manager opens, lists workspaces, selects a workspace, and calls `onClose` without a delete callback. Test that Focus Mode toggles and exposes accessible enter/exit labels.

- [ ] **Step 2: Run tests to verify failure**

```bash
npm test -- tests/workspace-focus.test.tsx
```

Expected: FAIL before components exist.

- [ ] **Step 3: Implement Workspace Manager**

Use semantic buttons, accessible labels, and non-destructive close semantics.

- [ ] **Step 4: Implement Focus Mode**

Provide one reversible control and a clear active state.

- [ ] **Step 5: Run tests**

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/ui/WorkspaceManager.tsx src/ui/FocusMode.tsx tests/workspace-focus.test.tsx
git commit -m "feat: add workspace manager and focus mode"
```

---

### Task 4: Collapsible sidebar and panels

**Files:**
- Create: `src/ui/Sidebar.tsx`
- Create: `src/ui/CollapsiblePanel.tsx`
- Create: `tests/collapsible-ui.test.tsx`

**Interfaces:**
- `Sidebar({ collapsed, onToggle, children })`
- `CollapsiblePanel({ title, collapsed, onToggle, children })`

- [ ] **Step 1: Write failing interaction tests**

Test sidebar collapse/expand, panel collapse/expand, keyboard activation, and accessible labels.

- [ ] **Step 2: Verify tests fail**

```bash
npm test -- tests/collapsible-ui.test.tsx
```

- [ ] **Step 3: Implement sidebar**

Preserve children and active navigation. Collapsed state changes layout only.

- [ ] **Step 4: Implement panel**

Preserve children while collapsed and expose `aria-expanded`.

- [ ] **Step 5: Run tests**

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/ui/Sidebar.tsx src/ui/CollapsiblePanel.tsx tests/collapsible-ui.test.tsx
git commit -m "feat: add collapsible navigation and panels"
```

---

### Task 5: Elevated ScholarEgine application shell

**Files:**
- Create: `src/ui/App.tsx`
- Create: `src/styles/app.css`
- Modify: `src/main.tsx`
- Create: `tests/app-shell.test.tsx`

**Interfaces:**
- App composes Workspace Manager, Focus Mode, Sidebar, and CollapsiblePanel without changing Slab-Zero.

- [ ] **Step 1: Write failing shell tests**

Verify ScholarEgine/GODSPEED identity, workspace controls, Focus Mode, sidebar toggle, panel toggle, and non-destructive workspace close behavior.

- [ ] **Step 2: Verify failure**

```bash
npm test -- tests/app-shell.test.tsx
```

- [ ] **Step 3: Implement App composition**

Use a small local UI state model. Keep active workspace state independent from collapsed UI state.

- [ ] **Step 4: Implement elevated responsive CSS**

Add restrained spacing, hierarchy, borders, subtle depth, responsive breakpoints, visible focus states, and reduced navigation in Focus Mode. Avoid stock imagery and unrelated branding.

- [ ] **Step 5: Run tests and typecheck**

```bash
npm test
npm run typecheck
npm run build
```

Expected: all tests PASS, typecheck PASS, build PASS.

- [ ] **Step 6: Commit**

```bash
git add src/ui/App.tsx src/styles/app.css src/main.tsx tests/app-shell.test.tsx
 git commit -m "feat: add elevated ScholarEgine shell"
```

---

### Task 6: Repository memory/truth file

**Files:**
- Create: `docs/SCHOLAREGINE_MEMORY.md`

**Interfaces:**
- Human-readable source-of-truth record of repository state and verification evidence.

- [ ] **Step 1: Record baseline facts**

Document that the original repository was Python/Slab-Zero centered and that the requested TypeScript files/UI were missing at baseline.

- [ ] **Step 2: Record implementation results**

Record each new component and status as `ADDED` only after it exists in the branch.

- [ ] **Step 3: Record verification evidence**

Record exact commands and outputs/exit codes. Never label a test `PASS` without fresh execution evidence.

- [ ] **Step 4: Record security state**

State that no credentials/private keys/API keys are stored in the new application files.

- [ ] **Step 5: Commit**

```bash
git add docs/SCHOLAREGINE_MEMORY.md
git commit -m "docs: record ScholarEgine memory and verification state"
```

---

### Task 7: Final verification

**Files:**
- Verify all changed files and existing Slab-Zero files remain intact.

- [ ] **Step 1: Run full test suite**

```bash
npm test
```

Expected: zero failures.

- [ ] **Step 2: Run TypeScript verification**

```bash
npm run typecheck
```

Expected: exit code 0.

- [ ] **Step 3: Run production build**

```bash
npm run build
```

Expected: exit code 0.

- [ ] **Step 4: Verify no secret patterns were introduced**

Search new files for PEM blocks, common token prefixes, and hard-coded API keys. Expected: no credentials.

- [ ] **Step 5: Verify Slab-Zero remains present**

Confirm `slab-zero/gatekeeper.py`, `manifest.json`, `policy.json`, `schema.json`, and tests still exist unchanged.

- [ ] **Step 6: Update memory file with final evidence**

Only record PASS/VERIFIED states supported by the commands above.

- [ ] **Step 7: Final review**

Review the branch diff for accidental deletions, duplicated application entry points, security regressions, and UI requirements that are missing.
