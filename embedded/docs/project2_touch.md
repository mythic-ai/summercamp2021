# Touch Sensor

The ESP32 can sense when a wire is being touched, kind of like a touch screen on a phone. We can use this like a button to detect if a person is touching a wire or a metal object.

To use the touch sensor, we first have to put a wire in the board that connects to the right wire on the ESP32 module.

But before we do that, we should probably unplug the USB. It's not a good idea to work on a live circuit. The ESP32 uses safe and low voltages, but it's possible to destroy the parts if a wire accidentally makes contact in the wrong spot.

Now that there's no power on the board, we can hook up our touch sense wire. find a wire with pins on both sides, and push one end into the hole just under the spot on the ESP32 marked `27`.

![touch breadboard diagram](https://github.com/mythic-ai/summercamp2021/blob/main/embedded/docs/fritzing/touch_bb.png)

Now plug the USB back into the PC. Click the STOP icon to connect to the board.

Double click on the `touch.py` file on the left side, and click the PLAY button to start the program.
