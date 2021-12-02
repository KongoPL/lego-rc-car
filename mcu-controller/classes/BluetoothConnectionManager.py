########
# Based on code by Keith Weaver
# Link: https://gist.github.com/keithweaver/3d5dbf38074cee4250c7d9807510c7c3
########

from typing import Union
import bluetooth
import socket
import errno

class BluetoothConnectionManager:
	def __init__(self) -> None:
		self.serverSocket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

		self.serverSocket.bind(("",1))
		self.serverSocket.listen(1)
		# self.serverSocket.setblocking(False)

	def __del__(self) -> None:
		self.serverSocket.close()

	def awaitConnection(self) -> None:
		self.clientSocket, address = self.serverSocket.accept()
		# self.clientSocket.setblocking(False)
		self.clientSocket.settimeout(2)

	def tryGetMessage(self) -> Union[bool, bytearray, None]:
		if self.clientSocket == False:
			return False
		
		try:
			data = bytearray(self.clientSocket.recv(1024))

			return data
		except socket.error as e:
			return False

	# def sendMessageTo(targetBluetoothMacAddress):
	# 	port = 1
	# 	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	# 	sock.connect((targetBluetoothMacAddress, port))
	# 	sock.send("hello!!")
	# 	sock.close()

	# def lookUpNearbyBluetoothDevices():
	# 	nearby_devices = bluetooth.discover_devices()
		
	# 	for bdaddr in nearby_devices:
	# 		print(str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]")