# SNEIA's Dev Team :)
# Original code by: https://github.com/Esteban8482
# https://github.com/SNEIA-DEV-TEAM/raspberryPiPicoProjects/blob/main/readyToRun/modules/blinck.py
# Date: 19/07/2022

#-----------------------------------------------------------------
# File: The microcontroller has an integrated temperature sensor 
# and it is connected to pin 4, we will see how to read the 
# information from that pin.
#We will also see how to convert that data into something more 
# easily readable and manipulable by standardization.
#-----------------------------------------------------------------

import machine
import utime

#indicate the pin to which the sensor is connected
sensor_temp = machine.ADC(4)

#Standardization method
conversion_factor = 3.3 / 65535

#Update temperature every iteration of the cycle
while True:
    reading = sensor_temp.read_u16() * conversion_factor

    #Decide how many decimal places to display in the data
    temperature = round(27 - (reading - 0.706) / 0.001721, 2)

    print("Temperature: ", temperature)

    #Cycle repetition timeout
    utime.sleep(0.1)

#REQUIRED CONNECTIONS
    #No connection is necessary as the sensor is integrated in the Pico.