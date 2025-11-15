#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

TiltPin = 17
Gpin   = 27
Rpin   = 22

def setup():
	GPIO.setmode(GPIO.BCM)       # Numbers GPIOs by physical location
	GPIO.setup(Gpin, GPIO.OUT)     # Set Green Led Pin mode to output
	GPIO.setup(Rpin, GPIO.OUT)     # Set Red Led Pin mode to output

def Led(x):
	if x == 1:
		GPIO.output(Rpin, 1)
		GPIO.output(Gpin, 0)
	if x == 0:
		GPIO.output(Rpin, 0)
		GPIO.output(Gpin, 1)

TiltPin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TiltPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Watching TiltPin (BCM 17). Press Ctrl+C to exit.")

setup()

try:
    while True:
        val = GPIO.input(TiltPin)
        Led(val)
        print("TiltPin =", val)
        time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
    

