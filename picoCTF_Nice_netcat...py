# picoCTF challenge Nice netcat...

# Tags:
# 15 points
# picoCTF 2021
# General skills

# Description:
# There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 7449, but it doesn't speak English...

# Imports the socket module.
import socket

host = "mercury.picoctf.net"
port = 7449

print(f"Connecting to {host}:{port}...")
# Creates a TCP, IPv4 socket object.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the host.
client.connect((host, port))
# Receives the data as a byte object.
print("Receiving data...")
numbers = client.recv(4096)
# Converts the byte object to a string.
numbers = numbers.decode("UTF-8")

# We have string with numbers, one number for each row. 
# We assume each number represent an ASCII character. 
# Let's convert the numbers into characters.

# Separates the numbers and assigns them to a list of strings.
list = numbers.split('\n')

# The last entry in the list is an empty string. It  will cause an error when being converted into an integer later.
# Removes the empty string from the list.
list.remove('')
# Prints the numbers received.
print(''.join(list))
# Converts every entry in the list from a string to an integer, then converts the integer into it's corresponding ASCII character and prints the results.
print("Converting numbers into corresponding ASCII characters...")
for integer in list:
    print(chr(int(integer)), end = '')


