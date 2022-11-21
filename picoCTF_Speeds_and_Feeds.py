# Solution to picoCTF challenge Speeds and Feeds.

# tags:
# 50 points
# picoCTF 2021
# Reverse engineering

# Description: There is something on my shop network running at nc mercury.picoctf.net 20301, but I can't tell what it is. Can you?
# Hint: What language does a CNC machine use?

import re
import socket

host = "mercury.picoctf.net"
port = 20301

# Establish a TCP client.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
response = ''
recv_len = 1
# Receive and store data until you stop receiving.
while recv_len:
    data = client.recv(4096).decode()
    response += data
    recv_len = len(data)

# Write the data to a file.
with open("file.gcode", "w") as f:
    f.write(response)

# I don't know how to visualise G-code in python... yet.
# Go to ncviewer.com and open the file "file.gcode" to visualise the flag.