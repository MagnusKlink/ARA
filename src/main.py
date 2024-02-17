from leg import Leg
import time
import config

Leg1 = Leg(config.pca1, 4, 5, 6, 60)
Leg2 = Leg(config.pca1, 0, 1, 2, 0)
Leg3 = Leg(config.pca1, 8, 9, 10, -60)
Leg4 = Leg(config.pca2, 0, 1, 2, -60)
Leg5 = Leg(config.pca2, 4, 5, 6, 0)
Leg6 = Leg(config.pca2, 8, 9, 10, 60)

Legs = [Leg1, Leg2, Leg3, Leg4, Leg5, Leg6]

#Leg1.move_to_pos(20, 20, 0)
#print(gyro.read())
#Leg6.move_to_pos(20, 0, -10)
#Leg5.set_angle(90, 180, 180)
#Leg1.set_angle_smooth("tibia", 1)

for leg in Legs:
    leg.move_to_pos(20, 0, 0)
    time.sleep(0.5)
#while True:
 #   print(gyro.read())
  #  time.sleep(2)


#while True:   
   # Leg2.move_smooth(20, -20, 0, 0.5)
   # time.sleep(0.5)
   # Leg2.move_smooth(20, 20, 0, 0.5)
   # time.sleep(0.5)
Leg1.move_smooth(20, -20, 0, 0.5)