import RPi.GPIO as GPIO
import time

# Preparing the GPIO board:
GPIO.setmode(GPIO.BOARD)

# Making pin 15 an output pin:
GPIO.setup(15, GPIO.OUT)

# Making this pin send a PWM signal:
servo = GPIO.PWM(15, 50)

# Start with no signal:
servo.start(0)

# The start cycle is 2 so it won't turn backwars at start:
duty = 2

print("Rotating 180 degrees in 10 steps")

# Making a servo rotate forward and then backwards:
while duty <= 12:
    print("Run with cycle ",duty)
    
    servo.ChangeDutyCycle(duty)
    time.sleep(0.5)
    
    duty = duty + 1

# Stop giving a signal on pin:
servo.ChangeDutyCycle(0)

# Stop using this pin at all:
servo.stop()
    
# Cleanup GPIO Board:
GPIO.cleanup()

# Goodbye
print("Goodbye")
