from smooth_servo import SmoothEaseInQuad
import inverse_kinematics
import time
from servo import Servos


class Leg:
    def __init__(self, pca9685, CoxaServo, FemurServo, TibiaServo):
        self.pca9685 = pca9685
        self.CoxaServo = CoxaServo
        self.FemurServo = FemurServo
        self.TibiaServo = TibiaServo
        self.CurrentAngles = {"coxa": float, "femur": float, "tibia": float}
        self.CurrentPos = {"x": float, "y": float, "z": float}
        
    def move_to_pos(self, x, y, z):
        angles = inverse_kinematics.angles(x, y, z)
        self.CurrentPos.update({"x": x, "y": y, "z": z})
        self.CurrentAngles.update({"coxa": angles[0], "femur": angles[1], "tibia": angles[2]})
        
        Servos(pca9685=self.pca9685).position(index=self.CoxaServo, degrees=angles[0])
        Servos(pca9685=self.pca9685).position(index=self.FemurServo, degrees=angles[1])
        Servos(pca9685=self.pca9685).position(index=self.TibiaServo, degrees=angles[2])
        print(self.CurrentPos)
        print(self.CurrentAngles)
        
    def set_angle(self, coxa, femur, tibia):
        Servos(pca9685=self.pca9685).position(index=self.CoxaServo, degrees=coxa)
        self.CurrentAngles["coxa"] = coxa
        Servos(pca9685=self.pca9685).position(index=self.FemurServo, degrees=femur)
        self.CurrentAngles["femur"] = femur
        Servos(pca9685=self.pca9685).position(index=self.TibiaServo, degrees=tibia)
        self.CurrentAngles["tibia"] = tibia
        return print(f"Setting angles to: {coxa}, {femur} and {tibia}")
    
#     def stance(self):
#         self.set_angle(self.CurrentAngles["coxa"], 80, 110)
# 
#     def set_angle_smooth_coxa(self, target):
#         startpoint = self.CurrentAngles["coxa"]
#         endpoint = target
#         time_ms = 1000
#         tick_time_ms = 50
#         InOutQuad = SmoothEaseInQuad(endpoint, time_ms, startpoint)
#         iterator = InOutQuad.generate(tick_time_ms)
#         for i in iterator:
#             servo.position(index=self.CoxaServo, degrees=i)
#     def set_angle_smooth_femur(self, target):
#         startpoint = self.CurrentAngles["femur"]
#         endpoint = target
#         time_ms = 1000
#         tick_time_ms = 50
#         InOutQuad = SmoothEaseInQuad(endpoint, time_ms, startpoint)
#         iterator = InOutQuad.generate(tick_time_ms)
#         for i in iterator:
#             servo.position(index=self.FemurServo, degrees=i)
#             
#     def set_angle_smooth_tibia(self, target):
#         startpoint = self.CurrentAngles["tibia"]
#         endpoint = target
#         time_ms = 1000
#         tick_time_ms = 50
#         InOutQuad = SmoothEaseInQuad(endpoint, time_ms, startpoint)
#         iterator = InOutQuad.generate(tick_time_ms)
#         for i in iterator:
#             servo.position(index=self.TibiaServo, degrees=i)
# 
#     def set_angles(self, coxa, femur, tibia):
#         self.set_angle_smooth_coxa(coxa)
#         self.set_angle_smooth_femur(femur)
#         self.set_angle_smooth_tibia(tibia)
#         
#     def walk_cycle(self):
#         #Initialize:
#         self.set_angles(0.1, 80, 110)
#         time.sleep(0.1)
#         #Lift
#         self.set_angles(0.1, 110, 110)
#         time.sleep(0.5)
#         #Swing
#         self.set_angles(180, 110, 110)
#         time.sleep(1)
#         #Stomp
#         self.set_angles(180, 80, 110)
#         time.sleep(0.5)
#         #Push
#         self.set_angles(0.1, 80, 110)
#         time.sleep(1)