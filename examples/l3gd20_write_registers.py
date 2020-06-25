import time
import board
import busio
import adafruit_l3gd20

# Hardware I2C setup:
I2C = busio.I2C(board.SCL, board.SDA)
SENSOR = adafruit_l3gd20.L3GD20_I2C(I2C, rng=adafruit_l3gd20.L3DS20_RANGE_2000DPS)

# Update the chip's register 0x20 (CTRL1)  with the value 0xBF
SENSOR.write_register(0x20, 0xBF)

# This sets the output data rate to 400Hz and keeps everything else on their default modes
# For more information about CTRL1, see section 7.2 of the datasheet

while True:
    print("Angular Momentum (rad/s): {}".format(SENSOR.gyro))
    print()
    time.sleep(1)
