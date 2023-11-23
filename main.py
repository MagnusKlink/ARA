from leg import Leg
import time

Leg1 = Leg(0, 1, 2)
Leg2 = Leg(3, 4, 5)
Leg3 = Leg(6, 7, 8)
Leg4 = Leg(9, 10, 11)
Leg5 = Leg(12, 13, 99)
Leg6 = Leg(14, 15, 16)

Legs = [Leg1, Leg2, Leg3, Leg4, Leg5, Leg6]
#"Flat" state angles (90, 55, 0)
#"Curled up" state angles (90, 180, 180)
#Possible walking start angles (90, 80, 110)
#Leg1.set_angle(0, 180, 180)
#Leg2.set_angle(90, 180, 180)
#Leg3.set_angle(90, 180, 180)
#Leg4.set_angle(90, 180, 180)
#Leg5.set_angle(90, 180, 180)
#Leg6.set_angle(90, 180, 180)

for leg in Legs:
    leg.set_angle(90, 180, 180)
while True:
    Leg1.ease("coxa", 0)
    Leg1.ease("coxa", 180)
#print(Leg1.CurrentAngles)
