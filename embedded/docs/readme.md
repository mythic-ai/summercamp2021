# Mythic Summer Camp 2021 Embedded Session

## Parts

* 1x [Heltec Automation ESP32 module](https://www.amazon.com/Development-0-96inch-Display-Arduino-Compatible/dp/B07428W8H3)
* 1x [VL53L0X Time-of-Flight Laser Ranging Sensor](https://www.amazon.com/gp/product/B08JYHJTQY)
* 1x [MPU6050 3 Axis Accelerometer and Gyroscope Module](https://www.amazon.com/gp/product/B00LP25V1A)
* 1x [Passive Buzzer Module](https://www.amazon.com/gp/product/B07MPYWVGD)
* 1x [Hall Effect Magnetic Sensor Module](https://www.amazon.com/gp/product/B07X97JXHT)
* 1x [Multicolored Wire Kit](https://www.amazon.com/gp/product/B01EV70C78)
* 1x [Solderless Breadboard](https://www.amazon.com/gp/product/B07NVWR495)
* 1x [Ceramid Magnets](https://www.amazon.com/gp/product/B07S75MD7X) (any magnet will do)
* 1x [Roll Copper Foil Tape](https://www.amazon.com/gp/product/B0741ZRP4W)

## Your first project

1. Plug the ESP32 module into the left side of the breadboard as shown below. Make sure that there is one empty row of holes on top and bottom. Push firmly over the pins, but not directly on the display or else you'll crack it. 

![Hello project breadboard](https://github.com/mythic-ai/summercamp2021/blob/main/embedded/docs/fritzing/hello_bb.png)

2. Now plug the micro USB cable between the left side of the ESP32 and your PC.

3. [Follow this guide](https://github.com/mythic-ai/summercamp2021/blob/main/embedded/docs/Getting_started_with_Thonny.md) if you do not have Thonny already installed on your PC.

4. Change the working directory in Thonny to the `projects` directory from the zip file. This is the upper left hand side of the window.

5. Double click `hello.py` to open it in the editor.

6. Find the line that says `YOUR_NAME_HERE` midway through and replace that with your name.

7. Connect to the ESP32 board by clicking the red STOP button. The green play button should light up at the top of the window.

8. Click the play button to upload and run your program.
