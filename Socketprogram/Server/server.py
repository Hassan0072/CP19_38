


# ////////////////////////////////////////////////

import socket                       # Import socket module
s= socket.socket()
host = socket.gethostname()
port= 8080
s.bind((host,port))
s.listen(1)
print(host)
print("Waiting for any incoming connection... ")
conn, addr = s.accept()

print(addr,"Has connected to the server")
# filename = 'C:\Users\Chamach\Desktop\Socket Programing\Client\tst'
filename = input(str("Please mention main directory path :"))
conn.send(filename.encode("utf-8"))



strFolderReceived = conn.recv(100000)
strFolderReceived = strFolderReceived[:-1]
print("========================\nFolder Directories are :\n========================\n" + strFolderReceived.decode('utf-8')+ "\n======================================================") 
downloadFolder = input(str("Please mention folder path to download or 'Q' to quit: "))
if downloadFolder == 'Q':
    exit
elif downloadFolder != 'Q':
    conn.send(downloadFolder.encode('utf-8'))
    strData = conn.recv(100000)
    strData = strData.decode('utf-8')
    tempStrData = str(strData)
    arrTempData = tempStrData.splitlines() # break data into new lines where find \n
    
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
            
print("Data has been transmittted successfully")