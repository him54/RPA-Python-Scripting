# import urllib.parse
# url = "http://abc.com:80/engineering/computer-science.html"
# tpl = urllib.parse.urlparse(url)
# print(tpl)
#
# print(tpl.scheme)
# print(tpl.port)
# print(tpl.netloc)
# print(tpl.params)
# print(tpl.geturl())

import socket

host = "localhost"
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_INIT - IP family IPv4 , IPv6
#socket.SOCK_STREAM - TCP / UDP

s.bind((host, port))    #ye dono ek dusre ko intermediate kar rahe hai

s.listen(1)
c, add = s.accept()
print(str(add))

c.send(b"Hello, how are you?") #client
msg="I am fine."
c.send(msg.encode())
c.close()

#OUTPUT
('127.0.0.1', 53152)


import socket
host="localhost"
port=5000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))

msg=s.recv(1024)
# s.rev multiple of 1024 Next value will take 1024 * 2 , 1024 * 4
while msg:
    print("message : "+ msg.decode())
    msg=s.recv(1024)
s.close()
#OUTPUT
Message : Hello, how are you?
Message : I am fine.

