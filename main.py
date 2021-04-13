import threading
from clock import Clock
from timer import Timer
from display import Display
from time import sleep
import requests
import json, os 

clock = Clock()
timer = Timer()
display = Display()

def checkdata(): #check json file for any changes
    with open("data.json") as f:
        data = json.load(f)
    return data

def changeModeZero(): # change data mode to 0
    data['mode'] = 0
    with open('data.json', 'w', encoding='utf-8') as outjson:
            json.dump(data, outjson,  indent=4)
            print(data)


data = {"minutes":0, "mode":0}
mode = 0
blink = 0
text = clock.text
display.update_screen(text)

while True: 
    data = checkdata()
    mode = data["mode"]
    minutes = int(data["minutes"])
    if mode == 1: 
        timer.setTimer(minutes)             # Run Timer
        clock.check_time()                  #Check for time difference
        changeModeZero()                    #Change Json mode = 0 
        display.update_screen(clock.text)   # Update display back to Clock
    else:
        if clock.check_time() == True:
            display.update_screen(clock.text)   #Update display with new time
    
    sleep(1)


    
    

