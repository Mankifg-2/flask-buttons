#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LedPins = [17,27]
Ledtoggle = []

def setup():
    for i in range(len(LedPins)):
        Ledtoggle.append(False)

    GPIO.setmode(GPIO.BCM)
    for led in LedPins:
        GPIO.setup(led, GPIO.OUT, initial=GPIO.HIGH)

def toggle(i):
    if Ledtoggle[i]:
        off(i)
        Ledtoggle[i] = False
    else:
        on(i)
        Ledtoggle[i] = True




def on(i):
    GPIO.output(LedPins[i], GPIO.LOW)
def off(i):
    GPIO.output(LedPins[i], GPIO.HIGH)


def destroy():
    for led in LedPins:
        GPIO.output(led, GPIO.HIGH)
    GPIO.cleanup()                   

''' 
if __name__ == '__main__':
    setup()
    try:
        main()
    except KeyboardInterrupt:
        destroy()'''