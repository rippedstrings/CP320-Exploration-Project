import RPi.GPIO as GPIO
import time

HALF_BIT_TIME = 0.001
CHARACTER_DELAY = 5 * HALF_BIT_TIME
NUM_BITS = 16

class Keypad():

    def __init__(self, pin_scl, pin_sdo, pin_mode=GPIO.BCM):
        self.pin_scl = pin_scl
        self.pin_sdo = pin_sdo

        GPIO.setmode(pin_mode)
        GPIO.setup(pin_scl, GPIO.OUT)
        GPIO.setup(pin_sdo, GPIO.IN)

        GPIO.output(pin_scl, GPIO.HIGH)
        time.sleep(HALF_BIT_TIME)


    def getKeyPressed(self):
        pressed = False
        button = 0
        time.sleep(CHARACTER_DELAY)
        while not pressed and button < 17:
            GPIO.output(self.pin_scl, GPIO.LOW)
            time.sleep(HALF_BIT_TIME)
            keyval = GPIO.input(self.pin_sdo)
            if not keyval:
                pressed = True
            GPIO.output(self.pin_scl, GPIO.HIGH)
            button += 1
        if not pressed:
            button = None
        return button

    def getNextKey(self):
        button = None
        while button is None:
            button = self.getKeyPressed()
        while self.getKeyPressed() is not None:
            pass 
        return button
