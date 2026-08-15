# Memory Slab Source-Preservation Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Establish a source-preserving master audit register that captures the feed-defined roadmap, separates AUDITED from VERIFIED, records evidence gaps, and provides the exact next verification target without overwriting existing Slab-Zero work.

**Architecture:** Keep Slab-Zero as the cryptographic verification engine and add a thin audit layer above it. The audit layer records claims, dependencies, evidence locators, and state; it never promotes a claim to VERIFIED. VERIFIED remains Gatekeeper-controlled and derived from proof.

**Tech Stack:** JSON, Markdown, existing Python Gatekeeper, GitHub Actions.

## Global Constraints

- Nothing enters VERIFIED memory without passing the existing verification gate.
- Historical proof is preserved; CURRENT and STALE remain distinct.
- Partial section/step verification is allowed.
- Completion percentages are derived, never manually asserted.
- Existing code, prompts, evidence, and documentation are preserved unless a verified defect requires correction.
- Missing source material is recorded as MISSING/BLOCKED rather than invented.

---

### Task 1: Create the master audit register

**Files:**
- Create: `slab-zero/audit/master-audit.json`
- Test: existing Slab-Zero schema/roadmap coverage tests should validate file presence and structure in a later task.

**Interfaces:**
- Consumes: the ordered 11-section Slab-Zero roadmap already established in the conversation and existing repository artifacts.
- Produces: a machine-readable audit inventory with `AUDITED`, `VERIFIED`, `UNVERIFIED`, `BLOCKED`, and `STALE` states.

- [ ] **Step 1:** Record the 11 ordered infrastructure sections without upgrading their status beyond evidence-supported state.
- [ ] **Step 2:** Record the current baseline as `NOT_CERTIFIED` until the Gatekeeper proves project claims.
- [ ] **Step 3:** Record evidence expectations and the exact next target.

### Task 2: Create the source-preservation contract

**Files:**
- Create: `slab-zero/audit/SOURCE-PRESERVATION.md`

**Interfaces:**
- Consumes: the feed-defined preservation/gap-fill rules.
- Produces: the canonical instruction that existing material is preserved and only missing pieces are added.

- [ ] **Step 1:** Document source categories: screenshots, code, prompts, repository artifacts, tests, records, and prior audit results.
- [ ] **Step 2:** Define `AUDITED != VERIFIED`.
- [ ] **Step 3:** Define the gap-fill-only rule.

### Task 3: Create the human-readable flight checklist

**Files:**
- Create: `slab-zero/audit/ROADMAP.md`

**Interfaces:**
- Consumes: `master-audit.json`.
- Produces: an ordered checklist showing the next actionable verification target.

- [ ] **Step 1:** List CONTRACT through BASELINE in dependency order.
- [ ] **Step 2:** Show per-section state and evidence locations.
- [ ] **Step 3:** Identify the first item that still requires proof.

### Task 4: Verify the audit layer

**Files:**
- Modify: `slab-zero/tests/test_roadmap_coverage.py` if present on the active branch.
- Test: Slab-Zero test suite and GitHub Actions.

- [ ] **Step 1:** Add structural tests for the audit register.
- [ ] **Step 2:** Reject malformed states and unsupported status promotion.
- [ ] **Step 3:** Run the full suite.
- [ ] **Step 4:** Record the resulting commit and test evidence.

### Task 5: Advance to the first real project claim

**Files:**
- Only modify the project-specific Memory Slab after evidence is available.

- [ ] **Step 1:** Use the audit register to select the first unverified dependency.
- [ ] **Step 2:** Gather/retrieve the evidence path.
- [ ] **Step 3:** Run Gatekeeper verification.
- [ ] **Step 4:** If it passes, create the first verified leaf and recompute the derived percentage.
- [ ] **Step 5:** If it cannot be proven, mark it `BLOCKED` or `UNVERIFIED` and move to the next independent item.
