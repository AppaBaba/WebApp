# Python 3 A Simple Client Socket
from socket import *
cs = socket(AF_INET, SOCK_STREAM)
host = gethostname()                           
port = 8881
cs.connect((host, port))                               
msg = cs.recv(1024)                                     
cs.close()
print (msg.decode('ascii'))
