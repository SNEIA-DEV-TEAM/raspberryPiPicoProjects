#-----------------------------------------------------------------
# File: The microcontroller has a led and this is connected to its
# pin 25, here we will see how to access this pin and alter its
# information.
# In the same way we will see a small piece of code that allows to
# control the flashing time of the LED.
#-----------------------------------------------------------------

#Import library that allows to control the physical pins of the Pico and a time controller.
from machine import Pin, Timer

#We use this function to assign one of the pins of the Pico inside a variable that we can
#manipulate, we select the pin that contains the LED and we indicate that this pin is to
#send data externally to the LED.
led = Pin(25, Pin.OUT)

#Initialize boolean variable that will define the state of the LED in each iteration of the loop.
led_state = True

#Store in a variable the function that initializes the time counter for the blinker
tim = Timer()

#Function that constantly changes the status of the LED
def tick(timer):
    #Bring variables from outside the function to inside it to be able to manipulate them,
    #since due to scope issues this would not be possible normally.
    global led, led_state
    
    #Invert the state of the LED, if it is on then it will turn it off and vice versa.
    led_state = not led_state
    
    #Update led value
    led.value(led_state)

#Call the function "tick" with a certain frequency so that each time it is
#executed the state of the led is changed.
tim.init(freq = 5, mode = Timer.PERIODIC, callback = tick)

#REQUIRED CONNECTIONS
    #No connection is necessary as the LED is integrated in the Pico.