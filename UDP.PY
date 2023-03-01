import socket
import time

host="localhost"
port=5000

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
time.sleep(5)

s.sendto(b"Hello Client",((host,port)))
Message="How Are You?"
s.sendto(Message.encode(), ((host, port)))
s.close()

#OUTPUT
