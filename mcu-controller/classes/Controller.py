from BaseObject import BaseObject
from BluetoothConnectionManager import BluetoothConnectionManager
from classes.GpioManager import GpioManager
from classes.GpioMotor import GpioMotor

class Controller(BaseObject):
    def __init__(self):
        super().__init__()

        communication = BluetoothConnectionManager()
        gpioManager = GpioManager()

        driveMotor = GpioMotor(gpioManager, 11, 13)
        # handbrakeMotor = GpioMotor()
        # steeringServo = GpioServo()

