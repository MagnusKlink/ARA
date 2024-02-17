# PROJECT ARA

![Six-legged black robot on dark background with red lighting, with text 'ARA'](/graphics/ARA_Title.png)

### About the project:

Hi! Welcome! And thank you for checking out my project!😊

I'm building a hexapod robot from the ground up - which includes sourcing components, modelling and 3D-printing structural pieces, wiring and soldering, and of course writing the code.

It is a *very* ambitious project - and i have many plans / goals / wishes. The very first is naturally to make a robot that is able to walk, which includes inverse kinematics and creating a gait - when that is achived (essentially making a platform in which development can continue), that's when the opportunity for some awesome stuff will arise!🙏🏻🔥

For example:
- Object recognition with artificial intelligence/neural networking
- Autonomous navigation 
- Gesture and/or voice command recognition
- Expressive body language (eg. 'defensive' when someone suddenly approches, 'looking up' when listening to command, etc.)
- Cellular connectivity 
- Regenerative shock absorption 
- Machine vision using 360 degree camera coverage, possibly combined with lidar and/or infrared (think navigation in low light or heat-seeking)
- No "locked" front or back. The robot can change "front" to any point, making it able to switch direction quickly.
- Computer running it's own operating system (probably a flavor of linux)
- High torque / muscle power (can we make it pull a car???)
- Built in wireless charger for phone (When not walking about, it's essentially a big powerbank - useful for something like [BornHack!](https://bornhack.dk/))
- And much, much more!

![Six-legged black robot on blue carpet, with one leg moving from side to side](/graphics/leg_easing.gif)

Do keep in mind that this is the first version of ARA and that it is a work in progress😊

I will try to make everything for the project available, so you can start your own project❤️

If you have any tips or suggestions for improvements, please let me know! It will be much appreciated!

### Components and parts:

| Part or component | Quantity | Description |
| ------------------|----------|-------------|
| MG996R servo      | 18       | Each leg contains 3 servos, 1 for the coxa, 1 for the femur and one for the tibia|
| PCA9685           | 2        | 16-channel PWM servo driver module, for controlling all of the servos through the I2C BUS|
| Wemos ESP8266 D1 Mini | 1    | Microcontroller flashed with MicroPython, for controlling everything.|
| RC Shock absorber | 6        | Shock absorbers for the legs, i found mine through a local RC-supplier.|
| Servo horn        | 18       | Servo horn for attaching the servo gear to their respective component.|
| M3 screw          | Lots!    | I think there is about 108 M3 screws in total (this is a rough estimate though..) |

### Credits:

- [Kevin McAleer](https://github.com/kevinmcaleer) for his MicroPython PCA9685 and Servo code.
- [Zarya / Rudy](https://github.com/zarya) for his help with the battery management and general circuitry.
- [Ryan from Aecert Robotics](https://www.youtube.com/@AecertRobotics) for inspiration.

You're free to use everything here to make your own robot or a variant - but not for commercial use. 