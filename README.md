# Android Autonomy Interface

AAI is an open, vehicle-agnostic interface standard for Android-based autonomy.

The goal is to create a plug-and-play interface between Android devices and embedded vehicle controllers, enabling hardware discovery, safety-limit negotiation, configuration, and control across ground, maritime, and aerial platforms.

## Core Concept

AAI separates autonomy from vehicle hardware.

An Android device provides autonomy, navigation, perception, user interface, and mission logic.

An embedded controller provides hardware access, actuator control, sensor interfaces, and safety enforcement.

On connection, the embedded controller advertises its hardware configuration and safety limits. Android maps that configuration into a vehicle profile and only sends commands that comply with the advertised limits.

## Initial Goals

- Define the AAI protocol.
- Build a software simulator.
- Build Arduino-compatible reference firmware.
- Build an Android Kotlin client.
- Validate all behavior in simulation before hardware testing.

## Repository Structure

- `docs/` — project vision, architecture, protocol, and safety documentation
- `specs/` — formal AAI specification documents
- `protocol/` — schemas and message definitions
- `android/` — Android client implementation
- `firmware/` — embedded controller reference firmware
- `simulator/` — software-only test simulator
- `tests/` — automated validation tests
- `examples/` — example vehicle configurations

## Safety Principle

No physical actuator output should occur unless the command has passed protocol validation, safety-limit validation, and arming-state validation.
