# Solution to picoCTF challenge Based.

# Tags:
# 200 points
# picoCTF 2019
# General skills

# Description: 
"""
To get truly 1337, you must understand different data encodings,
such as hexadecimal or binary. Can you get the flag from this program to prove
you are on the way to becoming 1337? 
Connect with nc jupiter.challenges.picoctf.org 29221.
"""

import socket
import re

HOST = "jupiter.challenges.picoctf.org"
PORT = 29221

def connect(HOST, PORT):

    print(f"Connecting to {HOST}:{PORT}")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    return client

def receive(client):

    response = client.recv(4096)
    print(f"RECEIVED MESSAGE: \n{response.decode()}")
    print("END OF MESSAGE\n")
    return response

def send(client, word):

    print(f"SENDING MESSAGE: \n{word}")
    word += "\n"
    client.send(word.encode())
    print("END OF MESSAGE\n")


def convert_binary(response):

    binary = re.findall("\d+", response.decode())
    binary.pop()
    word = ''
    for byte in binary:
        decimal = int(byte, 2)
        character = chr(decimal)
        word += character
    print(f"Binary converted to ASCII: {word}")
    return word


def convert_octals(response):

    octals = re.findall("\d+", response.decode())
    word = ''
    for octal in octals:
        decimal = int(octal, 8)
        word += chr(decimal)
    print(f"Octals converted to ASCII: {word}\n")
    return word

def convert_hexadecimals(response):

    hex = re.findall("(?<=Please give me the )\w+",response.decode())
    hexlist = re.findall(".{1,2}", ''.join(hex))
    word = ''
    for hex in hexlist:
        decimal = int(hex, 16)
        character = chr(decimal)
        word += character
    print(f"Hexadecimals converted to ASCII: {word}\n")
    return word


client = connect(HOST, PORT)

counter = 0
for i in range(3):
    response = receive(client)
    if counter == 0:
        word = convert_binary(response)
    elif counter == 1:
        word = convert_octals(response)
    elif counter == 2:
        word = convert_hexadecimals(response)
    else:
        print("Something went wrong!")
    send(client, word)
    counter += 1

response = client.recv(4096)
flag = response.decode()
print(flag)