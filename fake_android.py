"""Simple fake Android client for exercising the AAI simulator."""

import json
from simulator.fake_arduino import FakeArduino, VERSION


def run_demo():
    controller = FakeArduino()
    sequence = [
        {"type": "HELLO", "version": VERSION, "payload": {"client": "fake_android"}},
        {"type": "ARM_REQUEST", "version": VERSION, "payload": {}},
        {"type": "COMMAND", "version": VERSION, "payload": {"left_throttle": 0.25, "right_throttle": 0.25}},
        {"type": "DISARM", "version": VERSION, "payload": {}},
    ]
    for message in sequence:
        print("TX", json.dumps(message))
        print("RX", json.dumps(controller.handle(message)))


if __name__ == "__main__":
    run_demo()
