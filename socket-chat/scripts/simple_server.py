"""
   This script is the simplest version of the server script.
   It can maintain connection with only 1 client;
   the second client's connection request will never be accepted
   because the process is blocking inside the first while loop.
   
   An improved version using threading can be found in scripts/server_threading.py
"""
import socket

#Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server)

#Bind to an address and start listening to maximum 2 connections
server.bind(('', 8100))
server.listen(2)

#Accept first client
(client_socket, client_address) = server.accept()
print(client_socket)
print(client_address)

#Send greeting to the first client
client_socket.sendall(b"Welcome to the chatroom")

#Maintain connection with the first client and echo back whatever it sends
while True:
    message = client_socket.recv(256)
    if not message:
        break
    print(message)
    client_socket.sendall(message)

#Accept second client    
(client_socket2, client_address2) = server.accept()
print(client_socket2)
print(client_address2)

#Send greeting to the second client
client_socket2.sendall(b"Welcome to the chatroom")

#Maintain connection with the second client and echo back whatever it sends
while True:
    message = client_socket2.recv(256)
    if not message:
        break
    print(message)
    client_socket2.sendall(message)