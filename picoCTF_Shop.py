# Solution to picoCTF challenge Shop.

# Tags:
# 50 points
# picoCTF 2021
# Reverse engineering

# Description: 
# Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open for business at nc mercury.picoctf.net 37799.

import socket
import re

HOST = "mercury.picoctf.net"
PORT = 37799

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
client.settimeout(0.5)


inputs = ['1','-5','2','1']

def recv():
    response = client.recv(4096).decode()
    print(response)
    if re.findall("^Flag is:.*", response):
        global data
        data = response


def send(text):
    buffer = text + "\n"
    print("> " + buffer)
    client.send(buffer.encode())


recv()
recv()
for i in range(len(inputs)):
    send(inputs[i])
    try:
        recv()
        recv()
    except:
        continue 
decimals = re.findall("\d+", data)
print("Converting decimals to characters using ASCII table.")
flag = ''
for decimal in decimals:
    flag += chr(int(decimal))
print("\nThe flag is: " + flag + "\n")