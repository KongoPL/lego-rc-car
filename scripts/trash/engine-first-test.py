import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
#GPIO.setup(13,GPIO.OUT)

inA = GPIO.PWM(11,10)
#inB = GPIO.PWM(13,50)

inA.start(0)
#inB.start(0)

try:
    #while True:
    inA.ChangeDutyCycle(100)
    time.sleep(15000)
    inA.ChangeDutyCycle(0)

finally:
    inA.ChangeDutyCycle(0)
    #inB.ChangeDutyCycle(0)
    inA.stop()
    #inB.stop()
    GPIO.cleanup()
    print("Goodbye")

