import serial as s
import pygame 
import time

commands  = {
		"ext_forward" : 10,
		"ext_backward" : 20,
		"ext_f_left"	: 11,
		"ext_f_right"	: 12,
		"ext_b_left"	: 21,
		"ext_b_right"	: 22,
		"stop" : 48,
		"forward" : 49,
		"backward" : 50,
		"left" : 51,
		"right" : 52, 
		"f_left" : 53,
		"f_right" : 54,
		"b_left" : 55,
		"b_right" : 56,
		"lights"  : 57
}

class Client:
	def __init__(self):
		# Connect to arduino
		self.serial = s.Serial("/dev/ttyUSB0",9600)
	
	def send(self,data):
		print(data)
		self.serial.write(str.encode(chr(commands[data])))
	def send_ext(self,data,value):
		print(data)
		print(value)
		self.serial.write( str.encode( chr(commands[data]) + chr(value) ) )

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
					speed = round( ( self.joystick.get_axis(4) - self.joystick.get_axis(3) ) * 127.5 )
					
					rotation = self.joystick.get_axis(0)

					if speed == 0:
						if rotation > 0.5:
							self.sender.send("right")
						elif rotation < -0.5:
							self.sender.send("left")
						else:
							self.sender.send("stop")
					elif abs(rotation) < 0.5:
						if speed > 0:
							self.sender.send_ext("ext_forward",speed)
						else:
							self.sender.send_ext("ext_backward",-speed)
					elif rotation > 0.5:
						if speed > 0:
							self.sender.send_ext("ext_f_right",speed)
						else:
							self.sender.send_ext("ext_b_right",-speed)
					else:
						if speed > 0:
							self.sender.send_ext("ext_f_left",speed)
						else:
							self.sender.send_ext("ext_b_left",-speed)
					
				if event.type == pygame.JOYBUTTONDOWN:
					if self.joystick.get_button(4) or self.joystick.get_button(5):
						self.sender.send("lights")
					
			#time.sleep(0.3)
			#self.clock.tick(20)

def main():
	joystick = Dualshock_handler()
	joystick.handle()

if __name__ == '__main__':
		main()	
