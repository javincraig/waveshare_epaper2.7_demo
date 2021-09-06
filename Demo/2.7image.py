#import sys
#sys.path.insert(1, "./lib")
import epd2in7
from PIL import Image, ImageDraw, ImageFont

# Eink Display is 264x176 Pixels

epd = epd2in7.EPD()  # get the display
epd.init()  # initialize the display
print("Clear...")  # prints to console, not the display, for debugging
epd.Clear()  # clear the display

Himage = Image.open('mylittlelan.bmp')
epd.display(epd.getbuffer(Himage))

