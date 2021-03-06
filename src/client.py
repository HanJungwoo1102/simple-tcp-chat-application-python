from socket import *

class Client:
	def __init__(self, serverName, serverPort, bufferSize):
		self.serverPort = serverPort
		self.serverName = serverName
		self.bufferSize = bufferSize

	def start(self):
		clientSocket = socket(AF_INET, SOCK_STREAM)
		clientSocket.connect((self.serverName, self.serverPort))

		try:
			while True:
				message = input('send message: ')

				encodedMessage = message.encode()

				clientSocket.send(encodedMessage)

				receivedMessage = clientSocket.recv(self.bufferSize)

				print(receivedMessage.decode())

		except KeyboardInterrupt:
			print("Press Ctrl-C to terminate while statement")
			clientSocket.close()
			pass

