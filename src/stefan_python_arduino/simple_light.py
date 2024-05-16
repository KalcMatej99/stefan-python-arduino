import pyfirmata # Import pyFirmata
import time # Import the time

#port = 'COM3'# Windows
port = '/dev/ttyACM0' # Linux
#port = '/dev/tty.usbmodem11401'# Mac

HIGH = True# Create a high state for turn on led 
LOW = False # Create a low state for turn off led 
board = pyfirmata.Arduino(port) # Initialize the communication with the Arduino card
LED_pin = board.get_pin('d:8:o') # Initialize the pin (d => digital, 13 => Number of the pin, o => output)

LED_pin.write(LOW) # Turn off the led
for i in range(10): # Loop to blink the micro-led dix times
    print("Blink")
    LED_pin.write(HIGH) # Turn on the led
    time.sleep(0.5) # Delay of 0.5 seconds
    print("Blink 2")
    LED_pin.write(LOW) # Turn off the led
    time.sleep(0.5) # Delay of 0.5 seconds

board.exit() # Closing the communication with the Arduino card