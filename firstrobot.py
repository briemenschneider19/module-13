import RoboPiLib as RPL # (robotonomy setup.py)
from setup import RPL # (robotonomy README.md)
RPL.RoboPiInit("/dev/ttyAMA0",115200) # (robotonomy setup.py)

motorL = 1 # (robo-control control.py)
motorR = 0 # (robo-control control.py)
sensor_pin = 16 # (robotonomy basic.py)

RPL.servoWrite(motorR, 2000) # (robo-control control.py)
RPL.servoWrite(motorL, 1000) # (robo-control control.py)
RPL.pinMode(sensor_pin,RPL.INPUT) # (robo-control control.py)

while RPL.digitalRead(sensor_pin) == 1: # (robotonomy basic.py)
    PTW.state['d1'] = RPL.digitalRead(sensor_pin) # (robotonomy basic.py)
    RPL.servoWrite(motorR, 2000) # (robo-control control.py)
    RPL.servoWrite(motorL, 1000) # (robo-control control.py)
else:
    PTW.state['d1'] = RPL.digitalRead(sensor_pin) # (robotonomy basic.py)
    RPL.servoWrite(motorR, 0) # (robo-control control.py)
    RPL.servoWrite(motorL, 0) # (robo-control control.py)
