import RPi.GPIO as GPIO
import time

class IRSensor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.IN)

    def detect_motion(self):
        return GPIO.input(self.pin) == GPIO.HIGH

    def cleanup(self):
        GPIO.cleanup()
