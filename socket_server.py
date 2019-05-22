import socket                   # Import socket module
import os

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = "127.0.0.1"   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
   conn, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   data = conn.recv(1024)
   print('Server received', repr(data))
   filename='c:/Users/Chamach/Desktop/OWAIS_FP/Server/tst/'
   print (len([filename for filename in os.listdir('.')]))
   for file in os.listdir(filename):
       isDir = os.path.isdir(filename)
       if isDir:
          subDir = os.path.join(filename, file)
          print(subDir)
           subDir = 'c:/Users/Chamach/Desktop/OWAIS_FP/Server/tst/'+file'/'
          for subfile in os.listdir(subDir):
             print(subfile)
      else:
      print(file)
      file = filename + file
      print(file)
      f = open(file,'rb')
      l = f.read(1024)
      while (l):
         conn.send(l)
         print('Sent ',repr(l))
         l = f.read(1024)
      f.close()
      

   print('Done sending')
   # data = "/nThank you for connecting"
   # conn.send(data.encode('utf-8'))
   conn.close()
 # filename='C:/Users/Chamach/Desktop/test.txt' #In the same folder or path is this file running must the file you want to tranfser to be