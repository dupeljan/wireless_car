import socket
import struct
from joystic import Dualshock_handler

class Socket_client:

	def __init__(self, address='192.168.1.39', port=7777):
		self.socket = socket.socket()
		self.socket.connect((address, port))

	def send(self,data):
		self.socket.send(struct.pack('>B', data ))


def main():
	joystick = Dualshock_handler(Socket_client())
	joystick.handle()

if __name__ == '__main__':
		main()	
