from inv_kin import get_angles
from pca import PCA9685
from machine import Pin, I2C
from servo import Servos
import time

sda = Pin(4)
scl = Pin(5)
id = 0

i2c = I2C(sda=sda, scl=scl)

pca = PCA9685(i2c=i2c)
servo = Servos(i2c=i2c)

class Leg:
    def __init__(self, CoxaServo, FemurServo, TibiaServo):
        self.CoxaServo = CoxaServo
        self.FemurServo = FemurServo
        self.TibiaServo = TibiaServo
        self.CurrentAngles = dict.fromkeys(["coxa","femur","tibia"])
        
    def move_to(self, x, y, z):
        servo.position(index=self.CoxaServo, degrees=get_angles(x, y, z)[0])
        servo.position(index=self.FemurServo, degrees=get_angles(x, y, z)[1])
        servo.position(index=self.TibiaServo, degrees=get_angles(x, y, z)[2])
        
    def set_angle(self, coxa, femur, tibia):
        servo.position(index=self.CoxaServo, degrees=coxa)
        self.CurrentAngles["coxa"] = coxa
        servo.position(index=self.FemurServo, degrees=femur)
        self.CurrentAngles["femur"] = femur
        servo.position(index=self.TibiaServo, degrees=tibia)
        self.CurrentAngles["tibia"] = tibia
        return print(f"Setting angles to: {coxa}, {femur} and {tibia}")
    
    def easeInOutQuad(self, t):
        if t < 0.5:
            return 2 * t * t
        return (-2 * t * t) + (4 * t) - 1
    
    def map_value(self, in_v, in_min, in_max, out_min, out_max):
        v = (in_v - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        if v < out_min:
            v = out_min
        elif v > out_max:
            v = out_max
        return v
            
    def ease(self, servo_name, endpos):
        if servo_name == "coxa":
            startpos_coxa = self.CurrentAngles["coxa"]
            for frame in range(startpos_coxa, endpos):
                pos = self.map_value(self.easeInOutQuad(frame / endpos), 0, 1, 0, 180)
                print(pos)
                servo.position(index=self.CoxaServo, degrees=pos)
                time.sleep(0.008)
            self.CurrentAngles["coxa"] = endpos
        if servo_name == "femur":
            startpos_femur = self.CurrentAngles["femur"]
            for frame in range(startpos_femur, endpos):
                pos = self.map_value(self.easeInOutQuad(frame / endpos), 0, 1, 0, 180)
                #print(pos)
                servo.position(index=self.FemurServo, degrees=pos)
            self.CurrentAngles["femur"] = endpos
        if servo_name == "tibia":
            startpos_tibia = self.CurrentAngles["tibia"]
            for frame in range(startpos_tibia, endpos):
                pos = self.map_value(self.easeInOutQuad(frame / endpos), 0, 1, 0, 180)
                #print(pos)
                servo.position(index=self.TibiaServo, degrees=pos)
            self.CurrentAngles["tibia"] = endpos
    