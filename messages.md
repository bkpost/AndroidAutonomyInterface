# AAI Messages

## HELLO

Sent by Android to begin a session.

```json
{"type":"HELLO","version":"0.1.0","id":"msg-001","payload":{"client":"android"}}
```

## CONFIG

Sent by embedded controller to advertise hardware and limits.

```json
{"type":"CONFIG","version":"0.1.0","id":"msg-002","payload":{"controller":"arduino","mode":"NO_MOTION_TEST","channels":[{"name":"left_throttle","kind":"pwm","min":1000,"max":2000},{"name":"right_throttle","kind":"pwm","min":1000,"max":2000}],"watchdog_ms":500}}
```

## ARM_REQUEST

Sent by Android after validating configuration.

## ARM_OK

Sent by controller when armed.

## COMMAND

Sent by Android to command vehicle output through normalized values.

## ERROR

Sent when a message is malformed, invalid, unsafe, or not allowed in the current state.
