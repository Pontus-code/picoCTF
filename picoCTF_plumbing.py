# Solution to picoCTF challenge plumbing.

# Tags:
# 200 points
# picoCTF 2019
# General skills

# Description:
# Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to jupiter.challenges.picoctf.org 7480.

# Import socket module.
import socket
# Import regular expressions module.
import re

# Set variables for socket client.
host = "jupiter.challenges.picoctf.org"
port = 7480

# Initialize TCP IPv4 socket object.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Connecting to {host}:{port}...")
client.connect((host, port))

print("Receiving data...")
recv_len = 1
response = ''
while recv_len:
    data = client.recv(4096)
    recv_len = len(data)
    response += data.decode()

# Uncomment to view the response.
# print(response)

print("Scanning data for flag using regular expressions picoCTF{.*}...")
flag = re.findall("picoCTF{.*}", response)
print(''.join(flag))
