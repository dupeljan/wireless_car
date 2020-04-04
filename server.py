import socket
import serial as s
import pygame
from multiprocessing import Process
import subprocess
from sound import play_wav
import struct

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

        54 : "signal",
}

while True:
    data = conn.recv(1024)
    
    if not data:
        break

    
    #conn.send(data+b' recv')
    serial.write(struct.pack('>B', data[0] ))
        
    if Commands[data[0]] == "signal":
        #play()
        Process(target=play,args=(bark,)).start()


conn.close()