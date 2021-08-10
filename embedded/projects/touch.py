# Touch sensor example
# - Mythic Summer Camp 2021
#
# Connections:
# - Pin 4  - I2C SDA  -> OLED (onboard module), laser distance sensor, and IMU
# - Pin 15 - I2C SCL  -> OLED (onboard module), laser distance sensor, and IMU
# - Pin 22 - GPIO out -> Beeper, inverted
# - Pin 25 - GPIO out -> White LED (onboard module)
# - Pin 27 - Touch in -> Touch sense wire

from machine import I2C, Pin, TouchPad
import ssd1306
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
tp = TouchPad(Pin(27, Pin.IN, None))

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

# Do this forever
while True:
    # Blank the screen
    oled.fill(0)
    
    # Write some stuff at the top
    oled.text('Mythic', 45, 5)
    oled.text('MicroPython', 20, 20)
    
    # Print the sensor readings
    oled.text('Touch = ' + str(tp.read()), 10, 40)
    mythic_logo(oled)
    
    # Commit the screen changes
    oled.show()
    
    # Check if the touch pin sensor is less than 200
    # (the lower the number, the more likely something is touching the wire)
    if tp.read() < 200:
        # If it's being touched, turn on the white LED and beep the buzzer
        led.value(1)
        beeper.value(0)
    else:
        # If it's not being touched, turn the LED and buzzer off
        led.value(0)
        beeper.value(1)
    
    # Wait for a bit...
    time.sleep(0.1)