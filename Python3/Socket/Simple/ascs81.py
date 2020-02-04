# Python 3 A Simple Client Socket
from socket import *

# create socket object
cs = socket(AF_INET, SOCK_STREAM)

# get localhost name
host = gethostname()                           
port = 8881

# connetion to host on the port
cs.connect((host, port))

# no more than 1024 bytes
msg = cs.recv(1024)

# close client
cs.close()
print (msg.decode('ascii'))
