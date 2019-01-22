import socket
import serial as s

# Connect to PC
sock = socket.socket()
sock.bind(('', 7777))
sock.listen(1)
conn, addr = sock.accept()

# Connect to arduino
serial = s.Serial("/dev/ttyUSB0",9600)

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
}
state = 48
while True:
    data = conn.recv(1024)
    if not data:
        break
    if  data[0] == state:
    	continue
    #conn.send(data+b' recv')
    serial.write(str.encode(chr(data[0])))
    if data[0] == 57:
        continue
    #print(Motion[data[0]])
    state = data[0]

conn.close()