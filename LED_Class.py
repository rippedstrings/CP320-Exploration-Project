import RPi.GPIO as GPIO

class RG_LED():

    def __init__(self, pin_red, pin_green, pwm_freq=60, pin_mode=GPIO.BCM):
        GPIO.setmode(pin_mode)
        GPIO.setup(pin_red, GPIO.OUT)
        GPIO.setup(pin_green, GPIO.OUT)


        self.red_pwm = GPIO.PWM(pin_red, pwm_freq)
        self.green_pwm = GPIO.PWM(pin_green, pwm_freq)

        self.red_pwm.start(0)
        self.green_pwm.start(0)


    def setRed(self, brightness=100):
        self.red_pwm.ChangeDutyCycle(brightness)

    def onRed(self):
        self.red_pwm.ChangeDutyCycle(100)


    def offRed(self):
        self.red_pwm.ChangeDutyCycle(0)


    def setGreen(self, brightness=100):
        self.green_pwm.ChangeDutyCycle(brightness)


    def onGreen(self):
        self.green_pwm.ChangeDutyCycle(100)


    def offGreen(self):
        self.green_pwm.ChangeDutyCycle(0)


    def allOff(self):
        self.red_pwm.ChangeDutyCycle(0)
        self.green_pwm.ChangeDutyCycle(0)


    def stop(self):
        self.red_pwm.stop()
        self.green_pwm.stop()
