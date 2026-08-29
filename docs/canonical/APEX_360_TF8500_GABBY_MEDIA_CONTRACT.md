# APEX 360 + TF8500 + Gabby Media Contract

**Status:** Canonical hardware/media integration specification
**Date:** 2026-08-29

## Hardware identity

- Hardware identified by the operator as: **TF8500 V3.0 booth motor remote**.
- Reported control path: **IR/RF to the booth; not Bluetooth**.
- Treat the remote/control path as hardware-specific. Do not claim Bluetooth control without evidence.

## Required media relationship

The booth experience must keep these surfaces synchronized where the underlying hardware/software supports it:

1. **Booth wrap / physical rotation**
2. **Video capture/playback representation**
3. **True 360 look-around media**
4. **Gabby contextual state**

A true 360 source must remain a true 360 source. Do not flatten, crop, or fake a 360 interaction merely to fit a viewport.

## One-Gabby rule

There is **ONE Gabby runtime**. Booth controls, video, 360 viewing, voice, and contextual guidance are surfaces/capabilities of the same Gabby system, not duplicate assistants.

## Synchronization contract

When a booth capture/session has a supported rotation or motion signal, the application should preserve the relationship between the motion/capture state and the resulting media metadata. If live synchronization is not technically available, the system must state that limitation rather than simulate synchronization.

## No-Fake-Green verification

Hardware identification, protocol, live motor control, capture synchronization, and 360 rendering are separate claims. Each requires its own evidence. Required progression:

`IDENTIFIED → CONNECTED → COMMAND RECEIVED → HARDWARE RESPONDS → MEDIA CAPTURED → 360 VALIDATED → SYNC VERIFIED`

Do not promote any step based only on documentation, UI presence, or an AI assertion.

## UI requirement

360 media must remain discoverable and navigable on desktop and mobile. Users must be able to drag/swipe through the available 360 view without the interface hiding the source content. Whole Picture and horizontal navigation rules continue to apply.
