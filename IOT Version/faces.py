from time import sleep
from ili9341 import Display, color565,rotate_point
from machine import Pin, SPI
import time
import math
import random
 
# Constants
SPI_SPEED = 20000000
DC_PIN = Pin(6)
CS_PIN = Pin(17)
RST_PIN = Pin(7)
EYE_COLOR = color565(0, 0, 0)
MOUTH_COLOR = color565(255, 0, 0)
black = color565(0, 0, 0)
white = color565(255, 255, 255)
blue=color565(0,0,255)
red=color565(255,0,0)
light_red=color565(255,100,100)
sky_blue=color565(135,206,235)
light_grey=color565(211,211,211)
gold=color565(255,215,0)
DISPLAY_WIDTH=240
DISPLAY_HEIGHT=320
sizea=40
sizeb=40
 
# Create display object
spi = SPI(1, baudrate=SPI_SPEED, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=DC_PIN, cs=CS_PIN, rst=RST_PIN)

from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI

# Constants
SPI_SPEED = 10000000
DC_PIN = Pin(6)
CS_PIN = Pin(17)
RST_PIN = Pin(7)
BLUE = color565(0, 0, 255)

# Create display object
spi = SPI(1, baudrate=SPI_SPEED, sck=Pin(14), mosi=Pin(15))
display = Display(spi, dc=DC_PIN, cs=CS_PIN, rst=RST_PIN)

def rain(x0, y0, color):
    display.fill_circle(x0 - 30, y0, 20, color)
    display.fill_circle(x0 + 30, y0, 20, color)
    display.fill_circle(x0, y0 - 20, 20, color)
    display.fill_ellipse(x0, y0, 20, 15, color)
    drop_height = 10
    drop_width = 4
    erase_color = 0x0000
    draw_color = 0x001F

    for i in range(1, drop_height + 1):
        # Erase the top portion of the first raindrop
        display.fill_hrect(x0, y0 + 25 + i - 1, drop_width, 4, erase_color)

        # Draw the bottom portion of the first raindrop
        display.fill_hrect(x0, y0 + 25 + i, drop_width, 4, draw_color)

        # Erase the top portion of the second raindrop
        display.fill_hrect(x0 - 10, y0 + 35 + i - 1, drop_width, 4, erase_color)

        # Draw the bottom portion of the second raindrop
        display.fill_hrect(x0 - 10, y0 + 35 + i, drop_width, 4, draw_color)

        # Erase the top portion of the third raindrop
        display.fill_hrect(x0 + 10, y0 + 30 + i - 1, drop_width, 4, erase_color)

        # Draw the bottom portion of the third raindrop
        display.fill_hrect(x0 + 10, y0 + 30 + i, drop_width, 4, draw_color)

        # Wait for a small delay to control animation speed
        time.sleep_ms(10)
    display.partial_clear(x0-20,y0+2*drop_height+8 ,40 , 22, black)


def eyes1(x0,y0, sizea,sizeb, eye_color):
    display.fill_ellipse(x0, y0, sizea, sizea, eye_color)
    display.fill_ellipse(x0+120, y0, sizea, sizea, eye_color)
    display.fill_rectangle_inclined(x0-54,y0-52, 96, 48, -30, black)
    display.fill_rectangle_inclined(x0-54+133,y0-45, 96, 40, 30, black)



# Draw faces that can be dynamically animated
def blank_face(sizea,sizeb,color): 
    display.fill_ellipse(64,72, sizea,sizeb, color)
    display.fill_ellipse(176,72, sizea,sizeb, color)
    display.fill_half_ellipse(119,220,96,48, white)

    return

def blink_face(sizea,sizeb, eye_color):
    display.partial_clear(0,0,240,150,black)
    display.fill_ellipse(24+sizea,32+sizeb, sizea,sizeb, eye_color)
    display.fill_ellipse(216-sizea,32+sizeb, sizea,sizeb, eye_color)
    display.fill_half_ellipse(119,220,96,48, white)
    return


def hot_face(sizea,sizeb,eye_color):
    eyes1(60,72,sizea,sizeb,white)
    display.fill_circle(119,220,40, eye_color)
    display.fill_ellipse(40,200,10,30, blue)
    display.fill_ellipse(120,60,10,30, blue)
    display.fill_ellipse(200,150,10,30, blue)
    return

def grumpy_face(sizea,sizeb,eye_color):

    display.fill_half_ellipse(24+sizea,32+sizeb, sizea,sizea,eye_color)
    display.fill_half_ellipse(216-sizea,32+sizeb, sizea,sizea, eye_color)
    display.fill_ellipse(119,240,96,48, white)
    display.fill_half_ellipse(119,240,96,48, black)

def thirsty_face(sizea, sizeb, eye_color):
    eyes1(60,72,sizea,sizeb,white)
    display.fill_ellipse(119,220,96,32, white)
    display.fill_ellipse(119,265,60,30, black)
    display.fill_half_ellipse(119,235,27,30, red)

def happy_face(sizea,sizeb,eye_color):
    display.fill_ellipse(64,72, sizea,sizeb, eye_color)
    display.fill_ellipse(176,72, sizea,sizeb, eye_color)
    display.fill_triangle(64,77,24,122,104,122, black)
    display.fill_triangle(176,77,136,122,216,122, black)
    display.fill_circle(51,220,40,light_red)
    display.fill_circle(187,220,40,light_red)
    display.fill_half_ellipse(119,210,80,50, white)


def cold_face(sizea,sizeb,eye_color):
    eyes1(60,72,sizea,sizeb,sky_blue)
    display.fill_circle(79,240,20, blue)
    display.fill_circle(159,240,20, blue)
    display.fill_rectangle(79,220,80,40, white)
    display.fill_rectangle(79,235,80,10, blue)

def vampire_face(sizea,sizeb,eye_color):
    display.fill_ellipse(64,72, sizea//2,sizeb, gold)
    display.fill_ellipse(176,72, sizea//2,sizeb, gold)
    display.fill_half_ellipse(119,200,96,50, red)
    display.fill_half_ellipse(119,200,96,47, black)
    display.fill_triangle(70,240,80,240,75,300, light_red)
    display.fill_triangle(170,240,180,240,175,300, light_red)

def sad_face(sizea,sizeb,eye_color):
    #code for sad face
    return

def run(string):
        if string.lower().strip()=="grumpy":
            grumpy_face(sizea,sizeb, white)
        elif string.lower().strip()=="happy":
            happy_face(sizea,sizeb, white)
        elif string.lower().strip()=="hot":
            hot_face(sizea,sizeb, white)
        elif string.lower().strip()=="cold":
            cold_face(sizea,sizeb, white)
        elif string.lower().strip()=="vampire":
            vampire_face(sizea,sizeb, white)
        elif string.lower().strip()=="thirsty":
            thirsty_face(sizea,sizeb, white)
        elif string.lower().strip()=="blink":
            blink_face(sizea,sizeb, white)
        elif string.lower().strip()=="blank":
            blank_face(sizea,sizeb, white)
        elif string.lower().strip()=="sad":
            sad_face(sizea,sizeb, white)
        elif string.lower().strip()=="rain":
            rain(170,140, light_grey)

        else:
            display.clear(black)
