# Solution to picoCTF challenge Static ain't always noise.

# Tags:
# 20 points
# picoCTF 2021
# General skills

# Description:
# Can you look at the data in this binary: static? This BASH script might help!

import requests
import re

URL = "https://mercury.picoctf.net/static/66932732825076cad4ba43e463dae82f/static"
filename = ''.join(re.findall("\w+$", URL))

print(f"Downloading {filename} ...")
f = requests.get(URL)
print(f"Scanning raw data of {filename} for the flag using regular expressions...")
flag = ''.join(re.findall("picoCTF{.*}", str(f.content)))
print("The flag is: " + flag)
