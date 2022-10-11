#!/usr/bin/env pybricks-micropython

# Pybricks imports
from pybricks import robotics
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

# Robot definitions
ev3 = EV3Brick()

# Motor definitions
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Sensor definitions
left_light = ColorSensor(Port.S3)


# Start following the line endlessly.
while True:
