# Solution to picoCTF what's the net cat?

# Tags:
# 100 points
# picoCTF 2019
# General skills

# Description: 
# Using netcat (nc) is going to be pretty important. Can you connect to jupiter.challenges.picoctf.org at port 64287 to get the flag?

import socket # Imports the socket library

host = "jupiter.challenges.picoctf.org"
port = 64287

# Establish a IPv4 TCP connetion with the server.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

response = ''
recv_len = 1
while recv_len: # Run until you stop receiving data.
    data = client.recv(4096).decode()
    recv_len = len(data)
    response += data

print(response) # Print what you have received.
