import time
import RPi.GPIO as GPIO
from LED_Class import RG_LED
from Keypad_Class import Keypad

# Password Constants
PASSWORD_BANK = ["91723","5678","10111213","109312"]
PASSWORD_LENGTH = 4

# LED Constants
RED_PIN = 23
GREEN_PIN = 24

# Keypad Constants
SCL_PIN = 21
SDO_PIN = 20

led = RG_LED(RED_PIN, GREEN_PIN)
keypad = Keypad(SCL_PIN, SDO_PIN)

try:
    end_program = False

    while end_program == False:
        # Reset Password Input
        curr_pass_length = 0
        input_password = ""
        
        print("Enter pass: ")

        # Get Input From Keypad
        while curr_pass_length != PASSWORD_LENGTH:
            input_num = keypad.getNextKey();
            curr_pass_length += 1
            input_password += str(input_num)
            print("Keys entered: {}".format(keypad.getNextKey()))
            
        print("Your Password: {}".format(input_password))

        led.allOff()
        
        if input_password in PASSWORD_BANK:
            led.onGreen()
            print("Password is correct!")
            time.sleep(3)
            end_program = True
        else:
            led.onRed()
            print("Password is incorrect! Please try again.")
            time.sleep(3)

except Exception as e:
    pass

finally:
    led.stop()
    GPIO.cleanup()
    print("Closed Succesfully")
