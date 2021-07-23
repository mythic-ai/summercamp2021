#Get the mu Python editor program for your home computer

Using a web browser, go to: https://codewith.mu/

At the top of the page, click the Download tab

**Windows users should:**
_Note: If your username on the computer you're using has a space in it you may have trouble with the secondary install._
Click [64-bit] under the Windows Installer heading
When the installer file (Mu-Editor-Win64-1.1.0b5.msi for instance) is downloaded, open it (double click).
Windows' Microsoft Defender SmartScreen might prevent the installer from running. If so, click the More Info link in the dialog, then the [Run anyway] button that will show up.
Click the check box next to [ ] I accept the terms in the License Agreement
Click [Install]
Click [Finish] when the Setup Wizard finishes

To launch the editor, find Mu Editor in the Windows start menu and click it.

**Mac users should:** 
Click [Download] under the Mac OSX Installer heading

**Rasberry Pi users should:**
Click [Instructions] under the Python Package (Linux or Native Python) heading

#First Launch
The first time you run this software it will continue installing and setting up your system. The does play a cute animation of a python waiting patiently. 
After the secondary install completes, you'll be prompted with the Select Mode dialog. Choose ESP MicroPython and then click [OK]

#Get the MicroPython firmware file for the ESP32 microprocessor on the module

Use your browser to navigate to: 
https://micropython.org/download/esp32/

Download the latest "stable" bin file Firmware with ESP-IDF v4.x
As of 7/22/21, the latest was 
https://micropython.org/resources/firmware/esp32-20210623-v1.16.bin

#Flash the firmware
Connect a USB cable from your computer to the microcontroller board. The board should power up.

In Mu, click the gear icon in the lower right corner of the window

In the Mu Administration dialog click the ESP Firmware flasher tab at the top.

The Device: line shoud show a gray chip icon followed by CP210x (COM<something>).

Use the pull-down arrow at th e end of the Choose device type: selector, and select ESP32

Click the {Browse] button and navigate to the downloaded esp32-20210623-v1.16.bin (for example) file. It's probably in the Downloads directory. Click on the file name to select it and the click [Open].

Click the [Erase & write firmware] button.

When you get a message like:

Wrote 1510544 bytes (976957 compressed) at 0x00001000 in 86.8 seconds (effective 139.3 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...

Click the {OK] button. The display will not show anything until we write code to put something on it.

#Transferr the sample Python code to the module

Establish a connection to the module by clicking the REPL button in the Mu application

You should get the Python prompt >>> in the ESP MicroPython REPL pane at the bottom of the application window

Click the REPL button again to close the REPL pane

Click the Files button in Mu
