# app/controller.py

import time

try:
    import RPi.GPIO as GPIO
except ImportError:
    # For development/testing without Raspberry Pi
    from unittest import mock
    GPIO = mock.MagicMock()

from app.config import GATE_SERVO_PIN, GATE_OPEN_TIME


class GateController:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GATE_SERVO_PIN, GPIO.OUT)
        self.servo = GPIO.PWM(GATE_SERVO_PIN, 50)  # 50Hz PWM frequency
        self.servo.start(0)

    def _set_angle(self, angle):
        duty = angle / 18 + 2
        GPIO.output(GATE_SERVO_PIN, True)
        self.servo.ChangeDutyCycle(duty)
        time.sleep(0.5)
        GPIO.output(GATE_SERVO_PIN, False)
        self.servo.ChangeDutyCycle(0)

    def open_gate(self):
        print("Opening gate...")
        self._set_angle(90)  # open position
        time.sleep(GATE_OPEN_TIME)
        self.close_gate()

    def close_gate(self):
        print("Closing gate...")
        self._set_angle(0)  # closed position

    def cleanup(self):
        self.servo.stop()
        GPIO.cleanup()
