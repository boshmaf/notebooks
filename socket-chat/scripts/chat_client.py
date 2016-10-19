"""
   This is the final version of the chat server application.
   
   Just like the previous version of the script,
   the main thread is used for capturing user input and sending it to the chat server,
   and the child thread is used for receiving messages from the server and displaying it.
   
   The end-user can type the command "\q" to exit the program.
   There is an extra method terminate() in the ReceiveHandler class, to safely close the thread. 
"""
import socket, threading

#Create socket and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8100))

#Receive the greeting from server upon successful connection
greeting = client.recv(256) #receive greetings
print(greeting.decode('utf-8'))
print('Type \q to exit chat program')

#This class wraps the child thread process.
#The client's socket object is passed through the init arguments
class ReceiveHandler(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket
    
    #This method sets the instance attribute self.running to False
    #which is a terminate condition for the loop inside run() method.
    def terminate(self):
        self.running = False
    
    #This method wraps the routine to be run on the thread.
    #It waits to receive a message, and displays it upon receiving.
    #For safely breaking the while loop we use an instance attribute
    #self.running as the loop condition. The terminate() method sets
    #this attribute to False, thus safely exiting the loop
    def run(self):
        self.socket.setblocking(0)
        self.running = True
        while self.running:
            try:
                message = self.socket.recv(256)
                if not message:
                    continue
                print(message.decode('utf-8'))
            except BlockingIOError:
                continue
        print("shutting down receive handler...")

#Start the receive routine on a thread
receive_handler = ReceiveHandler(client)
receive_handler.start()

#Maintain connection with the server and prompt the user for messages to send.
while True:
    user_input = input('').encode('utf-8')
    if user_input == b'\q':
        break
    client.sendall(user_input)

#If user types \q the loop will break, and the code below will be run.
#Terminate the child thread and then close the socket.
receive_handler.terminate()
client.close()
print("bye bye")