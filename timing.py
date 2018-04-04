import RoboPiLib as RPL # (robotonomy setup.py)
from setup import RPL # (robotonomy README.md)
import time # (robotonomy post_to_web.py)
RPL.RoboPiInit("/dev/ttyAMA0",115200) # (robotonomy setup.py)

motorL = 1 # (robo-control control.py)
motorR = 0 # (robo-control control.py)

RPL.servoWrite(motorR, 2000) # (robo-control control.py)
RPL.servoWrite(motorL, 1000) # (robo-control control.py)

time.sleep(.500)

RPL.servoWrite(motorR, 2000) # (robo-control control.py)
RPL.servoWrite(motorL, 1000) # (robo-control control.py)

time.sleep(.500)

RPL.servoWrite(motorR, 2000) # (robo-control control.py)
RPL.servoWrite(motorL, 1000) # (robo-control control.py)

time.sleep(.500)
