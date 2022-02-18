import time
import board
from digitalio import DigitalInOut, Pull
import neopixel

# declare some color constants
RED = 0xff0000
GREEN = 0x00ff00
BLUE = 0x0000ff
YELLOW = 0xffff00
CYAN = 0x00ffff
MAGENTA = 0xff00ff
WHITE = 0xffffff
OFF = 0x000000

# initialize the neopixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
# color wheel
colors = [OFF, RED, MAGENTA, BLUE, CYAN, GREEN, YELLOW, WHITE]

# a variable to track the number of clicks
click_count = 0

# declare some input for button a and b
button_a = DigitalInOut(board.BUTTON_A)
button_a.switch_to_input(pull=Pull.DOWN)
button_b = DigitalInOut(board.BUTTON_B)
button_b.switch_to_input(pull=Pull.DOWN)

# a variable to track the on/off state of the neopixels
pixels_state = False

# a varible to track the previous reading of the button
button_a_pre = button_a.value
button_b_pre = button_b.value

while True:
    # gather input values as an integer
    button_a_read = button_a.value
    button_b_read = button_b.value

    if button_a_read != button_a_pre:
        # the button value has changed
        # save the read to previous for next iteration of the loop
        button_a_pre = button_a_read
        if button_a_read:
            # the button changed from False to True
            print("The button changed Not to Pressed")
            # toggle the pixels_state variable
            pixels_state = not pixels_state

    # do output based on input and calculated variables
    if pixels_state:
        # fill the pixels with color
        pixels.fill(CYAN)
    else:
        # fill the pixels black
        pixels.fill(OFF)

    if button_b_read != button_b_pre:
        # the button value has changed
        # save the read to previous for next iteration of the loop
        button_b_pre = button_b_read
        if button_b_read:
            # the button a changed from False to True
            print("The button changed Not to Pressed")
            # decrement the click_count variable
            click_count += 1
            print("click count is:", click_count)

    click_modulo = click_count % len(colors)
    print(click_modulo)
    # use click_modulo to select a color from the colors list
    color = colors[click_modulo]

    # do output based on input and calculated variables
    pixels.fill(color)

    # sleep to see changes in the serial monitor
    time.sleep(0.1)
