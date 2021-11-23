import RPi.GPIO as GPIO
import time

# Preparing the GPIO board:
GPIO.setmode(GPIO.BOARD)

# Making pin 15 an output pin:
GPIO.setup(15, GPIO.OUT)

frequency = 500

# Making this pin send a PWM signal:
servo = GPIO.PWM(15, frequency)

# Start with no signal:
servo.start(0)

# The start cycle is 2 so it won't turn backwars at start:
duty = 30

try:
    # cycle = (1 / frequency)
    while duty <= 100:
        servo.ChangeDutyCycle(duty)
        print("Run with cycle ",duty)
        duty = duty + 2
        time.sleep(1)
    
    xddd()
    
    
    print("Rotating 180 degrees in 10 steps")

    # Making a servo rotate forward and then backwards:
    while duty <= 24:
        print("Run with cycle ",duty)
        
        servo.ChangeDutyCycle(duty)
        time.sleep(5)
        
        duty = duty + 1
finally:
    # Stop giving a signal on pin:
    servo.ChangeDutyCycle(0)

    # Stop using this pin at all:
    servo.stop()
        
    # Cleanup GPIO Board:
    GPIO.cleanup()

    # Goodbye
    print("Goodbye")