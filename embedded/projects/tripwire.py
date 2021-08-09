# Laser trip wire
# - Mythic Summer Camp 2021
#
# Alarm that goes off if someone picks up a metal can that's touching a wire or crosses the laser trip wire.
# Putting a magnet near the Hall effect sensor or tilting the board disarms the alarm.
#
# Connections:
# - Pin 4  - I2C SDA  -> OLED (onboard module), laser distance sensor, and IMU
# - Pin 15 - I2C SCL  -> OLED (onboard module), laser distance sensor, and IMU
# - Pin 19 - GPIO in  -> Hall effect (magnet) sensor, inverted
# - Pin 22 - GPIO out -> Beeper, inverted
# - Pin 25 - GPIO out -> White LED (onboard module)

from machine import I2C, Pin, TouchPad
import ssd1306
import vl53l0x
import time

rst = Pin(16, Pin.OUT)
rst.value(1)
led = Pin(25, Pin.OUT)
led.value(0)
beeper = Pin(22, Pin.OUT)
beeper.value(1) # beeper makes noise if low (0) and quiet if high (1)
magnet = Pin(19, Pin.IN) # magnet sensor is low (0) when a magnet is detected and high (1) when not

scl = Pin(15, Pin.OUT, Pin.PULL_UP)
sda = Pin(4, Pin.OUT, Pin.PULL_UP)
i2c = I2C(scl=scl, sda=sda, freq=450000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3c)
laser = vl53l0x.VL53L0X(i2c)

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

tripped = False  # we use this to track the "tripped" state. start out in not-tripped state

# Do this forever
while True:
    # Start the laser measuring and wait a bit for it to be ready
    laser.start()
    time.sleep(0.05)
    # Blank the screen
    oled.fill(0)
    
    # Write some stuff at the top
    oled.text('Mythic', 45, 5)
    
    # Print the sensor readings
    oled.text('Magnet = ' + str(magnet.value()), 10, 20)
    oled.text('Laser = ' + str(laser.read()) + 'mm', 10, 30)

    mythic_logo(oled)
    
    # Commit the screen changes
    oled.show()
    
    # Check for our "key" - if the magnet value is 0, then the magnet is near the sensor
    # and we want to un-trip the alarm.
    if magnet.value() == 0:
        tripped = False
    else:
        # ...but if the magnet isn't by the sensor, we should check the laser trip wire.
        # The laser distance sensor reads out in millimeters when you run laser.read().
        if laser.read() < 1000:
            # and if it's less than our maximum distance we set the tripped state.
            tripped = True
        
    
    if tripped:
        # If we're in the tripped state, turn on the LED and buzzer
        led.value(1)
        beeper.value(0)
    else:
        # And if not, turn them both off
        led.value(0)
        beeper.value(1)
        
    # Stop the laser measurements and give the sensor a break    
    laser.stop()
    time.sleep(0.05)