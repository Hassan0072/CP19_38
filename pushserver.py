import socket                   # Import socket module

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = ""   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')


# while True:
conn, addr = s.accept()     # Establish connection with client.
print('Got connection from', addr)