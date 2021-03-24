#!/usr/bin/env python3

import time 
import sys 
from datetime import datetime
from currenttime import current_time

from rgbmatrix import RGBMatrix, RGBMatrixOptions

from PIL import Image, ImageDraw, ImageFont
screen_size = 64,32
inital_text_location = 4, 10

image = Image.new("RGB", screen_size)
image.thumbnail(screen_size, Image.ANTIALIAS)

#Configurations for Matrix 
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'



def generate_text(im, text, begin_loc, font_size):
    font = ImageFont.truetype('./fonts/digital-7-mono.ttf', size=(font_size))
    draw = ImageDraw.Draw(im)
    draw.text(begin_loc, text, font=font)
    return im 

generate_text(image, current_time(), inital_text_location, 16)
image.show()
matrix.SetImage(image.convert('RGB'))


try:
    print("Press CTRL-C to stop")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
    