# Python 3 A Simple Server Socket
from socket import *                                      
ss = socket(AF_INET, SOCK_STREAM) 
host = gethostname()                           
port = 8881                                          
ss.bind((host, port))                                  
ss.listen(3)                                           
while True:
   # establish a connection
   cs,addr = ss.accept()      
   print("connection from %s" % str(addr))
   msg = 'Hi there' + "\r\n"
   cs.send(msg.encode('ascii'))
   cs.close()
