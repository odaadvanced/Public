# 09_05_resistance.py

from PiAnalog import *
import time

p = PiAnalog()

while True:
    print(p.read_resistance())
    time.sleep(1)
