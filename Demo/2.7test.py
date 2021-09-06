import socket  # importing socket to get the hostname
from datetime import datetime  # Import datetime for screen refresh time
from gpiozero import Button  # import the Button control from gpiozero
import netifaces as ni  # Importing netifaces to gather network information
import epd2in7  # Importing epd2in7 as the driver
from signal import pause  # Importing pause so the program waits for an input
from PIL import Image, ImageDraw, ImageFont  # Importing image things for processing

# Eink Display is 264x176 Pixels (For reference)

# Keys are assigned to the corresponding pin
key1 = Button(5)
key2 = Button(6)
key3 = Button(13)
key4 = Button(19)


epd = epd2in7.EPD()  # get the display
epd.init()   # initialize the display
print("Clear...")  # prints to console, not the display, for debugging
epd.Clear()  # clear the display

hostname = socket.gethostname()

local_ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

def printToDisplay(string):
    HBlackImage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)

    draw = ImageDraw.Draw(HBlackImage)  # Create draw object and pass in the image layer we want to work with (HBlackImage)

    # Fonts with different sizes to be used
    font = ImageFont.truetype('Font.ttc', 18)  # Create our font, passing in the font file and font size
    fontsmall = ImageFont.truetype('Font.ttc', 12)  # Create our font, passing in the font file and font size
    fontsupersmall = ImageFont.truetype('Font.ttc', 8)  # Create our font, passing in the font file and font size

    draw.line((34, 22, 264, 22), fill=0)  # Draw top line
    draw.line((34, 23, 264, 23), fill=0)  # Draw top line (make thicker)
    draw.text((40, 2), string, font=font, fill=0)  # This is the overall Text

    # This is the bottom section of the screen with the date and time
    now = datetime.now()  # Gets the date and time now
    dt_string = now.strftime("%Y/%m/%d %H:%M:%S")  # Defines the layout of the datetime string
    draw.line((34, 158, 264, 158), fill=0)  # Draw bottom line
    draw.line((34, 159, 264, 159), fill=0)  # Draw bottom line (make thicker)
    draw.text((40, 160), f"Last Updated: {dt_string}     ", font=fontsmall, fill=0)  # Date Time String at bottom

    # This is the left section of the screen with key descriptions
    draw.line((34, 0, 34, 180), fill=0)  # Draw Vertical Key lines
    draw.line((35, 0, 35, 180), fill=0)  # Draw Vertical Key lines (make thicker)
    draw.text((2, 2), f"""Network \nInfo """, font=fontsupersmall, fill=0)  # Key1 Text
    draw.rectangle((0, 0, 34, 44), outline=0)  # Boxes around the key1 description
    draw.text((2, 52), f"""Network \nStats """, font=fontsupersmall, fill=0)  # Key2 Text
    draw.rectangle((0, 44, 34, 88), outline=0)  # Boxes around the key2 description
    draw.text((2, 102), f"""CPU \nInfo """, font=fontsupersmall, fill=0)  # Key3 Text
    draw.rectangle((0, 88, 34, 132), outline=0)  # Boxes around the key3 description
    draw.text((2, 152), f"""System \nTools """, font=fontsupersmall, fill=0)  # Key4 Text
    draw.rectangle((0, 132, 34, 176), outline=0)  # Boxes around the key4 description

    epd.display(epd.getbuffer(HBlackImage))


def handleBtnPress(btn):
    # python hack for a switch statement. The number represents the pin number and
    # the value is the message it will print
    switcher = {
        5: f"{net_info}",
        6: f"{net_stats}",
        13: f"{cpu_info}",
        19: f"{tools}"
    }

    # get the string based on the passed button and send it to printToDisplay()
    msg = switcher.get(btn.pin.number, "Error")
    printToDisplay(msg)

# These are the screens that are called when you press a button
net_info = f"""NETWORK INFORMATION
HOSTNAME: {hostname}
[ETH0]
MAC: {ni.ifaddresses('eth0')[ni.AF_LINK][0]['addr']}
IP: {ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']}


"""

net_stats = """NETWORK STATISTICS
This is where I
want my network stats 




"""

cpu_info = """CPU INFORMATION
Here I list 
CPU info  




"""

tools = """TOOLS
This screen allows 
me to shut things down 
in theory...



"""

printToDisplay(net_info)  # Default screen

# tell the button what to do when pressed
key1.when_pressed = handleBtnPress
key2.when_pressed = handleBtnPress
key3.when_pressed = handleBtnPress
key4.when_pressed = handleBtnPress

pause()
