# SNEIA's Dev Team :)
# Original code by: https://github.com/WowNotSmart
# https://github.com/SNEIA-DEV-TEAM/raspberryPiPicoProjects/blob/main/readyToRun/modules/blinck.py
# Date: 19/07/2022

#-----------------------------------------------------------------
# File: The microcontroller has a led and this is connected to its
# pin 25, here we will see how to access this pin and alter its
# information.
# In the same way we will see a small piece of code that allows to
# control the flashing time of the LED.
#-----------------------------------------------------------------

from machine import Pin, Timer

#Indicate the pin we are going to manipulate and what we are going to do with it.
led = Pin(25, Pin.OUT)

led_state = True

tim = Timer()

#Function that constantly changes the status of the LED
def tick(timer):
    #Bring global variables to the function to avoid scope problems
    global led, led_state
    
    led_state = not led_state
    
    led.value(led_state)

#Call the function "tick" with a certain frequency so that each time it is
#executed the state of the led is changed.
tim.init(freq = 5, mode = Timer.PERIODIC, callback = tick)

#REQUIRED CONNECTIONS
    #No connection is necessary as the LED is integrated in the Pico.