"""
   This is the final version of the chat server application.
   It can listen to up to 5 clients. It will generate a random
   string of length 8 and assign it to each client as the name.
   
   Just like the previous version of the script,
   it maintains connection with multiple clients by using threads.
   It keeps a list of clients and upon receiving a message from one of the clients
   in the list, it will broadcast the message to all the other clients in the list.
"""
import socket, threading, sys, random, string

#This function creates a random string of length 8
def randname():
    return ''.join(random.SystemRandom().choice(string.ascii_letters) for _ in range(8))

#Create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Bind to an address and start listening to maximum 5 connections
server.bind(('', 8100))
server.listen(5)
print("Starting Socket Server")

#Create an empty list of clients
clients = []

#This class wraps the child thread process.
#Thread-specific information such as the client's socket object and the address are passed through the init arguments
#The routine to be run on the thread is written in the run() method
class ClientHandler(threading.Thread):
    def __init__(self, client_socket, client_address):
        threading.Thread.__init__(self)
        self.socket = client_socket
        self.address = client_address
        self.name = randname()
        
    #This method wraps the routine to be run on the thread.
    #It sends a greeting message along with a list of online users, and then waits to receive
    #messages from the client, broadcasting the message upon receiving.
    def run(self):
        clients.append(self)
        print("Client "+self.name+" joined from "+str(self.address[0])+":"+str(self.address[1]))
        msg = "--------------------------\nList of Clients:\n--------------------------\n"
        for client in clients:
            if client == self:
                msg += client.name+" (YOU)\n"
            else:
                msg += client.name+"\n"
        msg += "--------------------------\n"
        self.socket.sendall(b"Welcome to the server\n"+msg.encode("utf-8"))
        while True:
            message = self.socket.recv(256)
            if not message:
                break
            print(self.name+" : "+message.decode("utf-8"))
            for client in clients:
                if not client == self:
                    client.socket.sendall(self.name.encode("utf-8")+b" : "+message)
        self.socket.close()
        clients.remove(self)
        print(str(self.name)+" was dropped.")

#Keep listening to incoming connection requests
#and start the thread upon accepting the connection
while True:
    (client_socket, address) = server.accept()	
    # print(clients)
    handler = ClientHandler(client_socket, address)
    handler.start()
    
server.close()