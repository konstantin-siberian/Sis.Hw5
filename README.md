# Sis.Hw5

1. Nikita Dayanov and Kostya Turubanov

Video:
https://youtu.be/Q2rxwgBQ4ZQ

2. We constructed a robot. 
We connected 2 ultrasonic sensors, facing opposite lateral directions. We also connected gyroscope.

Data acquired:

-ultrasonic_left.distance_centimeters - distance to the left wall;

-ultrasonic_right.distance_centimeters - distance to the right wall;

gyroscope.angle - angle;

gyroscope.rate - rate;

1000 values;

Kostya chose circle, Nikita - rectangle for the path.

3. We wrote our data in 2 text files and used information to build the graphs, obtained from left and right ultrasonic sensors.

4. Our trajectory guessing: 

Nikita: The trajectory is non-linear and has periodic structure. It has 2 periodic patterns, corresponding to the walls. Since, in our rectangular bathroom 2 walls are further away than the other 2. That means it is a circle - type trajectory. The period is slightly more than 2s. Maxima correspond to the angles of our bathroom. Derivative at minima yields the speed of rotation. The ratio of velocities are 2 to 1.

Kostya: I can observe parallel lines, because left and right data from ultrasonic sensors do not change through large segments of time. I can assume that the robot is moving in rectangular environment with rectangular shape trajectory. From 2 to 3 second, for instance, the sum of sensor data yields aproximately 65 sm, which correspond to my idea of trajectory. During the rotation trajectory changes drastically. It slips through, so some error appears, but the pattern is clear.

5. We applied Kalman filter for data fusing. We modeled our approximation function as simple curve to make the basic correspondence for shapes and robot movement in rectangular arena. 
