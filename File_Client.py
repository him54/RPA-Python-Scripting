import socket
import time


host = 'localhost'
port = 5000

s = socket.socket()
s.connect((host,port))


f_name = input("Enter file name:")
s.send(f_name.encode())

content = s.recv(1024)
msg = str(content)
print(msg)
s.close()
