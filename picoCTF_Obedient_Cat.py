# picoCTF challenge Obedient Cat.

# Tags:
# 5 points
# picoCTF 2021
# General skills

# Description:
# This file has a flag in plain sight (aka "in-the-clear"). Download flag.

import requests

url = "https://mercury.picoctf.net/static/704f877da185904ec3992e7255a15c6c/flag"

print("Downloading file...")
response = requests.get(url)
print("Printing the contents of the file...")
print(response.content.decode('UTF-8'))
