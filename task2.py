import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(22, GPIO.IN)
GPIO.setup(27, GPIO.OUT)
a = GPIO.input(22)
GPIO.output(27, a)