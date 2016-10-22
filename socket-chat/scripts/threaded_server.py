"""
   This is a version of the server script using threading.
   It can maintain connection with multiple clients by using threads.
   It keeps a list of clients and upon receiving a message from one of the clients
   in the list, it will broadcast the message to all the other clients in the list.
"""
import socket, threading

#Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(server)

#Bind to an address and start listening to maximum 2 connections
server.bind(('', 8100))
server.listen(2)

#Create an empty list of clients
clients = []

#This class wraps the child thread process.
#Thread-specific information such as the client's socket object are passed through the init arguments
#The routine to be run on the thread is written in the run() method
class ClientHandler(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.socket = client_socket
        clients.append(self)
        
    #This method wraps the routine to be run on the thread.
    #It sends a greeting message, and then waits to receive
    #messages from the client, broadcasting the message upon receiving.
    def run(self):
        self.socket.sendall(b"Welcome to the chatroom")
        while True:
            message = self.socket.recv(256)
            if not message:
                break
            print(message)
            #self.socket.sendall(message)
            for client in clients:
                if not client == self:
                    client.socket.sendall(message)
        clients.remove(self)
        self.socket.close()

#Keep listening to incoming connection requests
#and start the thread upon accepting the connection
while True:
    (client_socket, client_address) = server.accept()
    handler = ClientHandler(client_socket)
    handler.start()
server.close()