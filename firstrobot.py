import RoboPiLib as RPL
from setup import RPL
import time
RPL.RoboPiInit("/dev/ttyAMA0",115200)

motorL = 1
motorR = 0
sensor_pin = 16

RPL.servoWrite(motorR, 2000)
RPL.servoWrite(motorL, 1000)
RPL.pinMode(sensor_pin,RPL.INPUT)

while RPL.digitalRead(sensor_pin) == 1:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin)
    RPL.servoWrite(motorR, 2000)
    RPL.servoWrite(motorL, 1000)
else:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin)
    RPL.servoWrite(motorR, 0)
    RPL.servoWrite(motorL, 0)
