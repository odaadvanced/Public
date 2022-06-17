#!/usr/bin/python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
import asyncio
from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
from sphero_sdk import DriveControlAsync

import RPi.GPIO as GPIO
import time
loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
    )
)
async def collect():
    channel = 7
    data = []
    GPIO.setmode(GPIO.BOARD)
    time.sleep(2)
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(0.02)
    GPIO.output(channel, GPIO.HIGH)
    GPIO.setup(channel, GPIO.IN)
    while GPIO.input(channel) == GPIO.LOW:
        continue
    while GPIO.input(channel) == GPIO.HIGH:
        continue
    j = 0
    while j < 40:
        k = 0
        while GPIO.input(channel) == GPIO.LOW:
            continue
        while GPIO.input(channel) == GPIO.HIGH:
            k += 1
            if k > 100:
                break
        if k < 8:
            data.append(0)
        else:
            data.append(1)
        j += 1

    # print("sensor is working.")
    # print(data)
    humidity_bit = data[0:8]
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]
    humidity = 0
    humidity_point = 0
    temperature = 0
    temperature_point = 0
    check = 0
    for i in range(8):
        humidity += humidity_bit[i] * 2 ** (7 - i)
        humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
        temperature += temperature_bit[i] * 2 ** (7 - i)
        temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
        check += check_bit[i] * 2 ** (7 - i)
    tmp = humidity + humidity_point + temperature + temperature_point
    if check == tmp:
        global THdata
        THdata = []
        THdata.append(temperature + temperature_point / 10)
        THdata.append(humidity)
        return 
    else:
        # print("wrong")
#        time.sleep(.1)
        return await action()

THdata = [0, 0]
async def action():

    temperature = THdata[0] * 9/5 + 32
    print (f"temperature {temperature} F   humidity :  {THdata[1]} %")
    await rvr.wake()
    rvr_speed = 8
    if temperature > 90:
        rvr_direction = 1
    else:
        rvr_direction = 0
        
    
    await rvr.drive_with_heading(
        speed=rvr_speed,  # Valid speed values are 0-255
        heading=0,  # Valid heading values are 0-359
        flags=rvr_direction
    )
    await asyncio.sleep(2)
    await collect()
    return await action()

async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(.5)


if __name__ == '__main__':
    try:
        loop.run_until_complete(
            asyncio.gather(
                main(),
                collect(),               
                action()
            )
        )
    except KeyboardInterrupt:
        print('Program ended by KeyboardInterrupt')
        GPIO.cleanup()
        loop.run_until_complete(
            rvr.close()
        )

    finally:
        if loop.is_running():
            loop.close()