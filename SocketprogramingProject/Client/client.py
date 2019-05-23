

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
        for file in os.listdir(strDIR): # to search through a given path (".") for all files that endswith ".txt".
            isDir = os.path.isdir(strDIR) # check dir available or not
            if isDir:
                if file.find('.') == -1:
                    subDir += str(os.path.join(strDIR, file)) + '\n' # concat dir path and file
        s.send(subDir.encode('utf-8'))
        strFolderReceived = s.recv(100000)
        if(strFolderReceived!=""):
            # DownloadFilesFormFolder(strFolderReceived)
            displayFiles(strFolderReceived)

def displayFiles(strFolderPath):
    strDisplayFiles = strFolderPath.decode('utf-8')
    displayData = ""
    for file in os.listdir(strDisplayFiles):
        displayData +=str(file) + "\n"
    s.send(displayData.encode('utf-8'))
    strFolderDirData =  s.recv(100000)
    strFolderDirData = strFolderDirData.decode('utf-8')
    print(strFolderDirData )
    if(strFolderDirData=="D"):
        DownloadFilesFormFolder(strFolderPath)
    

def DownloadFilesFormFolder(strFolderPath):
    strFolderPath = strFolderPath.decode('utf-8')
    print(strFolderPath)
    data = ""
    for file in os.listdir(strFolderPath):
        f = open(strFolderPath + "\\" + file,'rb')
        temp = str(file) + "&\n"
        data += (temp + str(f.read(1024))) + '\n' # read files data
        
    print(data)
    s.send(data.encode('utf-8'))
            


host = '192.168.0.104'
# host=str(input("Enter host Name:  "))
port = 8080
s.connect((host,port)) ## connecting to the server 
print("connected...")

file_data=s.recv(1024)
if(file_data!=""):
    client(file_data)

