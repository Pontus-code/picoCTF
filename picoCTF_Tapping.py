# Solution to picoCTF challenge Tapping.

# Tags:
# 200 points
# picoCTF 2019
# Cryptography

# Description: Theres tapping coming in from the wires. What's it saying nc jupiter.challenges.picoctf.org 21610.

import socket

host = 'jupiter.challenges.picoctf.org' 
port = 21610

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
response = client.recv(4096)
text = response.decode()

print("The following message was received:")
print(text) # String of dots and dashes like Morse code.

english_to_morse = {'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

# Reverse the dictionary.
morse_to_english = {value: key for key, value in english_to_morse.items()}

print("Translating dots and dashes using a morse to english dictionary.")
flag = ''
for morse in text.split(" "):
    if morse in morse_to_english:
        flag += "".join(morse_to_english[morse])
    else: 
        flag += "".join(morse)

print(flag)