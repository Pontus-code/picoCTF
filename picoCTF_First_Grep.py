# Solution to picoCTF challenge First Grep.

# Tags:
# 100 points
# picoCTF 2019
# General skills

# Description:
# Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way.

# Imports the requests module
import requests
# Imports the regular expressions module.
import re

# URL for the file in the description.
url = "https://jupiter.challenges.picoctf.org/static/495d43ee4a2b9f345a4307d053b4d88d/file"
filename = ''.join(re.findall("\w*$", url))

# Requests the file.
print(f"Downloading {filename}...")
response = requests.get(url)

print("Searching for the flag using regular expressions... picoCTF{.*}")
flag = re.findall("picoCTF{.*}", response.content.decode())

# Prints the flag.
print("The flag is: " + ''.join(flag))
    

