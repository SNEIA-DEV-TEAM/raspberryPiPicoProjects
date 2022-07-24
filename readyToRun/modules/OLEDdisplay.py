# SNEIA's Dev Team :)
# Original code by: SNEIA's Dev Team
# https://github.com/SNEIA-DEV-TEAM/raspberryPiPicoProjects/blob/main/readyToRun/modules/OLEDdisplay.py
# Date: 24/07/2022

#-------------------------------------------------------------------
# File: Connections needed to display text on an OLED display,
# including pins for connection and concepts needed for further use 
#-------------------------------------------------------------------

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf, time
import utime

#To turn off the display change the value to false and re-run the code
runningStatus = True

oledWidth = 128
oledHeight = 64

#Create display object using digital connection pins
i2c = I2C(0, scl=Pin(9), sda=Pin(8), freq=200000)
oledDevice = SSD1306_I2C(oledWidth, oledHeight, i2c)

if runningStatus:
    #The first parameter is the text to display on the screen, the
    #second is the x-position, the third is the y-position (this function only accepts strings).
    oledDevice.text("SNEIA Dev Team", 1, 8)
    oledDevice.text(":)", 1, 18)
        
    #Send to the screen all the changes we have made (refresh)
    oledDevice.show()

#REQUIRED CONNECTIONS
    #The display requires 2 pins to provide input and output to the power,
    #then has 2 more on which the data will be sent.
    #
    # GND pin = pico 38 pin
    # VCC pin = pico 36 pin
    # SCL pin = pico 12 pin
    # SDA pin = pico 11 pin
    #
    # Picture for comparison: https://ibb.co/cT6RC7C
