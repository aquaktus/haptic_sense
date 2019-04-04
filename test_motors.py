#IMPORTS
import RPi.GPIO as GPIO
import time

#STARTUP
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)


#CODE
mi = [17,27,22,18,23,24]
def on(motors,duration = 1,wait=1):
    print("turning on motors: ",motors)
    for i in range(0,6):
        if(motors[i] == 1):
            GPIO.output(mi[i],GPIO.HIGH)
    time.sleep(duration)
    for i in range(0,6):
        if(motors[i] == 1):
            GPIO.output(mi[i],GPIO.LOW)
    time.sleep(wait)    

letter_codes = {
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
        "number":[0,0,1,1,1,1],
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
}


#ITERATE THROUGH MOTORS
#all on progressively
on([1,0,0,0,0,0])
on([1,1,1,0,0,0])
on([1,1,1,1,0,0])
on([1,1,1,1,1,0])
on([1,1,1,1,1,1])


on([0,1,1,1,1,1])
on([1,0,1,1,1,1])
on([1,1,0,1,1,1])
on([1,1,1,0,1,1])
on([1,1,1,1,0,1])
on([1,1,1,1,1,0])

on([0,0,0,0,0,0])

on([1,0,0,0,0,0])
on([0,1,0,0,0,0])
on([0,0,1,0,0,0])
on([0,0,0,1,0,0])
on([0,0,0,0,1,0])
on([0,0,0,0,0,1])

