import socket
host="127.0.0.1"
port=9000

s= socket.socket() # Socket is required
s.connect((host, port))  #Without double bracket showing error it is important as related our ETE
r=input("Enter the data to send:")
s.send(r.encode())

while True:
    response = s.recv(1024)
    Message=str(response.decode())
    print(Message)

    if not response:
        break

s.close()

# while r!="exit"
#     s.send(r.encode())
#     d=s.recv(1024)
#     d.decode()
#     r=input("Enter the data")
#
# s.close()
