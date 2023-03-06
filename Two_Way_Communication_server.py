import socket
host="127.0.0.1"
port=9000

s=socket.socket()

s.bind((host, port))
s.listen(1)

c,addr = s.accept()
print("client connected")


while True:  #Server runs continuously
    data = c.recv(1024)

    if not data:
        break
    print("From client:"+str(data.decode())) #Recieved his data
    response = input("Enter the responce")
    c.send(response.encode())
s.close(



