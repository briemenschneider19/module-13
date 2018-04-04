import RoboPiLib as RPL # (robotonomy setup.py)
from setup import RPL # (robotonomy README.md)
import time # (robotonomy post_to_web.py)
import post_to_web as PTW # (robotonomy basic.py)
RPL.RoboPiInit("/dev/ttyAMA0",115200) # (robotonomy setup.py)

motorL = 1 # (robo-control control.py)
motorR = 0 # (robo-control control.py)
t_ime = time.time() # (robotonomy post_to_web.py)
i = 3
e = 6

while True:
    while time.time() < t_ime + i: # (robotonomy post_to_web.py)
        RPL.servoWrite(motorR, 1000) # (robo-control control.py)
        RPL.servoWrite(motorL, 2000) # (robo-control control.py)
    while time.time() > t_ime + i and time.time() < t_ime + e: # (robotonomy post_to_web.py) 
        RPL.servoWrite(motorR, 0) # (robo-control control.py)
        RPL.servoWrite(motorL, 0) # (robo-control control.py)
    while time.time() > t_ime + e: # (robotonomy post_to_web.py)
        i = i + 3
        e = e + 3
