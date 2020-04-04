import pyaudio  
import wave  
'''
class Player:
'''	

'''fast WAW player'''
def play_wav(file_name):
	#define stream chunk   
	chunk = 1024  
	#open a wav format music  
	f = wave.open(file_name,"rb")  
	#instantiate PyAudio  
	p = pyaudio.PyAudio()  
	#open stream  
	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
	                channels = f.getnchannels(),  
	                rate = f.getframerate(),  
	                output = True)  
	#read data  
	data = f.readframes(chunk)  
		#play stream  
	while data:  
	    stream.write(data)  
	    data = f.readframes(chunk)  

	#stop stream  
	stream.stop_stream()  
	stream.close()  

	#close PyAudio  
	p.terminate()  

	'''def __init__(self,file_name):
		self.chunk = 1024  
		#define stream chunk   
		#open a wav format music  
		self.f = wave.open(file_name,"rb")  
		#instantiate PyAudio  
		self.p = pyaudio.PyAudio()  
		#open stream  
		self.stream = self.p.open(format = self.p.get_format_from_width(self.f.getsampwidth()),  
		                channels = self.f.getnchannels(),  
		                rate = self.f.getframerate(),  
		                output = True)  
		#read data  
		self.data = self.f.readframes(self.chunk)  
	def play(self):
		#play stream  
		while self.data:  
		    self.stream.write(self.data)  
		    self.data = self.f.readframes(self.chunk)  


		self.stream = self.p.open(format = self.p.get_format_from_width(self.f.getsampwidth()),  
		    channels = self.f.getnchannels(),  
		    rate = self.f.getframerate(),  
		    output = True)  
	'''
	'''
		#stop stream  
		self.stream.stop_stream()  
		self.stream.stop_stream()  
		self.stream.close()  

		#close PyAudio  
		self.p.terminate()  
	'''