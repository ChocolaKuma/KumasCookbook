import time
import socket
import os

def readfile():    #reads str into memory calls it f
    text_file = open("input.jpg","rb")
    f = text_file.read()
    return f

stringtoSend = readfile()

def Make_Server(IP="",port=1337,AMT_Requests=5):
    if(IP==""):
        IP = socket.gethostname()    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    global s
    # bind to port
    s.bind((IP, port))
    s.listen(AMT_Requests)


Make_Server()
while True:
    # establish connection
    clientSocket, addr = s.accept()
    print("got a connection from %s" % str(addr))
    sent = stringtoSend
    clientSocket.send(sent)
    clientSocket.close()
