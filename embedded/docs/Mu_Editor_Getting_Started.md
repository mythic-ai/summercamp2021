# Getting started with the Mu editor

[toc]

> **Note:** These instructions might require help from a seasoned computer user or adult.

## Get the Mu Python editor program for your home computer

Using a web browser, go to: https://codewith.mu/

At the top of the page, click the `Download` tab

### Windows users

> _**Note:** If your username on the computer you're using has a space in it you may have trouble with the secondary install._

Click `64-bit` under the Windows Installer heading.
When the installer file (Mu-Editor-Win64-1.1.0b5.msi for instance) is downloaded, open it (double click).
Windows' Microsoft Defender SmartScreen might prevent the installer from running. If so, click the <u>More Info</u> link in the dialog, then the `Run anyway` button that will show up.
Click the check box next to: **I accept the terms in the License Agreement**.
Click the `Install` button.
Click `Finish` when the Setup Wizard finishes.

To launch the editor, find `Mu Editor` in the Windows start menu and click it.

### Mac users

Click `Download` under the Mac OSX Installer heading

### Raspberry Pi users

Click `Instructions` under the Python Package (Linux or Native Python) heading.

### First Launch

The first time you run this software it will continue with a secondary install to set up your system. While this happens Mu plays a cute animation of a python waiting patiently. 

After the secondary install completes, you'll be prompted with the Select Mode dialog. Choose `ESP MicroPython` and then click `OK.`

## Get the MicroPython firmware file for the ESP32 microprocessor on the module

Use your browser to navigate to: 
https://micropython.org/download/esp32/

Download the latest "stable" bin file under **Firmware with ESP-IDF v4.x**
As of 7/22/21, the latest was: 
https://micropython.org/resources/firmware/esp32-20210623-v1.16.bin

## Flash the firmware to the board

Connect a USB cable from your computer to the microcontroller board. The board should power up.

In Mu, click the gear icon in the lower right corner of the window.

In the Mu Administration dialog, click the `ESP Firmware flasher` tab at the top.

The **Device:** line shoud show a gray chip icon followed by CP210x (COM\<SomeNumber>).

Use the pull-down arrow at the end of the **Choose device type:** selector, and select `ESP32`.

Click the `Browse` button and navigate to the downloaded file (esp32-20210623-v1.16.bin for example). It's probably in your Downloads directory. Click on the file name to select it and the click `Open`.

Click the `Erase & write firmware` button.

When you get a message like:

```
Wrote 1510544 bytes (976957 compressed) at 0x00001000 in 86.8 seconds (effective 139.3 kbit/s)...
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
```

Click the `OK` button. The display will not show anything until we write code to put something on it.

## Transfer the sample Python code to the module

### Download the .zip file from the Mythic Summer Camp repository on GitHub.

Go to https://github.com/mythic-ai/summercamp2021/archive/refs/heads/main.zip . Your browser may automatically put that in your computer's Downloads directory.

Extract the Python code (.py files) from the zip file to the mu_code directory.

Open the zip file and copy all the .py files from the zip file's **embedded/modules** and **embedded/projects** directories to **C:\Users\\**\<YourUserName>**\mu_code** (for Windows users). The mu_code directory is the same place shown in the **Files on your computer:** side of the lower pane that opens when you click the `Files` button on Mu.

### Copy the files from your computer to the module

Establish an initial connection to the module by clicking the `REPL` button in the Mu application.

You should get the Python prompt **>>>** in the **ESP MicroPython REPL** pane at the bottom of the application window.

Click the `REPL` button again to close the REPL pane.

Click the `Files` button in Mu.

Individually drag each of the files from the **Files on your computer:** side to the **Files on your device:** side. Wait for the file to show up on the destination side before copying the next.

