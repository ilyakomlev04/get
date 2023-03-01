import RPi.GPIO as GPIO
import time

leds = [24, 25, 8, 7, 12, 16, 20, 21]

nofrep = [0, 1, 2]

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
for j in nofrep: 
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)

GPIO.output(leds, 0)

GPIO.cleanup()

