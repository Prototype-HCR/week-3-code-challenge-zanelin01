import board
import time
from digitalio import DigitalInOut, Direction, Pull
import neopixel
pixels = neopixel.NeoPixel(board.A1, 30)   


# declare a digitial input
button_1 = DigitalInOut(board.A3)
button_1.direction = Direction.INPUT

# A variable to track the LED led state
led_state = False


while True:
    # gather all input values from sensors
    # print the value of our button_a object
    button_1_read = button_1.value
    print("button 1 read is:", button_1_read)

    if button_1_read == False:
        pixels[0] = (255, 150, 0)       # yellow
        pixels[1] = (255, 0, 0)         # red
        pixels[2] = (255, 255, 255)     # white
        pixels[3] = (255, 150, 0)
        pixels[4] = (255, 0, 0)
        pixels[5] = (255, 255, 255) 
        pixels[6] = (255, 150, 0)
        pixels[7] = (255, 0, 0)
        pixels[8] = (255, 255, 255) 
        pixels[9] = (255, 150, 0)
        pixels[10] = (255, 0, 0)
        pixels[11] = (255, 255, 255) 
        pixels[12] = (255, 150, 0)
        pixels[13] = (255, 0, 0)
        pixels[14] = (255, 255, 255) 
        pixels[15] = (255, 150, 0)
        pixels[16] = (255, 0, 0)
        pixels[17] = (255, 255, 255) 
        pixels[18] = (255, 150, 0)
        pixels[19] = (255, 0, 0)
        pixels[20] = (255, 255, 255) 
        pixels[21] = (255, 150, 0)
        pixels[22] = (255, 0, 0)
        pixels[23] = (255, 255, 255) 
        pixels[24] = (255, 150, 0)
        pixels[25] = (255, 0, 0)
        pixels[26] = (255, 255, 255) 
        pixels[27] = (255, 150, 0)
        pixels[28] = (255, 0, 0)
        pixels[29] = (255, 255, 255) 
        pixels[30] = (255, 150, 0)
        pixels[31] = (255, 255, 255) 
    else:
        led_state = True
        pixels.fill(0)
    time.sleep(0.2)




# import modules
import board
from digitalio import DigitalInOut, Direction
import time
import neopixel
pixels = neopixel.NeoPixel(board.A1, 30) 
pixels.fill((255, 150, 0))
# variables to control sleep time for blinking
onTime = 0.3
offTime = 0.3

led_state = True
# loop forever
while True:
    # turn the led on (stand for S)
    led_state = True
    pixels.fill((255, 0, 0))
    led_state = False
    time.sleep(onTime)
    pixels.fill(0)
    time.sleep(offTime)
    


