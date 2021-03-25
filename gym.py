from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

class gym:
    inital_text_location = 0, 4
    screen_size = 64,32
    now = datetime.now()
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    image = Image.new("RGB", screen_size)
    t = {
        'hour': hour,
        'minute': minute
    }

    timer = {
        'minutes': 0,
        'seconds': 0
    }

    def run(self):
        self.check_time(self.t)


    def check_time(self, current):
        print('current Time: ', current['hour'], ':', current['minute'])
        now = datetime.now()
        new_hour = now.strftime("%I")
        new_minute = now.strftime("%M")

        if(new_hour != current['hour'] or new_minute != current['minute']):
            current['hour'] = new_hour
            current['minute'] = new_minute
            print('New Time: ', new_hour,':',new_minute)
            self.update_display(current) 
        

    def update_display(self, text_display):
        image = Image.new("RGB", self.screen_size)
        image.thumbnail(self.screen_size, Image.ANTIALIAS)
        text = text_display['hour'] + ":" + text_display['minute']
        self.generate_text(image, text , self.inital_text_location, 27)
        print("display updated")
        print(text_display)
        

    def generate_text(self, im, text, begin_loc, font_size):
        font = ImageFont.truetype('./fonts/digital-7-mono.ttf', size=(font_size))
        draw = ImageDraw.Draw(im)
        draw.text(begin_loc, text, font=font)