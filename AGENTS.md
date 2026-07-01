# AAI Project Instructions

This repository defines and implements the Android Autonomy Interface (AAI).

AAI is a vehicle-agnostic interface between Android-based autonomy software and embedded vehicle controllers.

## Core Rules

1. Safety before motion.
2. No actuator output may bypass validation.
3. Arduino-class controllers advertise hardware configuration and safety limits.
4. Android maps hardware configuration into a vehicle profile.
5. All protocol behavior must be testable in simulation before hardware.

## Initial Validation Gates

- HELLO / CONFIG handshake
- ARM / DISARM state machine
- watchdog timeout
- malformed packet rejection
- command limit enforcement
- simulator integration test

## Initial Hardware Mode

Firmware must default to `NO_MOTION_TEST` mode.
Actuator outputs should log intended behavior before driving physical pins.

## Implementation Guidance

- Prefer clear, readable code over clever code.
- Keep protocol definitions versioned.
- Every new behavior should have a simulator test.
- Do not add physical hardware output unless it is protected by protocol validation, safety-limit validation, and arming-state validation.
