import time
from board import SCL, SDA
import busio
import adafruit_l3gd20

I2C = busio.I2C(SCL, SDA)
SENSOR = adafruit_l3gd20.L3GD20_I2C(I2C)

while True:

    print('Acceleration (m/s^2): {}'.format(SENSOR.acceleration))

    print()

    time.sleep(1)
