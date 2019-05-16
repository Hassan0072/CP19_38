import socket                   # Import socket module
import os

s = socket.socket()             # Create a socket object
host = "127.0.0.1"  #Ip address that the TCPServer  is there
port = 50000                     # Reserve a port for your service every new transfer wants a new port or you must wait.
s.connect((host, port))
data = "c:/Users/Chamach/Desktop/OWAIS_FP/Server/tst/"
# data=input("enter path:")

s.send(data.encode('utf-8'))
count = 0
# with open('received_file', 'wb') as f:
# print("connecting to server..")
while True:
    data = s.recv(1024)
    if not data:
        break
    else:
        count = count + 1
        filename = 'received_file' + str(count)+".txt"
        
        f = open(filename,'wb')
        print('receiving data...')
        # print('data=%s', (data))
        # write data to a file
        f.write(data)
        f.close()


print('Successfully get the file')
s.close()
print('connection closed')

# import socket
# import sys
# import os

# HOST = 'localhost' 
# PORT = 8082 
# size = 1024

# def ls():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#     s.connect((HOST,PORT))
#     s.send(userInput)
#     result = s.recv(size)
#     print (result)
#     s.close()
#     return

# def put(commandName):
#     socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     socket1.connect((HOST, PORT))
#     socket1.send(commandName)
#     string = commandName.split(' ', 1)
#     inputFile = string[1]
#     with open(inputFile, 'rb') as file_to_send:
#         for data in file_to_send:
#             socket1.sendall(data)
#     print ('PUT Successful')
#     socket1.close()
#     return


# def get(commandName):
#     socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     socket1.connect((HOST, PORT))
#     socket1.send(commandName)
#     string = commandName.split(' ', 1)
#     inputFile = string[1]
#     with open(inputFile, 'wb') as file_to_write:
#         while True:
#             data = socket1.recv(1024)
#             print (data)
#             if not data:
#                 break
#             print (data)
#             file_to_write.write(data)
#     file_to_write.close()
#     print ('GET Successful')
#     #socket1.close()
#     return

# done = False
# while not done:
#     userInput = input()
#     if "quit" == userInput:
#         done = True
#     elif "ls" == userInput:
#        ls()
#     else:
#         string = userInput.split(' ', 1)
#         if (string[0] == 'put'):
#             put(userInput)
#         elif (string[0] == 'get'):
#             get(userInput)
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#     s.connect((HOST,PORT))
#     s.send(userInput) 
#     data = s.recv(size) 
#     s.close() 
#     print ('Received:', data)