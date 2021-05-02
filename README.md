### Project is aimed to connect raspberrypi with waveshare e-paper display  

This one is based on 5.83inch e-paper

1. Pin connection:  
Pin connections can be viewed in \lib\epdconfig.py and will be repeated here:  
VCC    ->    3.3  
GND    ->    GND  
DIN    ->    10(SPI0_MOSI)  
CLK    ->    11(SPI0_SCK)  
CS     ->    8(SPI0_CS0)  
DC     ->    25  
RST    ->    17  
BUSY   ->    24  


2. Install dependencies  
   sudo apt-get update  
   sudo apt-get install python3-pip  
    sudo apt-get install python3-pil  
    sudo apt-get install python3-numpy  
    sudo pip3 install Jetson.GPIO  
   



