from BaseObject import BaseObject
from BluetoothConnectionManager import BluetoothConnectionManager
from classes.GpioManager import GpioManager
from classes.GpioMotor import GpioMotor

class Controller(BaseObject):
	def __init__(self):
		super().__init__()

		self.communication = BluetoothConnectionManager()
		self.gpioManager = GpioManager()

		self.driveMotor = GpioMotor(self.gpioManager, 11, 13)
		# self.handbrakeMotor = GpioMotor()
		# self.steeringServo = GpioServo()

		self.communication.awaitConnection()

	def update(self, deltaTime):
		super().update(deltaTime)

		data = self.communication.tryGetMessage()

		if data == False:
			self.executeEmergencyStop()
			return

		self.executeCommand(data)

	def executeEmergencyStop(self):
		self.communication.awaitConnection()

	def executeCommand(self, data: bytearray):
		# print("Command "+str(data[0])+", "+str(data[1]))

		commandCode = int(data[0])

		if commandCode == ECommandCodes.Drive:
			axisValue = int8ToFloatAxis(byteToSignedInt(data[1]))

			self.drive(axisValue)
		elif commandCode == ECommandCodes.Steer:
			axisValue = int8ToFloatAxis(byteToSignedInt(data[1]))

			self.steer(axisValue)
		else:
			# raise "Unknown command!"
			pass

	def drive(self, value):
		self.driveMotor.drive(value)

	def steer(self, value):
		pass
	
def byteToSignedInt(byte):
	if byte > 127:
		return (256-byte) * (-1)
	else:
		return byte

def int8ToFloatAxis(number):
	if number > 0:
		return number / 127
	else:
		return number / 128

class ECommandCodes:
	Drive = 1
	Steer = 2
	Handbrake = 3
	Lights = 4
	