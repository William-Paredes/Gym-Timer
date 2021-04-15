import time 
import json
from display import Display

class Timer(): 
    def __init__(self):
        self.min = 0
        self.text = '00:00'
        self.seconds = 0
        self.display = Display()
        self.cancel = False

    def setTimer(self, min):
        self.min = min
        self.countdown_min(self.min)

    def checkCancel(self):
        data = self.checkdata()
        self.cancel = data
        print('Cancel: ', self.cancel)

    def checkdata(self): #check json file for any changes
        with open("data.json") as f:
            data = json.load(f)
        return data['timer']
    def setCancel(self):
        with open('data.json', 'r', encoding='utf-8') as outjson:
            json_data = json.load(outjson)
            print(json_data)
            json_data['timer'] = False
    
        with open('data.json', 'w') as output:
            json.dump(json_data, output, indent=4)

    def countdown_min(self, t):
        seconds = t * 60
        self.seconds = seconds
        while seconds: 
            self.checkCancel()
            if self.cancel == False: 
                mins,sec = divmod(seconds,60)
                timer = '{:02d}:{:02d}'.format(mins, sec) 
                self.text = timer
                self.display.update_screen(timer)
                time.sleep(1)
                seconds-=1
            else:
                break
        self.cancel = False
        self.setCancel()
        