# SNEIA's Dev Team :)
# Original code by: https://github.com/Esteban8482
# https://github.com/SNEIA-DEV-TEAM/raspberryPiPicoProjects/blob/main/readyToRun/modules/ShowIcon.py
# Date: 24/07/2022

#-------------------------------------------------------------------
# File: Connections needed to display an image on an OLED display
# Conversion process necessary to convert a jpg to a pbm (binary
# file that can display a monochrome screen).
# Code to read the pbm type files and update the screen.
# The images in pbm file are text, as such we will make the Pico
# take that text and send it as pixels to be turned on or off on
# the screen.
# A sample image is included for testing
#-------------------------------------------------------------------

from machine import Pin, I2C
from time import sleep_ms
from ssd1306 import SSD1306_I2C
import framebuf

#To turn off the display change the value to false and re-run the code
runningStatus = True

ANCHO = 128
ALTO = 64

#Create display object using digital connection pins
i2c = I2C(1, scl = Pin(19), sda = Pin(18))
oled = SSD1306_I2C(ANCHO, ALTO, i2c)

ruta_icono = "images/Raspberry.pbm"

doc = open(ruta_icono, "rb")
    
#Skip first line of document as it is not important for the image.
doc.readline()
    
#From subsequent lines read data such as the image size
xy = doc.readline()
x = int(xy.split()[0])
y = int(xy.split()[1])
    
#Finish reading the document indicating which pixels turn on or off.
icono = bytearray(doc.read())
    
doc.close()

#Transfer image information to the format that the screen will be using (Monochrome).
screenImage = framebuf.FrameBuffer(icono, x, y, framebuf.MONO_HLSB)

#Select the image to be displayed and its position
oled.blit(screenImage, 35, 10)

if runningStatus:
    oled.show()

#REQUIRED CONNECTIONS
    
    
