from adxl345 import ADXL345
from machine import Pin, SoftI2C
from pca import PCA9685

sda = Pin(21)
scl = Pin(22)

i2c = SoftI2C(sda=sda, scl=scl)
#gyro = ADXL345(i2c=i2c)

pca1 = PCA9685(i2c=i2c, address=0x40)
pca2 = PCA9685(i2c=i2c, address=0x41)