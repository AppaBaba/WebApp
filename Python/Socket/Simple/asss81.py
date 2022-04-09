# Python 3 A Simple Server Socket
from socket import *

# create socket object
ss = socket(AF_INET, SOCK_STREAM)

# localhost
host = gethostname()                           
port = 8881

# bind to the port
ss.bind((host, port))

# up to 3 requests
ss.listen(3)

while True:
   # establish a connection
   cs,addr = ss.accept()
   
   print("connection from %s" % str(addr))

   # send mesage to client
   msg = 'Hi there' + "\r\n"
   cs.send(msg.encode('ascii'))
   cs.close()
