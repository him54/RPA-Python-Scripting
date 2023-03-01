#UDP SERVER
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




#UDP CLIENT

import socket
import time

host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, port))
c, addr = s.recvfrom(1024)

try:
    s.settimeout(5) # Set the timeout value for the socket  setTimeout() method sets a timer
                    # which executes a function or specified piece of code once the timer expires.

    while c:
        print("Received Message: " + c.decode())
        c, addr = s.recvfrom(1024) #recvfrom() function receives data on a socket named by descriptor socket and stores it in a buffer.
except socket.timeout:
    print("Time is over and hence terminating")
s.close()







#OUTPUT
Received Message: Hello Client
Received Message: How Are You?
Time is over and hence terminating
