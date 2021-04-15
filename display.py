
from PIL import Image, ImageDraw, ImageFont
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import const

class Display():

    options = RGBMatrixOptions()
    options.rows = 32
    options.cols = 64
    options.parallel = 1
    options.hardware_mapping = 'adafruit-hat'
    options.brightness = 50
    
    matrix = RGBMatrix(options = options)
    
    def __init__(self):
        self.screen_size = const.screen_size
        self.image = Image.new("RGB", self.screen_size)
        self.t = {'first': '00', 'second': '00'}

    def update_screen(self, text):
        self.clear_screen()
        self.generate_text(self.image, text, const.initial_text_location, const.font_size)
        print(text)
        self.matrix.SetImage(self.image.convert('RGB'))

    def clear_screen(self):
        self.image = Image.new("RGB",self.screen_size)

    def update_text(self):
        text = self.t['first'] + ':' + self.t['second']
        return text

    def generate_text(self, im, text, begin_loc, font_size):
        font = ImageFont.truetype('./fonts/digital-7-mono.ttf', size=(font_size))
        draw = ImageDraw.Draw(im)
        draw.text(begin_loc, text, font=font, fill='red')
