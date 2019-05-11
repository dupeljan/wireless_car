import serial as s
import struct
from joystic import Dualshock_handler

class Serial_client:
	def __init__(self):
		# Connect to arduino
		self.serial = s.Serial("/dev/ttyUSB0",9600)
	
	def send(self,data):
		self.serial.write(struct.pack('>B', data ) )
	def send_ext(self,data,value):
		print(value)
		self.serial.write( str.encode( chr(data) ) )


def main():
	joystick = Dualshock_handler(Serial_client())
	joystick.handle()

if __name__ == '__main__':
		main()	
