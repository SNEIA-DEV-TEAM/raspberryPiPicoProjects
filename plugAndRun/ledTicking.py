# SNEIA's Dev Team :)
# Original code by: https://github.com/WowNotSmart
# https://github.com/SNEIA-DEV-TEAM/raspberryPiPicoProjects/blob/main/plugAndRun/ledTicking.py

from machine import Pin
import time, random

raspberryLed = Pin(25, Pin.OUT)
raspberryLedStatus = False

# - - - - - IMPORTANT - - - - -

# Change runningStatus's value
# to True if you want to run the
# code, change it back to False
# if you don't want to run the
# code. (Testing purposes)

runningStatus = True

# - - - - - - - - - - - - - - -

timePeriod = 1          # How much time wait before the raspberryLedStatus change
workMethod = "random"   # Possible values: ["random", "period"]

def ledTicklingRandom():
    global raspberryLed, raspberryLedStatus
    if raspberryLedStatus == False:
        raspberryLed.value(raspberryLedStatus)
        time.sleep(random.uniform(0.01, 0.12))
        raspberryLedStatus = True
        
    elif raspberryLedStatus == True:
        raspberryLed.value(raspberryLedStatus)
        time.sleep(random.uniform(0.01, 0.12))
        raspberryLedStatus = False

def ledTicklingPeriod():
    global raspberryLed, raspberryLedStatus
    if raspberryLedStatus == False:
        raspberryLed.value(raspberryLedStatus)
        time.sleep(timePeriod)
        raspberryLedStatus = True
        
    elif raspberryLedStatus == True:
        raspberryLed.value(raspberryLedStatus)
        time.sleep(timePeriod)
        raspberryLedStatus = False
        
while runningStatus == True:
    if workMethod == "random":
        ledTicklingRandom()
    elif workMethod == "period":
        ledTicklingPeriod()
