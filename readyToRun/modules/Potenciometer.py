# SNEIA's Dev Team :)
# Original code by: https://github.com/WowNotSmart
# https://github.com/SNEIA-DEV-TEAM/raspberryPiPicoProjects/blob/main/readyToRun/modules/Potenciometer.py
# Date: 19/07/2022

#-----------------------------------------------------------------
# File: Here are the connections necessary to operate a basic
# potentiometer, including the pins used within this code and their
# standardization method for the data resulting from the connection
#
# WARNING: it has been shown in projects using this module that
# the data standardization method generates some anomalies in
# some states of the incoming data, use under the discretion
# of this problem.
#-----------------------------------------------------------------

import machine
import utime

#The value changes depending on the pin to which the potentiometer is connected.
adc_read = machine.ADC(28)

#Each time the analog value of the potentiometer is updated, it will be updated digitally.
while True:
    #Take the current value at which the potentiometer is set
    reading = adc_read.read_u16()
    
    #Statistical process of data standardization, with this process the data will be in this range [0 - 3.3].
    normalize = (3.3 / 65535) * reading
    
    print("ADC", normalize)
    
    #Frequency at which the data output of the potentiometer is read, decrease the value to increase the frequency.
    utime.sleep(0.5)



#REQUIRED CONNECTIONS
    #It is necessary to give power to the potentiometer by one of the pins at the ends and the other to give a GND output to that power,
    #for the correct operation of this code is recommended to be 3.3V, no matter the order of connection.
    
    #First potentiometer pin = pin 36 Pico
    #Second potentiometer pin (data pin)= pin 34 Pico
    #Third potentiometer pin = pin 38 Pico