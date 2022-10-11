# Ericsson Workshop
This document describes the workshop that was planned for a Ericsson "Black Box"-event held in the end of October. The goal of the workshop is to entertain Ericsson developers with non-work related work (UwU).

## Main objective
In the main objective the group of software developers are supposed to implement a line-follow function that is run on a EV3 Lego robot running py-bricks. 

Here is a link to the intended solution: https://pybricks.com/ev3-micropython/examples/robot_educator_line.html

If there is any time left after the group has been able to implement line-following there are extra challanges listed below.

## Single group Challenges
These challanges are intended to be performed by a single group.

### Parking (Easy)
Follows the line until it finds a parking spot. Shall then park in the space.

### Racing (Easy)
Try to get the fastest lap time on a part of the course! By tuning the robot, try to get the fastest laptime of the day. Any collisions with the track is a half a secound penalty. "Lights out and away you go!". 

### Avoid colors (Medium)
Follows a predefined color and avoids all others which may come in the way.

## Multiple group Challenges
In the multiple group challanges it is intended to create a network between different robots. The tasks focuses on syncronization between robots.

### Take requests (Medium)
One robot acts as the controller, when you press a button on it, the other robot should do a predefined action like spinning.

### Synchronized dancing (Hard)
In this challenge, we want two groups to collaborate and create a network of two robots. One robot should act as a server and the other one as a consumer. The server shall send dance commands to the consumer and the aim is for the two robots to "dance" in synchronization. The connection between the robots can be poor, so it is important that the server only moves if it knows that the consumer also is going to move.
