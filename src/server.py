from socket import *

class Server:
	def __init__(self, port, bufferSize):
		self.port = port
		self.bufferSize = bufferSize

	def start(self):
		serverSocket = socket(AF_INET, SOCK_STREAM)

		serverSocket.bind(('', self.port))

		serverSocket.listen(1)

		print("The server is ready to receive.")

		connectionSocket, clientAddress = serverSocket.accept()
		try:
			while True:
				receivedMessage = connectionSocket.recv(self.bufferSize)
				
				decodedMessage = receivedMessage.decode()

				message = 'The number of characters: ' + str(len(decodedMessage)) + '\nThe reversed string(s): ' + ''.join(reversed(decodedMessage))

				connectionSocket.send(message.encode())
		except KeyboardInterrupt:
			print("Press Ctrl-C to terminate while statement")
			connectionSocket.close()
			pass