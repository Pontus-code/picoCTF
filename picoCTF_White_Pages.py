# Solution to picoCTF challenge White Pages.

# Tags:
# 250 points
# pioCTF 2019
# Forensics

# Description: I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

import requests, re

url = "https://jupiter.challenges.picoctf.org/static/74274b96fe966126a1953c80762af80d/whitepages.txt"

print(f"Downloading {url}")
r = requests.get(url)
text = r.text
print("Printing the text...")
print(text)
print("No visibile characters. Only empty spaces...")
print("\n\nPrinting the same text encoded in raw bytes...")
print(text.encode())

print("\nSo there are 'spaces' and other 'whitespace' bytes...")
print("Let's turn every 'space' into a 1 and every 'whitespace' into a 0...")

binary = ''
for char in text:
    if char == ' ':
        binary += '1'
    else:
        binary += '0'

print(binary)

flag = ''
print("\nNow lets separate the bits into 8 bit bytes, convert them into decimals and the corresponding ASCII character...")
for byte in re.findall("\d{8}", binary):
    decimal = int(byte, 2)
    char = chr(decimal)
    print(f"{byte}\t{decimal}\t{char}") 
    flag += char

    
print("\nThe cleartext is:")
print(flag)


    

