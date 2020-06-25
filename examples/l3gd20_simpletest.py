import time
import board
import busio
import adafruit_l3gd20

# Hardware I2C setup:
I2C = busio.I2C(board.SCL, board.SDA)
# Initializes L3GD20 object using default range, 250dps
SENSOR = adafruit_l3gd20.L3GD20_I2C(I2C)
# Initialize L3GD20 object using a different range.
#SENSOR = adafruit_l3gd20.L3GD20_I2C(I2C, rng=adafruit_l3gd20.L3DS20_RANGE_2000DPS)

# Possible values for rng are:
# adafruit_l3gd20.L3DS20_Range_250DPS, 250 degrees per second. Default range
# adafruit_l3gd20.L3DS20_Range_500DPS, 500 degrees per second
# adafruit_l3gd20.L3DS20_Range_2000DPS, 2000 degrees per second


# Hardware SPI setup:
# import digitalio
# CS = digitalio.DigitalInOut(board.D5)
# SPIB = busio.SPI(board.SCK, board.MOSI, board.MISO)
# SENSOR = adafruit_l3gd20.L3GD20_SPI(SPIB, CS)

while True:
    print("Angular Momentum (rad/s): {}".format(SENSOR.gyro))
    print()
    time.sleep(1)
