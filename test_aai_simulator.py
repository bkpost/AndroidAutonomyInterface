from simulator.fake_arduino import FakeArduino, VERSION


def msg(msg_type, payload=None):
    return {"type": msg_type, "version": VERSION, "payload": payload or {}}


def test_hello_returns_config():
    controller = FakeArduino()
    response = controller.handle(msg("HELLO", {"client": "test"}))
    assert response["type"] == "CONFIG"
    assert response["payload"]["mode"] == "NO_MOTION_TEST"


def test_command_rejected_until_armed():
    controller = FakeArduino()
    response = controller.handle(msg("COMMAND", {"left_throttle": 0, "right_throttle": 0}))
    assert response["type"] == "ERROR"
    assert response["payload"]["code"] == "DISARMED"


def test_arm_then_valid_command_acknowledged():
    controller = FakeArduino()
    assert controller.handle(msg("ARM_REQUEST"))["type"] == "ARM_OK"
    response = controller.handle(msg("COMMAND", {"left_throttle": 0.5, "right_throttle": -0.5}))
    assert response["type"] == "ACK"
    assert response["payload"]["no_motion_test"] is True


def test_limit_exceeded_rejected():
    controller = FakeArduino()
    controller.handle(msg("ARM_REQUEST"))
    response = controller.handle(msg("COMMAND", {"left_throttle": 1.5, "right_throttle": 0}))
    assert response["type"] == "ERROR"
    assert response["payload"]["code"] == "LIMIT_EXCEEDED"


def test_unknown_message_rejected():
    controller = FakeArduino()
    response = controller.handle(msg("LAUNCH_MISSILES"))
    assert response["type"] == "ERROR"
    assert response["payload"]["code"] == "UNKNOWN_MESSAGE"
