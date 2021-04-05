from src.client import Client
from testEnv import SERVER_NAME, SERVER_PORT, BUFFER_SIZE

client = Client(SERVER_NAME, SERVER_PORT, BUFFER_SIZE)

client.start()

