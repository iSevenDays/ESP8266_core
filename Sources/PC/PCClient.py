import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
conn.connect( ("127.0.0.1", 9999) )
data = "Send me kiss \n"
conn.send(str.encode(data))
print("TX(send): " + data)