from time import sleep
import RPi.GPIO as GPIO

print("IoT Greenhouse - Introduction to GPIO.")
print("Blink an LED")
print()

# Use board pin numbers
GPIO.setmode(GPIO.BOARD)
# Set pin 3 as LED output
GPIO.setup(3, GPIO.OUT)

for i in range(0, 50):
    GPIO.output(3,True)
    time.sleep(1)
    GPIO.output(3,False)
    time.sleep(1)

GPIO.cleanup()