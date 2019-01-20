import pygame 
import socket

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

class Client:
	
	def __init__(self, address='192.168.1.39', port=7777):
		self.state = "stop"
		self.socket = socket.socket()
		self.socket.connect((address, port))

	def send(self,state):
		self.socket.send(States[state])

class Dualshock_handler:
	def __init__(self):
		self.sender = Client()
		pygame.init()
		pygame.joystick.init()
		self.joystick = pygame.joystick.Joystick(0)
		self.joystick.init()

	def handle(self):
		clock = pygame.time.Clock()
		while True:
			for event in pygame.event.get(): # User did something
		        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
				if event.type == pygame.JOYHATMOTION:
					hat = self.joystick.get_hat( 0 )
					if hat == (0,1):
						self.sender.send("forward")
					elif hat == (0,-1):
						self.sender.send("backward")
					elif hat == (-1,0):
						self.sender.send("left")
					elif hat == (1,0):
						self.sender.send("right")
					elif hat == (-1,1):
						self.sender.send("f_left")
					elif hat == (1,1):
						self.sender.send("f_right")
					elif hat == (-1,-1):
						self.sender.send("b_left")
					elif hat == (1,-1):
						self.sender.send("b_right")
					elif hat == (0,0):
						self.sender.send("stop")

			clock.tick(20)

def main():
	joystick = Dualshock_handler()
	joystick.handle()

if __name__ == '__main__':
		main()	
