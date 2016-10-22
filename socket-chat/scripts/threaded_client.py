"""
   This is a version of the client script using threading.
   Instead of the script waiting for a recv() before processing the next send(),
   the script starts a thread dedicated to handling recv().
   The main thread is used for capturing user input and sending it to the chat server,
   and the child thread is used for receiving messages from the server and displaying it.
"""
import socket, threading

#Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client)

#Connect to the server
client.connect(('localhost', 8100))

#Receive the greeting from server upon successful connection
greeting = client.recv(64)
print(greeting)

#This class wraps the child thread process.
#The client's socket object is passed through the init arguments
class ReceiveHandler(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket
        
    #This method wraps the routine to be run on the thread.
    #It waits to receive a message, and displays it upon receiving.
    def run(self):
        while True:
            message = self.socket.recv(256)
            if not message:
                continue
            print(message.decode('utf-8'))

#Start the receive routine on a thread
receive_handler = ReceiveHandler(client)
receive_handler.start()

#Maintain connection with the server and prompt the user for messages to send.
while True:
    user_input = input('').encode('utf-8')
    client.sendall(user_input)
client.close()