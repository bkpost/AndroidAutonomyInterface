# AAI Safety Model

AAI uses layered safety enforcement.

## Required Conditions Before Motion

1. Valid protocol message
2. Valid hardware configuration
3. Valid vehicle profile mapping
4. Controller armed
5. Command within advertised safety limits
6. Watchdog current

If any condition fails, the controller must reject the command or disarm.

## Initial Testing Rule

The first firmware implementation must run in `NO_MOTION_TEST` mode and log intended actuator outputs rather than driving real actuators.
