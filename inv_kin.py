import math

femur_length = 20.0
tibia_length = 19.4859

def stretch_length(y, z):
    return math.sqrt(y**2 + z**2)

def tibia_angle(y, z):
    return math.acos(((femur_length**2 + tibia_length**2) - stretch_length(y, z)**2) / (2 * femur_length * tibia_length)) * (180 / math.pi)

def femur_angle(y, z):
    B = math.acos((stretch_length(y, z)**2 + femur_length**2 - tibia_length**2) / (2 * stretch_length(y, z) * femur_length)) * (180 / math.pi)
    A = math.atan(z / y) * (180 / math.pi)
    return B + A + 90

def get_angles(x, y, z):
    return [x, tibia_angle(y, z), femur_angle(y, z)]
    
#print(get_angles(90, 19.28, 17.5)[0:3])
    

