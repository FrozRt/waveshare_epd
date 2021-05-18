import os
import sys
import logging
import time
from PIL import Image, ImageDraw, ImageFont

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd1in54

logging.basicConfig(level=logging.DEBUG)


def epd_run(pic_path: str):
    try:
        logging.info("epd1in54")

        # Display init, clear
        logging.debug("Initialize screen")
        display = epd1in54.EPD()
        display.init(display.lut_full_update)
        display.Clear(255)

        logging.info("drawing on the horizontal image")
        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        image = Image.new('1', (display.width, display.height), 255)
        draw = ImageDraw.Draw(image)
        draw.text((10, 10), "Hi, there!", font=font24, fill=0, align='left')
        display.display(display.getbuffer(image))
        time.sleep(2)

        white_back = Image.new('1', (display.width, display.height), 255)
        image.paste(white_back)

        # Show qr code
        logging.info("Display image file on screen")
        thanos = Image.open(pic_path)
        image.paste(thanos, (0, 0))
        display.display(display.getbuffer(image))  # Update display
        time.sleep(5)

#        logging.info("Clear screen")
#        display.Clear()

    except IOError as e:
        print(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd1in54.epdconfig.module_exit()
        exit()


if __name__ == '__main__':
    test_path = os.path.join(picdir, 'kit.jpg')
    epd_run(test_path)
