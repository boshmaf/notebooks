"""
   This script is the simplest version of the client script.
   The first instance of this script can maintain connection with the server,
   send messages to it, and see it echoed back.
   The second instance will not be able to connect to the server until
   the first instance "hangs up" and breaks the first while loop on the server.
   
   An improved version using threading can be found in scripts/server_threading.py
"""
import socket

#Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(client)

#Connect to the server
client.connect(('localhost', 8100))

#Receive the greeting from server upon successful connection
greeting = client.recv(64)
print(greeting)

#Maintain connection with the server and prompt the user for messages to send.
#After sending the message, receive the reply and print it
while True:
    user_input = input('').encode('utf-8')
    client.sendall(user_input)
    reply = client.recv(64)
    print(reply)
client.close()