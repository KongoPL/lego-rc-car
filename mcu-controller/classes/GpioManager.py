import RPi.GPIO as GPIO

class GpioManager:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

    def __del__(self):
        GPIO.cleanup()

    def setPinAsOutput(self, pinNumber):
        GPIO.setup(pinNumber, GPIO.OUT)

    def setupPinForPWM(self, pinNumber: int, frequency: int, initialValue: float = 0):
        pinPWM = GPIO.PWM(pinNumber, frequency)

        pinPWM.start(initialValue)

        return pinPWM