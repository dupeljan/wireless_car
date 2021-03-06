import socket
from pynput import keyboard
import struct


RETURN_CHAR = 'r'
#BUTTONS
FORWARD_LED = 'l'
SIGNAL_KEY = 'p'
FORWARD_KEY = 'w'
BACKWARD_KEY = 's'
LEFT_KEY = 'a'
RIGHT_KEY = 'd'
RET_FORWARD_KEY = RETURN_CHAR + 'w'
RET_BACKWARD_KEY = RETURN_CHAR + 's'
RET_LEFT_KEY = RETURN_CHAR + 'a'
RET_RIGHT_KEY = RETURN_CHAR + 'd'
States  = {
		"stop" : b'0',
		"forward" : b'1',
		"backward" : b'2',
		"left" : b'3',
		"right" : b'4', 
		"f_left" : b'5',
		"f_right" : b'6',
		"b_left" : b'7',
		"b_right" : b'8',
}

tr_commands = {
	"stop" : 48,
	"forward" : 49,
	"backward" : 50,
	"left" : 51,
	"right" : 52,
	"straight" : 53 
} 

Commands = {
	"lights" : 57,
	"signal" : 54,
}

class Client:
	
	def __init__(self, address='192.168.1.39', port=7777):
		self.state = "stop"
		self.socket = socket.socket()
		self.socket.connect((address, port))

	def receive(self):
		data = self.socket.recv(1024)
		print(' receve ', data)

	def translate_send(self,state):
		
		if state == "stop":
			arg = (tr_commands["stop"],tr_commands["straight"])
		elif state == "forward":
			arg = (tr_commands["forward"],tr_commands["straight"])
		elif state == "backward":
			arg = (tr_commands["backward"],tr_commands["straight"])
		elif state == "left":
			arg = (tr_commands["stop"],tr_commands["left"])
		elif state == "right":
			arg = (tr_commands["stop"],tr_commands["right"])
		elif state == "f_left":
			arg = (tr_commands["forward"],tr_commands["left"])
		elif state == "f_right":
			arg = (tr_commands["forward"],tr_commands["right"])
		elif state == "b_left":
			arg = (tr_commands["backward"],tr_commands["left"])
		elif state == "b_right":
			arg = (tr_commands["backward"],tr_commands["right"])

		for i in range(2):
			self.socket.send(struct.pack('>B', arg[i] ) )

	def send(self,key):
		state = self.state

		if self.state == "stop":
			if key == FORWARD_KEY:
				self.state = "forward"
			elif key == BACKWARD_KEY:
				self.state = "backward"
			elif key == LEFT_KEY:
				self.state = "left"
			elif key == RIGHT_KEY:
				self.state = "right"
			
		elif self.state == "forward":
			if key == LEFT_KEY:
				self.state = "f_left"
			elif key == RIGHT_KEY:
				self.state = "f_right"
			elif key == RET_FORWARD_KEY:
				self.state = "stop"
		
		elif self.state == "backward":
			if key == LEFT_KEY:
				self.state = "b_left"
			elif key == RIGHT_KEY:
				self.state = "b_right"
			elif key == RET_BACKWARD_KEY:
				self.state = "stop"

		elif self.state == "left":
			if key == FORWARD_KEY:
				self.state = "f_left"
			elif key == BACKWARD_KEY:
				self.state = "b_left"
			elif key == RET_LEFT_KEY:
				self.state = "stop"

		elif self.state == "right":
			if key == FORWARD_KEY:
				self.state = "f_right"
			elif key == BACKWARD_KEY:
				self.state = "b_right"
			elif key == RET_RIGHT_KEY:
				self.state = "stop"

		elif self.state == "f_left":
			if key == RET_FORWARD_KEY:
				self.state = "left"
			elif key == RET_LEFT_KEY:
				self.state = "forward"

		elif self.state == "f_right":
			if key == RET_FORWARD_KEY:
				self.state = "right"
			elif key == RET_RIGHT_KEY:
				self.state = "forward"

		elif self.state == "b_left":
			if key == RET_BACKWARD_KEY:
				self.state = "left"
			elif key == RET_LEFT_KEY:
				self.state = "backward"

		elif self.state == "b_right":
			if key == RET_BACKWARD_KEY:
				self.state = "right"
			elif key == RET_RIGHT_KEY:
				self.state = "backward"
		
		if state != self.state:
			self.translate_send(self.state)
		
		elif key == FORWARD_LED:
			self.socket.send(struct.pack('>B', Commands["lights"] ))
		elif key == SIGNAL_KEY:
			self.socket.send(struct.pack('>B', Commands["signal"]) )


sender = Client()

def on_press(key):
	try:
		sender.send(key.char)
		#self.socket.send(bytes(key.char,"utf-8"))
		#sender.receive()
		
	except AttributeError:
		print('special key {0} pressed'.format(key))

def on_release(key):
	sender.send(RETURN_CHAR+key.char)
   	#self.socket.send(b'r'+key.char)

def main():
	# Collect events until released
	with keyboard.Listener(
	        on_press= on_press,
	        on_release= on_release) as listener:
	    listener.join()

	self.socket.close()

	

if __name__ == '__main__':
	main()
 



	
