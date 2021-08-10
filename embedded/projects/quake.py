# Earthquake alert
#
# (note from author - this is an example to learn about embedded systems. You shouldn't rely on it
#  to detect an actual earthquake.)
# - Mythic Summer Camp 2021
#
# Connections:
# - Pin 4  - I2C SDA  -> OLED (onboard module), laser distance sensor, and IMU
# - Pin 15 - I2C SCL  -> OLED (onboard module), laser distance sensor, and IMU
# - Pin 22 - GPIO out -> Beeper, inverted
# - Pin 25 - GPIO out -> White LED (onboard module)

from machine import I2C, Pin, TouchPad
import ssd1306
import imu
import time

rst = Pin(16, Pin.OUT)
rst.value(1)
led = Pin(25, Pin.OUT)
led.value(0)
beeper = Pin(22, Pin.OUT)
beeper.value(1) # beeper makes noise if low (0) and quiet if high (1)

scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl=scl, sda=sda, freq=450000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
imu = imu.MPU6050(i2c)

def mythic_logo(oled):
    logo=[
        (0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
        (1,1), (2,2), (3,3), (4,4), (3,5),
        (5,4), (6,3), (7,2), (8,1),
        (9,0), (9,1), (9,2), (9,3), (9,4), (9,5), (9,6), (9,7),
        (8,6), (7,5)
        ]
    for x,y in logo:
        oled.pixel(x, y, 1)

# *** Interesting code starts here! ***

# Set up 128 samples, one per horizontal pixel in the OLED
plot = [1.0] * 128

# Do this forever
while True:

    # Blank the screen
    oled.fill(0)
    
    # Write some stuff at the top
    oled.text('Mythic', 45, 0)
    
    # Print the sensor readings
    #oled.text('Accel = ' + str(imu.accel.magnitude) + ' G', 10, 10)
    oled.text('Accel = {:.4f} G'.format(imu.accel.magnitude) + ' G', 0, 10)
    mythic_logo(oled)
    
    # Remove oldest element from the plot
    plot.pop(0)
    
    plot.append(imu.accel.magnitude)
    
    found_a_quake = False
    # Plot the line
    for x in range(0, 128):
        y = 48 - int((plot[x] - 1.0) * 12.0) 
        oled.pixel(x, y, 1)
        # Look at each point, and check if we have a high enough peak to be a quake
        if plot[x] > 2.3:
            found_a_quake = True
    
    if found_a_quake:
        # If we found a quake in the sample set, beep and light up LED
        led.value(1)
        beeper.value(0)
    else:
        # And if not, turn them both off
        led.value(0)
        beeper.value(1)
    
    # Commit the screen changes
    oled.show()

    time.sleep(0.01)