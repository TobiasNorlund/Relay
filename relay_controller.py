import RPi.GPIO as GPIO

RELAY_PINS = [11, 12, 15, 16]

def init():
    GPIO.setup(RELAY_PINS[0], GPIO.OUT)
    GPIO.setup(RELAY_PINS[1], GPIO.OUT)
    GPIO.setup(RELAY_PINS[2], GPIO.OUT)
    GPIO.setup(RELAY_PINS[3], GPIO.OUT)

def reset():
    init()
    GPIO.output(RELAY_PINS[0], False)
    GPIO.output(RELAY_PINS[0], False)
    GPIO.output(RELAY_PINS[0], False)
    GPIO.output(RELAY_PINS[0], False)


def on(relay):
    GPIO.output(RELAY_PINS[relay], True)

def off(relay):
    GPIO.output(RELAY_PINS[relay], False)