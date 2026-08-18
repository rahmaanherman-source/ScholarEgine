# APEX Human-First Engineering Memory

**Status:** Canonical design principle
**Applies to:** APEX, ScholarEgine, Gabby, Golden World, and future connected systems

## Core Principle

APEX must help the human understand the technology while the technology is being built and operated.

The system must not require the user to already know technical terminology in order to direct the system.

For important actions and concepts, present:

1. **Human name** — the plain-language name the user sees and uses.
2. **Technical name** — the computer/system term used internally.
3. **What it does** — a short plain-language definition.
4. **Why it matters** — why the operation or concept is being used.
5. **Result** — what actually happened, with truthful status.

This is a learning architecture, not merely a UI preference.

## Human ↔ Computer Naming Law

Every important asset, workspace, project, environment, connector, service, and operation should have a human-readable identity permanently associated with its technical identity.

Example:

- Human name: `Goldies Main Character`
- Computer name: `goldies_main_character_v01_<system-id>`

The human name is primary in the user interface. The technical identity remains available when useful, but the user must not be forced to memorize it.

One asset may have many representations across desktop, APEX, Gabby, Sketchpad, GitHub, GCP, Vercel, creation engines, and archives while retaining one human-facing identity.

## Teach While Building

When APEX or Gabby asks the user to perform a technical action, explain it at the moment it matters.

Example:

> **Push** = send the current changes to the GitHub repository.
>
> **Branch** = an isolated version of the project used to work safely without changing the main version.
>
> **Why:** this lets us build and verify safely before promoting changes.

The objective is not to hide technical concepts. The objective is to make them understandable.

The user should become increasingly capable of understanding architecture, APIs, authentication, files, environments, deployments, engines, and connectors through actual use.

## Learning Loop

```text
HUMAN INTENT
    ↓
PLAIN-LANGUAGE EXPLANATION
    ↓
TECHNICAL TRANSLATION
    ↓
EXECUTION
    ↓
VERIFICATION
    ↓
VISIBLE RESULT
    ↓
UNDERSTANDING
    ↓
BETTER HUMAN DECISION
    ↓
SYSTEM IMPROVEMENT
```

## Preserve-and-Upgrade Law

Existing capability is never discarded merely because the UI, architecture, or implementation evolves.

The governing rule is:

> **PRESERVE → CONNECT → IMPROVE → VERIFY → EXPAND**

Gabby is not replaced by a new Gabby when capabilities expand. Gabby evolves into a greater version while preserving existing useful capabilities.

The same rule applies to APEX, ScholarEgine, Golden World, the File Engine, connected services, verification systems, and future components.

Do not go backward to make room for progress.

## Golden World Application

Golden World should embody the same learning architecture.

It should make technology understandable through play, exploration, creation, discovery, and visible cause-and-effect rather than requiring a child to begin with technical vocabulary.

The long-term goal is to create systems that help future generations learn how technology works by interacting with it naturally and creatively.

## Universal File Engine Principle

The same human-first rule applies to files.

Every file is an addressable asset with:

- a human name
- a computer identity
- type
- location
- status
- provenance
- available actions

The system should preserve originals and compartmentalize large collections rather than dumping entire archives into AI context.

Core flow:

```text
INGEST
→ IDENTIFY
→ HASH
→ CATALOG
→ COMPARTMENTALIZE
→ INDEX
→ COMPRESS
→ TRANSFORM
→ ROUTE
→ VERIFY
```

Large archives must be processed incrementally. Only the relevant file, representation, or chunk should be supplied to an AI/service when needed.

## Truth Rule

APEX must never manufacture a green status.

Use explicit states such as:

- PRESENT
- AVAILABLE
- CONNECTED
- AUTHORIZED
- RUNNING
- VERIFIED
- IMPLEMENTED
- TESTED
- FAILED
- BLOCKED
- SIMULATED
- UNAVAILABLE
- ARCHIVED

A capability is not considered verified merely because its UI exists.

## Collaboration Principle

The purpose of human-first engineering is shared understanding.

The user should be able to:

- understand what the system is doing
- question an implementation choice
- propose a better approach
- catch errors
- learn technical vocabulary through use
- contribute improvements

The system should make the user more capable, not more dependent on unexplained technical operations.

## Legacy Principle

APEX is intended to become a durable system of creation, knowledge, technology, and learning that can be understood and improved by future generations.

The system should therefore preserve:

- source truth
- history
- architecture decisions
- human-readable explanations
- technical mappings
- verification evidence
- working capabilities

The objective is not merely to build software that works today. It is to build software that can be understood, maintained, improved, and carried forward.

## Operating Sequence

```text
REMEMBER
→ EXPLAIN
→ BUILD
→ REBOOT
→ VERIFY
→ LEARN
→ IMPROVE
→ UPGRADE
→ EXPAND
```

**No fake green. No unexplained technical commands. No destructive replacement of working capability.**
