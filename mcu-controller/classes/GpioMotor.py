from _typeshed import Self
from classes.GpioManager import GpioManager

class GpioMotor:
    def __init__(self, gpioManager: GpioManager, pinForward: int, pinBackward: int):
        super().__init__()

        gpioManager.setPinAsOutput(pinForward)
        gpioManager.setPinAsOutput(pinBackward)
        self.pinForwardPWM = gpioManager.setupPinForPWM(pinBackward)
        self.pinBackwardPWM = gpioManager.setupPinForPWM(pinBackward)


    def drive(self, direction: float):
        if direction > 0:
            self.__driveForward(direction)
        else:
            self.__driveBackwards(-direction)

    def __driveForward(self, direction: float):
        self.pinBackwardPWM.ChangeDutyCycle(0)
        self.pinForwardPWM.ChangeDutyCycle(direction)

    def __driveBackwards(self, direction: float):
        self.pinForwardPWM.ChangeDutyCycle(0)
        self.pinBackwardPWM.ChangeDutyCycle(direction)