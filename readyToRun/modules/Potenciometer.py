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

#LIBRARIES
#Library to control the physical pins of the microcontroller
import machine
#Library to control the iterations on the speed at which information is entered and displayed
import utime

#BODY
#Connect the pin where the potentiometer data will be input to the variable "adc_read"
adc_read = machine.ADC(28)

#While loop to ensure that each time the physical value of the potentiometer is updated, it is also updated as fast as possible in the code.
while True:
    #Take the current value at which the potentiometer is set and store it in the variable "reading".
    reading = adc_read.read_u16()
    
    #Statistical process for the processing of data that come in very high value numbers, it is intended that the data go like this [0 - 3.3]
    #for easier usability of the potentiometer output.
    normalize = (3.3 / 65535) * reading
    
    print("ADC", normalize)
    
    #Frequency at which the data output of the potentiometer is read, decrease the value to increase the frequency.
    utime.sleep(0.5)

#REQUIRED CONNECTIONS
    #It is necessary to give power to the potentiometer by one of the pins at the ends and the other to give a GND output to that power,
    #for the correct operation of this code is recommended to be 3.3V, no matter the order of connection. The order of connection is not important
    
    #First potentiometer pin = pin 36 Pico
    #Second potentiometer pin (data pin)= pin 34 Pico
    #Third potentiometer pin = pin 38 Pico

    