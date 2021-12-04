from BaseObject import BaseObject
from BluetoothConnectionManager import BluetoothConnectionManager
from GpioServo import GpioServo
from classes.GpioManager import GpioManager
from classes.GpioMotor import GpioMotor
from config import CONFIG
import time

class Controller(BaseObject):
	def __init__(self):
		super().__init__()

		self.communication = BluetoothConnectionManager()
		self.gpioManager = GpioManager()

		self.driveMotor = GpioMotor(
			self.gpioManager, 
			CONFIG["driveMotor"]["pinForward"], 
			CONFIG["driveMotor"]["pinBackward"]
		)
		self.handbrakeMotor = GpioMotor(
			self.gpioManager,
			CONFIG["handbrakeMotor"]["pinForward"],
			CONFIG["handbrakeMotor"]["pinBackward"],
		)
		self.steeringServo = GpioServo(
			self.gpioManager, 
			CONFIG["steeringServo"]["pin"], 
			CONFIG["steeringServo"]["forwardPulseWidthRange"], 
			CONFIG["steeringServo"]["backwardPulseWidthRange"],
			CONFIG["steeringServo"]["valueShift"]
		)
		self.isHandbrakeEnabled = False

		self.communication.awaitConnection()


	def update(self, deltaTime):
		super().update(deltaTime)

		data = self.communication.tryGetMessage()

		if data == False:
			self.executeEmergencyStop()
			return

		self.executeCommand(data)


	def executeEmergencyStop(self):
		self.drive(0)
		self.steer(0)
		# self.handbrake(True)
		# time.sleep(5)
		# self.handbrake(False)
		self.communication.awaitConnection()


	def executeCommand(self, data: bytearray):
		commandCode = int(data[0])

		if commandCode == ECommandCodes.Drive:
			if(self.isHandbrakeEnabled):
				return

			axisValue = int8ToFloatAxis(byteToSignedInt(data[1]))

			self.drive(axisValue)
		elif commandCode == ECommandCodes.Steer:
			axisValue = int8ToFloatAxis(byteToSignedInt(data[1]))

			self.steer(axisValue)
		elif commandCode == ECommandCodes.HandbrakeStart:
			self.handbrake(True)
		elif commandCode == ECommandCodes.HandbrakeEnd:
			self.handbrake(False)
		else:
			# raise "Unknown command!"
			pass


	def drive(self, value):
		self.driveMotor.rotate(value)


	def steer(self, value):
		self.steeringServo.rotate(value)


	def handbrake(self, enable: bool = True):
		self.isHandbrakeEnabled = enable

		if enable:
			self.handbrakeMotor.rotate(1)

			if CONFIG["handbrakeMotor"]["usingStopsDriveMotor"]:
				self.driveMotor.rotate(0)
		else:
			self.handbrakeMotor.rotate(0)


	
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
	HandbrakeStart = 3
	HandbrakeEnd = 4
	