from src.server import Server
from testEnv import SERVER_NAME, SERVER_PORT, BUFFER_SIZE

server = Server(SERVER_PORT, BUFFER_SIZE)

server.start()

