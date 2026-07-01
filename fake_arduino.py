"""Software-only fake Arduino for the Android Autonomy Interface."""

import json
import sys
import time
from dataclasses import dataclass, field

VERSION = "0.1.0"
WATCHDOG_SECONDS = 0.5


@dataclass
class FakeArduino:
    armed: bool = False
    last_command_time: float = field(default_factory=time.monotonic)

    def config(self):
        return {
            "type": "CONFIG",
            "version": VERSION,
            "payload": {
                "controller": "fake_arduino",
                "mode": "NO_MOTION_TEST",
                "channels": [
                    {"name": "left_throttle", "kind": "normalized", "min": -1.0, "max": 1.0},
                    {"name": "right_throttle", "kind": "normalized", "min": -1.0, "max": 1.0},
                ],
                "watchdog_ms": int(WATCHDOG_SECONDS * 1000),
            },
        }

    def error(self, code, detail):
        return {"type": "ERROR", "version": VERSION, "payload": {"code": code, "detail": detail}}

    def handle(self, message):
        msg_type = message.get("type")
        if message.get("version") != VERSION:
            return self.error("VERSION_MISMATCH", "Unsupported protocol version")

        if msg_type == "HELLO":
            return self.config()

        if msg_type == "ARM_REQUEST":
            self.armed = True
            self.last_command_time = time.monotonic()
            return {"type": "ARM_OK", "version": VERSION, "payload": {"armed": True}}

        if msg_type == "DISARM":
            self.armed = False
            return {"type": "ACK", "version": VERSION, "payload": {"armed": False}}

        if msg_type == "COMMAND":
            if not self.armed:
                return self.error("DISARMED", "Command rejected because controller is not armed")
            payload = message.get("payload", {})
            left = payload.get("left_throttle")
            right = payload.get("right_throttle")
            if not isinstance(left, (int, float)) or not isinstance(right, (int, float)):
                return self.error("BAD_COMMAND", "Command requires numeric left_throttle and right_throttle")
            if not (-1.0 <= left <= 1.0 and -1.0 <= right <= 1.0):
                return self.error("LIMIT_EXCEEDED", "Command exceeds normalized throttle limits")
            self.last_command_time = time.monotonic()
            return {"type": "ACK", "version": VERSION, "payload": {"no_motion_test": True, "left_throttle": left, "right_throttle": right}}

        return self.error("UNKNOWN_MESSAGE", f"Unsupported message type: {msg_type}")


def main():
    controller = FakeArduino()
    for line in sys.stdin:
        try:
            message = json.loads(line)
            response = controller.handle(message)
        except json.JSONDecodeError:
            response = controller.error("MALFORMED_JSON", "Input was not valid JSON")
        print(json.dumps(response), flush=True)


if __name__ == "__main__":
    main()
