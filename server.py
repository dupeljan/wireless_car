import socket
import serial as s
import pygame
from multiprocessing import Process
import subprocess
from sound import play_wav

bark = "sound4.wav"


#FNULL = open(os.devnull, 'w')
def play(file_name):
    play_wav(file_name)
    #subprocess.call(["ffplay", "-nodisp", "-autoexit", file_name ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# Connect to PC
sock = socket.socket()
sock.bind(('', 7777))
sock.listen(1)
conn, addr = sock.accept()

# Connect to arduino
serial = s.Serial("/dev/ttyUSB0",9600)

print ('connected:', addr )
Commands  = {
		48 : "stop" ,
		49 : "forward",
		50 : "backward",
		51 : "left",
		52 : "right", 
		53 : "f_left",
		54 : "f_right",
		55 : "b_left",
		56 : "b_right",
        57 : "lights",
        58 : "signal",
}
state = 48
not_motions = (57,58)
while True:
    data = conn.recv(1024)
    
    if not data:
        break

    if  data[0] != state:
        #conn.send(data+b' recv')
        serial.write(str.encode(chr(data[0])))
        
        if Commands[data[0]] == "signal":
            #play()
            Process(target=play,args=(bark,)).start()

        if not data[0] in not_motions:
            #print(Commands[data[0]])
            state = data[0]

conn.close()