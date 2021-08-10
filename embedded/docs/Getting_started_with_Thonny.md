# Getting started with Thonny

[TOC]

> **Note:** These instructions might require help from a seasoned computer user or adult.

## Get the Thonny IDE for your home computer

Using a web browser, go to: https://thonny.org/

### Windows users

At the top of the Thonny webpage, click the **<u>Windows</u>** link under the **Download version x.y.z for** line. x.y.z will be the numbers for the latest version (3.3.11 as of 7/26/2021).

This should start a the download of a file called **thonny-x.y.z.exe**. It will probably go into the Downloads folder on your computer.

When the file is downloaded, open it (double click). The installer will launch, and present the Setup - Thonny dialog that says **Welcome to using Thonny!**

Click the `Next` button.

Leave the **I accept the agreement** radio button selected, and click `Next`.

Leave the install folder at the default: C:\Users\\<YourUserName>\AppData\Local\Programs\Thonny and click `Next`.

**Check the box** next to **Create desktop icon** and click `Next`.

Click `Install`.

At the Great success! dialog, click `Finish`.

Find Thonny's `Th` icon on your desktop and double click it.

### Mac users

At The top of the Thonny webpage,  click <u>**Mac**</u> link.

Click `Allow` at the Do you want to allow Downloads on "thonny .org" dialog.

When the download completes click the icon that looks like an open box and then double click the **thonny-3.3.13.pkg** file.

At the Welcome to the Thonny Installer dialog, click the `Continue` button.

At the Software License Agreement page, click Continue, then click Agree on the next dialog.

Click Install on the Standard Install on "Macintosh HD" dialog.

You'll be prompted to type the user password, type it and the click the Install Software button.

When installation completes press the Close button

At the Do you want to move the "Thonny" installer to the Trash? dialog, click Move to Trash.

Click the Launchpad (Rocket Icon), find Thonny's `Th` icon and click it.

### Raspberry Pi users

We'll assume it goes similarly to the Windows setup, but you click the <u>**Linux**</u> link. Thonny may already be installed on your Raspberry Pi, if you used an official release.

## First Launch

On the first use of Thonny, it will prompt you for two pieces of information for program setup.

1. Pick what you'd like to use for the language of the user interface.
2. Pick **Standard** for the **Initial settings** (Raspberry Pi settings are for coding for Raspberry Pi?).

### Tell Thonny you'll be writing code for MicroPython

Click `Tools` on the menu bar and then `Options...` from the drop-down menu.

Click the `Interpreter` tab

Select MicroPython (ESP32) from the **Which interpreter or device should Thonny use for running your code?** selector (click the down arrow at the end).

Leave the Port or WebREPL selector at < Try to detect port automatically >.

Click `OK`, but we'll be back here in a bit to install the firmware.

## Get the MicroPython firmware file for the ESP32 microprocessor on the module

Use your browser to navigate to: 
https://micropython.org/download/esp32/

Download the latest "stable" bin file under **Firmware with ESP-IDF v4.x**
As of 7/22/21, the latest was: 
https://micropython.org/resources/firmware/esp32-20210623-v1.16.bin

## Flash the MicroPython firmware to the board

> **Note:**  You'll only need to do this once on your microcontroller board. Well, unless something goes really wrong and you need to start over from scratch.

Connect a USB cable from your computer to the microcontroller board. The board should power up.

From the Tools/Options/Interpreter tab, click the **<u>Install or update firmware</u>** link near the bottom of the dialog.

Click the `Browse` button and navigate to the downloaded file (esp32-20210623-v1.16.bin for example). It's probably in your Downloads directory. Click on the file name to select it and the click `Open`.

Select the **Silicon Labs CP210x USB to UART Bridge (COM\<SomeNumber>)** item in the **Port** pull down selector.

Leave the **Flash mode** radio button set at **From image file (keep)**.

Leave the **Erase flash before installing** check box `checked`.

Click the `Install` button.

When you get a message like:

```
Hash of data verified.

Leaving...
Hard resetting via RTS pin...
Done!
```

Click the `Close` button.

Click the `OK` button.

Hopefully, you'll see something like this in the Shell tab at the bottom of Thonny. It's the Python **>>>** prompt.

```
MicroPython v1.16 on 2021-06-23; ESP32 module with ESP32

Type "help()" for more information.
>>> 
```

## Transfer the sample Python code to the module

### Download the .zip file from the Mythic Summer Camp repository on GitHub.

Go to https://github.com/mythic-ai/summercamp2021/archive/refs/heads/main.zip . Your browser may automatically put **summercamp2021-main.zip** in your computer's Downloads directory.

### Extract the files in the the zip file

If you're a Windows user, right click on the zip file and click `Extract All...`. 

It's fine to extract into your computer's Downloads directory, but you might want to choose another location. For this example we'll just put them all in **C:\Users\\**YourUserName>**\Downloads\summercamp2021-main** . 

Click the `Extract` button and the directory shown above will be created with all the files you need in it.

### Copy the files from your computer to the module

We need to copy these files from the summer camp directory to the module, we'll use Thonny to do that.

```
C:\Users\<YourUsername>\Downloads\summercamp2021-main\summercamp2021-main\embedded\modules\mpu9250.py
C:\Users\<YourUsername>\Downloads\summercamp2021-main\summercamp2021-main\embedded\modules\ssd1306.py
C:\Users\<YourUsername>\Downloads\summercamp2021-main\summercamp2021-main\embedded\modules\vl53l0x.py
C:\Users\<YourUsername>\Downloads\summercamp2021-main\summercamp2021-main\embedded\projects\oledtest.py
```

All of these will be copied to the top directory on the module.

### To copy a file

In Thonny, click the Open... file icon (it looks like a folder). Ctrl-O works too.

Click the `This computer` button

Navigate to the source file directory e.g. *C:\Users\<YourUsername>\Downloads\summercamp2021-main\summercamp2021-main\embedded\modules\*

Select the file.

Click the `Open` button.

When the file is open and it's tab is selected, use the `File` menu and select `Save as...`. Ctrl-Shift-S works too.

Click the `MicroPython device` button.

type the filename. Type just the filename part. It's the same as listed in the selected editor tab or instructions above.

Click the `OK` button.

When the **Saving...** dialog closes it's been copied.

You can leave each file open in the editor as you go, or close them. leave oledtest.py open as you'll need it next.

## Run the Test Program

With the **oledtest.py** file open and editor tab selected, click the green `Run current scrip`t icon. F5 works too.

