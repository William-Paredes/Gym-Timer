#!/usr/bin/env python3
from gym import gym

#from rgbmatrix import RGBMatrix, RGBMatrixOptions

 options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.brightness = 50

matrix = RGBMatrix(options = options)

try:
    gymClock = gym()
    
    while True:
        gymClock.run()
        matrix.SetImage(gymClock.image.convert('RGB'))
        time.sleep(1)

except KeyboardInterrupt:
    sys.exit(0)
