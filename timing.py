import RoboPiLib as RPL # (robotonomy setup.py)
from setup import RPL # (robotonomy README.md)
import time # (robotonomy post_to_web.py)
RPL.RoboPiInit("/dev/ttyAMA0",115200) # (robotonomy setup.py)

motorL = 1 # (robo-control control.py)
motorR = 0 # (robo-control control.py)
t_ime = time.time() # (robotonomy post_to_web.py)
a = 3
b = 6

while True:
    while time.time() < t_ime + a: # (robotonomy post_to_web.py)
        RPL.servoWrite(motorR, 2000) # (robo-control control.py)
        RPL.servoWrite(motorL, 1000) # (robo-control control.py)
    while time.time() > t_ime + a and time.time() < t_ime + b: # (robotonomy post_to_web.py) 
        RPL.servoWrite(motorR, 0) # (robo-control control.py)
        RPL.servoWrite(motorL, 0) # (robo-control control.py)
    while time.time() > t_ime + b: # (robotonomy post_to_web.py)
        a = a + 3
        b = b + 3
