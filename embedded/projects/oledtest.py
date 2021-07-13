from machine import I2C, Pin, TouchPad
import ssd1306
import vl53l0x
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


while True:
    laser.start()
    time.sleep(0.05)

    oled.fill(0)
    oled.text('ESP32', 45, 5)
    oled.text('MicroPython', 20, 20)
    oled.text('Laser = ' + str(laser.read()) + 'mm', 10, 30)
    oled.text('Touch = ' + str(tp.read()), 10, 40)
    oled.show()
    if (laser.read() < 1000) or (tp.read() < 450):
        led.value(1)
    else:
        led.value(0)
    laser.stop()
    time.sleep(0.05)