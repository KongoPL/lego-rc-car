from classes.GpioManager import GpioManager

class GpioMotor:
    def __init__(self, gpioManager: GpioManager, pinForward: int, pinBackward: int):
        super().__init__()

        gpioManager.setPinAsOutput(pinForward)
        gpioManager.setPinAsOutput(pinBackward)
        self.pinForwardPWM = gpioManager.setupPinForPWM(pinForward, 100)
        self.pinBackwardPWM = gpioManager.setupPinForPWM(pinBackward, 100)

    def drive(self, direction: float):
        if direction > 0:
            self.__driveForward(direction)
        else:
            self.__driveBackwards(-direction)

    def __driveForward(self, direction: float):
        direction = max(0, min(direction, 1))

        self.pinBackwardPWM.ChangeDutyCycle(0)
        self.pinForwardPWM.ChangeDutyCycle(direction * 100)

    def __driveBackwards(self, direction: float):
        direction = max(0, min(direction, 1))

        self.pinForwardPWM.ChangeDutyCycle(0)
        self.pinBackwardPWM.ChangeDutyCycle(direction * 100)