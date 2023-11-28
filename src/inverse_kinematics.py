import math

def angles(x, y, z):
    lcoxa = 7.55  # Coxa length
    lfemur = 20.009  # Femur length
    ltibia = 22.7391  # Tibia length

    # Calculate coxa rotation and handle divide by zero error:
    theta1 = math.atan(x and y / x or 0)
    r1 = math.sqrt(x**2 + y**2) - lcoxa
    r2 = z
    r3 = math.sqrt(r1**2 + r2**2)
    
    # Check if the hypotenuse is longer than combined length of femur and tibia:
    if r3 > lfemur + ltibia:
        raise Exception("Distance too great!") 
    
    fi2 = math.atan(r2/r1)
    fi1 = math.acos((ltibia**2 - lfemur**2 - r3**2) / (-(2 * lfemur * r3)))
    theta2 = fi2 + fi1
    
    fi3 = math.acos((r3**2 - lfemur**2 - ltibia**2) / (-(2 * lfemur * ltibia)))
    theta3 = 180 - math.degrees(fi3)

    coxa_angle = max(0, min(180, math.degrees(theta1) + 90))
    femur_angle = max(0, min(180, math.degrees(theta2) + 55))
    tibia_angle = max(0, min(180, theta3))
    
    return coxa_angle, femur_angle, tibia_angle