# APEX 360 Media Interaction Contract

Status: CANONICAL UX REQUIREMENT

When an asset is a true 360° photograph or equirectangular panorama, the UI should present it as an interactive 360° viewer when technically supported—not flatten it into a cropped static thumbnail.

## Required behavior

- Preserve the complete source image/data.
- Allow drag/swipe left and right to rotate the 360° view.
- Support mouse/touch interaction where supported.
- Keep full-resolution/source media separate from thumbnails/previews.
- On narrow screens, reflow or navigate; never hide meaningful panorama content merely to fit.
- Do not label an ordinary photograph as 360° unless it actually contains 360° panoramic data.
- 360° media must not create a duplicate Gabby instance or obstruct primary controls.

## Acceptance

1. Source type is identified.
2. True 360° assets enter 360 viewer mode.
3. Horizontal drag/swipe rotates the view.
4. Desktop/mobile interaction is tested where supported.
5. No meaningful source content is silently discarded.
6. Runtime evidence exists before reporting completion.

Verification chain: `SOURCE TYPE → VIEWER MODE → INTERACTION TEST → RESPONSIVE TEST → VISUAL CHECK → EVIDENCE`.
