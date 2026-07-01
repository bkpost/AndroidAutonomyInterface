# AAI Protocol

AAI initially uses JSON-lines messages over a serial transport.

Each message is a single JSON object followed by a newline.

## Required Message Types

- `HELLO`
- `CONFIG`
- `ARM_REQUEST`
- `ARM_OK`
- `DISARM`
- `COMMAND`
- `ACK`
- `ERROR`
- `WATCHDOG`

The protocol should remain transport-agnostic so it can later support USB serial, Bluetooth, Wi-Fi, or other transports.
