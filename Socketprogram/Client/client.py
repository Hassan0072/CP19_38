

import socket
import os
s= socket.socket()

def client(strDIR):
    filename = ""
    strDIR = strDIR.decode('utf-8')
    subDir = ""
    if strDIR == 'Q':
        exit
    else:
        for file in os.listdir(strDIR):
            isDir = os.path.isdir(strDIR)
            if isDir:
                if file.find('.') == -1:
                    subDir += str(os.path.join(strDIR, file)) + '\n'
        s.send(subDir.encode('utf-8'))
        strFolderReceived = s.recv(100000)
        if(strFolderReceived!=""):
            DownloadFilesFormFolder(strFolderReceived)


def DownloadFilesFormFolder(strFolderPath):
    strFolderPath = strFolderPath.decode('utf-8')
    print(strFolderPath)
    data = ""
    for file in os.listdir(strFolderPath):
        f = open(strFolderPath + "\\" + file,'rb')
        temp = str(file) + "&\n"
        data += (temp + str(f.read(1024))) + '\n'
        
    print(data)
    s.send(data.encode('utf-8'))
            


host = 'Chamach-PC'
# host=str(input("Enter host Name:  "))
port = 8080
s.connect((host,port))
print("connected...")

file_data=s.recv(1024)
if(file_data!=""):
    client(file_data)

