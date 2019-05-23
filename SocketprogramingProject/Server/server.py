
# ////////////////////////////////////////////////

import socket      
import os                 # Import socket module
s= socket.socket()
host = "192.168.0.104"
# socket.gethostname() # getting computer name
port= 8080
s.bind((host,port)) #we are simply attempeting to bind a socket locally, on port 8989
s.listen(10) # we're going to use s.listen to listen. Here, the "1" stands for how many incoming connections we're willing to queue before denying any more.
print(host)
print("Waiting for any incoming connection... ")
conn, addr = s.accept() #  Establish connection with client. 

print(addr,"Has connected to the server")
# filename = 'C:\Users\Chamach\Desktop\Socket Programing\Client\tst'
filename = input(str("Please mention main directory path :"))
conn.send(filename.encode("utf-8")) # strings are stored as Unicode, i.e. each character in the string is represented by a code point.
strFolderReceived = conn.recv(100000) # receive data from the server (100000) for huge data
strFolderReceived = strFolderReceived[:-1] # remove last  str i.e owais = owai
print("========================\nFolder Directories are :\n========================\n" + strFolderReceived.decode('utf-8')+ "\n======================================================") 
displayFiles = input(str("Please mention folder path to Display Files or 'Q' to Quit:"))
if displayFiles != 'Q':
    conn.send(displayFiles.encode('utf-8'))
    strDisplayFiles = conn.recv(10000)
    strDisplayFiles = strDisplayFiles.decode('utf-8')
    print("========================\Files in Directory are :\n========================\n" + strDisplayFiles + "\n======================================================") 
    downloadFolder = input(str("Press 'D' to download files from the client folder or 'Q' to quit: "))
    if downloadFolder == 'Q':
        exit
    elif downloadFolder != 'Q':
        conn.send(downloadFolder.encode('utf-8'))
        strData = conn.recv(100000)
        strData = strData.decode('utf-8') #  It accepts the encoding of the encoding string to decode it and returns the original string.
        tempStrData = str(strData)
        arrTempData = tempStrData.splitlines() # The function returns a list of lines in the string
        for data in arrTempData:
            flag = 1
            if data.find("&") != -1:
                flag =  0
                if flag == 0:
                    f = open(data[:-1],'wb') # remove last value and open file
            else:
                # objSpace = 
                copyData = data
                #data
                f.write(copyData.encode('utf-8'))  # write data
                flag = 1
print("================================================================")        
print("Files successfully downloaded from client system to server system")
print("Download file Folder path: " + os.getcwd())
print("================================================================") 