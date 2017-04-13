import socket as socket
import time as t
import random as r

# creates socket object

def receve_MSG(IP="",port=1337,MSG_Size=1024,TEXT_Decode='ascii',ExpectedFileType="TXT"):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if(IP==""):
        IP = socket.gethostname()
    s.connect((IP, port))
    tm = s.recv(MSG_Size) # msg can only be x bytes long
    if(ExpectedFileType == "TXT"):
        RecevedText = tm.decode(TEXT_Decode)
    if(ExpectedFileType == "IMG"):
        RecevedText = tm
    s.close()
    return RecevedText

def WriteToFile(toBewritten,FileName="out",FileType=".txt",WriteType="w+"):
    FileName = FileName+FileType
    text_file = open(FileName, WriteType)
    text_file.write(toBewritten)
    text_file.close()

x=0
while(1==1):
    print("Mesage Receved")
    #Only can revece 9Mb of file
    WriteToFile(receve_MSG("",1337,9999999,'ascii',"IMG"),"Output",".jpg","wb+")
    t.sleep(1)
    x=x+1
    print(x)
