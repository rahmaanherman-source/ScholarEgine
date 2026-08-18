# APEX Elevation Standard

## Purpose

This is the cross-APEX UI/UX and engineering quality law for APEX Terminal, APEX Heritage, Golden World, ScholarEgine, and future APEX products.

## Core Law

**PRESERVE → UNDERSTAND → UPGRADE → VERIFY → EXPAND**

We do not get rid of what works merely because the interface changes.

- Working capability stays.
- Weak capability is elevated.
- Broken capability is fixed.
- Missing capability is built.
- Obsolete capability is replaced only by a verified better version.
- Verification is evidence-based.

## APEX Quality Standard

Every product should feel:

- premium
- intentional
- powerful
- clean
- accessible
- responsive
- modular
- connected
- verifiable
- professional

Do not ship generic dashboard styling, random cards, decorative controls, fake functionality, fake green status, or low-effort substitutes merely to claim completion.

## Screen/Grid Law

The interface is one engineered surface, not a pile of independently positioned panels.

Use a canonical layout grid with shared:

- margins
- columns
- gutters
- spacing scale
- panel geometry
- border system
- corner radius system
- typography hierarchy
- icon sizing
- interaction states

**EVERY BORDER SHOULD LINE UP. EVERY PANEL SHOULD BELONG TO THE GRID.**

Use reusable layout primitives rather than hand-positioning each panel.

## Sidebar Standard

Sidebars are core navigation, not expendable decoration.

Desktop: full sidebar.

Tablet: intelligent collapse.

Mobile: compact rail/drawer.

Collapsing preserves navigation through icons and restores the full navigation when expanded. Core functionality must not disappear solely because the viewport changed.

Provide accessible collapse/expand controls, active states, hover states, focus states, tooltips when collapsed, and keyboard navigation.

## Panel Standard

Panels are functional layers.

Appropriate panels support:

- EXPAND
- COLLAPSE

Collapse means reducing visual footprint, not deleting data or state.

Use one consistent icon language across the product.

## Progressive Disclosure

Not every capability must be visible simultaneously, but important capabilities must remain easy to find.

Use tabs, rails, drawers, overlays, contextual menus, tooltips, and Focus Mode to manage complexity without hiding core functions unnecessarily.

## Focus Mode

Focus Mode reduces secondary visual noise while preserving:

- active task
- active workspace
- primary controls
- critical status
- explicit exit control

Exiting Focus Mode restores the previous layout.

## Layered UI Architecture

Every major UI layer should have:

- Human name
- Technical name
- Purpose
- State
- Actions
- Inputs
- Outputs
- Dependencies
- Verification

This supports human-first learning while maintaining precise technical implementation.

## Human-First Development

For important technical actions, show:

1. What the human asked for.
2. What the technical term means.
3. What the system is changing.
4. Where it lives.
5. What it connects to.
6. How it is tested.
7. How it is verified.

The system should teach technical language through real work rather than requiring technical fluency in advance.

## Product Separation

APEX Terminal and APEX Heritage are related but distinct products.

**APEX Terminal:** private engineering command center for creating, connecting, building, running, testing, verifying, deploying, and publishing APEX products.

**APEX Heritage:** public-facing heritage, history, culture, learning, community, and Time Capsule platform.

They share APEX principles but do not need identical visual identities or navigation.

## Universal Truth Standard

**NO FAKE GREEN.**

Allowed truth states include:

- PRESENT
- AVAILABLE
- AUTHORIZED
- CONNECTED
- HEALTHY
- EXECUTABLE
- RUNNING
- ADDED
- IMPLEMENTED
- TESTED
- VERIFIED
- BLOCKED
- MISSING
- FAILED
- UNAVAILABLE
- SIMULATED

Only show VERIFIED when evidence exists.

UI existence does not equal verification.

## Functional Control Standard

Every button must have a meaningful action or truthful unavailable state.

Every tab must navigate or switch a real view.

Every toggle must change a real state.

Every status must represent real state.

If a feature is unavailable, report why.

If simulated, label it DEMO/SIMULATED.

## Preserve-and-Upgrade Rule

When changing an existing screen:

1. Inspect what exists.
2. Identify what works.
3. Identify what is weak.
4. Preserve working functionality.
5. Upgrade the visual and interaction system.
6. Add requested capabilities.
7. Test the result.
8. Compare with the previous behavior.
9. Verify that important capability was not lost.
10. Only then mark the upgrade complete.

Before removing anything ask:

> **CAN THIS BE UPGRADED?**

If yes, upgrade it.

Before replacing anything ask:

> **IS THE NEW VERSION ACTUALLY BETTER?**

If not, do not replace it.

## Responsive Standard

Desktop: full command center.

Tablet: intelligent compression and collapsible navigation.

Mobile: purposeful reflow and compact controls.

Do not create accidental horizontal overflow, cut off actions, or squeeze the desktop interface into an unusable mobile layout.

## Accessibility Standard

Interactive elements must support:

- semantic HTML
- keyboard navigation
- visible focus
- accessible labels
- logical tab order
- useful tooltips where needed
- sufficient contrast

## Security Standard

Never expose API keys, tokens, passwords, private keys, PEM files, or service credentials in UI or frontend source.

Never store secrets in localStorage.

Never log secrets.

## Final Quality Gate

Before declaring an interface complete, verify:

- existing functionality preserved
- sidebar works
- sidebar collapses and expands
- panels collapse and expand
- Workspace Manager works where applicable
- Focus Mode works where applicable
- responsive behavior works
- buttons and tabs work
- keyboard navigation works
- borders align
- grid aligns
- typography and spacing are consistent
- no accidental overflow
- no secrets are exposed
- no fake status is displayed
- build passes where supported
- tests pass where supported
- verification produces evidence

## Final Command

**BUILD WITH EXCELLENCE.**

Preserve what exists.
Connect what is disconnected.
Improve what exists.
Add what is missing.
Verify what is claimed.
Teach the human while building.
Never lower the standard.

**DO NOT BUILD DOWN. BUILD UP.**
