import time
from datetime import datetime

class Clock:

    def __init__(self):
        self.now = datetime.now()
        self.hour = self.now.strftime("%I")
        self.minute = self.now.strftime("%M")
        self.t = {'hour':self.hour, 'minute': self.minute}
        self.text = self.t['hour'] + ':' + self.t['minute']


    def check_time(self):
            now = datetime.now()
            new_hour = now.strftime("%I")
            new_minute = now.strftime("%M")

            if(new_minute != self.t['minute'] and new_hour != self.t['hour']):
                self.t['minute'] = new_minute
                self.t['hour'] = new_hour
                self.text = self.t['hour'] + ':' + self.t['minute']
                return True

            if(new_minute != self.t['minute']):
                self.t['minute'] = new_minute
                self.text = self.t['hour'] + ':' + self.t['minute']
                return True
                
            if(new_hour != self.t['hour']):
                self.t['hour'] = new_hour
                self.text = self.t['hour'] + ':' + self.t['minute']
                return True

            return False
            
            


            
            
