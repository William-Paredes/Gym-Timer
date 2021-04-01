from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

class gym:
    initial_text_location = 2, 4
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
        self.check_time()
        self.generate_text(self.image, self.update_text(), self.initial_text_location, 27)

    def check_time(self):
        now = datetime.now()
        new_hour = now.strftime("%I")
        new_minute = now.strftime("%M")

        if(new_minute != self.t['minute']):
            print('New Min: ', new_minute)
            self.t['minute'] = new_minute
            self.clear_screen()

        if(new_hour != self.t['hour']):
            self.t['hour'] = new_hour
            print('New Hour: ', new_hour)
            self.clear_screen()

    def clear_screen(self):
        self.image = Image.new("RGB",self.screen_size)

    def update_text(self):
        text = self.t['hour'] + ':' + self.t['minute']
        return text

    def generate_text(self, im, text, begin_loc, font_size):
        font = ImageFont.truetype('./fonts/digital-7-mono.ttf', size=(font_size))
        draw = ImageDraw.Draw(im)
        draw.text(begin_loc, text, font=font, fill='red')
