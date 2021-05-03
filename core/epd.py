import os
import sys
import logging
import time
from PIL import Image, ImageDraw, ImageFont

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd5in83

logging.basicConfig(level=logging.DEBUG)


def epd_run(pic_path: str):
    try:
        logging.info("epd5in83")

        # Display init, clear
        logging.info("init and clear")
        display = epd5in83.EPD()
        display.init()
        display.Clear()  # 0: Black, 255: White

        logging.info("drawing on the horizontal image")
        font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
        image = Image.new('1', (display.width, display.height), 255)
        draw = ImageDraw.Draw(image)
        draw.text((150, 200), "Let's check qr code displaying", font=font24, fill=0, align='left')
        display.display(display.getbuffer(image))
        display.Clear()
        time.sleep(3)

        # Show Thanos image.
        logging.info("show image during the 10 secs")
        thanos = Image.open(pic_path)
        image.paste(thanos, (160, 80))
        display.display(display.getbuffer(image))  # Update display
        time.sleep(10)

        logging.info("clear display")
        display.Clear()

    except IOError as e:
        print(e)

    except KeyboardInterrupt:
        logging.info("ctrl + c:")
        epd5in83.epdconfig.module_exit()
        exit()


if __name__ == '__main__':
    test_path = os.path.join(picdir, 'qr.jpg')
    epd_run(test_path)
