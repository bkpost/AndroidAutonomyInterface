# AAI Architecture

## Conceptual Layers

1. Android autonomy layer
2. AAI protocol layer
3. Embedded controller layer
4. Hardware I/O layer
5. Vehicle-specific actuators and sensors

## Connection Flow

1. Android connects to embedded controller.
2. Android sends `HELLO`.
3. Controller replies with hardware configuration and safety limits.
4. Android maps configuration into a vehicle profile.
5. Android requests arming.
6. Controller only accepts commands while armed and within limits.
