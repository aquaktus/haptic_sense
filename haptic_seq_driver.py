#IMPORTS
import RPi.GPIO as GPIO
import time
import numpy as np

class hapticSeqDriver():
    def __init__(self, char_frequency=4, char_vibration_time=0.3, debug=False):
        #STARTUP
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(27,GPIO.OUT)
        GPIO.setup(22,GPIO.OUT)
        GPIO.setup(18,GPIO.OUT)
        GPIO.setup(23,GPIO.OUT)
        GPIO.setup(24,GPIO.OUT)

        self.char_frequency = char_frequency
        self.char_vibration_time = char_vibration_time
        self.debug = debug

        self.motor_GPIO_ID = [17,27,22,18,23,24]

        self.letter_codes = {
            "a":[1,0,0,0,0,0],
            "b":[1,1,0,0,0,0],
            "c":[1,0,0,1,0,0],
            "d":[1,0,0,1,1,0],
            "e":[1,0,0,0,1,0],
            "f":[1,1,0,1,0,0],
            "g":[1,1,0,1,1,0],
            "h":[1,1,0,0,1,0],
            "i":[0,1,0,1,0,0],
            "j":[0,1,0,1,1,0],
            "k":[1,0,1,0,0,0],
            "l":[1,1,1,0,0,0],
            "m":[1,0,1,1,0,0],
            "n":[1,0,1,1,1,0],
            "o":[1,0,1,0,1,0],
            "p":[1,1,1,1,0,0],
            "q":[1,1,1,1,1,0],
            "r":[1,1,1,0,1,0],
            "s":[0,1,1,1,0,0],
            "t":[0,1,1,1,1,0],
            "u":[1,0,1,0,0,1],
            "v":[1,1,1,0,0,1],
            "w":[1,0,0,1,1,1],
            "x":[1,0,1,1,0,1],
            "y":[1,0,1,1,1,1],
            "z":[1,0,1,0,1,1],
            "#":[0,0,1,1,1,1],
            "1":[1,0,0,0,0,0],
            "2":[1,1,0,0,0,0],
            "3":[1,0,0,1,0,0],
            "4":[1,0,0,1,1,0],
            "5":[1,0,0,0,1,0],
            "6":[1,1,0,1,0,0],
            "7":[1,1,0,1,1,0],
            "8":[1,1,0,0,1,0],
            "9":[0,1,0,1,0,0],
            "0":[0,1,0,1,1,0],
            " ":[0,0,0,0,0,0],
        
        }

    def write_message(self, message="hello world"):
        for char in str(message):
            self.write_char(char)
    
    def write_char(self, char):
        if self.debug:
            print("writing char:", str(char))

        motor_mask = self.letter_codes[char]

        if self.debug:
            print("turning on motors: ", motor_mask)

        motor_num = sum(motor_mask)
        
        for motor_ID, enabled in zip(self.motor_GPIO_ID, motor_mask):
            if enabled:
                GPIO.output(motor_ID,GPIO.HIGH)
                time.sleep(self.char_vibration_time/(self.char_frequency * motor_num))
                GPIO.output(motor_ID,GPIO.LOW)
        
        time.sleep((1 - self.char_vibration_time)/self.char_frequency)
