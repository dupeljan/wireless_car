# Recording 
import socket
from time import time
import numpy as np

RECORDS_DIR = "rec"

sock = socket.socket()
sock.bind(('', 9091))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr )
Motion  = {
		48 : "stop" ,
		49 : "forward",
		50 : "backward",
		51 : "left",
		52 : "right", 
		53 : "f_left",
		54 : "f_right",
		55 : "b_left",
		56 : "b_right",
		57 : "recording"
}
state = 48
recording = False
commands = list()
start = stop = 0
while True:
    data = conn.recv(1024)[0]
    if not data:
        break
    if  data == state:
    	continue

    #conn.send(data+b' recv')
    if Motion(data) == "recording":
    	if not recording:
    		print("start recording...")
    		start = time()
    		recording = True
    	else
    		# Save list to file
    		np.save(str(time) ,np.array( commands ) )
    		commands.clear()
    		recording = false

    
    if Motion(data) != state:	
    	print(Motion[data])
    	stop = time()
    	commands.append( ( state, start - stop ) )
    	start = stop
    	state = data

conn.close()