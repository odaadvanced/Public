#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

TiltPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Watching TiltPin (BCM 17). Press Ctrl+C to exit.")

try:
    while True:
        val = GPIO.input(TiltPin)
        print("TiltPin =", val)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()