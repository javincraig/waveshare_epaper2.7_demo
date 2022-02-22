# Waveshare e-paper 2.7inch demo
This is a demo for the Waveshare 2.7" epaper display.

# Video for this code here: https://youtu.be/o1eppNELKj0

* I followed this guide and took some code. I tried to reduce it down a bit and expand some things to get it to work.
https://dev.to/ranewallin/getting-started-with-the-waveshare-2-7-epaper-hat-on-raspberry-pi-41m8

* The wiki for the device:
https://www.waveshare.com/wiki/2.7inch_e-Paper_HAT

*UPDATE 2/21/2022 by Aaron Hickman
Building upon code

The following is how I got it working on a Raspberry Pi 4
---
sudo raspi-config

Interface Options -> SPI -> Would you like the interface to be enabled (Select Yes)


sudo apt-get install python3-venv

python3 -m venv einkdemo

source einkdemo/bin/activate

cd einkdemo/


Copy all the files in this git to einkdemo

sudo apt-get install python3-rpi.gpio python3-pil python3-smbus python3-dev libopenjp2-7

pip3 install wheel

pip3 install gpiozero netifaces spidev rpi.gpio pillow

Run the test app

python3 2.7test.py

2.7test.py is the script the script that uses the buttons

2.7image.py displays an image. 
