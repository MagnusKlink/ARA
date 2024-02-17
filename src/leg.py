import inverse_kinematics
import time
from servo import Servos
from easing import *

def smooth(start, end, duration):
    points = []
    a = QuadEaseInOut(start=start, end=end, duration=duration)
    
    for i in range(duration):
        points.append(a.ease(i))
    points.append(end)
    return points

class Leg:
    def __init__(self, pca9685, CoxaServo, FemurServo, TibiaServo, PosOffset):
        self.pca9685 = pca9685
        self.CoxaServo = CoxaServo
        self.FemurServo = FemurServo
        self.TibiaServo = TibiaServo
        self.PosOffset = PosOffset
        self.CurrentAngles = {"coxa": float, "femur": float, "tibia": float}
        self.CurrentPos = {"x": float, "y": float, "z": float}
        
    def move_to_pos(self, x, y, z):
        angles = inverse_kinematics.angles(x, y, z)
        
        Servos(pca9685=self.pca9685).position(index=self.CoxaServo, degrees=angles[0] + self.PosOffset)
        Servos(pca9685=self.pca9685).position(index=self.FemurServo, degrees=angles[1])
        Servos(pca9685=self.pca9685).position(index=self.TibiaServo, degrees=angles[2])
        self.CurrentPos.update({"x": x, "y": y, "z": z})
        self.CurrentAngles.update({"coxa": angles[0] + self.PosOffset, "femur": angles[1], "tibia": angles[2]})
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
    
    def move_smooth(self, x, y, z, t):
        steps = 10
        time_per_step = t / steps
        
        curve_x = smooth(self.CurrentPos["x"], x, steps)
        curve_y = smooth(self.CurrentPos["y"], y, steps)
        curve_z = smooth(self.CurrentPos["z"], z, steps)
        
        for i in range(steps):
            self.move_to_pos(curve_x[i], curve_y[i], curve_z[i])
            time.sleep(time_per_step)
    