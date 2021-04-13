import time 
from display import Display

class Timer(): 
    def __init__(self):
        self.min = 0
        self.text = '00:00'
        self.seconds = 0
        self.display = Display()


    def setTimer(self, min):
        self.min = min
        self.countdown_min(self.min)

    def countdown_min(self, t):
        seconds = t * 60
        self.seconds = seconds
        while seconds: 
            mins,sec = divmod(seconds,60)
            timer = '{:02d}:{:02d}'.format(mins, sec) 
            self.text = timer
            self.display.update_screen(timer)
            time.sleep(1)
            seconds-=1
        self.text = "00:00"
        self.display.update_screen(self.text)
        print('BEEP BEEP')
        