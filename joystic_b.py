import serial as s
import pygame 
import struct

commands  = {
		"stop" : 48,
		"forward" : 49,
		"backward" : 50,
		"left" : 51,
		"right" : 52, 
		"straight" : 53,
		"lights"  : 57
}

class Client:
	def __init__(self):
		# Connect to arduino
		self.serial = s.Serial("/dev/ttyUSB0",9600)
	
	def send(self,data):
		self.serial.write(struct.pack('>B', data ) )
	def send_ext(self,data,value):
		print(value)
		self.serial.write( str.encode( chr(data) ) )

class Dualshock_handler:
	def __init__(self):
		self.sender = Client()
		pygame.init()
		pygame.joystick.init()
		self.joystick = pygame.joystick.Joystick(0)
		self.joystick.init()
		# Used to manage how fast the screen updates
		self.clock = pygame.time.Clock()

	def handle(self):
		clock = pygame.time.Clock()
		while True:
			for event in pygame.event.get(): # User did something
		        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
				if event.type == pygame.JOYAXISMOTION:
					'''
					Axis 4 - R2
					Axis 3 - L2
					Button 4 - L1
					Button 5 - L2
					'''
					speed = round( ( self.joystick.get_axis(4) - self.joystick.get_axis(3) ) * 48.5 )
					print("speed ",speed)
					if speed == 0:
						self.sender.send(commands["stop"])
					elif speed > 0:
						self.sender.send(speed + 60)
					else:
						self.sender.send(-speed+158)

					rotation = self.joystick.get_axis(0)
					if rotation > 0.5:
						self.sender.send(commands["right"])
					elif rotation < -0.5:
						self.sender.send(commands["left"])
					else:
						self.sender.send(commands["straight"])

					
					
				if event.type == pygame.JOYBUTTONDOWN:
					if self.joystick.get_button(4) or self.joystick.get_button(5):
						self.sender.send(commands["lights"])
					
			#time.sleep(0.3)
			#self.clock.tick(20)

def main():
	joystick = Dualshock_handler()
	joystick.handle()

if __name__ == '__main__':
		main()	
