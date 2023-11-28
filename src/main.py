from leg import Leg
from pca import PCA9685
from machine import Pin, I2C
import time

sda = Pin(4)
scl = Pin(5)

i2c = I2C(sda=sda, scl=scl)

pca1 = PCA9685(i2c=i2c, address=0x40)
#pca2 = PCA9685(i2c=i2c, address=0x41)

Leg1 = Leg(pca9685=pca1, CoxaServo=0, FemurServo=1, TibiaServo=2)
Leg2 = Leg(pca1, 3, 4, 5)
Leg3 = Leg(pca1, 6, 7, 8)
Leg4 = Leg(pca1, 9, 10, 11)
Leg5 = Leg(pca1, 12, 13, 99)
Leg6 = Leg(pca1, 14, 15, 16)

Legs = [Leg1, Leg2, Leg3, Leg4, Leg5, Leg6]

Leg1.move_to_pos(20, 0, -10)
#Leg1.set_angle(90, 180, 180)

#for leg in Legs:
 #   leg.set_angle_raw(90, 180, 180)
#time.sleep(2)
#while True:
 #   Leg1.walk_cycle()