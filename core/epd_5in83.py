import sys
import os

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd5in83
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

try:
    # Display init, clear
    display = epd5in83.EPD()
    display.init()
    display.Clear()  # 0: Black, 255: White
    w = display.height
    h = display.width

    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
    image = Image.new('1', (display.width, display.height), 255)
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), "Let's check it", font=font24, fill=0, align='left')
    display.display(display.getbuffer(image))
    display.Clear()

    # Show Thanos image.
    time.sleep(3)  # Pause for 3 seconds.
    thanos = Image.open(os.path.join(picdir, '5in65_n5.bmp'))
    image.paste(thanos, (0, 0))
    display.display(display.getbuffer(image))  # Update display
    time.sleep(10)
    display.Clear()

except IOError as e:
    print(e)
