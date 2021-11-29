########
# Based on code by Keith Weaver
# Link: https://gist.github.com/keithweaver/3d5dbf38074cee4250c7d9807510c7c3
########

import bluetooth

class BluetoothConnectionManager:
	async def receiveMessages(self):
		server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )

		port = 1
		server_sock.bind(("",port))
		server_sock.listen(1)

		client_sock,address = server_sock.accept()
		print("Accepted connection from " + str(address))

		try:
			while True:
				data = bytearray(client_sock.recv(1024))

				print("Command: "+str(data[0])+", Value: "+str(data[1]))
		except:
			print("Client disconnected!")
		finally:
			client_sock.close()
			server_sock.close()

	# def sendMessageTo(targetBluetoothMacAddress):
	# 	port = 1
	# 	sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
	# 	sock.connect((targetBluetoothMacAddress, port))
	# 	sock.send("hello!!")
	# 	sock.close()

	def lookUpNearbyBluetoothDevices():
		nearby_devices = bluetooth.discover_devices()
		
		for bdaddr in nearby_devices:
			print(str(bluetooth.lookup_name( bdaddr )) + " [" + str(bdaddr) + "]")