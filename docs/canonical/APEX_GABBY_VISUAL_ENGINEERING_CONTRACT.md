# APEX / GABBY VISUAL ENGINEERING CONTRACT

**Status: CANONICAL IMPLEMENTATION REQUIREMENT**
**Source of truth:** `rahmaanherman-source/Apex-Hub`

## Core law

The UI must preserve the complete intended workspace. Never crop, shorten, delete, or hide primary content simply to make a layout fit.

If a collection is wider than the viewport, the complete collection remains available through horizontal scroll/swipe or an equivalent navigation mechanism. If content is vertically longer than the viewport, vertical scrolling remains usable.

Provide an explicit `WHOLE PICTURE` / `OVERVIEW` control that exposes the complete workspace and allows direct navigation to its regions.

Responsive layouts may reflow, resize, or collapse secondary panels. They may not destructively remove primary content.

## Gabby law

There is exactly ONE Gabby runtime, conversation, voice, command system, and canonical orb. The orb must remain available without obstructing primary work.

## Preservation law

UI upgrades must preserve existing working capabilities: navigation, thumbnails/content collections, editing, animation, audio, capture, export/share, chat, and publish behavior where present in the application.

## Verification law

Never treat a code edit, screenshot, preview, or AI statement as proof of completion.

Required verification loop:

`INSPECT → CHANGE → BUILD → TEST → RUN → INTERACT → VISUAL-CHECK → EVIDENCE → REPORT`

Publish is only successful after the actual deployed runtime can be opened and exercised.

## Exactness

The APEX/Gabby visual reference is an engineering acceptance target, not inspiration. If the implementation differs materially, correct it or document an authorized deviation. Do not silently simplify the design.

For the current exact visual/cartographic contract, consult the canonical files in `rahmaanherman-source/Apex-Hub` before implementation or UI review.