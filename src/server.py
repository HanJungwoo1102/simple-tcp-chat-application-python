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
				length = str(len(decodedMessage))
				reversedMessage = ''.join(reversed(decodedMessage))
				message = 'The number of characters: ' + length + '\nThe reversed string(s): ' + reversedMessage
				connectionSocket.send(message.encode())
		except KeyboardInterrupt:
			print("Press Ctrl-C to terminate while statement")
			connectionSocket.close()
			pass