#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

LedPin = 17 # Set GPIO17 as LED pin
BtnPin = 18 # Set GPIO18 as button pin


Led_status = True # Set Led status to True(OFF)

# Define a setup function for some setup
def setup():
	# Set the GPIO modes to BCM Numbering
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LedPin, GPIO.OUT, initial=GPIO.HIGH)  # Set LedPin's mode to output, and initial level to high (3.3v)
	GPIO.setup(BtnPin, GPIO.IN) # Set BtnPin's mode to input.
	GPIO.output(LedPin, 0)
	print('setup')
	time.sleep(3)

# Define a callback function for button callback
def swLed(ev=None):
	global Led_status
	# Switch led status(on-->off; off-->on)
	#Led_status = not Led_status
	Led_status = GPIO.input(BtnPin)
	GPIO.output(LedPin, Led_status)
	print ('Led_status ' + str(not Led_status))



# Define a main function for main process
def main():
	# Set up a falling detect on BtnPin, 
	# and callback function to swLed
#	GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=swLed)
	while True:
		# Don't do anything.
		swLed()
		time.sleep(.01)

# Define a destroy function for clean up everything after
# the script finished 
def destroy():
	# Turn off LED
	GPIO.output(LedPin, GPIO.HIGH)
	# Release resource
	GPIO.cleanup()

# If run this script directly, do:
if __name__ == '__main__':
	setup()
	try:
		main()
	# When 'Ctrl+C' is pressed, the program 
	# destroy() will be  executed.
	except KeyboardInterrupt:
		destroy()
