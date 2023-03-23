
#File server - Read the content of that File
#File Client - Take a file name

import socket
import time

host = "localhost"
port = 5000
s = socket.socket()
s.bind((host,port))
s.listen(1)

c,addr = s.accept()
print("Connected")
f_name = c.recv(1024)
fn=str(f_name.decode())
try:
    print(fn)
    f=open(fn,"rb")
    content = f.read()
    c.send(content)
    print("Data sent")
    f.close()
except FileNotFoundError:
        c.send("File not found")
c.close(



# import socket
#
# host="localhost"
# port=5000
# s=socket.socket()
#
# s.bind((host, port)) #We canot use
#
# s.listen(1) #Means maximum number of connection we want to make
#
# c, addr = s.accept()
# print("Connected")
# FName=c.recv(1024)
# FN=str(FName.decode())#Buffer store in file  ; Decode it to string
#
# try:
#     f=open(FName,"rb")
#     content=f.read()
#     c.send(content)
#     print("File Data Sent")
#     f.close()
# except FileNotFoundError:
#     c.send("File not Found")
# c.close()

#We create a socket object and bind it to the given host and port.
#The server listens for incoming connections.
#When a connection is established, we accept it and receive the filename from the client.
#If the file is found, we read its contents and send it to the client.
#If the file is not found, we send an error message to the client.
#We close the connection and the server socket.

