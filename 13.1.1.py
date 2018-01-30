import RoboPiLib as RPL # from setup.py
from setup import RPL # from basic.py
import time
import post_to_web as PTW # from basic.py
RPL.RoboPiInit("/dev/ttyAMA0",115200)# from setup.py

motorL = 1 # motor pin number
motorR = 0 # motor pin number
sensor_pin = 16 # sensor pin number

RPL.servoWrite(motorR, 1000) # turns right motor on
RPL.servoWrite(motorL, 2000) # turns left motor on
RPL.pinMode(sensor_pin,RPL.INPUT)

while RPL.digitalRead(sensor_pin) == 1: # what terminal prints if something is in the way
    PTW.state['d1'] = RPL.digitalRead(sensor_pin) # referring to the 16th pin (the sensor)
    RPL.servoWrite(motorR, 1000) # turns right motor on
    RPL.servoWrite(motorL, 2000) # turns left motor on
    PTW.post()
else:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin) # referring to the 16th pin (the sensor)
    RPL.servoWrite(motorR, 0) # shuts off right motor
    RPL.servoWrite(motorL, 0) # shuts off left motor
    PTW.post()
