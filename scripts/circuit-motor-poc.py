import RPi.GPIO as GPIO
import time

# Preparing the GPIO board:
GPIO.setmode(GPIO.BOARD)

# Making pins 11 and 13 an output pins:
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

# Making those pins a pins that will send a PWM signal:
inA = GPIO.PWM(11, 50000)
inB = GPIO.PWM(13, 50000)

# Start with no signal on both pins:
inA.start(0)
inB.start(0)

try:
    # Set signal on pin 11 (INA)
    inA.ChangeDutyCycle(100)
    
    # Just wait a moment :)
    time.sleep(5)
finally:
    # Stop giving a signal on both pins:
    inA.ChangeDutyCycle(0)
    inB.ChangeDutyCycle(0)
    
    # Stop using those pins at all:
    inA.stop()
    inB.stop()
        
    # Cleanup GPIO Board:
    GPIO.cleanup()

    # Goodbye
    print("Goodbye")

