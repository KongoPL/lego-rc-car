import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
#GPIO.setup(13,GPIO.OUT)

inA = GPIO.PWM(11,50000)
#inB = GPIO.PWM(13,50)

inA.start(0)
#inB.start(0)

wypelnienie = 5

try:
    while wypelnienie <= 100:
        print(wypelnienie)
        inA.ChangeDutyCycle(wypelnienie)
        time.sleep(1)
        wypelnienie += 5
        
    inA.ChangeDutyCycle(0)
    inA.stop()
    GPIO.cleanup()
finally:
    inA.ChangeDutyCycle(0)
    #inB.ChangeDutyCycle(0)
    inA.stop()
    #inB.stop()
    GPIO.cleanup()
    print("Goodbye")


