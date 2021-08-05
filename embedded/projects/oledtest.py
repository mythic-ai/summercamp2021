# Print sensor values to the display
# - Mythic Summer Camp 2021
#
# Connections:
# - Pin 4  - I2C SDA  -> OLED (onboard module), laser distance sensor, and IMU
# - Pin 15 - I2C SCL  -> OLED (onboard module), laser distance sensor, and IMU
# - Pin 19 - GPIO in  -> Hall effect (magnet) sensor, inverted
# - Pin 22 - GPIO out -> Beeper, inverted
# - Pin 25 - GPIO out -> White LED (onboard module)
# - Pin 27 - Touch in -> Touch sense wire

from machine import I2C, Pin, TouchPad
import ssd1306
import vl53l0x
import imu
import time

rst = Pin(16, Pin.OUT)
rst.value(1)
led = Pin(25, Pin.OUT)
led.value(0)
scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl=scl, sda=sda, freq=450000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
laser = vl53l0x.VL53L0X(i2c)
tp = TouchPad(Pin(27, Pin.IN, None))
imu = imu.MPU6050(i2c)

# Do this forever
while True:
    # Start the laser measuring and wait a bit for it to be ready
    laser.start()
    time.sleep(0.05)
    
    # Blank the screen
    oled.fill(0)
    
    # Write some stuff at the top
    oled.text('Mythic', 45, 5)
    oled.text('MicroPython', 20, 20)
    
    # Print the sensor readings
    oled.text('Laser = ' + str(laser.read()) + 'mm', 10, 30)
    oled.text('Touch = ' + str(tp.read()), 10, 40)
    oled.text('Tilt = ' + str(imu.accel.inclination) + 'deg', 10, 50)
    
    # Commit the screen changes
    oled.show()
    
    # Stop the laser measurements and give the sensor a break
    laser.stop()
    time.sleep(0.05)