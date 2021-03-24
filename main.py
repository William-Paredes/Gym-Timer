#!/usr/bin/env python3

import time 
import sys 
from datetime import datetime
from currenttime import current_time

from PIL import Image, ImageDraw, ImageFont
screen_size = 64,32
inital_text_location = 4, 10

image = Image.new("RGB", screen_size)

image.thumbnail(screen_size, Image.ANTIALIAS)





def generate_text(im, text, begin_loc, font_size):
    font = ImageFont.truetype('./fonts/digital-7-mono.ttf', size=(font_size))
    draw = ImageDraw.Draw(im)
    draw.text(begin_loc, text, font=font)
    return im 

generate_text(image, current_time(), inital_text_location, 16)
image.show()
